from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubElleryItOdooSerialScaleDrivers(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/ellery-it_odoo-serial-scale-drivers', 'source_file': '25.07/SSD-KernDE.py', 'class_name': 'KernDEDriver', 'import_roots': [], 'candidate_methods': ['supported'], 'metadata': {'repo': 'ellery-it/odoo-serial-scale-drivers', 'repo_url': 'https://github.com/ellery-it/odoo-serial-scale-drivers', 'unit_id': 'gh_kern_eoc', 'source_file': '25.07/SSD-KernDE.py', 'candidate_score': 59, 'manufacturer': 'Kern', 'model_name': 'Kern EOC/DE系列'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def supported(self, **kwargs):
        return self.call('supported', kwargs=kwargs)

