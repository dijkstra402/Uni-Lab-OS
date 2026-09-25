from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentADGxKGfK(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/djorlando24__pyLabDataLogger', 'source_file': 'src/device/picotc08Device.py', 'class_name': 'usbtc08_logger', 'import_roots': ['src'], 'candidate_methods': ['config', 'test', 'clear_data', 'process_data', 'configuration_data', 'open_unit_async', 'open_unit_progress', 'get_unit_info', 'get_unit_info2', 'export_unit_info2', 'get_formatted_info', 'set_channel', 'disable_channel', 'set_mains', 'get_minimum_interval_ms', 'run', 'get_temp', 'get_temp_deskew', 'stop', 'get_single', 'unit_celsius', 'unit_fahrenheit', 'unit_kelvin', 'unit_rankine', 'close_self'], 'action_targets': {}, 'metadata': {'repo': 'djorlando24/pyLabDataLogger', 'repo_url': 'https://github.com/djorlando24/pyLabDataLogger', 'brand': 'A&D', 'model': 'GX-K / GF-K', 'device_type_cn': '电子天平', 'device_type_en': 'Balance', 'source_framework': 'pyLabDataLogger', 'tag_id': '4426', 'tag_name': '电子天平', 'tag_name_en': 'Electronic Balance', 'candidate_score': 230, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def config(self, **kwargs):
        return self.call('config', kwargs=kwargs)

    def test(self, **kwargs):
        return self.call('test', kwargs=kwargs)

    def clear_data(self, **kwargs):
        return self.call('clear_data', kwargs=kwargs)

    def process_data(self, **kwargs):
        return self.call('process_data', kwargs=kwargs)

    def configuration_data(self, **kwargs):
        return self.call('configuration_data', kwargs=kwargs)

    def open_unit_async(self, **kwargs):
        return self.call('open_unit_async', kwargs=kwargs)

    def open_unit_progress(self, **kwargs):
        return self.call('open_unit_progress', kwargs=kwargs)

    def get_unit_info(self, **kwargs):
        return self.call('get_unit_info', kwargs=kwargs)

    def get_unit_info2(self, **kwargs):
        return self.call('get_unit_info2', kwargs=kwargs)

    def export_unit_info2(self, **kwargs):
        return self.call('export_unit_info2', kwargs=kwargs)

    def get_formatted_info(self, **kwargs):
        return self.call('get_formatted_info', kwargs=kwargs)

    def set_channel(self, **kwargs):
        return self.call('set_channel', kwargs=kwargs)

    def disable_channel(self, **kwargs):
        return self.call('disable_channel', kwargs=kwargs)

    def set_mains(self, **kwargs):
        return self.call('set_mains', kwargs=kwargs)

    def get_minimum_interval_ms(self, **kwargs):
        return self.call('get_minimum_interval_ms', kwargs=kwargs)

    def run(self, **kwargs):
        return self.call('run', kwargs=kwargs)

    def get_temp(self, **kwargs):
        return self.call('get_temp', kwargs=kwargs)

    def get_temp_deskew(self, **kwargs):
        return self.call('get_temp_deskew', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

    def get_single(self, **kwargs):
        return self.call('get_single', kwargs=kwargs)

    def unit_celsius(self, **kwargs):
        return self.call('unit_celsius', kwargs=kwargs)

    def unit_fahrenheit(self, **kwargs):
        return self.call('unit_fahrenheit', kwargs=kwargs)

    def unit_kelvin(self, **kwargs):
        return self.call('unit_kelvin', kwargs=kwargs)

    def unit_rankine(self, **kwargs):
        return self.call('unit_rankine', kwargs=kwargs)

    def close_self(self, **kwargs):
        return self.call('close_self', kwargs=kwargs)

