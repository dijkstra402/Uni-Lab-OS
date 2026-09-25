from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictAfg3252(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/QCoDeS__Qcodes_contrib_drivers', 'source_file': 'src/qcodes_contrib_drivers/drivers/Tektronix/AFG3000.py', 'class_name': 'AFG3000', 'import_roots': ['src'], 'candidate_methods': ['self_calibrate', 'self_test', 'abort', 'reset', 'wait', 'save', 'recall', 'synchronize_phase', 'reset_edit_memory', 'upload_waveform', 'get_trigger_mode', 'set_trigger_mode', 'get_ref_osc_source', 'set_ref_osc_source', 'get_trigger_slope', 'set_trigger_slope', 'get_trigger_source', 'set_trigger_source', 'get_trigger_timer', 'set_trigger_timer'], 'action_targets': {'get_trigger_mode': '__qcodes_param_get__trigger_mode', 'set_trigger_mode': '__qcodes_param_set__trigger_mode', 'get_ref_osc_source': '__qcodes_param_get__ref_osc_source', 'set_ref_osc_source': '__qcodes_param_set__ref_osc_source', 'get_trigger_slope': '__qcodes_param_get__trigger_slope', 'set_trigger_slope': '__qcodes_param_set__trigger_slope', 'get_trigger_source': '__qcodes_param_get__trigger_source', 'set_trigger_source': '__qcodes_param_set__trigger_source', 'get_trigger_timer': '__qcodes_param_get__trigger_timer', 'set_trigger_timer': '__qcodes_param_set__trigger_timer'}, 'metadata': {'repo': 'QCoDeS/Qcodes_contrib_drivers', 'repo_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers', 'source_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers/blob/main/src/qcodes_contrib_drivers/drivers/Tektronix/AFG3000.py', 'confidence': 0.95, 'quality_score': 1.11, 'parse_status': 'class_reselected', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'get_trigger_mode': '__qcodes_param_get__trigger_mode', 'set_trigger_mode': '__qcodes_param_set__trigger_mode', 'get_ref_osc_source': '__qcodes_param_get__ref_osc_source', 'set_ref_osc_source': '__qcodes_param_set__ref_osc_source', 'get_trigger_slope': '__qcodes_param_get__trigger_slope', 'set_trigger_slope': '__qcodes_param_set__trigger_slope', 'get_trigger_source': '__qcodes_param_get__trigger_source', 'set_trigger_source': '__qcodes_param_set__trigger_source', 'get_trigger_timer': '__qcodes_param_get__trigger_timer', 'set_trigger_timer': '__qcodes_param_set__trigger_timer'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def self_calibrate(self, **kwargs):
        return self.call('self_calibrate', kwargs=kwargs)

    def self_test(self, **kwargs):
        return self.call('self_test', kwargs=kwargs)

    def abort(self, **kwargs):
        return self.call('abort', kwargs=kwargs)

    def reset(self, **kwargs):
        return self.call('reset', kwargs=kwargs)

    def wait(self, **kwargs):
        return self.call('wait', kwargs=kwargs)

    def save(self, **kwargs):
        return self.call('save', kwargs=kwargs)

    def recall(self, **kwargs):
        return self.call('recall', kwargs=kwargs)

    def synchronize_phase(self, **kwargs):
        return self.call('synchronize_phase', kwargs=kwargs)

    def reset_edit_memory(self, **kwargs):
        return self.call('reset_edit_memory', kwargs=kwargs)

    def upload_waveform(self, **kwargs):
        return self.call('upload_waveform', kwargs=kwargs)

    def get_trigger_mode(self, **kwargs):
        return self.call('get_trigger_mode', kwargs=kwargs)

    def set_trigger_mode(self, **kwargs):
        return self.call('set_trigger_mode', kwargs=kwargs)

    def get_ref_osc_source(self, **kwargs):
        return self.call('get_ref_osc_source', kwargs=kwargs)

    def set_ref_osc_source(self, **kwargs):
        return self.call('set_ref_osc_source', kwargs=kwargs)

    def get_trigger_slope(self, **kwargs):
        return self.call('get_trigger_slope', kwargs=kwargs)

    def set_trigger_slope(self, **kwargs):
        return self.call('set_trigger_slope', kwargs=kwargs)

    def get_trigger_source(self, **kwargs):
        return self.call('get_trigger_source', kwargs=kwargs)

    def set_trigger_source(self, **kwargs):
        return self.call('set_trigger_source', kwargs=kwargs)

    def get_trigger_timer(self, **kwargs):
        return self.call('get_trigger_timer', kwargs=kwargs)

    def set_trigger_timer(self, **kwargs):
        return self.call('set_trigger_timer', kwargs=kwargs)

