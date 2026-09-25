from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentNewEraNe1000(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/florian-lapp__nesp-lib-py', 'source_file': 'nesp_lib/pump.py', 'class_name': 'Pump', 'import_roots': [], 'candidate_methods': ['address', 'model_number', 'firmware_version', 'firmware_upgrade', 'safe_mode_timeout', 'status', 'running', 'syringe_diameter', 'pumping_direction', 'pumping_volume', 'pumping_rate', 'volume_infused', 'volume_infused_clear', 'volume_withdrawn', 'volume_withdrawn_clear', 'run', 'run_purge', 'stop', 'wait_while_running'], 'action_targets': {}, 'metadata': {'repo': 'florian-lapp/nesp-lib-py', 'repo_url': 'https://github.com/florian-lapp/nesp-lib-py', 'brand': 'New Era', 'model': 'NE-1000', 'device_type_cn': '注射泵', 'device_type_en': 'Syringe Pump', 'source_framework': '泵阀/液体处理', 'tag_id': '4413', 'tag_name': '注射泵', 'tag_name_en': 'Syringe Pump', 'candidate_score': 226, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def address(self, **kwargs):
        return self.call('address', kwargs=kwargs)

    def model_number(self, **kwargs):
        return self.call('model_number', kwargs=kwargs)

    def firmware_version(self, **kwargs):
        return self.call('firmware_version', kwargs=kwargs)

    def firmware_upgrade(self, **kwargs):
        return self.call('firmware_upgrade', kwargs=kwargs)

    def safe_mode_timeout(self, **kwargs):
        return self.call('safe_mode_timeout', kwargs=kwargs)

    def status(self, **kwargs):
        return self.call('status', kwargs=kwargs)

    def running(self, **kwargs):
        return self.call('running', kwargs=kwargs)

    def syringe_diameter(self, **kwargs):
        return self.call('syringe_diameter', kwargs=kwargs)

    def pumping_direction(self, **kwargs):
        return self.call('pumping_direction', kwargs=kwargs)

    def pumping_volume(self, **kwargs):
        return self.call('pumping_volume', kwargs=kwargs)

    def pumping_rate(self, **kwargs):
        return self.call('pumping_rate', kwargs=kwargs)

    def volume_infused(self, **kwargs):
        return self.call('volume_infused', kwargs=kwargs)

    def volume_infused_clear(self, **kwargs):
        return self.call('volume_infused_clear', kwargs=kwargs)

    def volume_withdrawn(self, **kwargs):
        return self.call('volume_withdrawn', kwargs=kwargs)

    def volume_withdrawn_clear(self, **kwargs):
        return self.call('volume_withdrawn_clear', kwargs=kwargs)

    def run(self, **kwargs):
        return self.call('run', kwargs=kwargs)

    def run_purge(self, **kwargs):
        return self.call('run_purge', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

    def wait_while_running(self, **kwargs):
        return self.call('wait_while_running', kwargs=kwargs)

