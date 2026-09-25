from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentChemspeedCstApiClairify(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/ac-rad__clairify-chemspeed', 'source_file': 'match_function.py', 'class_name': '', 'import_roots': [], 'candidate_methods': ['load_spacy_model', 'preprocess_text', 'match_to_function'], 'action_targets': {'load_spacy_model': 'load_spacy_model', 'preprocess_text': 'preprocess_text', 'match_to_function': 'match_to_function'}, 'metadata': {'repo': 'ac-rad/clairify-chemspeed', 'repo_url': 'https://github.com/ac-rad/clairify-chemspeed', 'brand': 'Chemspeed', 'model': 'CST-API (clairify)', 'device_type_cn': '并行反应仪', 'device_type_en': 'Parallel Synthesizer', 'source_framework': '独立驱动', 'tag_id': '4385', 'tag_name': '并行反应仪', 'tag_name_en': 'Parallel Reactor', 'candidate_score': 21, 'parse_status': 'module_selected', 'quality_status': 'thin', 'quality_reasons': [], 'action_targets': {'load_spacy_model': 'load_spacy_model', 'preprocess_text': 'preprocess_text', 'match_to_function': 'match_to_function'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def load_spacy_model(self, **kwargs):
        return self.call('load_spacy_model', kwargs=kwargs)

    def preprocess_text(self, **kwargs):
        return self.call('preprocess_text', kwargs=kwargs)

    def match_to_function(self, **kwargs):
        return self.call('match_to_function', kwargs=kwargs)

