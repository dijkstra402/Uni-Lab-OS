from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentHamiltonPsd(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/uwmisl__hamiltonPSD', 'source_file': 'PSD8.py', 'class_name': 'PSD8', 'import_roots': [], 'candidate_methods': ['home', 'abs_position', 'dispense', 'pickup', 'set_valve', 'set_speed', 'mix', 'set_aux'], 'action_targets': {}, 'metadata': {'repo': 'uwmisl/hamiltonPSD', 'repo_url': 'https://github.com/uwmisl/hamiltonPSD', 'brand': 'Hamilton', 'model': 'PSD', 'device_type_cn': '柱塞泵', 'device_type_en': 'Plunger Pump', 'source_framework': '专用驱动', 'tag_id': '4403', 'tag_name': '柱塞泵', 'tag_name_en': 'Plunger Pump', 'candidate_score': 144, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def home(self, **kwargs):
        return self.call('home', kwargs=kwargs)

    def abs_position(self, **kwargs):
        return self.call('abs_position', kwargs=kwargs)

    def dispense(self, **kwargs):
        return self.call('dispense', kwargs=kwargs)

    def pickup(self, **kwargs):
        return self.call('pickup', kwargs=kwargs)

    def set_valve(self, **kwargs):
        return self.call('set_valve', kwargs=kwargs)

    def set_speed(self, **kwargs):
        return self.call('set_speed', kwargs=kwargs)

    def mix(self, **kwargs):
        return self.call('mix', kwargs=kwargs)

    def set_aux(self, **kwargs):
        return self.call('set_aux', kwargs=kwargs)

