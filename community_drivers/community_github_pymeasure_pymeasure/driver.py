from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubPymeasurePymeasure(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/hp/hp8753e.py', 'class_name': 'HP8753E', 'import_roots': [], 'candidate_methods': ['set_sweep_time_fastest', 'averaging_restart', 'emit_beep', 'manu', 'model', 'fw', 'set_fixed_frequency', 'measuring_parameter', 'measuring_parameter', 'reset', 'scan', 'scan_single', 'frequencies', 'data_complex', 'shutdown'], 'metadata': {'repo': 'pymeasure/pymeasure', 'repo_url': 'https://github.com/pymeasure/pymeasure', 'unit_id': 'gh_thermotron_3800', 'source_file': 'pymeasure/instruments/hp/hp8753e.py', 'candidate_score': 197, 'manufacturer': 'Thermotron', 'model_name': 'Thermotron 3800'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def set_sweep_time_fastest(self, **kwargs):
        return self.call('set_sweep_time_fastest', kwargs=kwargs)

    def averaging_restart(self, **kwargs):
        return self.call('averaging_restart', kwargs=kwargs)

    def emit_beep(self, **kwargs):
        return self.call('emit_beep', kwargs=kwargs)

    def manu(self, **kwargs):
        return self.call('manu', kwargs=kwargs)

    def model(self, **kwargs):
        return self.call('model', kwargs=kwargs)

    def fw(self, **kwargs):
        return self.call('fw', kwargs=kwargs)

    def set_fixed_frequency(self, **kwargs):
        return self.call('set_fixed_frequency', kwargs=kwargs)

    def measuring_parameter(self, **kwargs):
        return self.call('measuring_parameter', kwargs=kwargs)

    def measuring_parameter(self, **kwargs):
        return self.call('measuring_parameter', kwargs=kwargs)

    def reset(self, **kwargs):
        return self.call('reset', kwargs=kwargs)

    def scan(self, **kwargs):
        return self.call('scan', kwargs=kwargs)

    def scan_single(self, **kwargs):
        return self.call('scan_single', kwargs=kwargs)

    def frequencies(self, **kwargs):
        return self.call('frequencies', kwargs=kwargs)

    def data_complex(self, **kwargs):
        return self.call('data_complex', kwargs=kwargs)

    def shutdown(self, **kwargs):
        return self.call('shutdown', kwargs=kwargs)

