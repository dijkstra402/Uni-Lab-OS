from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubPhotometricsPyvcam(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/Photometrics_PyVCAM', 'source_file': 'src/pyvcam/camera.py', 'class_name': 'Camera', 'import_roots': [], 'candidate_methods': ['get_available_camera_names', 'detect_camera', 'select_camera', 'open', 'close', 'check_frame_status', 'get_param', 'set_param', 'check_param', 'read_enum', 'reset_pp', 'reset_rois', 'set_roi', 'poll_frame', 'get_frame', 'get_sequence', 'get_vtm_sequence', 'start_live', 'start_seq', 'finish'], 'metadata': {'repo': 'photometrics/pyvcam', 'repo_url': 'https://github.com/Photometrics/PyVCAM', 'unit_id': 'gh_photometrics_prime_bsi', 'source_file': 'src/pyvcam/camera.py', 'candidate_score': 68, 'manufacturer': 'Photometrics', 'model_name': 'Photometrics Prime BSI'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def get_available_camera_names(self, **kwargs):
        return self.call('get_available_camera_names', kwargs=kwargs)

    def detect_camera(self, **kwargs):
        return self.call('detect_camera', kwargs=kwargs)

    def select_camera(self, **kwargs):
        return self.call('select_camera', kwargs=kwargs)

    def open(self, **kwargs):
        return self.call('open', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def check_frame_status(self, **kwargs):
        return self.call('check_frame_status', kwargs=kwargs)

    def get_param(self, **kwargs):
        return self.call('get_param', kwargs=kwargs)

    def set_param(self, **kwargs):
        return self.call('set_param', kwargs=kwargs)

    def check_param(self, **kwargs):
        return self.call('check_param', kwargs=kwargs)

    def read_enum(self, **kwargs):
        return self.call('read_enum', kwargs=kwargs)

    def reset_pp(self, **kwargs):
        return self.call('reset_pp', kwargs=kwargs)

    def reset_rois(self, **kwargs):
        return self.call('reset_rois', kwargs=kwargs)

    def set_roi(self, **kwargs):
        return self.call('set_roi', kwargs=kwargs)

    def poll_frame(self, **kwargs):
        return self.call('poll_frame', kwargs=kwargs)

    def get_frame(self, **kwargs):
        return self.call('get_frame', kwargs=kwargs)

    def get_sequence(self, **kwargs):
        return self.call('get_sequence', kwargs=kwargs)

    def get_vtm_sequence(self, **kwargs):
        return self.call('get_vtm_sequence', kwargs=kwargs)

    def start_live(self, **kwargs):
        return self.call('start_live', kwargs=kwargs)

    def start_seq(self, **kwargs):
        return self.call('start_seq', kwargs=kwargs)

    def finish(self, **kwargs):
        return self.call('finish', kwargs=kwargs)

