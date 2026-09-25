from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubBuchiLabortechnikAgOpeninterfaceExamplesPython(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/buchi-labortechnik-ag_openinterface_examples_python', 'source_file': 'modbus_server/modbus_server.py', 'class_name': 'CallbackDataBlock', 'import_roots': [], 'candidate_methods': ['setValues'], 'metadata': {'repo': 'buchi-labortechnik-ag/openinterface_examples_python', 'repo_url': 'https://github.com/buchi-labortechnik-ag/openinterface_examples_python', 'unit_id': 'gh_buchi_rotavapor_r_300', 'source_file': 'modbus_server/modbus_server.py', 'candidate_score': 33, 'manufacturer': 'Buchi', 'model_name': 'Buchi Rotavapor R-300'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def setValues(self, **kwargs):
        return self.call('setValues', kwargs=kwargs)

