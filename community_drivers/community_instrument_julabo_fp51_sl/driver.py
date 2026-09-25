from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentJulaboFp51Sl(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/Dennis-van-Gils__python-dvg-devices', 'source_file': 'src/dvg_devices/Keysight_N8700_protocol_SCPI.py', 'class_name': 'Keysight_N8700', 'import_roots': ['src'], 'candidate_methods': ['close', 'connect', 'begin', 'reinitialize', 'write', 'query', 'clear_and_reset', 'wait_for_OPC', 'wait_for_OPC_indefinitely', 'prepare_wait_for_OPC_indefinitely', 'query_error', 'query_all_errors_in_queue', 'query_status_QC', 'query_status_OC', 'set_PON_off', 'clear_output_protection', 'set_ENA_OCP', 'query_ENA_OCP', 'set_OVP_level', 'query_OVP_level', 'clear_output_protection_and_turn_on', 'turn_on', 'turn_off', 'set_ENA_output', 'query_ENA_output', 'set_I_source', 'set_V_source', 'query_I_source', 'query_V_source', 'query_I_meas', 'query_V_meas', 'speed_test', 'speed_test2', 'report', 'read_config_file', 'write_config_file'], 'action_targets': {}, 'metadata': {'repo': 'Dennis-van-Gils/python-dvg-devices', 'repo_url': 'https://github.com/Dennis-van-Gils/python-dvg-devices', 'brand': 'Julabo', 'model': 'FP51-SL', 'device_type_cn': '循环浴', 'device_type_en': 'Circulating Bath', 'source_framework': '反应器/合成设备', 'tag_id': '4369', 'tag_name': '冷热水机', 'tag_name_en': 'Chiller / Heater Unit', 'candidate_score': 334, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def connect(self, **kwargs):
        return self.call('connect', kwargs=kwargs)

    def begin(self, **kwargs):
        return self.call('begin', kwargs=kwargs)

    def reinitialize(self, **kwargs):
        return self.call('reinitialize', kwargs=kwargs)

    def write(self, **kwargs):
        return self.call('write', kwargs=kwargs)

    def query(self, **kwargs):
        return self.call('query', kwargs=kwargs)

    def clear_and_reset(self, **kwargs):
        return self.call('clear_and_reset', kwargs=kwargs)

    def wait_for_OPC(self, **kwargs):
        return self.call('wait_for_OPC', kwargs=kwargs)

    def wait_for_OPC_indefinitely(self, **kwargs):
        return self.call('wait_for_OPC_indefinitely', kwargs=kwargs)

    def prepare_wait_for_OPC_indefinitely(self, **kwargs):
        return self.call('prepare_wait_for_OPC_indefinitely', kwargs=kwargs)

    def query_error(self, **kwargs):
        return self.call('query_error', kwargs=kwargs)

    def query_all_errors_in_queue(self, **kwargs):
        return self.call('query_all_errors_in_queue', kwargs=kwargs)

    def query_status_QC(self, **kwargs):
        return self.call('query_status_QC', kwargs=kwargs)

    def query_status_OC(self, **kwargs):
        return self.call('query_status_OC', kwargs=kwargs)

    def set_PON_off(self, **kwargs):
        return self.call('set_PON_off', kwargs=kwargs)

    def clear_output_protection(self, **kwargs):
        return self.call('clear_output_protection', kwargs=kwargs)

    def set_ENA_OCP(self, **kwargs):
        return self.call('set_ENA_OCP', kwargs=kwargs)

    def query_ENA_OCP(self, **kwargs):
        return self.call('query_ENA_OCP', kwargs=kwargs)

    def set_OVP_level(self, **kwargs):
        return self.call('set_OVP_level', kwargs=kwargs)

    def query_OVP_level(self, **kwargs):
        return self.call('query_OVP_level', kwargs=kwargs)

    def clear_output_protection_and_turn_on(self, **kwargs):
        return self.call('clear_output_protection_and_turn_on', kwargs=kwargs)

    def turn_on(self, **kwargs):
        return self.call('turn_on', kwargs=kwargs)

    def turn_off(self, **kwargs):
        return self.call('turn_off', kwargs=kwargs)

    def set_ENA_output(self, **kwargs):
        return self.call('set_ENA_output', kwargs=kwargs)

    def query_ENA_output(self, **kwargs):
        return self.call('query_ENA_output', kwargs=kwargs)

    def set_I_source(self, **kwargs):
        return self.call('set_I_source', kwargs=kwargs)

    def set_V_source(self, **kwargs):
        return self.call('set_V_source', kwargs=kwargs)

    def query_I_source(self, **kwargs):
        return self.call('query_I_source', kwargs=kwargs)

    def query_V_source(self, **kwargs):
        return self.call('query_V_source', kwargs=kwargs)

    def query_I_meas(self, **kwargs):
        return self.call('query_I_meas', kwargs=kwargs)

    def query_V_meas(self, **kwargs):
        return self.call('query_V_meas', kwargs=kwargs)

    def speed_test(self, **kwargs):
        return self.call('speed_test', kwargs=kwargs)

    def speed_test2(self, **kwargs):
        return self.call('speed_test2', kwargs=kwargs)

    def report(self, **kwargs):
        return self.call('report', kwargs=kwargs)

    def read_config_file(self, **kwargs):
        return self.call('read_config_file', kwargs=kwargs)

    def write_config_file(self, **kwargs):
        return self.call('write_config_file', kwargs=kwargs)

