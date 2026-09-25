from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List
from datetime import datetime
import pandas as pd
import numpy as np
import sqlite3
import random
import warnings
import GPy
from GPy.inference.latent_function_inference import Laplace
from GPy.kern import Kern, RBF
from GPy.core.parameterization import Param
from rdkit import Chem
from rdkit.Chem import AllChem
from sklearn.preprocessing import MinMaxScaler
from scipy.stats import entropy
import os
import logging
from typing import Optional
import pickle 
from fastapi import HTTPException
from pydantic import BaseModel

from send_to_chemspeed import get_token, build_wf63_payload, send_and_queue_run, get_ready_reactions, build_wf64_payload

SEED = 42                               

import os, random, numpy as np
random.seed(SEED)                        
np.random.seed(SEED)                    
os.environ["PYTHONHASHSEED"] = str(SEED)


app = FastAPI(title="Bayesian Optimization API")
DB_PATH   = "chemspeed.db"
LOG_DIR   = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

ALLOWED_TABLES = {"reactions", "multi_reactions"}
DEFAULT_TABLE  = os.getenv("TABLE_NAME", "reactions")
if DEFAULT_TABLE not in ALLOWED_TABLES:
    raise RuntimeError(
        f"Invalid TABLE_NAME env‑var: {DEFAULT_TABLE}. Allowed: {ALLOWED_TABLES}")

def pick_table(table_q: Optional[str]) -> str:
    """Return a validated table name (query param overrides env)."""
    tbl = table_q or DEFAULT_TABLE
    if tbl not in ALLOWED_TABLES:
        raise HTTPException(status_code=400, detail="Unknown table name")
    return tbl



class Config(BaseModel):
    n_candidates: int = 100
    top_k: int = 4
    n_bits: int = 1024
    beta: float = 1.0
    temperature_range: tuple = (20, 50)
    time_range: tuple = (1, 60)
    # monomer_a_conc_range: tuple = (0.0034, 0.03)
    # monomer_b_conc_range: tuple = (0.0016, 0.01)
    additive_conc_range: tuple = (0.01, 0.04)
    valid_additives: List[str] = ["No_additive", "NaOH", "DBU", "TEA", "CsCO3"]
    allowed_monomers: List[str] = [ "CJ13", "CB31", "CB174", "CA177", "DB8", "DC13",
                                    "DB106", "CA147", "CA64", "CK20", "DC84", "DC67",
                                    "CI42", "CA221", "DC68", "CA206", "CA94", "CI107",
                                    "CH30", "CO14", "CQ50", "CK58", "CB3", "CB137",
                                    "CB181", "CP33"]
    max_temperature: float = 40.0   # hard “cap” for temperature feasibility
    max_time:        float = 30.0   # hard “cap” for time feasibility

class TanimotoKernel(Kern):
    def __init__(self, input_dim, variance=1.0, active_dims=None, name='tanimoto'):
        super().__init__(input_dim, active_dims, name)
        self.variance = Param('variance', variance)
        self.link_parameters(self.variance)

    def K(self, X, X2=None):
        if X2 is None:
            X2 = X
        numerator = np.dot(X, X2.T)
        denom = np.sum(X, axis=1)[:, None] + np.sum(X2, axis=1)[None, :] - numerator
        denom = np.where(denom == 0, 1e-10, denom)
        return self.variance * (numerator / denom)

    def Kdiag(self, X):
        return np.full(X.shape[0], self.variance)

    def update_gradients_full(self, dL_dK, X, X2=None):
        self.variance.gradient = 0.0

    def gradients_X(self, dL_dK, X, X2=None):
        return np.zeros_like(X)
    
    def to_dict(self):
        input_dict = super()._save_to_input_dict()
        input_dict["class"] = "TanimotoKernel"
        # no extra state beyond variance for this kernel
        input_dict["variance"] = float(self.variance)
        return input_dict

    @staticmethod
    def from_dict(d):
        kern = TanimotoKernel(input_dim=d["input_dim"], variance=d["variance"], name=d["name"])
        return kern

