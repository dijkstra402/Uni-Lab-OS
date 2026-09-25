from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityMissingPsyfoodPyqmix(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/psyfood__pyqmix', 'source_file': 'pyqmix/pump.py', 'class_name': 'QmixPump', 'import_roots': [], 'candidate_methods': ['enable', 'disable', 'is_enabled', 'is_in_fault_state', 'clear_fault_state', 'calibrate', 'set_volume_unit', 'set_flow_unit', 'set_syringe_params', 'set_syringe_params_by_type', 'volume_max', 'max_flow_rate', 'aspirate', 'dispense', 'set_fill_level', 'generate_flow', 'fill'], 'metadata': {'repo': 'psyfood/pyqmix', 'repo_url': 'https://github.com/psyfood/pyqmix', 'source_file': 'pyqmix/bus.py', 'candidate_score': 54, 'candidate_reason': '', 'manufacturers': ['Cetoni'], 'models': ['Nemesys系列注射泵'], 'tags': ['柱塞泵'], 'notes': ['PyPI: pyqmix / conda-forge可装'], 'comm_protocols': ['CFFI调用QmixSDK DLL'], 'review_status': 'good', 'review_notes': ['改选 QmixPump 类，覆盖 Cetoni 注射泵业务操作。']}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def enable(self, **kwargs):
        return self.call('enable', kwargs=kwargs)

    def disable(self, **kwargs):
        return self.call('disable', kwargs=kwargs)

    def is_enabled(self, **kwargs):
        return self.call('is_enabled', kwargs=kwargs)

    def is_in_fault_state(self, **kwargs):
        return self.call('is_in_fault_state', kwargs=kwargs)

    def clear_fault_state(self, **kwargs):
        return self.call('clear_fault_state', kwargs=kwargs)

    def calibrate(self, **kwargs):
        return self.call('calibrate', kwargs=kwargs)

    def set_volume_unit(self, **kwargs):
        return self.call('set_volume_unit', kwargs=kwargs)

    def set_flow_unit(self, **kwargs):
        return self.call('set_flow_unit', kwargs=kwargs)

    def set_syringe_params(self, **kwargs):
        return self.call('set_syringe_params', kwargs=kwargs)

    def set_syringe_params_by_type(self, **kwargs):
        return self.call('set_syringe_params_by_type', kwargs=kwargs)

    def volume_max(self, **kwargs):
        return self.call('volume_max', kwargs=kwargs)

    def max_flow_rate(self, **kwargs):
        return self.call('max_flow_rate', kwargs=kwargs)

    def aspirate(self, **kwargs):
        return self.call('aspirate', kwargs=kwargs)

    def dispense(self, **kwargs):
        return self.call('dispense', kwargs=kwargs)

    def set_fill_level(self, **kwargs):
        return self.call('set_fill_level', kwargs=kwargs)

    def generate_flow(self, **kwargs):
        return self.call('generate_flow', kwargs=kwargs)

    def fill(self, **kwargs):
        return self.call('fill', kwargs=kwargs)

