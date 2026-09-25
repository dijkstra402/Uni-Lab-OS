from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentSartoriusQuintix(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/holgi__sartoriusb', 'source_file': 'sartoriusb/__init__.py', 'class_name': 'SartoriusUsb', 'import_roots': [], 'candidate_methods': ['connection', 'connect', 'open', 'close', 'send', 'read', 'readline', 'readlines', 'get', 'measure'], 'action_targets': {}, 'metadata': {'repo': 'holgi/sartoriusb', 'repo_url': 'https://github.com/holgi/sartoriusb', 'brand': 'Sartorius', 'model': 'Quintix', 'device_type_cn': '电子天平(USB)', 'device_type_en': 'Electronic Balance (USB)', 'source_framework': '电化学/热分析/天平', 'tag_id': '4426', 'tag_name': '电子天平', 'tag_name_en': 'Electronic Balance', 'candidate_score': 158, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def connection(self, **kwargs):
        return self.call('connection', kwargs=kwargs)

    def connect(self, **kwargs):
        return self.call('connect', kwargs=kwargs)

    def open(self, **kwargs):
        return self.call('open', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def send(self, **kwargs):
        return self.call('send', kwargs=kwargs)

    def read(self, **kwargs):
        return self.call('read', kwargs=kwargs)

    def readline(self, **kwargs):
        return self.call('readline', kwargs=kwargs)

    def readlines(self, **kwargs):
        return self.call('readlines', kwargs=kwargs)

    def get(self, **kwargs):
        return self.call('get', kwargs=kwargs)

    def measure(self, **kwargs):
        return self.call('measure', kwargs=kwargs)

