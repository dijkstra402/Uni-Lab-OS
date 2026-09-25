from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentLeicaDmi82(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/MartinHjelmare__leicacam', 'source_file': 'src/leicacam/cam.py', 'class_name': 'CAM', 'import_roots': ['src'], 'candidate_methods': ['connect', 'flush', 'send', 'receive', 'wait_for', 'close', 'start_scan', 'stop_scan', 'autofocus_scan', 'pause_scan', 'enable', 'disable', 'enable_all', 'disable_all', 'save_template', 'load_template', 'get_information'], 'action_targets': {}, 'metadata': {'repo': 'MartinHjelmare/leicacam', 'repo_url': 'https://github.com/MartinHjelmare/leicacam', 'brand': 'Leica', 'model': 'DMi8', 'device_type_cn': '荧光显微镜', 'device_type_en': 'Fluorescence Microscope', 'source_framework': 'leicacam', 'tag_id': '4447', 'tag_name': '荧光显微镜', 'tag_name_en': 'Fluorescence Microscope', 'candidate_score': 182, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def connect(self, **kwargs):
        return self.call('connect', kwargs=kwargs)

    def flush(self, **kwargs):
        return self.call('flush', kwargs=kwargs)

    def send(self, **kwargs):
        return self.call('send', kwargs=kwargs)

    def receive(self, **kwargs):
        return self.call('receive', kwargs=kwargs)

    def wait_for(self, **kwargs):
        return self.call('wait_for', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def start_scan(self, **kwargs):
        return self.call('start_scan', kwargs=kwargs)

    def stop_scan(self, **kwargs):
        return self.call('stop_scan', kwargs=kwargs)

    def autofocus_scan(self, **kwargs):
        return self.call('autofocus_scan', kwargs=kwargs)

    def pause_scan(self, **kwargs):
        return self.call('pause_scan', kwargs=kwargs)

    def enable(self, **kwargs):
        return self.call('enable', kwargs=kwargs)

    def disable(self, **kwargs):
        return self.call('disable', kwargs=kwargs)

    def enable_all(self, **kwargs):
        return self.call('enable_all', kwargs=kwargs)

    def disable_all(self, **kwargs):
        return self.call('disable_all', kwargs=kwargs)

    def save_template(self, **kwargs):
        return self.call('save_template', kwargs=kwargs)

    def load_template(self, **kwargs):
        return self.call('load_template', kwargs=kwargs)

    def get_information(self, **kwargs):
        return self.call('get_information', kwargs=kwargs)