def safe_fetch_solubility(cursor, query, param):
    cursor.execute(query, (param,))
    result = cursor.fetchone()
    if result:
        sol = result[0]
        if sol is None:
            return None
        try:
            if np.isnan(sol):
                return None
            return sol
        except TypeError:
            return sol  # if sol is not a float, assume it's fine
    return None

def volume_calculator(c_target, c_stock, target_volume=1.0):
    if c_target >= c_stock:
        print(f"Target concentration {c_target} is greater than stock concentration {c_stock}. Returning 80% of stock concentration.")
        return c_stock*0.95
    else:
        return (c_target * target_volume) / c_stock

def mol_to_fp(smiles, radius=2, n_bits=1024):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        raise ValueError(f"Invalid SMILES: {smiles}")
    fp = AllChem.GetMorganFingerprintAsBitVect(mol, radius, nBits=n_bits)
    arr = np.zeros((n_bits,), dtype=int)
    Chem.DataStructs.ConvertToNumpyArray(fp, arr)
    return arr

def encode_reaction(smiles_a, smiles_b, n_bits):
    return np.concatenate([mol_to_fp(smiles_a, n_bits=n_bits), mol_to_fp(smiles_b, n_bits=n_bits)])

def get_prev_monomers(cursor, last_iteration: int) -> set[str]:
    rows = cursor.execute(
        "SELECT BarcodeA, BarcodeB FROM multi_reactions WHERE Iteration = ?",
        (last_iteration,)
    ).fetchall()
    prev = {m for pair in rows for m in pair if m is not None}
    return prev

def select_diverse(ranking, metadata, top_k, max_per_monomer=2, exclude_monomers=None):
    from collections import defaultdict
    config = Config()
    selected, counts = [], defaultdict(int)
    seen_pairs = set()
    exclude_monomers = exclude_monomers or set()

    for idx in ranking:
        a, b = metadata[idx][0], metadata[idx][1]

        if a not in config.allowed_monomers:
            warnings.warn(f"Monomer A {a} not in allowed_monomers; skipping.")
            continue

        if b not in config.allowed_monomers:
            warnings.warn(f"Monomer B {b} not in allowed_monomers; skipping.")
            continue
        
        if a in exclude_monomers:
            continue

        pair = (a, b)
        if pair in seen_pairs:
            continue
        if counts[a] >= max_per_monomer or counts[b] >= max_per_monomer:
            continue

        selected.append(idx)
        seen_pairs.add(pair)
        counts[a] += 1
        counts[b] += 1

        if len(selected) == top_k:
            break

    if len(selected) < top_k:
        raise RuntimeError(
            f"Could only select {len(selected)} of {top_k} under your diversity rules"
        )
    return selected

class TransferCallback(BaseModel):
    reaction_id: int
    message: str  # "ImagesTransferred" or "Error"

@app.post("/transfer_callback")
def transfer_callback(cb: TransferCallback, table: str = Query("multi_reactions")):
    tbl = pick_table(table)
    conn = sqlite3.connect(DB_PATH, timeout=5.0)
    cur  = conn.cursor()
    cur.execute(
        f"UPDATE {tbl} SET Status=? WHERE ReactionID=?",
        (cb.message, cb.reaction_id),
    )
    if cur.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="ReactionID not found")
    conn.commit()
    conn.close()
    return {"status": "success", "reaction_id": cb.reaction_id, "updated_to": cb.message}

@app.post("/folder_ready_callback")
def folder_ready_callback(cb: TransferCallback, table: str = Query("multi_reactions")):
    tbl = pick_table(table)
    if cb.message != "FolderReadyToTransfer":
        raise HTTPException(
            status_code=400,
            detail="Invalid message for folder-ready; must be 'FolderReadyToTransfer'"
        )

    conn = sqlite3.connect(DB_PATH, timeout=5.0)
    cur  = conn.cursor()
    cur.execute(
        f"UPDATE {tbl} SET Status = 'FolderReadyToTransfer' WHERE ReactionID = ?",
        (cb.reaction_id,)
    )
    if cur.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="ReactionID not found")
    conn.commit()
    conn.close()

    return {"status": "success", "reaction_id": cb.reaction_id}

