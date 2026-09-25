from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubJmovsJump(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/JMoVS_JUMP', 'source_file': 'MeasurementHardware.py', 'class_name': 'MeasurementDeviceChooser', 'import_roots': [], 'candidate_methods': ['initialize_instrument', 'detect_devices', 'select_device'], 'metadata': {'repo': 'jmovs/jump', 'repo_url': 'https://github.com/JMoVS/JUMP', 'unit_id': 'gh_novocontrol_alpha_analyzer', 'source_file': 'MeasurementHardware.py', 'candidate_score': 235, 'manufacturer': 'Novocontrol', 'model_name': 'Novocontrol Alpha Analyzer'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def initialize_instrument(self, **kwargs):
        return self.call('initialize_instrument', kwargs=kwargs)

    def detect_devices(self, **kwargs):
        return self.call('detect_devices', kwargs=kwargs)

    def select_device(self, **kwargs):
        return self.call('select_device', kwargs=kwargs)

