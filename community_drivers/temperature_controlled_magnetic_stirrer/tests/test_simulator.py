"""控温磁力搅拌器内存模拟驱动测试。"""

from __future__ import annotations

import json

import pytest

from temperature_controlled_magnetic_stirrer.simulator import (
    TemperatureControlledMagneticStirrerSimulator,
)
from unilabos.registry.decorators import get_all_registered_devices, get_topic_config


class FakeClock:
    def __init__(self) -> None:
        self.now = 1_000.0

    def __call__(self) -> float:
        return self.now

    def advance(self, seconds: float) -> None:
        assert seconds >= 0
        self.now += seconds


def create_simulator(
    clock: FakeClock | None = None,
) -> tuple[TemperatureControlledMagneticStirrerSimulator, FakeClock]:
    active_clock = clock or FakeClock()
    simulator = TemperatureControlledMagneticStirrerSimulator(
        device_id="stirrer-a",
        config={
            "ambient_temperature": 25,
            "temperature_rate": 5,
            "speed_rate": 100,
        },
        _clock=active_clock,
    )
    return simulator, active_clock


def test_initial_state_is_complete_and_serializable() -> None:
    simulator, _clock = create_simulator()

    state = {
        "status": simulator.status,
        "fault": simulator.fault,
        "idle": simulator.idle,
        "fault_code": simulator.fault_code,
        "current_speed": simulator.current_speed,
        "current_temperature": simulator.current_temperature,
        "current_time": simulator.current_time,
        "target_stir_speed": simulator.target_stir_speed,
        "target_heating_temperature": simulator.target_heating_temperature,
        "target_time": simulator.target_time,
    }

    assert state == {
        "status": "idle",
        "fault": False,
        "idle": True,
        "fault_code": 0,
        "current_speed": 0.0,
        "current_temperature": 25.0,
        "current_time": 0.0,
        "target_stir_speed": 0.0,
        "target_heating_temperature": 25.0,
        "target_time": 0.0,
    }
    json.dumps(state, allow_nan=False)


def test_only_simulator_registers_the_device_contract() -> None:
    registered = get_all_registered_devices()
    assert registered["temperature_controlled_magnetic_stirrer"] is (
        TemperatureControlledMagneticStirrerSimulator
    )

    action_names = [
        name
        for name, value in vars(TemperatureControlledMagneticStirrerSimulator).items()
        if getattr(value, "_action_registry_meta", None) is not None
    ]
    assert sorted(action_names) == [
        "initialize",
        "set_heating_mode",
        "set_heating_temperature",
        "set_safety_temperature",
        "set_stir_speed",
        "set_temperature_unit",
        "set_time",
        "set_work_mode",
        "stir",
    ]
    assert len(action_names) == len(set(action_names))


def test_setters_update_targets_without_faking_current_values() -> None:
    simulator, clock = create_simulator()

    assert simulator.set_stir_speed(600) == {}
    assert simulator.set_heating_temperature(80) == {}
    assert simulator.set_time(30) == {}
    clock.advance(10)

    assert simulator.target_stir_speed == 600
    assert simulator.target_heating_temperature == 80
    assert simulator.target_time == 30
    assert simulator.status == "ready"
    assert simulator.idle is True
    assert simulator.current_speed == 0
    assert simulator.current_temperature == 25
    assert simulator.current_time == 0


def test_stir_advances_current_values_without_overshoot() -> None:
    simulator, clock = create_simulator()
    simulator.set_stir_speed(600)
    simulator.set_heating_temperature(80)
    simulator.set_time(30)

    assert simulator.stir() == {}
    assert simulator.status == "running"
    assert simulator.idle is False

    clock.advance(2)
    assert simulator.current_speed == pytest.approx(200)
    assert simulator.current_temperature == pytest.approx(35)
    assert simulator.current_time == pytest.approx(2)

    clock.advance(100)
    assert simulator.current_speed == 0
    assert simulator.current_temperature == 80
    assert simulator.current_time == 30
    assert simulator.status == "idle"
    assert simulator.idle is True


def test_retarget_continues_from_current_value() -> None:
    simulator, clock = create_simulator()
    simulator.set_stir_speed(500)
    simulator.set_heating_temperature(80)
    simulator.stir()
    clock.advance(2)
    assert simulator.current_speed == pytest.approx(200)
    assert simulator.current_temperature == pytest.approx(35)

    simulator.set_stir_speed(100)
    simulator.set_heating_temperature(30)
    assert simulator.current_speed == pytest.approx(200)
    assert simulator.current_temperature == pytest.approx(35)

    clock.advance(1)
    assert simulator.current_speed == pytest.approx(100)
    assert simulator.current_temperature == pytest.approx(30)


def test_zero_target_time_runs_continuously() -> None:
    simulator, clock = create_simulator()
    simulator.set_stir_speed(100)
    simulator.set_time(0)
    simulator.stir()

    clock.advance(100)

    assert simulator.status == "running"
    assert simulator.idle is False
    assert simulator.current_speed == 100
    assert simulator.current_time == 100


def test_invalid_parameters_do_not_partially_change_state() -> None:
    simulator, _clock = create_simulator()
    simulator.set_heating_temperature(80)

    with pytest.raises(ValueError, match="搅拌速度不能小于 0"):
        simulator.set_stir_speed(-1)
    with pytest.raises(ValueError, match="运行时间必须是有限数字"):
        simulator.set_time(float("nan"))
    with pytest.raises(ValueError, match="安全温度不能低于"):
        simulator.set_safety_temperature(70)

    assert simulator.target_stir_speed == 0
    assert simulator.target_time == 0
    assert simulator.safety_temperature == 0
    assert simulator.target_heating_temperature == 80


def test_initialize_resets_one_instance_without_affecting_another() -> None:
    first, first_clock = create_simulator()
    second, _second_clock = create_simulator()
    first.set_stir_speed(300)
    first.stir()
    first_clock.advance(1)
    assert first.current_speed == 100

    assert first.initialize() == {}

    assert first.status == "idle"
    assert first.idle is True
    assert first.current_speed == 0
    assert first.target_stir_speed == 0
    assert second.status == "idle"
    assert second.current_speed == 0


def test_mode_setters_and_topic_contract() -> None:
    simulator, _clock = create_simulator()

    assert simulator.set_work_mode("constant") == {}
    assert simulator.set_heating_mode("pid") == {}
    assert simulator.set_temperature_unit(1) == {}
    assert simulator.set_safety_temperature(120) == {}
    assert simulator.work_mode == "constant"
    assert simulator.heating_mode == "pid"
    assert simulator.temperature_unit == 1
    assert simulator.safety_temperature == 120

    properties = (
        "status",
        "fault",
        "idle",
        "fault_code",
        "current_speed",
        "current_temperature",
        "current_time",
        "target_stir_speed",
        "target_heating_temperature",
        "target_time",
        "safety_temperature",
        "temperature_unit",
        "heating_mode",
        "work_mode",
    )
    for name in properties:
        descriptor = getattr(TemperatureControlledMagneticStirrerSimulator, name)
        assert isinstance(descriptor, property)
        assert get_topic_config(descriptor.fget) == {
            "period": 1.0,
            "print_publish": None,
            "qos": None,
            "name": None,
        }
