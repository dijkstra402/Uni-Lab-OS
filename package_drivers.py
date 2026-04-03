#!/usr/bin/env python3
"""Batch package 185 community drivers into LabDeviceTemplate format.

For each driver:
1. Strip build-agent boilerplate (Qt shim, debug logger, vendor path)
2. Remove injected debug lines (_unilab_logger.debug / print("[UNILAB]"))
3. Keep original class logic intact
4. Create package: {name}/{name}/driver.py + __init__.py + requirements.txt
5. Detect external dependencies for requirements.txt
"""

import json
import os
import re
import sys

COMMUNITY_DIR = "community_drivers"
OUTPUT_DIR = "packaged_drivers"

IMPORT_TO_PIP = {
    "serial": "pyserial",
    "minimalmodbus": "minimalmodbus",
    "pyvisa": "pyvisa",
    "visa": "pyvisa",
    "usb": "pyusb",
    "numpy": "numpy",
    "scipy": "scipy",
    "matplotlib": "matplotlib",
    "PIL": "Pillow",
    "cv2": "opencv-python",
    "skimage": "scikit-image",
    "nidaqmx": "nidaqmx",
    "pymodbus": "pymodbus",
    "can": "python-can",
    "smbus2": "smbus2",
    "spidev": "spidev",
    "RPi": "RPi.GPIO",
    "ftd2xx": "ftd2xx",
    "pylablib": "pylablib",
    "thorlabs_apt": "thorlabs-apt",
    "zaber_motion": "zaber-motion",
    "pyftdi": "pyftdi",
}

STDLIB_MODULES = {
    "os", "sys", "time", "struct", "socket", "logging", "re", "json",
    "threading", "queue", "collections", "enum", "abc", "math", "copy",
    "functools", "itertools", "pathlib", "io", "subprocess", "signal",
    "ctypes", "array", "binascii", "codecs", "datetime", "decimal",
    "fractions", "glob", "hashlib", "hmac", "http", "inspect",
    "operator", "pickle", "pprint", "random", "shutil", "string",
    "tempfile", "textwrap", "traceback", "types", "typing", "unittest",
    "urllib", "uuid", "warnings", "weakref", "xml", "argparse",
    "configparser", "csv", "contextlib", "dataclasses", "heapq",
    "multiprocessing", "platform", "select", "selectors", "stat",
    "statistics", "bisect", "errno", "timeit", "atexit", "importlib",
    "numbers", "ntpath", "asyncio", "base64", "fcntl", "termios",
    "faulthandler", "concurrent",
}

# False-positive imports to skip (comments parsed as imports, internal refs, etc.)
SKIP_IMPORTS = {
    "the", "tests", "src", "drivers",
}

# Boilerplate patterns to remove
BOILERPLATE_END_MARKER = re.compile(
    r'_sys\.path\.insert\(0,\s*str\(_vendor_root\)\)'
)
QT_SHIM_START = re.compile(r'^if\s+"lantz\.utils\.qt"\s+not\s+in\s+_sys\.modules')
DEBUG_LOGGER_START = re.compile(r'^_unilab_logger\s*=\s*logging\.getLogger')
VENDOR_PATH_START = re.compile(r'^# Vendored repo packages')

DEBUG_LINE = re.compile(r'^\s*_unilab_logger\.debug\(.*\)\s*$')
UNILAB_PRINT = re.compile(r'^\s*print\("\[UNILAB\].*\)\s*$')


EXTRA_DEVICES = [
    "_asi_controller", "a_star_speed", "afms", "agilent33210_a",
    "arduino_encoder", "crsf_joy_bridge", "d435_rgb_stream", "dmm",
    "filter_wheel", "i7540d", "meter_care_lite", "mso5k",
    "prior", "py_spec_client", "reader", "rotary_encoder",
    "sdm630", "serial_controller", "stpdrv", "tf_mini",
    "tron1_bridge", "tron1_odom_bridge",
]


def get_device_folders():
    """Get list of real device folder names (185 original + 22 extra)."""
    with open(os.path.join(COMMUNITY_DIR, "all_devices_startup.json")) as f:
        data = json.load(f)
    folders = [n["id"].replace("test_", "") for n in data.get("nodes", [])]
    for extra in EXTRA_DEVICES:
        if extra not in folders:
            folders.append(extra)
    return folders


