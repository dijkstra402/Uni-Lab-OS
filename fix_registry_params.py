"""
Fix registry parameters for all 185 community devices:
1. Fill missing manufacturer (from CSV match or manual mapping)
2. Assign proper tags from tag标签列表.csv
3. Fix bad device names
"""
import csv, json, re, os, sys
from pathlib import Path

BASE = Path(__file__).parent
TAG_CSV = Path("/Users/sml/work/Uni-Lab-OS/tag 标签列表.csv")
INSTR_CSV = Path("/Users/sml/work/Uni-Lab-OS/1_instruments_merged_dedup.csv")
REAL_DEVICES = BASE / "real_devices.json"
YAML_DIR = BASE / "unilabos" / "registry" / "devices"

# ── Load valid tags ──
def load_tags():
    tags = {}
    with open(TAG_CSV, encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            t = row.get("type", "").strip().strip('"')
            n = row.get("name", "").strip().strip('"')
            if t == "device_template_tag" and n:
                tags[n] = n
    return tags

VALID_TAGS = load_tags()

# ── Load instrument CSV for manufacturer/brand matching ──
def load_instruments():
    instruments = []
    with open(INSTR_CSV, encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            instruments.append({
                "brand": (row.get("品牌") or "").strip(),
                "model": (row.get("型号") or "").strip(),
                "name": (row.get("产品名称") or "").strip(),
                "manufacturer": (row.get("生产厂家") or "").strip(),
                "category1": (row.get("分类_一级") or "").strip(),
                "category2": (row.get("分类_二级") or "").strip(),
                "category3": (row.get("分类_三级") or "").strip(),
            })
    return instruments

print("Loading instruments CSV...")
INSTRUMENTS = load_instruments()
print(f"  Loaded {len(INSTRUMENTS)} instruments")

# ── Keyword → tag mapping ──
KEYWORD_TO_TAG = {
    "camera": "普通光学显微镜",
    "microscope": "普通光学显微镜",
    "显微镜": "普通光学显微镜",
    "fluorescence": "荧光显微镜",
    "laser": "光化学反应器",
    "激光": "光化学反应器",
    "spectrometer": "紫外-可见分光光谱仪",
    "光谱": "紫外-可见分光光谱仪",
    "raman": "拉曼光谱仪",
    "uvvis": "紫外-可见分光光谱仪",
    "uv-vis": "紫外-可见分光光谱仪",
    "oscilloscope": "电化学工作站",
    "示波器": "电化学工作站",
    "power_supply": "电化学工作站",
    "直流电源": "电化学工作站",
    "psu": "电化学工作站",
    "pump": "蠕动泵",
    "泵": "蠕动泵",
    "syringe": "注射泵",
    "注射": "注射泵",
    "peristaltic": "蠕动泵",
    "flow_controller": "蠕动泵",
    "flow_meter": "蠕动泵",
    "valve": "多通阀",
    "阀": "多通阀",
    "motor": "机械臂",
    "电机": "机械臂",
    "servo": "机械臂",
    "controller": "电化学工作站",
    "控制器": "电化学工作站",
    "temperature": "高低温金属浴",
    "thermostat": "高低温金属浴",
    "heater": "电热板",
    "chiller": "冷热水机",
    "cooler": "冷热水机",
    "冷": "冷热水机",
    "balance": "电子天平",
    "天平": "电子天平",
    "centrifuge": "离心机",
    "离心": "离心机",
    "shaker": "恒温摇床",
    "摇床": "恒温摇床",
    "stirrer": "控温磁力搅拌器",
    "搅拌": "控温磁力搅拌器",
    "detector": "电化学工作站",
    "数据采集": "电化学工作站",
    "daq": "电化学工作站",
    "acquisition": "电化学工作站",
    "lidar": "AGV",
    "雷达": "AGV",
    "gps": "AGV",
    "robot": "机械臂",
    "机器人": "机械臂",
    "gripper": "机械臂",
    "positioning": "机械臂",
    "定位": "机械臂",
    "stage": "机械臂",
    "filter_wheel": "普通光学显微镜",
    "filter": "过滤器",
    "dmd": "光化学反应器",
    "led": "光化学反应器",
    "光源": "光化学反应器",
    "power_meter": "电化学工作站",
    "功率计": "电化学工作站",
    "signal_generator": "电化学工作站",
    "信号发生器": "电化学工作站",
    "network_analyzer": "电化学工作站",
    "网络分析": "电化学工作站",
    "spectrum_analyzer": "电化学工作站",
    "频谱": "电化学工作站",
    "multimeter": "电化学工作站",
    "万用表": "电化学工作站",
    "gpio": "电化学工作站",
    "i2c": "电化学工作站",
    "spi": "电化学工作站",
    "serial": "电化学工作站",
    "socket": "电化学工作站",
    "tcp": "电化学工作站",
    "usb": "电化学工作站",
    "visa": "电化学工作站",
    "scpi": "电化学工作站",
    "epics": "电化学工作站",
    "webcam": "普通光学显微镜",
    "video": "普通光学显微镜",
    "image": "普通光学显微镜",
    "battery": "电池测试柜",
    "电池": "电池测试柜",
    "sem": "扫描电子显微镜",
    "tem": "透射电子显微镜",
    "xrd": "X射线衍射仪",
    "nmr": "核磁共振波谱仪",
    "hplc": "液相色谱质谱联用仪",
    "gc": "气相色谱质谱联用仪",
    "pcr": "实时定量PCR仪",
    "sensor": "电化学工作站",
    "传感器": "电化学工作站",
    "humidity": "电化学工作站",
    "pressure": "电化学工作站",
    "vacuum": "电化学工作站",
    "真空": "电化学工作站",
    "干燥": "真空干燥箱",
    "oven": "真空干燥箱",
    "furnace": "箱式电阻炉",
    "incubator": "微生物培养箱",
    "培养箱": "微生物培养箱",
    "field_strength": "电化学工作站",
    "场强": "电化学工作站",
    "attenuator": "电化学工作站",
    "衰减": "电化学工作站",
    "audio": "电化学工作站",
    "音频": "电化学工作站",
}

# ── Manual manufacturer mapping for 40 devices without manufacturer ──
MANUAL_MANUFACTURER = {
    "aisa_kestrel_camera": "Specim",
    "anaheim_automation_smc40": "Anaheim Automation",
    "bode100": "Omicron Lab",
    "camera_device": "Generic Camera",
    "camera_interface": "Generic Camera",
    "camera_pi_cam": "Raspberry Pi",
    "camera_redis_daemon": "Generic Camera",
    "daq__detector": "PyMoDAQ",
    "daq__move": "PyMoDAQ",
    "daq__move__hardware": "PyMoDAQ",
    "data_device": "Micro-Manager",
    "debug_echo_device": "Generic",
    "debug_physical_device": "Micro-Manager",
    "digital_io": "Micro-Manager",
    "echo_device": "Generic",
    "flow_controller": "Alicat Scientific",
    "frame_grabber": "Generic",
    "it63_xx": "ITECH",
    "ja_socket": "Generic",
    "ja_visa": "Generic",
    "k2015": "Keithley Instruments",
    "laser_power_control": "Generic Laser",
    "mi6960": "MI Technologies",
    "mi_wave5nn": "MI-Wave",
    "mighty_mini": "Harvard Apparatus",
    "motor_control": "Generic",
    "ndram_dataset_java": "D-TACQ Solutions",
    "open_cv_camera": "Generic Camera",
    "oscilloscope_device": "Generic",
    "phd2000": "Harvard Apparatus",
    "pump": "Harvard Apparatus",
    "py_uvvis": "Generic",
    "ra_scmu200_audio": "Rohde & Schwarz",
    "scanner_interface": "Generic",
    "serial_device": "Generic",
    "shared_serial": "Micro-Manager",
    "source_ac": "Generic",
    "spectrometer": "Ocean Insight",
    "tcp_sampler": "Generic",
    "x_keys_device": "P.I. Engineering",
}

# ── Manual name fixes for devices with bad names ──
MANUAL_NAME_FIX = {
    "bode100": "Omicron Lab Bode 100 网络分析仪",
    "camera_device": "通用 CameraDevice 相机",
    "camera_interface": "通用 CameraInterface 相机",
    "camera_pi_cam": "Raspberry Pi Camera 相机",
    "camera_redis_daemon": "通用 Redis Camera 相机",
    "data_device": "Micro-Manager DataDevice 控制器",
    "debug_echo_device": "通用 EchoDevice 调试设备",
    "debug_physical_device": "Micro-Manager PhysicalDevice 调试设备",
    "digital_io": "Micro-Manager DigitalIO 数字IO",
    "echo_device": "通用 EchoDevice 调试设备",
    "flow_controller": "Alicat Scientific FlowController 流量控制器",
    "frame_grabber": "通用 FrameGrabber 图像采集卡",
    "it63_xx": "ITECH IT63XX 直流电源",
    "ja_socket": "通用 Socket 通信接口",
    "ja_visa": "通用 VISA 通信接口",
    "k2015": "Keithley 2015 万用表",
    "laser_power_control": "通用 LaserPowerControl 激光功率控制器",
    "mi6960": "MI Technologies MI6960 功率计",
    "mi_wave5nn": "MI-Wave MI-Wave5nn 衰减器",
    "motor_control": "通用 MotorControl 电机控制器",
    "ndram_dataset_java": "D-TACQ Solutions NDRAM 数据集",
    "open_cv_camera": "通用 OpenCV Camera 相机",
    "oscilloscope_device": "通用 Oscilloscope 示波器",
    "phd2000": "Harvard Apparatus PHD2000 注射泵",
    "pump": "Harvard Apparatus Pump 泵",
    "py_uvvis": "通用 pyUVVIS 紫外可见光谱仪",
    "scanner_interface": "通用 ScannerInterface 扫描接口",
    "serial_device": "通用 SerialDevice 串口设备",
    "shared_serial": "Micro-Manager SharedSerial 串口复用器",
    "source_ac": "通用 SourceAC 交流电源",
    "spectrometer": "Ocean Insight 光谱仪",
    "tcp_sampler": "通用 TcpSampler 采样器",
    "x_keys_device": "P.I. Engineering X-Keys 输入设备",
    "mighty_mini": "Harvard Apparatus MightyMini 泵",
    "camera_esp32_cam_serial": "Espressif ESP32-CAM 串口相机",
    "camera_pi_cam": "Raspberry Pi PiCamera 相机",
    "ra_scmu200_audio": "Rohde & Schwarz CMU200 音频分析仪",
}


def infer_tag(folder, name, description, driver_source_path=""):
    """Infer best tag from device info using keyword matching."""
    search_text = f"{folder} {name} {description} {driver_source_path}".lower()

    for keyword, tag in KEYWORD_TO_TAG.items():
        if keyword.lower() in search_text:
            if tag in VALID_TAGS:
                return tag

    return list(VALID_TAGS.keys())[0] if VALID_TAGS else ""


def try_match_instrument(folder, name, manufacturer):
    """Try to match device against instruments CSV for better info."""
    search_terms = [folder.replace("_", " "), name]
    if manufacturer:
        search_terms.append(manufacturer)

    for inst in INSTRUMENTS:
        for term in search_terms:
            term_lower = term.lower()
            if (term_lower in inst["brand"].lower()
                or term_lower in inst["model"].lower()
                or term_lower in inst["name"].lower()
                or inst["brand"].lower() in term_lower):
                return inst
    return None


def fix_yaml(folder, yaml_path):
    """Fix a single device YAML file. Returns dict of changes made."""
    with open(yaml_path, encoding="utf-8") as f:
        content = f.read()

    changes = {}
    key = f"community.ba.{folder}"

    # Extract current values
    name_m = re.search(r"^  name:\s*(.+)$", content, re.MULTILINE)
    name = name_m.group(1).strip().strip("'\"") if name_m else ""

    mfr_m = re.search(r"^  manufacturer:\s*(.+)$", content, re.MULTILINE)
    mfr = mfr_m.group(1).strip().strip("'\"") if mfr_m else ""

    desc_m = re.search(r"^  description:\s*(.+)$", content, re.MULTILINE)
    desc = desc_m.group(1).strip().strip("'\"") if desc_m else ""

    # Extract source path from description for context
    src_m = re.search(r"自动集成自\s+(\S+)", desc)
    src_path = src_m.group(1) if src_m else ""

    # ── Fix manufacturer ──
    if not mfr:
        if folder in MANUAL_MANUFACTURER:
            new_mfr = MANUAL_MANUFACTURER[folder]
        else:
            inst = try_match_instrument(folder, name, "")
            new_mfr = inst["brand"] or inst["manufacturer"] if inst else ""
        if new_mfr:
            old_line = mfr_m.group(0) if mfr_m else None
            if old_line:
                content = content.replace(old_line, f"  manufacturer: {new_mfr}")
            else:
                content = content.replace(f"  name: {name}", f"  name: {name}\n  manufacturer: {new_mfr}")
            mfr = new_mfr
            changes["manufacturer"] = new_mfr

    # ── Fix name ──
    if folder in MANUAL_NAME_FIX:
        new_name = MANUAL_NAME_FIX[folder]
        if new_name != name:
            content = content.replace(f"  name: {name}", f"  name: {new_name}")
            changes["name"] = f"{name} -> {new_name}"
            name = new_name

    # ── Fix tags ──
    tags_m = re.search(r"^  tags:\s*\[([^\]]*)\]", content, re.MULTILINE)
    tags_block = re.search(r"^  tags:\s*\n((?:  - .+\n)*)", content, re.MULTILINE)

    has_tags = False
    if tags_m and tags_m.group(1).strip():
        existing = [t.strip().strip("'\"") for t in tags_m.group(1).split(",") if t.strip()]
        valid_existing = [t for t in existing if t in VALID_TAGS]
        has_tags = bool(valid_existing)
    elif tags_block and tags_block.group(1).strip():
        existing_lines = tags_block.group(1).strip().split("\n")
        existing = [l.strip().lstrip("- ").strip("'\"") for l in existing_lines]
        valid_existing = [t for t in existing if t in VALID_TAGS]
        has_tags = bool(valid_existing)

    if not has_tags:
        tag = infer_tag(folder, name, desc, src_path)
        if tag and tag in VALID_TAGS:
            if tags_m:
                content = content.replace(tags_m.group(0), f"  tags:\n  - {tag}")
            elif tags_block:
                content = content.replace(tags_block.group(0), f"  tags:\n  - {tag}\n")
            else:
                content = content.replace(f"  name: {name}", f"  name: {name}\n  tags:\n  - {tag}")
            changes["tags"] = tag

    with open(yaml_path, "w", encoding="utf-8") as f:
        f.write(content)

    return changes


def main():
    with open(REAL_DEVICES, encoding="utf-8") as f:
        real_devices = json.load(f)

    total = 0
    mfr_fixed = 0
    tags_fixed = 0
    names_fixed = 0

    for dev in real_devices:
        folder = dev["folder"]
        yaml_path = YAML_DIR / f"community_ba_{folder}.yaml"
        if not yaml_path.exists():
            continue

        total += 1
        changes = fix_yaml(folder, yaml_path)

        if "manufacturer" in changes:
            mfr_fixed += 1
        if "tags" in changes:
            tags_fixed += 1
        if "name" in changes:
            names_fixed += 1

        if changes:
            print(f"  {folder}: {changes}")

    print(f"\n{'='*60}")
    print(f"总计: {total} 个设备")
    print(f"修复厂商: {mfr_fixed}")
    print(f"修复标签: {tags_fixed}")
    print(f"修复名称: {names_fixed}")


if __name__ == "__main__":
    main()
