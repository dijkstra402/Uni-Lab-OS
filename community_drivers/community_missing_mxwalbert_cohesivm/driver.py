from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityMissingMxwalbertCohesivm(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/mxwalbert__cohesivm', 'source_file': 'cohesivm/devices/agilent/Agilent4284A.py', 'class_name': 'Agilent4284A', 'import_roots': [], 'candidate_methods': ['enable', 'disable', 'set_oscillator_frequency', 'set_oscillator_voltage', 'set_oscillator_current', 'measure_impedance', 'channels'], 'metadata': {'repo': 'mxwalbert/cohesivm', 'repo_url': 'https://github.com/mxwalbert/cohesivm', 'source_file': 'cohesivm/devices/agilent/Agilent4156C.py', 'candidate_score': 159, 'candidate_reason': '', 'manufacturers': ['Agilent/HP'], 'models': ['4284A精密LCR表'], 'tags': ['介电常数测定仪'], 'notes': ['COHESIVM测量框架的一部分'], 'comm_protocols': ['GPIB via pyvisa'], 'review_status': 'good', 'review_notes': ['改选 Agilent4284A（HP 4284A LCR 表），与元数据标注仪器一致。']}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def enable(self, **kwargs):
        return self.call('enable', kwargs=kwargs)

    def disable(self, **kwargs):
        return self.call('disable', kwargs=kwargs)

    def set_oscillator_frequency(self, **kwargs):
        return self.call('set_oscillator_frequency', kwargs=kwargs)

    def set_oscillator_voltage(self, **kwargs):
        return self.call('set_oscillator_voltage', kwargs=kwargs)

    def set_oscillator_current(self, **kwargs):
        return self.call('set_oscillator_current', kwargs=kwargs)

    def measure_impedance(self, **kwargs):
        return self.call('measure_impedance', kwargs=kwargs)

    def channels(self, **kwargs):
        return self.call('channels', kwargs=kwargs)

