from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubCambiegroupFlowchem(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/cambiegroup_flowchem', 'source_file': 'src/flowchem/devices/mettlertoledo/icir.py', 'class_name': 'IcIR', 'import_roots': [], 'candidate_methods': ['initialize', 'is_local', 'ensure_version_is_supported', 'is_iCIR_connected', 'probe_info', 'probe_status', 'last_sample_time', 'sample_count', 'is_template_name_valid', 'parse_probe_info', 'spectrum_from_node', 'last_spectrum_treated', 'last_spectrum_raw', 'last_spectrum_background', 'start_experiment', 'stop_experiment', 'wait_until_idle'], 'metadata': {'repo': 'cambiegroup/flowchem', 'repo_url': 'https://github.com/cambiegroup/flowchem', 'unit_id': 'gh_harvard_apparatus_elite_11', 'source_file': 'src/flowchem/devices/mettlertoledo/icir.py', 'candidate_score': 104, 'manufacturer': 'Harvard Apparatus', 'model_name': 'Harvard Apparatus Elite 11'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def initialize(self, **kwargs):
        return self.call('initialize', kwargs=kwargs)

    def is_local(self, **kwargs):
        return self.call('is_local', kwargs=kwargs)

    def ensure_version_is_supported(self, **kwargs):
        return self.call('ensure_version_is_supported', kwargs=kwargs)

    def is_iCIR_connected(self, **kwargs):
        return self.call('is_iCIR_connected', kwargs=kwargs)

    def probe_info(self, **kwargs):
        return self.call('probe_info', kwargs=kwargs)

    def probe_status(self, **kwargs):
        return self.call('probe_status', kwargs=kwargs)

    def last_sample_time(self, **kwargs):
        return self.call('last_sample_time', kwargs=kwargs)

    def sample_count(self, **kwargs):
        return self.call('sample_count', kwargs=kwargs)

    def is_template_name_valid(self, **kwargs):
        return self.call('is_template_name_valid', kwargs=kwargs)

    def parse_probe_info(self, **kwargs):
        return self.call('parse_probe_info', kwargs=kwargs)

    def spectrum_from_node(self, **kwargs):
        return self.call('spectrum_from_node', kwargs=kwargs)

    def last_spectrum_treated(self, **kwargs):
        return self.call('last_spectrum_treated', kwargs=kwargs)

    def last_spectrum_raw(self, **kwargs):
        return self.call('last_spectrum_raw', kwargs=kwargs)

    def last_spectrum_background(self, **kwargs):
        return self.call('last_spectrum_background', kwargs=kwargs)

    def start_experiment(self, **kwargs):
        return self.call('start_experiment', kwargs=kwargs)

    def stop_experiment(self, **kwargs):
        return self.call('stop_experiment', kwargs=kwargs)

    def wait_until_idle(self, **kwargs):
        return self.call('wait_until_idle', kwargs=kwargs)

