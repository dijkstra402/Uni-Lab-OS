from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentBuchiRotavaporR300(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/buchi-labortechnik-ag__openinterface_examples_python', 'source_file': 'modbus_server/modbus_server.py', 'class_name': '', 'import_roots': [], 'candidate_methods': ['get_value', 'read_api', 'updating_writer', 'rescale_value', 'write_api', 'read_device_map', 'device_writer', 'run_modbus_server'], 'action_targets': {'get_value': 'get_value', 'read_api': 'read_api', 'updating_writer': 'updating_writer', 'rescale_value': 'rescale_value', 'write_api': 'write_api', 'read_device_map': 'read_device_map', 'device_writer': 'device_writer', 'run_modbus_server': 'run_modbus_server'}, 'metadata': {'repo': 'buchi-labortechnik-ag/openinterface_examples_python', 'repo_url': 'https://github.com/buchi-labortechnik-ag/openinterface_examples_python', 'brand': 'Buchi', 'model': 'Rotavapor R-300', 'device_type_cn': '旋转蒸发器', 'device_type_en': 'Rotary Evaporator', 'source_framework': '泵阀/液体处理', 'tag_id': '4397', 'tag_name': '旋转蒸发器', 'tag_name_en': 'Rotary Evaporator', 'candidate_score': 56, 'parse_status': 'module_reselected', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'get_value': 'get_value', 'read_api': 'read_api', 'updating_writer': 'updating_writer', 'rescale_value': 'rescale_value', 'write_api': 'write_api', 'read_device_map': 'read_device_map', 'device_writer': 'device_writer', 'run_modbus_server': 'run_modbus_server'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_value(self, **kwargs):
        return self.call('get_value', kwargs=kwargs)

    def read_api(self, **kwargs):
        return self.call('read_api', kwargs=kwargs)

    def updating_writer(self, **kwargs):
        return self.call('updating_writer', kwargs=kwargs)

    def rescale_value(self, **kwargs):
        return self.call('rescale_value', kwargs=kwargs)

    def write_api(self, **kwargs):
        return self.call('write_api', kwargs=kwargs)

    def read_device_map(self, **kwargs):
        return self.call('read_device_map', kwargs=kwargs)

    def device_writer(self, **kwargs):
        return self.call('device_writer', kwargs=kwargs)

    def run_modbus_server(self, **kwargs):
        return self.call('run_modbus_server', kwargs=kwargs)

