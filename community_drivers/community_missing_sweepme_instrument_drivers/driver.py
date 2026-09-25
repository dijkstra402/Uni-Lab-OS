from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityMissingSweepmeInstrumentDrivers(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/SweepMe__instrument-drivers', 'source_file': 'src/LCRmeter-HP_4284A/main.py', 'class_name': 'Device', 'import_roots': ['src/LCRmeter-HP_4284A'], 'candidate_methods': ['initialize', 'deinitialize', 'configure', 'measure', 'read_result', 'set_frequency', 'set_voltage', 'set_bias_voltage', 'set_bias_current', 'set_integration', 'poweron', 'poweroff'], 'metadata': {'repo': 'SweepMe/instrument-drivers', 'repo_url': 'https://github.com/SweepMe/instrument-drivers', 'source_file': 'src/Logger-DeviceClass_template/main.py', 'candidate_score': 131, 'candidate_reason': '', 'manufacturers': ['MBraun'], 'models': ['SCU101手套箱控制单元'], 'tags': ['气体保护干燥箱'], 'notes': ['文件: src/Switch-MBRAUN_SCU101/main.py'], 'comm_protocols': ['pysweepme框架(串口)'], 'review_status': 'good', 'review_notes': ['改选 HP 4284A LCR 表具体驱动（从模板基类改为具体仪器）。']}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def initialize(self, **kwargs):
        return self.call('initialize', kwargs=kwargs)

    def deinitialize(self, **kwargs):
        return self.call('deinitialize', kwargs=kwargs)

    def configure(self, **kwargs):
        return self.call('configure', kwargs=kwargs)

    def measure(self, **kwargs):
        return self.call('measure', kwargs=kwargs)

    def read_result(self, **kwargs):
        return self.call('read_result', kwargs=kwargs)

    def set_frequency(self, **kwargs):
        return self.call('set_frequency', kwargs=kwargs)

    def set_voltage(self, **kwargs):
        return self.call('set_voltage', kwargs=kwargs)

    def set_bias_voltage(self, **kwargs):
        return self.call('set_bias_voltage', kwargs=kwargs)

    def set_bias_current(self, **kwargs):
        return self.call('set_bias_current', kwargs=kwargs)

    def set_integration(self, **kwargs):
        return self.call('set_integration', kwargs=kwargs)

    def poweron(self, **kwargs):
        return self.call('poweron', kwargs=kwargs)

    def poweroff(self, **kwargs):
        return self.call('poweroff', kwargs=kwargs)

