from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentMettlerToledoWxs205sdu(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/PyLabRobot__pylabrobot', 'source_file': 'pylabrobot/scales/mettler_toledo_backend.py', 'class_name': 'MettlerToledoWXS205SDUBackend', 'import_roots': [], 'candidate_methods': ['clear_tare', 'get_dynamic_weight', 'get_serial_number', 'get_stable_weight', 'get_tare_weight', 'get_weight', 'get_weight_value_immediately', 'read_dynamic_weight', 'read_stable_weight', 'read_weight', 'read_weight_value_immediately', 'request_serial_number', 'request_tare_weight', 'set_display_text', 'set_weight_display', 'setup', 'stop', 'tare', 'tare_immediately', 'tare_stable', 'tare_timeout', 'zero', 'zero_immediately', 'zero_stable', 'zero_timeout'], 'action_targets': {}, 'metadata': {'repo': 'PyLabRobot/pylabrobot', 'repo_url': 'https://github.com/PyLabRobot/pylabrobot', 'brand': 'Mettler Toledo', 'model': 'WXS205SDU', 'device_type_cn': '天平', 'device_type_en': 'Balance', 'source_framework': 'PyLabRobot', 'source_file': 'pylabrobot/scales/mettler_toledo_backend.py', 'class_name': 'MettlerToledoWXS205SDUBackend', 'candidate_methods': ['clear_tare', 'get_dynamic_weight', 'get_serial_number', 'get_stable_weight', 'get_tare_weight', 'get_weight', 'get_weight_value_immediately', 'read_dynamic_weight', 'read_stable_weight', 'read_weight', 'read_weight_value_immediately', 'request_serial_number', 'request_tare_weight', 'set_display_text', 'set_weight_display', 'setup', 'stop', 'tare', 'tare_immediately', 'tare_stable', 'tare_timeout', 'zero', 'zero_immediately', 'zero_stable', 'zero_timeout']}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def clear_tare(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('clear_tare', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_dynamic_weight(self, timeout=None, **kwargs):
        _kw = {'timeout': timeout}
        _kw.update(kwargs)
        return self.call('get_dynamic_weight', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_serial_number(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_serial_number', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_stable_weight(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_stable_weight', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_tare_weight(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_tare_weight', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_weight(self, timeout=None, **kwargs):
        _kw = {'timeout': timeout}
        _kw.update(kwargs)
        return self.call('get_weight', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_weight_value_immediately(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_weight_value_immediately', kwargs={k: v for k, v in _kw.items() if v is not None})

    def read_dynamic_weight(self, timeout=None, **kwargs):
        _kw = {'timeout': timeout}
        _kw.update(kwargs)
        return self.call('read_dynamic_weight', kwargs={k: v for k, v in _kw.items() if v is not None})

    def read_stable_weight(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('read_stable_weight', kwargs={k: v for k, v in _kw.items() if v is not None})

    def read_weight(self, timeout=None, **kwargs):
        _kw = {'timeout': timeout}
        _kw.update(kwargs)
        return self.call('read_weight', kwargs={k: v for k, v in _kw.items() if v is not None})

    def read_weight_value_immediately(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('read_weight_value_immediately', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_serial_number(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_serial_number', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_tare_weight(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_tare_weight', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_display_text(self, text=None, **kwargs):
        _kw = {'text': text}
        _kw.update(kwargs)
        return self.call('set_display_text', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_weight_display(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('set_weight_display', kwargs={k: v for k, v in _kw.items() if v is not None})

    def setup(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('setup', kwargs={k: v for k, v in _kw.items() if v is not None})

    def stop(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('stop', kwargs={k: v for k, v in _kw.items() if v is not None})

    def tare(self, timeout=None, **kwargs):
        _kw = {'timeout': timeout}
        _kw.update(kwargs)
        return self.call('tare', kwargs={k: v for k, v in _kw.items() if v is not None})

    def tare_immediately(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('tare_immediately', kwargs={k: v for k, v in _kw.items() if v is not None})

    def tare_stable(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('tare_stable', kwargs={k: v for k, v in _kw.items() if v is not None})

    def tare_timeout(self, timeout=None, **kwargs):
        _kw = {'timeout': timeout}
        _kw.update(kwargs)
        return self.call('tare_timeout', kwargs={k: v for k, v in _kw.items() if v is not None})

    def zero(self, timeout=None, **kwargs):
        _kw = {'timeout': timeout}
        _kw.update(kwargs)
        return self.call('zero', kwargs={k: v for k, v in _kw.items() if v is not None})

    def zero_immediately(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('zero_immediately', kwargs={k: v for k, v in _kw.items() if v is not None})

    def zero_stable(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('zero_stable', kwargs={k: v for k, v in _kw.items() if v is not None})

    def zero_timeout(self, timeout=None, **kwargs):
        _kw = {'timeout': timeout}
        _kw.update(kwargs)
        return self.call('zero_timeout', kwargs={k: v for k, v in _kw.items() if v is not None})

