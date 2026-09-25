from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubPythonMicroscopeMicroscope(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/python-microscope_microscope', 'source_file': 'microscope/controllers/zaber.py', 'class_name': 'ZaberDaisyChain', 'import_roots': [], 'candidate_methods': ['devices'], 'metadata': {'repo': 'python-microscope/microscope', 'repo_url': 'https://github.com/python-microscope/microscope', 'unit_id': 'gh_ximea_mc023mg_sy_ub', 'source_file': 'microscope/controllers/zaber.py', 'candidate_score': 83, 'manufacturer': 'Ximea', 'model_name': 'Ximea MC023MG-SY-UB'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def devices(self, **kwargs):
        return self.call('devices', kwargs=kwargs)

