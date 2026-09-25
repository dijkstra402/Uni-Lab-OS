from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubMicrosoftQcodes(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/microsoft_Qcodes', 'source_file': 'src/qcodes/instrument_drivers/QuantumDesign/DynaCoolPPMS/DynaCool.py', 'class_name': 'DynaCool', 'import_roots': [], 'candidate_methods': ['error_code', 'get_idn', 'ramp', 'write', 'ask', 'close'], 'metadata': {'repo': 'microsoft/qcodes', 'repo_url': 'https://github.com/microsoft/Qcodes', 'unit_id': 'gh_agilent_e4980a', 'source_file': 'src/qcodes/instrument_drivers/QuantumDesign/DynaCoolPPMS/DynaCool.py', 'candidate_score': 270, 'manufacturer': 'Agilent/Keysight', 'model_name': 'Agilent/Keysight E4980A/AL'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def error_code(self, **kwargs):
        return self.call('error_code', kwargs=kwargs)

    def get_idn(self, **kwargs):
        return self.call('get_idn', kwargs=kwargs)

    def ramp(self, **kwargs):
        return self.call('ramp', kwargs=kwargs)

    def write(self, **kwargs):
        return self.call('write', kwargs=kwargs)

    def ask(self, **kwargs):
        return self.call('ask', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

