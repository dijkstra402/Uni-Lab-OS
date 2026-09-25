from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubMachineagencyScienceJubilee(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/machineagency_science-jubilee', 'source_file': 'src/science_jubilee/tools/AS7341.py', 'class_name': 'AS7341', 'import_roots': [], 'candidate_methods': ['load_config', 'find_seeed', 'connect_seeed', 'disconnect_seeed', 'blink', 'measure_spectrum', 'get_raw_spectrum'], 'metadata': {'repo': 'machineagency/science-jubilee', 'repo_url': 'https://github.com/machineagency/science-jubilee', 'unit_id': 'gh_qsonica_sonicator', 'source_file': 'src/science_jubilee/tools/AS7341.py', 'candidate_score': 117, 'manufacturer': 'Qsonica', 'model_name': 'Qsonica Sonicator'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def load_config(self, **kwargs):
        return self.call('load_config', kwargs=kwargs)

    def find_seeed(self, **kwargs):
        return self.call('find_seeed', kwargs=kwargs)

    def connect_seeed(self, **kwargs):
        return self.call('connect_seeed', kwargs=kwargs)

    def disconnect_seeed(self, **kwargs):
        return self.call('disconnect_seeed', kwargs=kwargs)

    def blink(self, **kwargs):
        return self.call('blink', kwargs=kwargs)

    def measure_spectrum(self, **kwargs):
        return self.call('measure_spectrum', kwargs=kwargs)

    def get_raw_spectrum(self, **kwargs):
        return self.call('get_raw_spectrum', kwargs=kwargs)

