import io
from typing import Any, Dict

import yaml


def normalize_object_mapping(raw_value: Any) -> Dict[str, Any]:
    """
    Normalize registry object-like fields to a plain dict.

    Supports:
    - dict: pass through
    - list[{key,value}] / list[(key,value)]: convert to dict
    - YAML/JSON string: parse and keep only mapping values
    - anything else: {}
    """
    if isinstance(raw_value, dict):
        return raw_value

    if isinstance(raw_value, list):
        target: Dict[str, Any] = {}
        for item in raw_value:
            if isinstance(item, dict) and "key" in item:
                target[str(item.get("key", ""))] = item.get("value")
            elif isinstance(item, (list, tuple)) and len(item) == 2:
                target[str(item[0])] = item[1]
        return target

    if isinstance(raw_value, str):
        value = raw_value.strip()
        if not value:
            return {}
        try:
            parsed = yaml.safe_load(io.StringIO(value))
        except Exception:
            return {}
        return parsed if isinstance(parsed, dict) else {}

    return {}
