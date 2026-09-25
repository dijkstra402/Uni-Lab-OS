from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubPsyfoodPyqmix(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/psyfood_pyqmix', 'source_file': 'pyqmix/bus.py', 'class_name': 'QmixBus', 'import_roots': [], 'candidate_methods': ['open', 'close', 'start', 'stop'], 'metadata': {'repo': 'psyfood/pyqmix', 'repo_url': 'https://github.com/psyfood/pyqmix', 'unit_id': 'gh_cetoni_nemesys', 'source_file': 'pyqmix/bus.py', 'candidate_score': 54, 'manufacturer': 'Cetoni', 'model_name': 'Cetoni neMESYS'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def open(self, **kwargs):
        return self.call('open', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def start(self, **kwargs):
        return self.call('start', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

