from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentUniqsisFlowsyn(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/JohanvdWesthuizen__FlowChem-ClosedLoopOpt', 'source_file': 'Python_code/Allylation_code.py', 'class_name': 'Allylation1', 'import_roots': [], 'candidate_methods': ['grab_data', 'to_dict'], 'action_targets': {}, 'metadata': {'repo': 'JohanvdWesthuizen/FlowChem-ClosedLoopOpt', 'repo_url': 'https://github.com/JohanvdWesthuizen/FlowChem-ClosedLoopOpt', 'brand': 'Uniqsis', 'model': 'FlowSyn', 'device_type_cn': '微通道反应器', 'device_type_en': 'Microreactor', 'source_framework': '专用驱动', 'tag_id': '4388', 'tag_name': '微通道反应器', 'tag_name_en': 'Microreactor', 'candidate_score': 46, 'parse_status': 'ok', 'quality_status': 'thin', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def grab_data(self, **kwargs):
        return self.call('grab_data', kwargs=kwargs)

    def to_dict(self, **kwargs):
        return self.call('to_dict', kwargs=kwargs)

