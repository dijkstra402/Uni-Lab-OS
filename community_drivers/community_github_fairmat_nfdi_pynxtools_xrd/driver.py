from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubFairmatNfdiPynxtoolsXrd(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/FAIRmat-NFDI_pynxtools-xrd', 'source_file': 'src/pynxtools_xrd/reader.py', 'class_name': 'XRDReader', 'import_roots': [], 'candidate_methods': ['convert_quantity_to_value_units', 'handle_objects', 'get_attr', 'setup_template', 'read'], 'metadata': {'repo': 'fairmat-nfdi/pynxtools-xrd', 'repo_url': 'https://github.com/FAIRmat-NFDI/pynxtools-xrd', 'unit_id': 'gh_panalytical_xpert_pro__xrdml', 'source_file': 'src/pynxtools_xrd/reader.py', 'candidate_score': 54, 'manufacturer': 'PANalytical', 'model_name': "PANalytical X'Pert PRO (.xrdml)"}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def convert_quantity_to_value_units(self, **kwargs):
        return self.call('convert_quantity_to_value_units', kwargs=kwargs)

    def handle_objects(self, **kwargs):
        return self.call('handle_objects', kwargs=kwargs)

    def get_attr(self, **kwargs):
        return self.call('get_attr', kwargs=kwargs)

    def setup_template(self, **kwargs):
        return self.call('setup_template', kwargs=kwargs)

    def read(self, **kwargs):
        return self.call('read', kwargs=kwargs)

