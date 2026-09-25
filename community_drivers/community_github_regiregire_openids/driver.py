from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubRegiregireOpenids(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/regiregire_OpenIDS', 'source_file': 'OpenIDS_sys.py', 'class_name': 'System', 'import_roots': [], 'candidate_methods': ['connection', 'ink_manual_move', 'set_current_position', 'syringe_init', 'line', 'printing_Act', 'printing_T', 'printing_both', 'flush', 'pre_wet', 'printing_Test', 'x_init', 'moving', 'wait', 'blow', 'Sblow', 'Bulk_dT', 'wash', 'oxidation', 'wash_no_use'], 'metadata': {'repo': 'regiregire/openids', 'repo_url': 'https://github.com/regiregire/OpenIDS', 'unit_id': 'gh_openids_openids_v1', 'source_file': 'OpenIDS_sys.py', 'candidate_score': 80, 'manufacturer': 'OpenIDS', 'model_name': 'OpenIDS OpenIDS v1'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def connection(self, **kwargs):
        return self.call('connection', kwargs=kwargs)

    def ink_manual_move(self, **kwargs):
        return self.call('ink_manual_move', kwargs=kwargs)

    def set_current_position(self, **kwargs):
        return self.call('set_current_position', kwargs=kwargs)

    def syringe_init(self, **kwargs):
        return self.call('syringe_init', kwargs=kwargs)

    def line(self, **kwargs):
        return self.call('line', kwargs=kwargs)

    def printing_Act(self, **kwargs):
        return self.call('printing_Act', kwargs=kwargs)

    def printing_T(self, **kwargs):
        return self.call('printing_T', kwargs=kwargs)

    def printing_both(self, **kwargs):
        return self.call('printing_both', kwargs=kwargs)

    def flush(self, **kwargs):
        return self.call('flush', kwargs=kwargs)

    def pre_wet(self, **kwargs):
        return self.call('pre_wet', kwargs=kwargs)

    def printing_Test(self, **kwargs):
        return self.call('printing_Test', kwargs=kwargs)

    def x_init(self, **kwargs):
        return self.call('x_init', kwargs=kwargs)

    def moving(self, **kwargs):
        return self.call('moving', kwargs=kwargs)

    def wait(self, **kwargs):
        return self.call('wait', kwargs=kwargs)

    def blow(self, **kwargs):
        return self.call('blow', kwargs=kwargs)

    def Sblow(self, **kwargs):
        return self.call('Sblow', kwargs=kwargs)

    def Bulk_dT(self, **kwargs):
        return self.call('Bulk_dT', kwargs=kwargs)

    def wash(self, **kwargs):
        return self.call('wash', kwargs=kwargs)

    def oxidation(self, **kwargs):
        return self.call('oxidation', kwargs=kwargs)

    def wash_no_use(self, **kwargs):
        return self.call('wash_no_use', kwargs=kwargs)

