from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentBrukerTensor27(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/qedsoftware__brukeropusreader', 'source_file': 'brukeropusreader/opus_reader.py', 'class_name': '', 'import_roots': [], 'candidate_methods': ['read_data_type', 'read_channel_type', 'read_text_type', 'read_chunk_size', 'read_offset', 'read_chunk'], 'action_targets': {'read_data_type': 'read_data_type', 'read_channel_type': 'read_channel_type', 'read_text_type': 'read_text_type', 'read_chunk_size': 'read_chunk_size', 'read_offset': 'read_offset', 'read_chunk': 'read_chunk'}, 'metadata': {'repo': 'qedsoftware/brukeropusreader', 'repo_url': 'https://github.com/qedsoftware/brukeropusreader', 'brand': 'Bruker', 'model': 'Tensor 27', 'device_type_cn': 'FTIR光谱仪', 'device_type_en': 'FTIR Spectrometer', 'source_framework': '光谱分析', 'tag_id': '4440', 'tag_name': '红外光谱仪', 'tag_name_en': 'Infrared Spectrometer', 'candidate_score': 62, 'parse_status': 'module_reselected', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'read_data_type': 'read_data_type', 'read_channel_type': 'read_channel_type', 'read_text_type': 'read_text_type', 'read_chunk_size': 'read_chunk_size', 'read_offset': 'read_offset', 'read_chunk': 'read_chunk'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def read_data_type(self, **kwargs):
        return self.call('read_data_type', kwargs=kwargs)

    def read_channel_type(self, **kwargs):
        return self.call('read_channel_type', kwargs=kwargs)

    def read_text_type(self, **kwargs):
        return self.call('read_text_type', kwargs=kwargs)

    def read_chunk_size(self, **kwargs):
        return self.call('read_chunk_size', kwargs=kwargs)

    def read_offset(self, **kwargs):
        return self.call('read_offset', kwargs=kwargs)

    def read_chunk(self, **kwargs):
        return self.call('read_chunk', kwargs=kwargs)