@app.get("/get_with_chemspeed")
def get_with_chemspeed(table: str = Query("multi_reactions")):
    tbl = pick_table(table)
    conn = sqlite3.connect(DB_PATH, timeout=5.0)
    cur  = conn.cursor()
    cur.execute(
        f"""
        SELECT *
          FROM {tbl}
         WHERE Status = 'WithChemspeed'
      ORDER BY ReactionID ASC
         LIMIT 1
        """
    )
    row = cur.fetchone()
    conn.close()

    if not row:
        return {}
    cols = [c[0] for c in cur.description]
    return dict(zip(cols, row))

@app.get("/get_ready_transfer_folder")
def get_with_chemspeed(table: str = Query("multi_reactions")):
    tbl = pick_table(table)
    conn = sqlite3.connect(DB_PATH, timeout=5.0)
    cur  = conn.cursor()
    cur.execute(
        f"""
        SELECT *
          FROM {tbl}
         WHERE Status = 'FolderReadyToTransfer'
      ORDER BY ReactionID ASC
         LIMIT 1
        """
    )
    row = cur.fetchone()
    conn.close()

    if not row:
        return {}
    cols = [c[0] for c in cur.description]
    return dict(zip(cols, row))

@app.post("/send_top_endpoint")
def send_top_endpoint(
    table: str = "multi_reactions",
    WorkflowId: str = "64"):
    tbl = pick_table(table)
    API_BASE_URL = "http://10.73.58.47/"

    if WorkflowId not in ["63", "64"]:
        raise HTTPException(status_code=400, detail="Invalid WorkflowId. Allowed: 63, 64")

    try:
        token   = get_token(base_URL=API_BASE_URL)
        df_top  = get_ready_reactions(n=4, table=tbl)

        # pull the iteration number out of results
        iteration = int(df_top["Iteration"].iloc[0])
        label     = f"Closed_Loop_GP_multi_reaction_iter_{iteration}"

        # build  payload with that dynamic label
        if WorkflowId == "64":
            payload = build_wf64_payload(df_top, label=label)
        else:
            payload = build_wf63_payload(df_top, label=label)

        run_id = send_and_queue_run(payload, token)

        # mark them in the DB
        conn = sqlite3.connect(DB_PATH, timeout=5.0)
        cur  = conn.cursor()
        cur.executemany(
            f"UPDATE {tbl} SET Status='WithChemspeed' WHERE ReactionID=?",
            [(rid,) for rid in df_top.ReactionID.tolist()],
        )
        conn.commit()
        conn.close()

        return {
            "status":   "success",
            "run_id":   run_id,
            "label":    label,
            "data":     payload,
            # "Comment": "test-comment",
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/run_gp_optimization")
def run_gp_optimization(config: Config, table: str = Query("multi_reactions"),):
    conn = sqlite3.connect(DB_PATH, timeout=5.0)
    cursor = conn.cursor()
    tbl = pick_table(table)
    logging.basicConfig(filename=f"{LOG_DIR}/gp_optimization.log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    cursor.execute(f"""
        SELECT c1.SMILES, c2.SMILES,
               r.ConcentrationA, r.ConcentrationB,
               r.Temperature,   r.Time, r.AdditiveConcentration,
               r.RealOutcome
          FROM {tbl} r
     JOIN chemical_space c1 ON r.BarcodeA = c1.Barcode
     JOIN chemical_space c2 ON r.BarcodeB = c2.Barcode
         WHERE r.RealOutcome IS NOT NULL
        """)
    rows = cursor.fetchall()
    if not rows:
        raise ValueError("No training data available.")



    X_fp, X_numeric, y_train = [], [], []
    for row in rows:
        X_fp.append(encode_reaction(row[0], row[1], config.n_bits))
        X_numeric.append([row[2], row[3], row[4], row[5], row[6]])
        y_train.append(row[7])

    X_fp = np.array(X_fp)
    X_numeric = np.array(X_numeric)
    y_train = np.array(y_train).reshape(-1, 1)

    scaler = MinMaxScaler(feature_range=(-1, 1))
    X_numeric_scaled = scaler.fit_transform(X_numeric)
    X_combined = np.hstack([X_fp, X_numeric_scaled])

    fp_kernel = TanimotoKernel(input_dim=X_fp.shape[1], active_dims=np.arange(X_fp.shape[1]))
    num_kernel = RBF(input_dim=X_numeric_scaled.shape[1], active_dims=np.arange(X_fp.shape[1], X_combined.shape[1]))
    kernel = fp_kernel + num_kernel

    model = GPy.models.GPClassification(X_combined, y_train, kernel=kernel, inference_method=Laplace())
    model.optimize(messages=True)
    
    # model.save_model("trained_gp_model_iter_36.pkl", compress=True)
    with open("trained_gp_model_iter_36.pkl", "wb") as f:
        pickle.dump(model, f)
    logging.info("GP model trained and saved successfully.")

    # constrained-BO feasibility models

    # 1) build “feasible?” labels on your TRAINING set
    #    X_numeric was [conc_a, conc_b, temp, t, adc] before scaling
    temps_train = X_numeric[:, 2]
    times_train = X_numeric[:, 3]
    y_temp_ok = (temps_train <= config.max_temperature).astype(int).reshape(-1,1)
    y_time_ok = (times_train <= config.max_time).astype(int).reshape(-1,1)

    feas_temp_gp = GPy.models.GPClassification(
        X_combined, y_temp_ok,
        kernel=RBF(input_dim=X_combined.shape[1])
    )
    feas_temp_gp.optimize()

    feas_time_gp = GPy.models.GPClassification(
        X_combined, y_time_ok,
        kernel=RBF(input_dim=X_combined.shape[1])
    )
    feas_time_gp.optimize()

    cursor.execute("SELECT Barcode, SMILES FROM chemical_space WHERE MonomerType = 'A'")
    barcode_to_smiles_A = dict(cursor.fetchall())
    barcodes_A = list(barcode_to_smiles_A.keys())

    cursor.execute("SELECT Barcode, SMILES FROM chemical_space WHERE MonomerType = 'B'")
    barcode_to_smiles_B = dict(cursor.fetchall())
    barcodes_B = list(barcode_to_smiles_B.keys())

    barcode_to_smiles = {**barcode_to_smiles_A, **barcode_to_smiles_B}

    pairs = [(a, b) for a in barcodes_A for b in barcodes_B if a != b]

    if not pairs:                       # no feasible A/B combinations
        conn.close()
        raise ValueError("No valid A/B monomer pairs available.")

    # k = min(config.n_candidates, len(pairs))   # never larger than population
    k = config.n_candidates
    pairs = random.choices(pairs, k=k) ###  random sample of pairs many times TODO this is only for 1-monomer pair testing.

    candidates, metadata = [], []
    for pair in pairs:
        a, b = tuple(pair)
        cursor.execute("""
                SELECT MinRange, MaxRange
                FROM chemical_space
                WHERE Barcode = ?
            """, (a,))
        min_a, max_a = cursor.fetchone()
        rng_a = (min_a, max_a)

        cursor.execute("""
                SELECT MinRange, MaxRange
                FROM chemical_space
                WHERE Barcode = ?
            """, (b,))
        min_b, max_b = cursor.fetchone()
        rng_b = (min_b, max_b)

        sa, sb = barcode_to_smiles[a], barcode_to_smiles[b]

        conc_a = round(np.random.uniform(min_a, max_a), 4)
        conc_b = round(np.random.uniform(min_b, max_b), 4)

        temp = round(np.random.uniform(*config.temperature_range), 1)
        t = round(np.random.uniform(*config.time_range), 1)
        
        additive = random.choice(config.valid_additives)
        adc = 0.0 if additive == "No_additive" else round(np.random.uniform(*config.additive_conc_range), 3)

        candidates.append(np.hstack([
            encode_reaction(sa, sb, config.n_bits),
            scaler.transform([[conc_a, conc_b, temp, t, adc]])[0]
        ]))
        metadata.append((a, b, conc_a, conc_b, temp, t, additive, adc))

    X_cand = np.array(candidates)
    probs, _ = model.predict(X_cand)
    probs = probs.flatten()
    epsilon = 1e-9
    uncertainty = -probs * np.log(probs + epsilon) - (1 - probs) * np.log(1 - probs + epsilon)
    ucb = probs + config.beta * uncertainty

    p_temp_feas, _ = feas_temp_gp.predict(X_cand)
    p_time_feas, _ = feas_time_gp.predict(X_cand)
    p_feas        = (p_temp_feas * p_time_feas).flatten()

    alpha_constr  = ucb * p_feas

    # top_idx       = np.argsort(alpha_constr)[::-1][:config.top_k]
    iteration = (cursor.execute(f"SELECT MAX(Iteration) FROM {tbl}").fetchone()[0] or 0) + 1

    ranking = np.argsort(alpha_constr)[::-1]
    prev_mono = get_prev_monomers(cursor, iteration - 1)
    print(f"Previous monomers: {prev_mono}")
    print("iteration:", iteration)
    top_idx = select_diverse(
                ranking,
                metadata,
                config.top_k,
                max_per_monomer=2,
                exclude_monomers=None # prev_mono old
            )
    # top_idx = select_diverse(ranking, metadata, config.top_k) # old

    now = datetime.now().isoformat()

    IMAGE_ROOT = "/home/ignaczg/projects/closed_loop"
    os.makedirs(IMAGE_ROOT, exist_ok=True)
    # iteration = (cursor.execute("SELECT MAX(Iteration) FROM reactions").fetchone()[0] or 0) + 1

    ### averaging temperature and time, this will probably make the gp slower to converge. There is no upside (maybe more robust?). 
    avg_temp = np.mean([metadata[i][4] for i in top_idx])
    avg_time = np.mean([metadata[i][5] for i in top_idx])
    logging.warning(f"Average temperature: {avg_temp}, Average time: {avg_time}")

    out_rows = []
    for rank, i in enumerate(top_idx):
        print(metadata[i])
        ba, bb, ca, cb, tm, t, ad, adc = metadata[i]
        tm = avg_temp
        t  = avg_time
        # build a unique folder name
        gp_init_time = datetime.now().strftime("%Y-%m-%d-%Hh-%Mm")
        folder_name = f"{iteration}_iter_{gp_init_time}_{ba}_{bb}_{int(tm)}min_{int(t)}C_{ad}"
        folder_path = os.path.join(IMAGE_ROOT, folder_name)  
        os.makedirs(folder_path, exist_ok=True)              

        # Fetch solubility for BarcodeA 
        # if Nan, it will fallback to the naoh solubility
        cursor.execute("""
            SELECT SolubilityWater FROM chemical_space WHERE Barcode = ?
        """, (ba,))
        stock_concentration_a = cursor.fetchone()

        cursor.execute("""
            SELECT SolubilityToluene FROM chemical_space WHERE Barcode = ?
        """, (bb,))
        stock_concentration_b = cursor.fetchone()


        if ad != "No_additive":
            cursor.execute("""
                SELECT SolubilityWater FROM chemical_space WHERE SubstanceCAS = ?
            """, (ad,))
            solubility_additive = cursor.fetchone()
            stock_concentration_additive = solubility_additive[0] if solubility_additive and solubility_additive[0] is not None else 0.1
        else:
            stock_concentration_additive = 0.1

        monomer_a_volume = volume_calculator(ca, stock_concentration_a[0])
        monomer_b_volume = volume_calculator(cb, stock_concentration_b[0])
        additive_volume = volume_calculator(adc, stock_concentration_additive)

        solvent_a_volume = 1.0 - monomer_a_volume - additive_volume
        if solvent_a_volume < 0:
            warnings.warn(f"Solvent A volume is negative: {solvent_a_volume}. Adjusting to 0.0 mL.")
            additive_volume = 1.0 - monomer_a_volume
            adc = additive_volume / 1.0  # Adjusting additive concentration to match volume
            solvent_a_volume = 0.0
        


        solvent_b_volume = 1.0 - monomer_b_volume
        if solvent_b_volume < 0:
            warnings.warn(f"Solvent B volume is negative: {solvent_b_volume}. Adjusting to 0.0 mL.")
            solvent_b_volume = 0.0

        prob, uncert, ucb_val = float(probs[i]), float(uncertainty[i]), float(ucb[i])
        
        cursor.execute("SELECT SubstanceCAS FROM chemical_space WHERE Barcode = ?", (ba,))
        cas_a = cursor.fetchone()
        cas_a = cas_a[0] if cas_a else None

        cursor.execute("SELECT SubstanceCAS FROM chemical_space WHERE Barcode = ?", (bb,))
        cas_b = cursor.fetchone()
        cas_b = cas_b[0] if cas_b else None

        cursor.execute("SELECT ArticleID FROM chemical_space WHERE Barcode = ?", (ba,))
        article_id_a = cursor.fetchone()
        article_id_a = int(article_id_a[0]) if article_id_a and article_id_a[0] else None

        cursor.execute("SELECT ArticleID FROM chemical_space WHERE Barcode = ?", (bb,))
        article_id_b = cursor.fetchone()
        article_id_b = int(article_id_b[0]) if article_id_b and article_id_b[0] else None

        if ad != "No_additive":
            cursor.execute("""
                SELECT ArticleID FROM chemical_space 
                WHERE ContainerName = ? OR SubstanceCAS = ?
                LIMIT 1
            """, (ad, ad))
            logging.warning(f"Additive: {ad}")
            art_add = cursor.fetchone()
            article_id_add = int(art_add[0]) if art_add and art_add[0] else None
        else:
            article_id_add = None
            logging.warning(f"Additive: {ad} not found, setting ArticleID to None.")

        cursor.execute(f"""
            INSERT INTO {tbl} (
                BarcodeA, MonomerA, ConcentrationA, MonomerAVolume,
                BarcodeB, MonomerB, ConcentrationB, MonomerBVolume,
                Temperature, Time,
                SolventA, SolventAVolume,
                SolventB, SolventBVolume,
                AdditiveName, AdditiveConcentration, AdditiveVolume,
                ExpectedOutcome, ReactionDate, Iteration,
                UCB_score, Uncertainty, Acquisition_rank, Status, 
                ArticleIDA, ArticleIDB, ArticleIDAdditive,
                ImageFolder
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """, (
                ba, cas_a, ca, monomer_a_volume,
                bb, cas_b, cb, monomer_b_volume,
                tm, t,
                "7732-18-5", solvent_a_volume,
                "108-88-3", solvent_b_volume,
                ad, adc, additive_volume,
                prob, now, iteration,
                ucb_val, uncert, rank + 1, "Ready", article_id_a, article_id_b, article_id_add,
                folder_path
            ))

        reaction_id = cursor.lastrowid

        out_rows.append({
                "BarcodeA": ba, 
                "MonomerA": cas_a,
                "ConcentrationA": ca,
                "MonomerAVolume": monomer_a_volume,
                
                "BarcodeB": bb, 
                "MonomerB": cas_b,
                "ConcentrationB": cb,
                "MonomerBVolume": monomer_b_volume,
                
                "Temperature": tm,
                "Time": t,
                
                "SolventA": "7732-18-5",
                "SolventAVolume": solvent_a_volume,
                "SolventB": "108-88-3",
                "SolventBVolume": solvent_b_volume,
                
                "AdditiveName": ad,
                "AdditiveConcentration": adc,
                "AdditiveVolume": additive_volume,
                
                "ExpectedOutcome": prob,
                "ReactionDate": now,
                "Iteration": iteration,
                
                "UCB_score": ucb_val,
                "Uncertainty": uncert,
                "Acquisition_rank": rank + 1,
                "Status": "Ready",

                "ArticleIDA":       article_id_a,
                "ArticleIDB":       article_id_b,
                "ArticleIDAdditive": article_id_add,
                "ImageFolder": folder_path
            })

    conn.commit()
    conn.close()

    df = pd.DataFrame(out_rows)
    df.to_csv(f"{LOG_DIR}/iteration_{iteration}.csv", index=False)

    return {"iteration": iteration, "results": out_rows}


