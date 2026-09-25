from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubDemarcolabFibsem(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/DeMarcoLab_fibsem', 'source_file': 'fibsem/microscope.py', 'class_name': 'ThermoMicroscope', 'import_roots': [], 'candidate_methods': ['reconnect', 'disconnect', 'connect_to_microscope', 'set_channel', 'acquire_image', 'last_image', 'acquire_chamber_image', 'autocontrast', 'auto_focus', 'beam_shift', 'move_stage_absolute', 'move_stage_relative', 'stable_move', 'vertical_move', 'get_stage_orientation', 'safe_absolute_stage_movement', 'project_stable_move', 'insert_manipulator', 'retract_manipulator', 'move_manipulator_relative'], 'metadata': {'repo': 'demarcolab/fibsem', 'repo_url': 'https://github.com/DeMarcoLab/fibsem', 'unit_id': 'gh_thermo_fisher_autoscript_fib_sem', 'source_file': 'fibsem/microscope.py', 'candidate_score': 72, 'manufacturer': 'Thermo Fisher', 'model_name': 'Thermo Fisher AutoScript FIB-SEM'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def reconnect(self, **kwargs):
        return self.call('reconnect', kwargs=kwargs)

    def disconnect(self, **kwargs):
        return self.call('disconnect', kwargs=kwargs)

    def connect_to_microscope(self, **kwargs):
        return self.call('connect_to_microscope', kwargs=kwargs)

    def set_channel(self, **kwargs):
        return self.call('set_channel', kwargs=kwargs)

    def acquire_image(self, **kwargs):
        return self.call('acquire_image', kwargs=kwargs)

    def last_image(self, **kwargs):
        return self.call('last_image', kwargs=kwargs)

    def acquire_chamber_image(self, **kwargs):
        return self.call('acquire_chamber_image', kwargs=kwargs)

    def autocontrast(self, **kwargs):
        return self.call('autocontrast', kwargs=kwargs)

    def auto_focus(self, **kwargs):
        return self.call('auto_focus', kwargs=kwargs)

    def beam_shift(self, **kwargs):
        return self.call('beam_shift', kwargs=kwargs)

    def move_stage_absolute(self, **kwargs):
        return self.call('move_stage_absolute', kwargs=kwargs)

    def move_stage_relative(self, **kwargs):
        return self.call('move_stage_relative', kwargs=kwargs)

    def stable_move(self, **kwargs):
        return self.call('stable_move', kwargs=kwargs)

    def vertical_move(self, **kwargs):
        return self.call('vertical_move', kwargs=kwargs)

    def get_stage_orientation(self, **kwargs):
        return self.call('get_stage_orientation', kwargs=kwargs)

    def safe_absolute_stage_movement(self, **kwargs):
        return self.call('safe_absolute_stage_movement', kwargs=kwargs)

    def project_stable_move(self, **kwargs):
        return self.call('project_stable_move', kwargs=kwargs)

    def insert_manipulator(self, **kwargs):
        return self.call('insert_manipulator', kwargs=kwargs)

    def retract_manipulator(self, **kwargs):
        return self.call('retract_manipulator', kwargs=kwargs)

    def move_manipulator_relative(self, **kwargs):
        return self.call('move_manipulator_relative', kwargs=kwargs)

