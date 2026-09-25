"""Map vendor-specific methods/properties onto a small semantic action set.

ponytail: alias table is exhaustive for the high-value SCPI families we care
about (DMM/PSU/SMU/scope/VNA/AWG). New families → add a row here, don't
invent a plugin system.
"""

from __future__ import annotations

# semantic_name -> try methods in order, then attribute setters/getters
ALIASES = {
    "initialize": {
        "methods": ("initialize", "init", "reset", "open", "connect"),
        "goal": {},
    },
    "start": {
        "methods": (
            "start",
            "enable_source",
            "enable_output",
            "output_on",
            "turn_on",
            "on",
        ),
        "setters": ("output_enabled", "source_enabled"),
        "value_keys": ("enabled", "value"),
        "goal": {},
    },
    "stop": {
        "methods": (
            "stop",
            "disable_source",
            "disable_output",
            "output_off",
            "shutdown",
            "turn_off",
            "off",
        ),
        "setters": ("output_enabled", "source_enabled"),
        "value_keys": ("enabled", "value"),
        "goal": {},
    },
    "measure": {
        "methods": (
            "measure",
            "measure_voltage",
            "measure_current",
            "read",
            "fetch",
            "readout",
        ),
        "getters": ("voltage", "current", "reading", "value"),
        "goal": {},
    },
    "set_voltage": {
        "methods": ("set_voltage", "apply_voltage", "ramp_to_voltage"),
        "setters": ("source_voltage", "voltage_setpoint", "voltage"),
        "value_keys": ("voltage", "value", "target_voltage"),
        "goal": {"voltage": "voltage"},
    },
    "set_current": {
        "methods": ("set_current", "apply_current", "ramp_to_current"),
        "setters": ("source_current", "current_setpoint", "current_limit", "current"),
        "value_keys": ("current", "value", "target_current"),
        "goal": {"current": "current"},
    },
    "set_frequency": {
        "methods": ("set_frequency",),
        "setters": ("frequency", "center_frequency"),
        "value_keys": ("frequency", "value"),
        "goal": {"frequency": "frequency"},
    },
    "set_amplitude": {
        "methods": ("set_amplitude",),
        "setters": ("amplitude",),
        "value_keys": ("amplitude", "value"),
        "goal": {"amplitude": "amplitude"},
    },
    "set_power": {
        "methods": ("set_power", "set_output_level"),
        "setters": ("power", "output_level"),
        "value_keys": ("power", "value"),
        "goal": {"power": "power"},
    },
    "set_temperature": {
        "methods": ("set_temperature", "setpoint"),
        "setters": ("temperature_setpoint", "setpoint", "temperature"),
        "value_keys": ("temperature", "value", "setpoint"),
        "goal": {"temperature": "temperature"},
    },
}


def _is_usable(cls, name: str) -> bool:
    if name.startswith("_"):
        return False
    attr = getattr(cls, name, None)
    return attr is not None


def _alias_call(target: str):
    def fn(self, *args, **kwargs):
        return getattr(self, target)(*args, **kwargs)

    fn.__name__ = target
    fn.__doc__ = f"Semantic alias → {target}()"
    return fn


def _setter_call(props, value_keys):
    def fn(self, *args, **kwargs):
        val = args[0] if args else None
        if val is None:
            for k in value_keys:
                if k in kwargs:
                    val = kwargs[k]
                    break
        if val is None and kwargs:
            val = next(iter(kwargs.values()))
        for p in props:
            if hasattr(self, p):
                setattr(self, p, val)
                return {"success": True}
        raise AttributeError(f"none of {props} exist on {type(self).__name__}")

    fn.__name__ = "set"
    fn.__doc__ = f"Semantic setter → {props}"
    return fn


def _getter_call(props):
    def fn(self, *args, **kwargs):
        for p in props:
            if hasattr(self, p):
                return getattr(self, p)
        raise AttributeError(f"none of {props} exist on {type(self).__name__}")

    fn.__name__ = "measure"
    fn.__doc__ = f"Semantic getter → {props}"
    return fn


