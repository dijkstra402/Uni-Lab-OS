"""
Step 1: Filter community_drivers/ to identify real instrument/device drivers.
Outputs a JSON list of confirmed devices.
"""
import os, re, json, ast, sys

COMMUNITY_DIR = os.path.join(os.path.dirname(__file__), "community_drivers")

def get_class_info(driver_path):
    """Extract class names, parents, and public methods from driver.py using AST."""
    with open(driver_path, "r", errors="ignore") as f:
        source = f.read()

    orig_match = re.search(r"Original:\s*(.+)", source)
    original = orig_match.group(1).strip() if orig_match else ""

    try:
        tree = ast.parse(source)
    except SyntaxError:
        return original, []

    classes = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            parents = []
            for base in node.bases:
                if isinstance(base, ast.Name):
                    parents.append(base.id)
                elif isinstance(base, ast.Attribute):
                    parents.append(ast.dump(base))
            methods = [
                n.name for n in node.body
                if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
                and not n.name.startswith("_")
            ]
            classes.append({
                "name": node.name,
                "parents": parents,
                "methods": methods,
                "lineno": node.lineno,
            })
    return original, classes


# Folder name patterns that indicate NOT a device
NOT_DEVICE_FOLDER_PATTERNS = [
    r"^__",                   # private/internal helpers
    r"^_[a-z]",               # internal classes
    r"_writer$",              # file writers
    r"_reader$",              # file readers
    r"_graphic$",             # UI graphics
    r"^graphic$",
    r"^interval_graphic$", r"^lattice_graphic$", r"^line_type_graphic$",
    r"^point_type_graphic$", r"^rectangle_type_graphic$", r"^ring_graphic$",
    r"^spot_graphic$", r"^wedge_graphic$",
    r"^data_group$", r"^data_item$", r"^data_mixer$",
    r"^display_data_channel$", r"^display_item$",
    r"^persistent_object$", r"^persistent_property$", r"^persistent_storage_system$",
    r"^file_persistent_storage_system$", r"^file_project_storage_system$",
    r"^memory_persistent_storage_system$", r"^memory_project_storage_system$",
    r"^interval_list_connection$", r"^property_connection$",
    r"^h5_backend$", r"^h5_browser$", r"^hdf5_file_entry$",
    r"^view2_d$", r"^viewer1_d$", r"^viewer_nd$",
    r"^scene$", r"^entity$", r"^goal$",
    r"^loader_plotter$", r"^dash_board$",
    r"^editor_controller$", r"^files_controller$",
    r"^signal$", r"^notifier$",
    r"^i_backend$", r"^i_stream$",
    r"^stream_pipe$", r"^stream_serial$", r"^stream_socket$",
    r"^tun_interface$", r"^hdlc$",
    r"^catalog$", r"^manifest$", r"^seekable$", r"^tub$",
    r"^flask_service$",
    r"^generic_optimization$",
]

# Source path patterns indicating utility/framework code
NOT_DEVICE_SRC_PATTERNS = [
    r"/model/", r"/models/", r"/io/", r"/utils/", r"/util/",
    r"/management/", r"/scripting/", r"/frontend/",
    r"Graphics\.py", r"DisplayItem\.py", r"Persistence\.py",
    r"FileStorageSystem\.py", r"Connection\.py", r"DataGroup\.py",
    r"DataItem\.py", r"datastore", r"/network\.py",
]

# Source path patterns strongly indicating a device
DEVICE_SRC_PATTERNS = [
    r"/HL/", r"/drivers/", r"/devices/", r"/instruments/",
    r"/interfaces/", r"/sources/", r"/detectors/",
    r"/cameras/", r"/spectrometers/", r"/filterwheels?/",
    r"/actuator", r"/lidar", r"/sensor",
    r"/controllers/", r"/lantzdrivers",
    r"PowerMeter/", r"PowerSource", r"SignalGenerator/",
    r"SpectrumAnalyser/", r"NetworkAnalyser/", r"Oscilloscope/",
    r"FieldStrength/", r"PowerAnalyser/", r"Positioner/",
    r"/cobolt", r"/pumpy", r"masterflexserial",
]

# Hardware-related base class keywords
HARDWARE_PARENTS = [
    "hardwarelayer", "device", "instrument", "driver", "camera",
    "laser", "stage", "controller", "bus", "microscope",
    "source", "motor", "sensor", "scpi", "detector",
    "flowmeter", "flowcontroller", "pump",
]

