from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubAlchem0x2aPyWdfReader(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/alchem0x2A_py-wdf-reader', 'source_file': 'renishawWiRE/wdfReader.py', 'class_name': 'WDFReader', 'import_roots': [], 'candidate_methods': ['close', 'print_info'], 'metadata': {'repo': 'alchem0x2a/py-wdf-reader', 'repo_url': 'https://github.com/alchem0x2A/py-wdf-reader', 'unit_id': 'gh_renishaw_invia_qontor', 'source_file': 'renishawWiRE/wdfReader.py', 'candidate_score': 57, 'manufacturer': 'Renishaw', 'model_name': 'Renishaw inVia Qontor'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def print_info(self, **kwargs):
        return self.call('print_info', kwargs=kwargs)

