from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentTwistBioscienceBiofoundryPlatform(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/Edinburgh-Genome-Foundry__DnaCauldron', 'source_file': 'dnacauldron/SequenceRepository.py', 'class_name': 'SequenceRepository', 'import_roots': [], 'candidate_methods': ['add_record', 'add_records', 'contains_record', 'get_record', 'get_records', 'import_records', 'get_part_names_by_collection', 'get_all_part_names', 'suggest_part_names'], 'action_targets': {}, 'metadata': {'repo': 'Edinburgh-Genome-Foundry/DnaCauldron', 'repo_url': 'https://github.com/Edinburgh-Genome-Foundry/DnaCauldron', 'brand': 'Twist Bioscience', 'model': 'BioFoundry Platform', 'device_type_cn': 'DNA合成仪', 'device_type_en': 'DNA Synthesizer', 'source_framework': 'DNA-Cauldron', 'tag_id': '4405', 'tag_name': '核酸合成仪', 'tag_name_en': 'Nucleic Acid Synthesizer', 'candidate_score': 126, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def add_record(self, **kwargs):
        return self.call('add_record', kwargs=kwargs)

    def add_records(self, **kwargs):
        return self.call('add_records', kwargs=kwargs)

    def contains_record(self, **kwargs):
        return self.call('contains_record', kwargs=kwargs)

    def get_record(self, **kwargs):
        return self.call('get_record', kwargs=kwargs)

    def get_records(self, **kwargs):
        return self.call('get_records', kwargs=kwargs)

    def import_records(self, **kwargs):
        return self.call('import_records', kwargs=kwargs)

    def get_part_names_by_collection(self, **kwargs):
        return self.call('get_part_names_by_collection', kwargs=kwargs)

    def get_all_part_names(self, **kwargs):
        return self.call('get_all_part_names', kwargs=kwargs)

    def suggest_part_names(self, **kwargs):
        return self.call('suggest_part_names', kwargs=kwargs)

