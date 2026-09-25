from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubPaulscherrerinstituteShimadzuPump(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/paulscherrerinstitute_shimadzu_pump', 'source_file': 'shimadzu_pump/ioc.py', 'class_name': 'EpicsShimadzuPumpDriver', 'import_roots': [], 'candidate_methods': ['try_connect', 'poll_pump', 'write'], 'metadata': {'repo': 'paulscherrerinstitute/shimadzu_pump', 'repo_url': 'https://github.com/paulscherrerinstitute/shimadzu_pump', 'unit_id': 'gh_shimadzu_cbm_20a', 'source_file': 'shimadzu_pump/ioc.py', 'candidate_score': 78, 'manufacturer': 'Shimadzu', 'model_name': 'Shimadzu CBM-20A'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def try_connect(self, **kwargs):
        return self.call('try_connect', kwargs=kwargs)

    def poll_pump(self, **kwargs):
        return self.call('poll_pump', kwargs=kwargs)

    def write(self, **kwargs):
        return self.call('write', kwargs=kwargs)

