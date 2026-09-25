from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubDennisVanGilsPythonDvgDevices(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/Dennis-van-Gils_python-dvg-devices', 'source_file': 'src/dvg_devices/Keysight_N8700_protocol_SCPI.py', 'class_name': 'Keysight_N8700', 'import_roots': [], 'candidate_methods': ['close', 'connect', 'begin', 'reinitialize', 'write', 'query', 'clear_and_reset', 'wait_for_OPC', 'wait_for_OPC_indefinitely', 'prepare_wait_for_OPC_indefinitely', 'query_error', 'query_all_errors_in_queue', 'query_status_QC', 'query_status_OC', 'set_PON_off', 'clear_output_protection', 'set_ENA_OCP', 'query_ENA_OCP', 'set_OVP_level', 'query_OVP_level'], 'metadata': {'repo': 'dennis-van-gils/python-dvg-devices', 'repo_url': 'https://github.com/Dennis-van-Gils/python-dvg-devices', 'unit_id': 'gh_julabo_fp51_sl', 'source_file': 'src/dvg_devices/Keysight_N8700_protocol_SCPI.py', 'candidate_score': 182, 'manufacturer': 'Julabo', 'model_name': 'Julabo FP51-SL'}}

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

