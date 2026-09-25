from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubRparakAbbEgmPython(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/rparak_ABB_EGM_Python', 'source_file': 'src/Lib/EGM/Core.py', 'class_name': 'EGM_Control_Cls', 'import_roots': [], 'candidate_methods': ['Time', 'Theta', 'T_EE', 'Close', 'Set_Absolute_Joint_Position'], 'metadata': {'repo': 'rparak/abb_egm_python', 'repo_url': 'https://github.com/rparak/ABB_EGM_Python', 'unit_id': 'gh_abb_irb_120', 'source_file': 'src/Lib/EGM/Core.py', 'candidate_score': 61, 'manufacturer': 'ABB', 'model_name': 'ABB IRB 120 / IRB 14000 (YuMi)'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def Time(self, **kwargs):
        return self.call('Time', kwargs=kwargs)

    def Theta(self, **kwargs):
        return self.call('Theta', kwargs=kwargs)

    def T_EE(self, **kwargs):
        return self.call('T_EE', kwargs=kwargs)

    def Close(self, **kwargs):
        return self.call('Close', kwargs=kwargs)

    def Set_Absolute_Joint_Position(self, **kwargs):
        return self.call('Set_Absolute_Joint_Position', kwargs=kwargs)

