from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubSbemimageSbemimage(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/SBEMimage_SBEMimage', 'source_file': 'src/microtome/Microtome_katana.py', 'class_name': 'Microtome_katana', 'import_roots': [], 'candidate_methods': ['save_to_cfg', 'connect', 'initialise_motor', 'do_full_cut', 'run_cut_sequence', 'check_cut_cycle_status', 'do_full_approach_cut', 'do_sweep', 'cut', 'retract_knife', 'get_stage_z', 'get_stage_z_prev_session', 'move_stage_to_z', 'near_knife', 'clear_knife', 'get_clear_position', 'set_clear_position', 'get_retract_clearance', 'set_retract_clearance', 'reset_error_state'], 'metadata': {'repo': 'sbemimage/sbemimage', 'repo_url': 'https://github.com/SBEMimage/SBEMimage', 'unit_id': 'gh_zeiss_merlin', 'source_file': 'src/microtome/Microtome_katana.py', 'candidate_score': 135, 'manufacturer': 'ZEISS', 'model_name': 'ZEISS Merlin/GeminiSEM'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def save_to_cfg(self, **kwargs):
        return self.call('save_to_cfg', kwargs=kwargs)

    def connect(self, **kwargs):
        return self.call('connect', kwargs=kwargs)

    def initialise_motor(self, **kwargs):
        return self.call('initialise_motor', kwargs=kwargs)

    def do_full_cut(self, **kwargs):
        return self.call('do_full_cut', kwargs=kwargs)

    def run_cut_sequence(self, **kwargs):
        return self.call('run_cut_sequence', kwargs=kwargs)

    def check_cut_cycle_status(self, **kwargs):
        return self.call('check_cut_cycle_status', kwargs=kwargs)

    def do_full_approach_cut(self, **kwargs):
        return self.call('do_full_approach_cut', kwargs=kwargs)

    def do_sweep(self, **kwargs):
        return self.call('do_sweep', kwargs=kwargs)

    def cut(self, **kwargs):
        return self.call('cut', kwargs=kwargs)

    def retract_knife(self, **kwargs):
        return self.call('retract_knife', kwargs=kwargs)

    def get_stage_z(self, **kwargs):
        return self.call('get_stage_z', kwargs=kwargs)

    def get_stage_z_prev_session(self, **kwargs):
        return self.call('get_stage_z_prev_session', kwargs=kwargs)

    def move_stage_to_z(self, **kwargs):
        return self.call('move_stage_to_z', kwargs=kwargs)

    def near_knife(self, **kwargs):
        return self.call('near_knife', kwargs=kwargs)

    def clear_knife(self, **kwargs):
        return self.call('clear_knife', kwargs=kwargs)

    def get_clear_position(self, **kwargs):
        return self.call('get_clear_position', kwargs=kwargs)

    def set_clear_position(self, **kwargs):
        return self.call('set_clear_position', kwargs=kwargs)

    def get_retract_clearance(self, **kwargs):
        return self.call('get_retract_clearance', kwargs=kwargs)

    def set_retract_clearance(self, **kwargs):
        return self.call('set_retract_clearance', kwargs=kwargs)

    def reset_error_state(self, **kwargs):
        return self.call('reset_error_state', kwargs=kwargs)

