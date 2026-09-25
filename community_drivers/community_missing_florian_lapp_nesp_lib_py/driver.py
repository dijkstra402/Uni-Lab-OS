from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityMissingFlorianLappNespLibPy(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/florian-lapp__nesp-lib-py', 'source_file': 'nesp_lib/pump.py', 'class_name': 'Pump', 'import_roots': [], 'candidate_methods': ['status', 'running', 'model_number', 'safe_mode_timeout', 'syringe_diameter', 'pumping_direction', 'pumping_volume', 'pumping_rate', 'volume_infused', 'volume_infused_clear', 'volume_withdrawn', 'volume_withdrawn_clear', 'run', 'run_purge', 'stop', 'wait_while_running'], 'metadata': {'repo': 'florian-lapp/nesp-lib-py', 'repo_url': 'https://github.com/florian-lapp/nesp-lib-py', 'source_file': 'nesp_lib/port.py', 'candidate_score': 102, 'candidate_reason': '', 'manufacturers': ['New Era Pump Systems'], 'models': ['全系列(也兼容WPI Aladdin, Landgraf LA)'], 'tags': ['柱塞泵'], 'notes': ['PyPI: NESP-Lib'], 'comm_protocols': ['RS-232 pyserial'], 'review_status': 'good', 'review_notes': ['改选 Pump 类，覆盖注射泵核心控制操作。']}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def status(self, **kwargs):
        return self.call('status', kwargs=kwargs)

    def running(self, **kwargs):
        return self.call('running', kwargs=kwargs)

    def model_number(self, **kwargs):
        return self.call('model_number', kwargs=kwargs)

    def safe_mode_timeout(self, **kwargs):
        return self.call('safe_mode_timeout', kwargs=kwargs)

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

