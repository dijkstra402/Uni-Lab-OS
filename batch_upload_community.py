"""
Batch upload all community device drivers to the lab.
Uses subprocess with timeout to handle each device.
"""
import subprocess, json, sys, os, time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REAL_DEVICES_JSON = os.path.join(BASE_DIR, "real_devices.json")

UPLOAD_CMD_TEMPLATE = [
    "/Users/sml/miniforge3/envs/unilab/bin/python3.11",
    "-u",  # unbuffered
    "-m", "unilabos.app.main",
    "-g", "{startup_json}",
    "--ak", "87e83cd4-eb45-4e2a-a287-cfae8637bd6a",
    "--sk", "9187b2cc-c38f-4392-be08-2aa988b2a2c6",
    "--upload_registry",
    "--addr", "test",
    "--disable_browser",
]

TIMEOUT = 120

def main():
    with open(REAL_DEVICES_JSON) as f:
        devices = json.load(f)

    print(f"Total devices to upload: {len(devices)}")

    success = []
    failed = []
    skipped = []

    env = {
        "HOME": os.environ.get("HOME", ""),
        "PATH": "/Users/sml/miniforge3/envs/unilab/bin:/usr/bin:/bin:/usr/sbin",
    }

    for i, dev in enumerate(devices):
        folder = dev["folder"]
        startup_json = os.path.join(BASE_DIR, "community_drivers", folder, "startup.json")

        if not os.path.exists(startup_json):
            print(f"[{i+1}/{len(devices)}] SKIP {folder}: no startup.json")
            skipped.append(folder)
            continue

        cmd = [c.replace("{startup_json}", startup_json) for c in UPLOAD_CMD_TEMPLATE]

        print(f"[{i+1}/{len(devices)}] Uploading {folder}...", end=" ", flush=True)
        start = time.time()

        try:
            result = subprocess.run(
                cmd,
                cwd=BASE_DIR,
                env=env,
                capture_output=True,
                text=True,
                timeout=TIMEOUT,
            )

            elapsed = time.time() - start
            output = result.stdout + result.stderr

            if "成功注册" in output:
                reg_line = [l for l in output.split("\n") if "成功注册" in l]
                print(f"OK ({elapsed:.1f}s) {reg_line[0].split('成功注册')[1].strip() if reg_line else ''}")
                success.append(folder)
            elif "注册失败" in output or "注册异常" in output:
                err_line = [l for l in output.split("\n") if "注册失败" in l or "注册异常" in l]
                print(f"FAIL ({elapsed:.1f}s) {err_line[0] if err_line else ''}")
                failed.append((folder, "registration failed"))
            elif result.returncode == 0:
                if "注册表设置完成" in output:
                    print(f"OK ({elapsed:.1f}s) registry loaded")
                    success.append(folder)
                else:
                    print(f"OK? ({elapsed:.1f}s) rc=0 but no explicit success msg")
                    success.append(folder)
            else:
                last_lines = output.strip().split("\n")[-3:]
                print(f"ERROR ({elapsed:.1f}s) rc={result.returncode}")
                for l in last_lines:
                    print(f"    {l[:200]}")
                failed.append((folder, f"rc={result.returncode}"))

        except subprocess.TimeoutExpired:
            print(f"TIMEOUT ({TIMEOUT}s)")
            failed.append((folder, "timeout"))
        except Exception as e:
            print(f"EXCEPTION: {e}")
            failed.append((folder, str(e)))

    print(f"\n{'='*60}")
    print(f"Results: {len(success)} success, {len(failed)} failed, {len(skipped)} skipped")
    print(f"{'='*60}")

    if failed:
        print(f"\nFailed devices:")
        for folder, reason in failed:
            print(f"  {folder}: {reason}")

    with open(os.path.join(BASE_DIR, "upload_results.json"), "w") as f:
        json.dump({
            "success": success,
            "failed": [{"folder": f, "reason": r} for f, r in failed],
            "skipped": skipped,
        }, f, indent=2, ensure_ascii=False)

    print(f"\nResults saved to upload_results.json")

if __name__ == "__main__":
    main()
