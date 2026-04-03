from unilabos.app.web.controller import _merge_runtime_device_with_registry


def test_merge_runtime_device_keeps_runtime_fields_and_restores_device_params():
    runtime_device = {
        "id": "MockStirrer1COPY",
        "class": "virtual_stirrer",
        "config": {"port": "MOCK"},
        "data": {"status": "Idle"},
    }
    registry_device = {
        "id": "virtual_stirrer",
        "device_params": {
            "测试力量精度": "0.001N,0.01N",
            "测试力量范围": "500N",
        },
        "description": "Virtual Stirrer",
        "icon": "Stirrer.webp",
    }

    merged = _merge_runtime_device_with_registry(runtime_device, registry_device)

    assert merged["id"] == "MockStirrer1COPY"
    assert merged["class"] == "virtual_stirrer"
    assert merged["config"] == {"port": "MOCK"}
    assert merged["data"] == {"status": "Idle"}
    assert merged["device_params"] == registry_device["device_params"]
    assert merged["description"] == "Virtual Stirrer"
    assert merged["icon"] == "Stirrer.webp"