def strip_boilerplate(lines):
    """Remove build-agent boilerplate, return clean code lines.

    Strategy: find the end of the boilerplate block, then keep everything after.
    The boilerplate always ends with either:
    - _sys.path.insert(0, str(_vendor_root))  (vendor path)
    - _unilab_logger.addHandler(_handler)     (debug logger, no vendor)
    """
    content = "".join(lines)

    # Find the end of boilerplate
    cut_idx = None

    # Try vendor path end marker first
    vendor_end = re.search(
        r'_sys\.path\.insert\(0,\s*str\(_vendor_root\)\)\n',
        content,
    )
    if vendor_end:
        cut_idx = vendor_end.end()

    # Try debug logger end marker
    if cut_idx is None:
        logger_end = re.search(
            r'_unilab_logger\.addHandler\(_handler\)\n',
            content,
        )
        if logger_end:
            cut_idx = logger_end.end()

    # Try Qt shim end marker
    if cut_idx is None:
        qt_end = re.search(
            r'_sys\.modules\["lantz\.utils\.qt"\]\s*=\s*_qt_mod\n',
            content,
        )
        if qt_end:
            cut_idx = qt_end.end()

    if cut_idx is not None:
        content = content[cut_idx:]
    else:
        # No boilerplate found - try stripping the docstring at least
        m = re.match(r'^""".*?"""\n', content, re.DOTALL)
        if m:
            content = content[m.end():]

    # Remove debug logging lines
    content = re.sub(r'^\s*_unilab_logger\.debug\([^\n]*\n', '', content, flags=re.MULTILINE)

    # Remove UNILAB print lines
    content = re.sub(r'^\s*print\("\[UNILAB\][^\n]*\n', '', content, flags=re.MULTILINE)

    # Remove leftover boilerplate comments
    content = re.sub(r'^# Unilab 驱动调试日志\n', '', content, flags=re.MULTILINE)

    # Strip leading blank lines
    content = content.lstrip('\n')

    return content.splitlines(keepends=True)


def detect_imports(lines):
    """Detect import statements and return set of top-level module names."""
    imports = set()
    for line in lines:
        stripped = line.strip()
        m = re.match(r'^import\s+(\w+)', stripped)
        if m:
            imports.add(m.group(1))
        m = re.match(r'^from\s+(\w+)', stripped)
        if m:
            imports.add(m.group(1))
    return imports


def get_requirements(imports, folder_name):
    """Convert import names to pip package names, excluding stdlib and vendored."""
    reqs = set()
    for mod in imports:
        if mod in STDLIB_MODULES:
            continue
        if mod in SKIP_IMPORTS:
            continue
        if mod.startswith("_"):
            continue
        if mod in ("basil",):
            reqs.add("pyserial")
            continue
        if mod in ("lantz",):
            continue
        if mod in IMPORT_TO_PIP:
            reqs.add(IMPORT_TO_PIP[mod])
        else:
            reqs.add(mod)
    return sorted(reqs)


def find_classes(lines):
    """Find class names defined in the file."""
    classes = []
    for line in lines:
        m = re.match(r'^class\s+(\w+)', line)
        if m:
            classes.append(m.group(1))
    return classes


def package_driver(folder_name):
    """Package a single community driver."""
    src_dir = os.path.join(COMMUNITY_DIR, folder_name)
    driver_path = os.path.join(src_dir, "driver.py")

    if not os.path.isfile(driver_path):
        return None

    with open(driver_path, "r", encoding="utf-8", errors="replace") as f:
        raw_lines = f.readlines()

    clean_lines = strip_boilerplate(raw_lines)
    if not clean_lines:
        return {"folder": folder_name, "error": "empty after stripping"}

    imports = detect_imports(clean_lines)
    requirements = get_requirements(imports, folder_name)
    classes = find_classes(clean_lines)

    # Create output package
    pkg_dir = os.path.join(OUTPUT_DIR, folder_name)
    inner_dir = os.path.join(pkg_dir, folder_name)
    os.makedirs(inner_dir, exist_ok=True)

    # Write cleaned driver
    driver_out = os.path.join(inner_dir, f"{folder_name}.py")
    with open(driver_out, "w", encoding="utf-8") as f:
        f.writelines(clean_lines)

    # Write __init__.py with version
    init_out = os.path.join(inner_dir, "__init__.py")
    with open(init_out, "w", encoding="utf-8") as f:
        f.write(f'"""Uni-Lab-OS device package: {folder_name}"""\n\n')
        f.write('__version__ = "0.1.0"\n')

    # Write requirements.txt
    req_out = os.path.join(pkg_dir, "requirements.txt")
    with open(req_out, "w", encoding="utf-8") as f:
        for r in requirements:
            f.write(r + "\n")

    return {
        "folder": folder_name,
        "classes": classes,
        "requirements": requirements,
        "lines": len(clean_lines),
    }


def main():
    folders = get_device_folders()
    print(f"Packaging {len(folders)} drivers...\n")

    results = []
    errors = []

    for folder in folders:
        result = package_driver(folder)
        if result is None:
            errors.append({"folder": folder, "error": "driver.py not found"})
        elif "error" in result:
            errors.append(result)
        else:
            results.append(result)

    # Summary
    print(f"\n{'='*60}")
    print(f"Successfully packaged: {len(results)}/{len(folders)}")
    if errors:
        print(f"Errors: {len(errors)}")
        for e in errors:
            print(f"  - {e['folder']}: {e.get('error', 'unknown')}")

    # Show requirements distribution
    all_reqs = {}
    for r in results:
        for req in r["requirements"]:
            all_reqs[req] = all_reqs.get(req, 0) + 1

    print(f"\nDependency distribution:")
    for req, count in sorted(all_reqs.items(), key=lambda x: -x[1]):
        print(f"  {req}: {count} drivers")

    print(f"\nPackages written to: {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
