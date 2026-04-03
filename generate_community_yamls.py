"""
Step 2-4 combined:
- Sync driver.py actions to registry
- Fill Device Square params (name, tags, manufacturer, description, device_params, scene, model)
- Generate individual YAML files per device
"""
import os, re, json, ast, csv, yaml, inspect, sys
from pathlib import Path
from collections import defaultdict

BASE_DIR = Path(__file__).resolve().parent
COMMUNITY_DIR = BASE_DIR / "community_drivers"
REGISTRY_OUT_DIR = BASE_DIR / "unilabos" / "registry" / "devices"
TAG_CSV = Path("/Users/sml/work/Uni-Lab-OS/tag 标签列表.csv")
INSTR_CSV = Path("/Users/sml/work/Uni-Lab-OS/1_instruments_merged_dedup.csv")
REAL_DEVICES_JSON = BASE_DIR / "real_devices.json"

# ─────────────────────── Load tag list ───────────────────────
def load_tags():
    tags = {}
    with open(TAG_CSV, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row_type = row.get("type", "").strip().strip('"')
            row_name = row.get("name", "").strip().strip('"')
            row_id = row.get("id", "").strip().strip('"')
            if row_type == "device_template_tag" and row_name:
                tags[row_name] = row_id
    return tags

VALID_TAGS = load_tags()
print(f"Loaded {len(VALID_TAGS)} valid device tags")

# ─────────────────────── Load instrument CSV for matching ───────────────────────
def load_instruments():
    instruments = []
    with open(INSTR_CSV, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            instruments.append(row)
    return instruments

INSTRUMENTS = load_instruments()
print(f"Loaded {len(INSTRUMENTS)} instruments from CSV")

# ─────────────────────── Manufacturer mapping ───────────────────────
MANUFACTURER_MAP = {
    "agilent": "Agilent Technologies",
    "keysight": "Keysight Technologies",
    "hp": "Hewlett-Packard",
    "rohde_schwarz": "Rohde & Schwarz",
    "wiltron": "Wiltron (Anritsu)",
    "marconi": "Marconi Instruments",
    "julabo": "JULABO",
    "binder": "BINDER GmbH",
    "bronkhorst": "Bronkhorst",
    "thorlabs": "Thorlabs",
    "cobolt": "Cobolt (HÜBNER)",
    "keithley": "Keithley Instruments",
    "tti": "TTi (Aim-TTi)",
    "ttipl": "TTi (Aim-TTi)",
    "hamamatsu": "Hamamatsu Photonics",
    "sensirion": "Sensirion",
    "weiss": "Weiss Technik",
    "pfeiffer": "Pfeiffer Vacuum",
    "newport": "Newport Corporation",
    "narda": "Narda Safety Test Solutions",
    "lumiloop": "Lumiloop GmbH",
    "iseg": "iseg Spezialelektronik",
    "obis": "Coherent (OBIS)",
    "coherent": "Coherent",
    "sutter": "Sutter Instrument",
    "labjack": "LabJack",
    "masterflex": "Cole-Parmer (Masterflex)",
    "alicat": "Alicat Scientific",
    "pylontech": "Pylontech",
    "temper": "TEMPer (PCsensor)",
    "nanonis": "SPECS (Nanonis)",
    "dps": "DPS (Ruideng)",
    "micro_fpga": "MicroFPGA",
    "debyeflex": "GE (Debyeflex)",
    "mercury": "PI (Mercury)",
    "racal": "Racal Instruments",
    "voltech": "Voltech Instruments",
    "rs_hmp": "Rohde & Schwarz",
    "vdipm": "VDI (Virginia Diodes)",
    "emc20": "Wandel & Goltermann",
    "ets2090": "ETS-Lindgren",
    "scientifica": "Scientifica",
    "zaber": "Zaber Technologies",
    "prior": "Prior Scientific",
    "spectra_iii": "Lumencor",
    "cool_led": "CoolLED",
    "grbl": "GRBL (Open Source)",
    "spidr": "Nikhef (SPIDR)",
    "timepix": "Medipix/Timepix",
    "pytuyo": "Pytuyo",
    "minitel": "France Telecom (Minitel)",
    "bimo": "BiMo Robotics",
    "aravis": "Aravis (GenICam)",
    "ocean": "Ocean Insight",
    "usbtmc": "USB TMC (Generic)",
    "usblini": "USBlini",
    "usbtin": "USBtin",
    "usb2fir": "Melexis (USB2FIR)",
    "donkeycar": "DonkeyCar (Open Source)",
    "robohat": "Robotics Masters (RoboHAT)",
    "feetech": "Feetech",
    "scpi": "SCPI (Generic)",
    "epics": "EPICS (APS)",
    "acq400": "D-TACQ Solutions",
    "acq1102": "D-TACQ Solutions",
    "acq2106": "D-TACQ Solutions",
    "mgt508": "D-TACQ Solutions",
    "pycrafter": "Texas Instruments (DLP)",
    "pylon": "Pylontech",
    "ip_camera": "Generic IP Camera",
    "webcam": "Generic Webcam",
    "video_file": "Generic Video",
    "folder_capture": "Generic Capture",
    "new_scale": "New Scale Technologies",
    "fibsem": "Thermo Fisher Scientific",
    "i_chrome": "Toptica Photonics",
    "gev": "GigE Vision (Generic)",
    "esp32": "Espressif (ESP32)",
    "rest_pi": "Raspberry Pi",
    "harvester": "GenICam (Harvester)",
    "basil": "SiLab (Basil Framework)",
    "frame_source": "Generic Frame Source",
    "nanocom": "Nanocom",
    "instru": "InstruDriver",
}

# ─────────────────────── Tag matching ───────────────────────
DEVICE_TAG_MAPPING = {
    "camera": "普通光学显微镜",
    "laser": "光化学反应器",
    "pump": "蠕动泵",
    "syringe_pump": "注射泵",
    "plunger_pump": "柱塞泵",
    "valve": "多通阀",
    "temperature": "高低温金属浴",
    "power_supply": "电热板",
    "oscilloscope": "电化学工作站",
    "spectrometer": "紫外-可见分光光谱仪",
    "signal_generator": "电化学工作站",
    "motor": "机械臂",
    "stage": "机械臂",
    "lidar": "扫描电子显微镜",
    "sensor": "电子天平",
    "robotic_arm": "机械臂",
    "robot": "机械臂",
    "gripper": "机械臂",
    "microscope": "普通光学显微镜",
    "fluorescence": "荧光显微镜",
    "sem": "扫描电子显微镜",
    "tem": "透射电子显微镜",
    "balance": "电子天平",
    "stirrer": "控温磁力搅拌器",
    "centrifuge": "离心机",
    "incubator": "微生物培养箱",
    "oven": "真空干燥箱",
    "furnace": "箱式电阻炉",
    "electrochemical": "电化学工作站",
    "pcr": "普通PCR仪",
    "flow_controller": "多通阀",
    "flow_meter": "多通阀",
    "multimeter": "电化学工作站",
    "dmm": "电化学工作站",
    "smu": "电化学工作站",
    "power_meter": "电化学工作站",
    "network_analyzer": "电化学工作站",
    "spectrum_analyzer": "电化学工作站",
    "filter_wheel": "普通光学显微镜",
    "led": "光化学反应器",
    "daq": "电化学工作站",
    "fpga": "电化学工作站",
    "vacuum": "真空干燥箱",
    "battery": "电池测试柜",
    "thermal": "热分析联用仪",
    "uv_vis": "紫外-可见分光光谱仪",
    "raman": "拉曼光谱仪",
    "ir": "红外光谱仪",
    "agv": "AGV",
    "dmd": "蒸镀仪",
    "liquid_handler": "移液工作站",
    "dispenser": "移液工作站",
}


def guess_manufacturer(folder, class_name, original):
    folder_lower = folder.lower()
    orig_lower = original.lower()
    
    for key, mfr in MANUFACTURER_MAP.items():
        if key in folder_lower or key in orig_lower:
            return mfr
    
    parts = original.split("/")
    if len(parts) >= 2:
        repo = parts[0].lower()
        for key, mfr in MANUFACTURER_MAP.items():
            if key in repo:
                return mfr
    
    return ""


def guess_tags(folder, class_name, original, description=""):
    """Match to valid tags from the CSV."""
    folder_lower = folder.lower()
    orig_lower = original.lower()
    combined = f"{folder_lower} {orig_lower} {class_name.lower()} {description.lower()}"
    
    matched_tags = []
    
    for keyword, tag_name in DEVICE_TAG_MAPPING.items():
        if keyword in combined and tag_name in VALID_TAGS:
            if tag_name not in matched_tags:
                matched_tags.append(tag_name)
    
    if not matched_tags:
        if any(kw in combined for kw in ["spectrum", "analyser", "analyzer", "signal", "rf", "power_meter", "modulation", "frequency", "attenuator", "audio"]):
            for t in ["电化学工作站"]:
                if t in VALID_TAGS and t not in matched_tags:
                    matched_tags.append(t)
        elif any(kw in combined for kw in ["camera", "imager", "vision", "capture"]):
            for t in ["普通光学显微镜"]:
                if t in VALID_TAGS and t not in matched_tags:
                    matched_tags.append(t)
        elif any(kw in combined for kw in ["serial", "controller", "switch"]):
            pass
    
    return matched_tags


def generate_device_name(folder, class_name, manufacturer, original):
    """Generate a standardized Chinese device name."""
    name_parts = []
    if manufacturer:
        name_parts.append(manufacturer)
    
    model = class_name.replace("_", " ")
    if model.startswith("class "):
        model = model[6:]
    
    device_type_map = {
        "SpectrumAnalyser": "频谱分析仪",
        "NetworkAnalyser": "网络分析仪",
        "Oscilloscope": "示波器",
        "PowerMeter": "功率计",
        "PowerSource": "直流电源",
        "PowerSourceAC": "交流电源",
        "PowerSourceDC": "直流电源",
        "SignalGenerator": "信号发生器",
        "FrequencyCounter": "频率计数器",
        "WaveformGenerator": "波形发生器",
        "ModulationMeter": "调制度分析仪",
        "AudioAnalyser": "音频分析仪",
        "FieldStrength": "场强计",
        "Attenuator": "衰减器",
        "PowerAnalyser": "功率分析仪",
        "Positioner": "定位器",
        "Switch": "开关矩阵",
        "camera": "相机",
        "laser": "激光器",
        "pump": "泵",
        "lidar": "激光雷达",
        "sensor": "传感器",
        "motor": "电机控制器",
        "microscope": "显微镜",
        "spectrometer": "光谱仪",
        "filter_wheel": "滤光轮",
        "temperature": "温控器",
        "controller": "控制器",
        "daq": "数据采集",
        "detector": "探测器",
        "led": "LED光源",
    }
    
    device_type = ""
    for key, dtype in device_type_map.items():
        if key.lower() in original.lower() or key.lower() in folder.lower():
            device_type = dtype
            break
    
    if device_type:
        name_parts.append(f"{model} {device_type}")
    else:
        name_parts.append(model)
    
    return " ".join(name_parts)


def generate_description(folder, class_name, original, manufacturer):
    """Generate a device description."""
    orig_parts = original.split("/")
    repo = orig_parts[0] if orig_parts else ""
    
    desc = f"社区驱动 - 自动集成自 {original}"
    if manufacturer:
        desc = f"{manufacturer} {class_name} 设备驱动，{desc}"
    else:
        desc = f"{class_name} 设备驱动，{desc}"
    return desc


# ─────────────────────── Extract methods from driver.py ───────────────────────
def extract_public_methods(driver_path):
    """Get all public methods from the main class in driver.py."""
    with open(driver_path, "r", errors="ignore") as f:
        source = f.read()
    
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return []
    
    all_methods = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            for item in node.body:
                if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    if not item.name.startswith("_"):
                        params = []
                        for arg in item.args.args:
                            if arg.arg != "self":
                                params.append(arg.arg)
                        defaults = item.args.defaults
                        default_offset = len(params) - len(defaults)
                        
                        param_info = {}
                        for i, p in enumerate(params):
                            di = i - default_offset
                            if di >= 0 and di < len(defaults):
                                d = defaults[di]
                                if isinstance(d, ast.Constant):
                                    param_info[p] = d.value
                                elif isinstance(d, ast.NameConstant):
                                    param_info[p] = d.value
                                else:
                                    param_info[p] = None
                            else:
                                param_info[p] = None
                        
                        all_methods.append({
                            "name": item.name,
                            "params": param_info,
                        })
            break
    
    return all_methods


def build_action_schema(method):
    """Build an action_value_mapping entry for a method."""
    props = {}
    goal_default = {}
    required = []
    
    for pname, default_val in method["params"].items():
        ptype = "string"
        if isinstance(default_val, bool):
            ptype = "boolean"
        elif isinstance(default_val, int):
            ptype = "integer"
        elif isinstance(default_val, float):
            ptype = "number"
        
        prop = {"type": ptype}
        if default_val is not None:
            prop["default"] = default_val
            goal_default[pname] = default_val
        else:
            goal_default[pname] = None
            required.append(pname)
        
        props[pname] = prop
    
    schema = {
        "description": f"{method['name']}的参数schema",
        "properties": {
            "feedback": {},
            "goal": {
                "type": "object",
                "properties": props,
            },
            "result": {},
        },
        "required": ["goal"],
        "title": f"{method['name']}参数",
        "type": "object",
    }
    
    if required:
        schema["properties"]["goal"]["required"] = required
    
    return {
        "type": "UniLabJsonCommand",
        "goal": {},
        "feedback": {},
        "result": {},
        "schema": schema,
        "goal_default": goal_default,
        "handles": {},
        "placeholder_keys": {},
    }


# ─────────────────────── Extract device entry from registry.yaml ───────────────────────
def extract_device_entry(registry_path, folder_name):
    """Extract the specific device entry from the shared registry.yaml."""
    with open(registry_path, "r", errors="ignore") as f:
        content = f.read()
    
    pattern = rf'^{re.escape(folder_name)}:\s*\n'
    m = re.search(pattern, content, re.MULTILINE)
    if not m:
        return {}
    
    block_start = m.end()
    next_key = re.search(r'^\S', content[block_start:], re.MULTILINE)
    if next_key:
        block = content[m.start():block_start + next_key.start()]
    else:
        block = content[m.start():]
    
    try:
        parsed = yaml.safe_load(block)
        if isinstance(parsed, dict) and folder_name in parsed:
            return parsed[folder_name]
    except:
        pass
    
    return {}


# ─────────────────────── Main processing ───────────────────────
def main():
    with open(REAL_DEVICES_JSON) as f:
        real_devices = json.load(f)
    
    print(f"Processing {len(real_devices)} real devices...")
    
    success_count = 0
    error_count = 0
    
    for dev in real_devices:
        folder = dev["folder"]
        class_name = dev["class_name"]
        original = dev["original"]
        
        driver_path = COMMUNITY_DIR / folder / "driver.py"
        registry_path = COMMUNITY_DIR / folder / "registry.yaml"
        
        # 1. Extract public methods
        methods = extract_public_methods(str(driver_path))
        
        # 2. Extract existing registry entry
        existing_entry = extract_device_entry(str(registry_path), folder)
        
        # 3. Build action_value_mappings
        existing_actions = {}
        if existing_entry and "class" in existing_entry:
            existing_actions = existing_entry.get("class", {}).get("action_value_mappings", {}) or {}
        
        action_mappings = dict(existing_actions)
        for method in methods:
            action_key = f"auto-{method['name']}"
            if action_key not in action_mappings:
                action_mappings[action_key] = build_action_schema(method)
        
        # 4. Get module path from existing entry
        module_path = ""
        if existing_entry and "class" in existing_entry:
            module_path = existing_entry.get("class", {}).get("module", "")
        
        if not module_path:
            module_path = f"unilabos.devices.community.{folder}:{class_name}"
        
        # 5. Get status_types from existing
        status_types = {}
        if existing_entry and "class" in existing_entry:
            status_types = existing_entry.get("class", {}).get("status_types", {}) or {}
        
        # 6. Get category from existing
        category = ["generic"]
        if existing_entry:
            cat = existing_entry.get("category", [])
            if cat:
                category = cat if isinstance(cat, list) else [cat]
        
        # 7. Fill Device Square params
        manufacturer = guess_manufacturer(folder, class_name, original)
        tags = guess_tags(folder, class_name, original)
        name = generate_device_name(folder, class_name, manufacturer, original)
        description = generate_description(folder, class_name, original, manufacturer)
        
        source_repo = original.split("/")[0] if "/" in original else original
        
        device_params = {
            "品牌": manufacturer if manufacturer else "社区开源",
            "型号": class_name,
            "设备类型": category[0] if category else "generic",
            "来源仓库": source_repo,
            "驱动类": class_name,
        }
        
        scene = {
            "domain": "Laboratory Automation",
            "scene_name": "Instrument Control",
            "step": "Measurement",
        }
        
        model_info = {
            "name": f"{class_name}",
            "type": "device",
        }
        
        # 8. Get init_param_schema from existing
        init_param = {}
        if existing_entry:
            init_param = existing_entry.get("init_param_schema", {})
        if not init_param:
            init_param = {
                "config": {
                    "type": "object",
                    "properties": {},
                    "required": [],
                },
            }
        
        # 9. Build final YAML entry
        device_key = f"community.ba.{folder}"
        entry = {
            device_key: {
                "name": name,
                "category": category,
                "class": {
                    "module": module_path,
                    "type": "python",
                    "status_types": status_types,
                    "action_value_mappings": action_mappings,
                },
                "config_info": [],
                "cover": "",
                "description": description,
                "device_params": device_params,
                "handles": [],
                "icon": "",
                "init_param_schema": init_param,
                "manufacturer": manufacturer,
                "model": model_info,
                "resource_type": "device",
                "scene": scene,
                "tags": tags,
                "version": "1.0.0",
            }
        }
        
        # 10. Write individual YAML
        out_filename = f"community_ba_{folder}.yaml"
        out_path = REGISTRY_OUT_DIR / out_filename
        
        try:
            with open(out_path, "w", encoding="utf-8") as f:
                yaml.dump(entry, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
            success_count += 1
        except Exception as e:
            print(f"  ERROR writing {out_filename}: {e}")
            error_count += 1
        
        # 11. Update startup.json to use the new device key
        startup_path = COMMUNITY_DIR / folder / "startup.json"
        if startup_path.exists():
            try:
                with open(startup_path) as f:
                    startup = json.load(f)
                
                if "nodes" in startup and len(startup["nodes"]) > 0:
                    startup["nodes"][0]["class"] = device_key
                    startup["nodes"][0]["name"] = name
                
                with open(startup_path, "w", encoding="utf-8") as f:
                    json.dump(startup, f, indent=2, ensure_ascii=False)
            except Exception as e:
                print(f"  ERROR updating startup.json for {folder}: {e}")
    
    print(f"\nDone! Generated {success_count} YAML files, {error_count} errors.")
    print(f"Output directory: {REGISTRY_OUT_DIR}")


if __name__ == "__main__":
    main()
