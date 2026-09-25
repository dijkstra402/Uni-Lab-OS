from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictMdt69xa(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/AlexShkarin__pyLabLib', 'source_file': 'pylablib/devices/Thorlabs/serial.py', 'class_name': 'MDT69xA', 'import_roots': [], 'candidate_methods': ['get_voltage', 'set_voltage', 'get_voltage_range', 'open', 'reconnect', 'sleep', 'using_write_buffer', 'get_id', 'get_esr', 'wait_sync', 'wait_dev', 'wait', 'get_arg_type', 'flush', 'read_binary_array_data', 'parse_array_data', 'apply_settings', 'close', 'is_opened', 'lock', 'unlock', 'locking', 'get_settings', 'get_full_status', 'get_full_info', 'get_device_variable', 'set_device_variable'], 'action_targets': {}, 'metadata': {'repo': 'AlexShkarin/pyLabLib', 'repo_url': 'https://github.com/AlexShkarin/pyLabLib', 'source_url': 'https://github.com/AlexShkarin/pyLabLib/blob/main/pylablib/devices/Thorlabs/serial.py', 'confidence': 0.95, 'quality_score': 1.11, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_voltage(self, **kwargs):
        return self.call('get_voltage', kwargs=kwargs)

    def set_voltage(self, **kwargs):
        return self.call('set_voltage', kwargs=kwargs)

    def get_voltage_range(self, **kwargs):
        return self.call('get_voltage_range', kwargs=kwargs)

    def open(self, **kwargs):
        return self.call('open', kwargs=kwargs)

    def reconnect(self, **kwargs):
        return self.call('reconnect', kwargs=kwargs)

    def sleep(self, **kwargs):
        return self.call('sleep', kwargs=kwargs)

    def using_write_buffer(self, **kwargs):
        return self.call('using_write_buffer', kwargs=kwargs)

    def get_id(self, **kwargs):
        return self.call('get_id', kwargs=kwargs)

    def get_esr(self, **kwargs):
        return self.call('get_esr', kwargs=kwargs)

    def wait_sync(self, **kwargs):
        return self.call('wait_sync', kwargs=kwargs)

    def wait_dev(self, **kwargs):
        return self.call('wait_dev', kwargs=kwargs)

    def wait(self, **kwargs):
        return self.call('wait', kwargs=kwargs)

    def get_arg_type(self, **kwargs):
        return self.call('get_arg_type', kwargs=kwargs)

    def flush(self, **kwargs):
        return self.call('flush', kwargs=kwargs)

    def read_binary_array_data(self, **kwargs):
        return self.call('read_binary_array_data', kwargs=kwargs)

    def parse_array_data(self, **kwargs):
        return self.call('parse_array_data', kwargs=kwargs)

    def apply_settings(self, **kwargs):
        return self.call('apply_settings', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def is_opened(self, **kwargs):
        return self.call('is_opened', kwargs=kwargs)

    def lock(self, **kwargs):
        return self.call('lock', kwargs=kwargs)

    def unlock(self, **kwargs):
        return self.call('unlock', kwargs=kwargs)

    def locking(self, **kwargs):
        return self.call('locking', kwargs=kwargs)

    def get_settings(self, **kwargs):
        return self.call('get_settings', kwargs=kwargs)

    def get_full_status(self, **kwargs):
        return self.call('get_full_status', kwargs=kwargs)

    def get_full_info(self, **kwargs):
        return self.call('get_full_info', kwargs=kwargs)

    def get_device_variable(self, **kwargs):
        return self.call('get_device_variable', kwargs=kwargs)

    def set_device_variable(self, **kwargs):
        return self.call('set_device_variable', kwargs=kwargs)

