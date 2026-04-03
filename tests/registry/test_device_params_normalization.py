from unilabos.app.register import _normalize_square_registry_entry
from unilabos.registry.field_normalizer import normalize_object_mapping


def test_normalize_object_mapping_supports_yaml_string():
    raw_value = """
channel_count: 1
supports_auto_feeding: true
workstation: bioyond_cell
"""

    assert normalize_object_mapping(raw_value) == {
        "channel_count": 1,
        "supports_auto_feeding": True,
        "workstation": "bioyond_cell",
    }


def test_square_registry_entry_keeps_device_params_from_yaml_string():
    entry = {
        "id": "bioyond_cell",
        "category": ["workstation"],
        "device_params": """
channel_count: 1
supports_auto_feeding: true
workstation: bioyond_cell
""",
    }

    normalized = _normalize_square_registry_entry(entry, default_resource_type="device")

    assert normalized["device_params"] == {
        "channel_count": 1,
        "supports_auto_feeding": True,
        "workstation": "bioyond_cell",
    }
