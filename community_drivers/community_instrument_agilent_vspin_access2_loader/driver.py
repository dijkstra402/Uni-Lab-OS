from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAgilentVspinAccess2Loader(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/PyLabRobot__pylabrobot', 'source_file': 'pylabrobot/centrifuge/vspin_backend.py', 'class_name': 'Access2Backend', 'import_roots': [], 'candidate_methods': ['close', 'get_status', 'load', 'open', 'park', 'setup', 'stop', 'unload'], 'action_targets': {}, 'metadata': {'repo': 'PyLabRobot/pylabrobot', 'repo_url': 'https://github.com/PyLabRobot/pylabrobot', 'brand': 'Agilent', 'model': 'VSpin Access2 Loader', 'device_type_cn': '离心机上料器', 'device_type_en': 'Centrifuge Loader', 'source_framework': 'PyLabRobot', 'source_file': 'pylabrobot/centrifuge/vspin_backend.py', 'class_name': 'Access2Backend', 'candidate_methods': ['close', 'get_status', 'load', 'open', 'park', 'setup', 'stop', 'unload']}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def close(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('close', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_status(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_status', kwargs={k: v for k, v in _kw.items() if v is not None})

    def load(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('load', kwargs={k: v for k, v in _kw.items() if v is not None})

    def open(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('open', kwargs={k: v for k, v in _kw.items() if v is not None})

    def park(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('park', kwargs={k: v for k, v in _kw.items() if v is not None})

    def setup(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('setup', kwargs={k: v for k, v in _kw.items() if v is not None})

    def stop(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('stop', kwargs={k: v for k, v in _kw.items() if v is not None})

    def unload(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('unload', kwargs={k: v for k, v in _kw.items() if v is not None})

