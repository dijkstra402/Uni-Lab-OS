from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentIkaEurostar60100Control(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/alexrudd2__ika', 'source_file': 'ika/driver.py', 'class_name': 'Vacuum', 'import_roots': [], 'candidate_methods': ['get_pressure', 'get_pressure_setpoint', 'get_status', 'get_vac_mode', 'get', 'get_info', 'set', 'set_mode', 'set_name', 'control', 'query', 'command'], 'action_targets': {}, 'metadata': {'repo': 'alexrudd2/ika', 'repo_url': 'https://github.com/alexrudd2/ika', 'brand': 'IKA', 'model': 'Eurostar 60/100 Control', 'device_type_cn': '机械搅拌反应釜', 'device_type_en': 'Mechanical Stirring Reactor', 'source_framework': 'ika-control', 'tag_id': '4401', 'tag_name': '机械搅拌反应釜', 'tag_name_en': 'Mechanical Stirring Reactor', 'candidate_score': 118, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_pressure(self, **kwargs):
        return self.call('get_pressure', kwargs=kwargs)

    def get_pressure_setpoint(self, **kwargs):
        return self.call('get_pressure_setpoint', kwargs=kwargs)

    def get_status(self, **kwargs):
        return self.call('get_status', kwargs=kwargs)

    def get_vac_mode(self, **kwargs):
        return self.call('get_vac_mode', kwargs=kwargs)

    def get(self, **kwargs):
        return self.call('get', kwargs=kwargs)

    def get_info(self, **kwargs):
        return self.call('get_info', kwargs=kwargs)

    def set(self, **kwargs):
        return self.call('set', kwargs=kwargs)

    def set_mode(self, **kwargs):
        return self.call('set_mode', kwargs=kwargs)

    def set_name(self, **kwargs):
        return self.call('set_name', kwargs=kwargs)

    def control(self, **kwargs):
        return self.call('control', kwargs=kwargs)

    def query(self, **kwargs):
        return self.call('query', kwargs=kwargs)

    def command(self, **kwargs):
        return self.call('command', kwargs=kwargs)