_CH_NAMES = ("ch_1", "ch1", "channel1", "ch_2", "ch2")
_CH_SETTERS = {
    "set_voltage": ("voltage_setpoint", "voltage"),
    "set_current": ("current_limit", "current_setpoint", "current"),
}
_CH_GETTERS = {"measure": ("voltage", "current", "reading")}


def _channel_setter(prop_names, value_keys):
    def fn(self, *args, **kwargs):
        val = args[0] if args else None
        if val is None:
            for k in value_keys:
                if k in kwargs:
                    val = kwargs[k]
                    break
        if val is None and kwargs:
            val = next(iter(v for k, v in kwargs.items() if k != "channel"))
        chn = kwargs.get("channel", 1)
        ch = getattr(self, f"ch_{chn}", None) or getattr(self, f"ch{chn}", None)
        if ch is None:
            for n in _CH_NAMES:
                ch = getattr(self, n, None)
                if ch is not None:
                    break
        if ch is None:
            raise AttributeError("no channel object")
        for p in prop_names:
            if hasattr(ch, p):
                setattr(ch, p, val)
                return {"success": True}
        raise AttributeError(prop_names)

    fn.__name__ = "set"
    return fn


def _channel_getter(prop_names):
    def fn(self, *args, **kwargs):
        chn = kwargs.get("channel", 1)
        ch = getattr(self, f"ch_{chn}", None) or getattr(self, f"ch{chn}", None)
        if ch is None:
            for n in _CH_NAMES:
                ch = getattr(self, n, None)
                if ch is not None:
                    break
        if ch is None:
            raise AttributeError("no channel object")
        for p in prop_names:
            if hasattr(ch, p):
                return getattr(ch, p)
        raise AttributeError(prop_names)

    fn.__name__ = "measure"
    return fn


def bind(cls):
    """Attach missing semantic methods onto *cls* (in place)."""
    for semantic, spec in ALIASES.items():
        if semantic in cls.__dict__:
            continue
        target = None
        for m in spec.get("methods", ()):
            if m == semantic:
                continue
            if _is_usable(cls, m) and callable(getattr(cls, m, None)):
                target = m
                break
        if target:
            setattr(cls, semantic, _alias_call(target))
            continue
        if spec.get("setters") and semantic.startswith("set_"):
            if any(_is_usable(cls, p) for p in spec["setters"]):
                setattr(cls, semantic, _setter_call(spec["setters"], spec.get("value_keys", ("value",))))
                continue
        if spec.get("getters") and semantic == "measure":
            if any(_is_usable(cls, p) for p in spec["getters"]):
                setattr(cls, semantic, _getter_call(spec["getters"]))
                continue
        if spec.get("setters") and semantic in ("start", "stop"):
            if any(_is_usable(cls, p) for p in spec["setters"]):
                on = semantic == "start"

                def _fn(self, *a, _props=spec["setters"], _val=on, **k):
                    for p in _props:
                        if hasattr(self, p):
                            setattr(self, p, _val)
                            return {"success": True}
                    raise AttributeError(_props)

                _fn.__name__ = semantic
                setattr(cls, semantic, _fn)
                continue
        has_ch = any(n in cls.__dict__ or _is_usable(cls, n) for n in _CH_NAMES)
        if has_ch and semantic in _CH_SETTERS:
            setattr(cls, semantic, _channel_setter(_CH_SETTERS[semantic], spec.get("value_keys", ("value",))))
        elif has_ch and semantic in _CH_GETTERS:
            setattr(cls, semantic, _channel_getter(_CH_GETTERS[semantic]))
    return cls


if __name__ == "__main__":
    class _Fake:
        def enable_source(self):
            return "on"

        def disable_source(self):
            return "off"

        def apply_voltage(self, voltage_range=None, compliance_current=0.1):
            return voltage_range

        voltage = 3.14

    bind(_Fake)
    f = _Fake()
    assert f.start() == "on", f.start()
    assert f.stop() == "off", f.stop()
    assert f.set_voltage(voltage_range=5) == 5
    assert f.measure() == 3.14
    print("_semantic_aliases self-check: PASS")