# Known non-device folders (manually verified)
KNOWN_NON_DEVICES = {
    "ascii_stl__writer", "binary_stl__writer", "blf_writer", "sqlite_writer", "sqlite_reader",
    "client", "local_client", "ssh_client",
    "tcp_client", "serial_client", "http_client", "mqtt_client",
    "tcp_client_value", "tcp_serve_value", "udp_value_pub", "udp_value_sub", "zmq_value_sub",
    "stream_client", "channel_client", "raw_client", "mgt_dram_pull_client",
    "create_joystick", "web_fpv", "local_web_controller",
    "file_io", "iq", "file_watcher",
    "wait_thread", "timing", "watchdog_task", "system",
    "decoder", "endpoint", "device", "device_handle",
    "post_wifi_connection", "post_wifi_connections", "get_wifi_connection",
    "rosbridge_ws_connection",
    "pv_log_folder", "pv_logger", "logged_pv",
    "tron1_bridge", "tron1_odom_bridge", "crsf_joy_bridge",
    "port_reader", "com_port",
    "keyboard_listener", "reader",
    "usb_device_description", "usb_port", "usb_train_id",
    "raw2_disk", "acquisition_stage", "pymepix_connection",
    "control_module", "parameter_control_module",
    "daq_scan", "daq__viewer_tcp_server",
    "put_ftp", "live_plot_client",
    "netclient", "siteclient",
    "debug_port", "physical_device",
    "communication_port",
    "register_interface",
    "a_star_speed",
    "virtual_bus", "serial_bus", "socketcan_bus", "socket_can_daemon_bus",
    "slcan_bus", "robotell_bus", "seeed_bus", "neousys_bus", "pcan_bus",
    "kvaser_bus", "neo_vi_bus", "nican_bus", "ni_xne_tcan_bus",
    "gs_usb_bus", "iscan_bus", "ca_nalyst_ii_bus",
    "general_purpose_udp_multicast_bus", "udp_multicast_bus",
    "multi_rate_cyclic_send_task",
    "pcan_basic", "ucan",
    "extended_request_support", "modbus_serial_client", "modbus_tcp_client",
    "modbus_client", "modbus_server", "modbus_serial_worker", "slave_serial_worker",
    "modbus_adu", "modbus_adu_cs",
    "routable", "sdm630",
    "py_spec_client", "sensor_polling_thread",
    "d435_rgb_stream",
    "esp32_device", "flash_firmware",
    "ai_channel",
    "serial_line_reader", "serial_port",
    "stpdrv", "i7540d", "telnet", "afms",
    "enumerate", "ieee488",
    "udp_handler", "udp_sampler",
    "streams_one",
}


def is_real_device(folder_name, original, classes):
    if folder_name in KNOWN_NON_DEVICES:
        return False

    for pat in NOT_DEVICE_FOLDER_PATTERNS:
        if re.search(pat, folder_name):
            return False

    # Check source path
    src_is_device = False
    src_is_util = False
    for pat in DEVICE_SRC_PATTERNS:
        if re.search(pat, original, re.IGNORECASE):
            src_is_device = True
            break
    for pat in NOT_DEVICE_SRC_PATTERNS:
        if re.search(pat, original, re.IGNORECASE):
            src_is_util = True
            break

    # Check class inheritance
    has_hw_parent = False
    total_public_methods = 0
    for cls in classes:
        for p in cls["parents"]:
            p_lower = p.lower()
            if any(kw in p_lower for kw in HARDWARE_PARENTS):
                has_hw_parent = True
                break
        total_public_methods += len(cls["methods"])

    hw_methods = 0
    hw_keywords = ["connect", "disconnect", "initialize", "close", "init",
                   "read", "write", "measure", "move", "home", "enable",
                   "disable", "start", "stop", "reset", "calibrate", "acquire",
                   "set_", "get_", "query"]
    for cls in classes:
        for m in cls["methods"]:
            if any(m.startswith(kw) or m == kw for kw in hw_keywords):
                hw_methods += 1

    if src_is_device and not src_is_util:
        return True
    if has_hw_parent:
        return True
    if hw_methods >= 3 and total_public_methods >= 3:
        return True
    if src_is_util:
        return False

    # For remaining ambiguous cases, accept if they have meaningful methods
    if total_public_methods >= 2 and hw_methods >= 1:
        return True

    return False


def main():
    folders = sorted([d for d in os.listdir(COMMUNITY_DIR) if os.path.isdir(os.path.join(COMMUNITY_DIR, d))])

    real_devices = []
    rejected = []

    for folder in folders:
        driver_path = os.path.join(COMMUNITY_DIR, folder, "driver.py")
        if not os.path.exists(driver_path):
            continue

        original, classes = get_class_info(driver_path)
        main_class = classes[0]["name"] if classes else "Unknown"
        main_methods = classes[0]["methods"] if classes else []

        if is_real_device(folder, original, classes):
            real_devices.append({
                "folder": folder,
                "class_name": main_class,
                "original": original,
                "public_methods": main_methods,
                "method_count": len(main_methods),
            })
        else:
            rejected.append(folder)

    print(f"Total folders: {len(folders)}")
    print(f"Real devices: {len(real_devices)}")
    print(f"Rejected: {len(rejected)}")
    print()

    # Save results
    out_path = os.path.join(os.path.dirname(__file__), "real_devices.json")
    with open(out_path, "w") as f:
        json.dump(real_devices, f, indent=2, ensure_ascii=False)
    print(f"Saved to {out_path}")

    print("\n=== Real devices ===")
    for d in real_devices:
        print(f"  {d['folder']}: class {d['class_name']} ({d['method_count']} methods) from {d['original']}")

    print(f"\n=== Rejected ({len(rejected)}) ===")
    for r in rejected:
        print(f"  {r}")


if __name__ == "__main__":
    main()
