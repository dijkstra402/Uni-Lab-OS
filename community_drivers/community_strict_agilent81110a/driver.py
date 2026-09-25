from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictAgilent81110a(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/mabuchilab__Instrumental', 'source_file': 'src/instrumental/drivers/funcgenerators/agilent.py', 'class_name': 'Agilent81110A', 'import_roots': ['src'], 'candidate_methods': ['set_subsystem', 'set_polarity', 'get_polarity', 'set_trigger_source', 'get_trigger_source', 'set_trigger_sensing', 'get_trigger_sensing', 'set_trigger_slope', 'get_trigger_slope', 'get_errors', 'set_delay', 'set_out_impedance', 'set_width', 'set_high', 'set_low', 'output1', 'output2', 'combined', 'trigger_level', 'get', 'close', 'save_instrument', 'observe', 'query', 'transaction', 'resource'], 'action_targets': {}, 'metadata': {'repo': 'mabuchilab/Instrumental', 'repo_url': 'https://github.com/mabuchilab/Instrumental', 'source_url': 'https://github.com/mabuchilab/Instrumental/blob/main/src/instrumental/drivers/funcgenerators/agilent.py', 'confidence': 0.9, 'quality_score': 1.06, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def set_subsystem(self, **kwargs):
        return self.call('set_subsystem', kwargs=kwargs)

    def set_polarity(self, **kwargs):
        return self.call('set_polarity', kwargs=kwargs)

    def get_polarity(self, **kwargs):
        return self.call('get_polarity', kwargs=kwargs)

    def set_trigger_source(self, **kwargs):
        return self.call('set_trigger_source', kwargs=kwargs)

    def get_trigger_source(self, **kwargs):
        return self.call('get_trigger_source', kwargs=kwargs)

    def set_trigger_sensing(self, **kwargs):
        return self.call('set_trigger_sensing', kwargs=kwargs)

    def get_trigger_sensing(self, **kwargs):
        return self.call('get_trigger_sensing', kwargs=kwargs)

    def set_trigger_slope(self, **kwargs):
        return self.call('set_trigger_slope', kwargs=kwargs)

    def get_trigger_slope(self, **kwargs):
        return self.call('get_trigger_slope', kwargs=kwargs)

    def get_errors(self, **kwargs):
        return self.call('get_errors', kwargs=kwargs)

    def set_delay(self, **kwargs):
        return self.call('set_delay', kwargs=kwargs)

    def set_out_impedance(self, **kwargs):
        return self.call('set_out_impedance', kwargs=kwargs)

    def set_width(self, **kwargs):
        return self.call('set_width', kwargs=kwargs)

    def set_high(self, **kwargs):
        return self.call('set_high', kwargs=kwargs)

    def set_low(self, **kwargs):
        return self.call('set_low', kwargs=kwargs)

    def output1(self, **kwargs):
        return self.call('output1', kwargs=kwargs)

    def output2(self, **kwargs):
        return self.call('output2', kwargs=kwargs)

    def combined(self, **kwargs):
        return self.call('combined', kwargs=kwargs)

    def trigger_level(self, **kwargs):
        return self.call('trigger_level', kwargs=kwargs)

    def get(self, **kwargs):
        return self.call('get', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def save_instrument(self, **kwargs):
        return self.call('save_instrument', kwargs=kwargs)

    def observe(self, **kwargs):
        return self.call('observe', kwargs=kwargs)

    def query(self, **kwargs):
        return self.call('query', kwargs=kwargs)

    def transaction(self, **kwargs):
        return self.call('transaction', kwargs=kwargs)

    def resource(self, **kwargs):
        return self.call('resource', kwargs=kwargs)

