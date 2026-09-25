from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictFsea20(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/mabuchilab__Instrumental', 'source_file': 'src/instrumental/drivers/spectrumanalyzers/rohde_schwarz.py', 'class_name': 'FSEA20', 'import_roots': ['src'], 'candidate_methods': ['get_trace', 'get', 'close', 'save_instrument', 'observe', 'query', 'transaction', 'resource'], 'action_targets': {}, 'metadata': {'repo': 'mabuchilab/Instrumental', 'repo_url': 'https://github.com/mabuchilab/Instrumental', 'source_url': 'https://github.com/mabuchilab/Instrumental/blob/main/src/instrumental/drivers/spectrumanalyzers/rohde_schwarz.py', 'confidence': 0.95, 'quality_score': 1.11, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_trace(self, **kwargs):
        return self.call('get_trace', kwargs=kwargs)

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

