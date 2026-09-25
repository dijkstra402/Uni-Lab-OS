from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubNiermannTemscript(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/niermann_temscript', 'source_file': 'temscript/remote_microscope.py', 'class_name': 'RemoteMicroscope', 'import_roots': [], 'candidate_methods': ['get_family', 'get_microscope_id', 'get_version', 'get_voltage', 'get_vacuum', 'get_column_valves_open', 'set_column_valves_open', 'get_stage_holder', 'get_stage_status', 'get_stage_limits', 'get_stage_position', 'get_cameras', 'get_stem_detectors', 'get_camera_param', 'set_camera_param', 'get_stem_detector_param', 'set_stem_detector_param', 'get_stem_acquisition_param', 'set_stem_acquisition_param', 'acquire'], 'metadata': {'repo': 'niermann/temscript', 'repo_url': 'https://github.com/niermann/temscript', 'unit_id': 'gh_thermo_fisher_titan', 'source_file': 'temscript/remote_microscope.py', 'candidate_score': 87, 'manufacturer': 'Thermo Fisher/FEI', 'model_name': 'Thermo Fisher/FEI Titan/Krios'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def get_family(self, **kwargs):
        return self.call('get_family', kwargs=kwargs)

    def get_microscope_id(self, **kwargs):
        return self.call('get_microscope_id', kwargs=kwargs)

    def get_version(self, **kwargs):
        return self.call('get_version', kwargs=kwargs)

    def get_voltage(self, **kwargs):
        return self.call('get_voltage', kwargs=kwargs)

    def get_vacuum(self, **kwargs):
        return self.call('get_vacuum', kwargs=kwargs)

    def get_column_valves_open(self, **kwargs):
        return self.call('get_column_valves_open', kwargs=kwargs)

    def set_column_valves_open(self, **kwargs):
        return self.call('set_column_valves_open', kwargs=kwargs)

    def get_stage_holder(self, **kwargs):
        return self.call('get_stage_holder', kwargs=kwargs)

    def get_stage_status(self, **kwargs):
        return self.call('get_stage_status', kwargs=kwargs)

    def get_stage_limits(self, **kwargs):
        return self.call('get_stage_limits', kwargs=kwargs)

    def get_stage_position(self, **kwargs):
        return self.call('get_stage_position', kwargs=kwargs)

    def get_cameras(self, **kwargs):
        return self.call('get_cameras', kwargs=kwargs)

    def get_stem_detectors(self, **kwargs):
        return self.call('get_stem_detectors', kwargs=kwargs)

    def get_camera_param(self, **kwargs):
        return self.call('get_camera_param', kwargs=kwargs)

    def set_camera_param(self, **kwargs):
        return self.call('set_camera_param', kwargs=kwargs)

    def get_stem_detector_param(self, **kwargs):
        return self.call('get_stem_detector_param', kwargs=kwargs)

    def set_stem_detector_param(self, **kwargs):
        return self.call('set_stem_detector_param', kwargs=kwargs)

    def get_stem_acquisition_param(self, **kwargs):
        return self.call('get_stem_acquisition_param', kwargs=kwargs)

    def set_stem_acquisition_param(self, **kwargs):
        return self.call('set_stem_acquisition_param', kwargs=kwargs)

    def acquire(self, **kwargs):
        return self.call('acquire', kwargs=kwargs)

