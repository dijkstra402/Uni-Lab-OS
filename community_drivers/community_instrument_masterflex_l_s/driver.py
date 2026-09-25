from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentMasterflexLS(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/PyLabRobot__pylabrobot', 'source_file': 'pylabrobot/pumps/cole_parmer/masterflex_backend.py', 'class_name': 'MasterflexBackend', 'import_roots': [], 'candidate_methods': ['halt', 'run_continuously', 'run_revolutions', 'setup', 'stop'], 'action_targets': {}, 'metadata': {'repo': 'PyLabRobot/pylabrobot', 'repo_url': 'https://github.com/PyLabRobot/pylabrobot', 'brand': 'Masterflex', 'model': 'L/S', 'device_type_cn': '蠕动泵', 'device_type_en': 'Peristaltic Pump', 'source_framework': 'PyLabRobot', 'tag_id': '4451', 'tag_name': '蠕动泵', 'tag_name_en': 'Peristaltic Pump', 'candidate_score': 2318, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}, 'source_file': 'pylabrobot/pumps/cole_parmer/masterflex_backend.py', 'class_name': 'MasterflexBackend'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def halt(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('halt', kwargs={k: v for k, v in _kw.items() if v is not None})

    def run_continuously(self, speed=None, **kwargs):
        _kw = {'speed': speed}
        _kw.update(kwargs)
        return self.call('run_continuously', kwargs={k: v for k, v in _kw.items() if v is not None})

    def run_revolutions(self, num_revolutions=None, **kwargs):
        _kw = {'num_revolutions': num_revolutions}
        _kw.update(kwargs)
        return self.call('run_revolutions', kwargs={k: v for k, v in _kw.items() if v is not None})

    def setup(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('setup', kwargs={k: v for k, v in _kw.items() if v is not None})

    def stop(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('stop', kwargs={k: v for k, v in _kw.items() if v is not None})

