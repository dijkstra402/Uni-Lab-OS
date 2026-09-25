from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentWatsonMarlow520530(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/Auto-flow-synthesis__HSCF-based-automation', 'source_file': 'asiapumpFn.py', 'class_name': 'asiapumpFn', 'import_roots': [], 'candidate_methods': ['asiapump_status', 'asiapump_keepActi', 'asiapump_init', 'asiapump_status_update', 'asiapump_lbl_update', 'asiapump_filling', 'asiapump_emptying', 'asiapump_pumping', 'asiapump_stoping', 'close', 'asiapump_getlasterror'], 'action_targets': {}, 'metadata': {'repo': 'Auto-flow-synthesis/HSCF-based-automation', 'repo_url': 'https://github.com/Auto-flow-synthesis/HSCF-based-automation', 'brand': 'Watson-Marlow', 'model': '520/530', 'device_type_cn': '蠕动泵', 'device_type_en': 'Peristaltic Pump', 'source_framework': '专用驱动', 'tag_id': '4451', 'tag_name': '蠕动泵', 'tag_name_en': 'Peristaltic Pump', 'candidate_score': 146, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def asiapump_status(self, **kwargs):
        return self.call('asiapump_status', kwargs=kwargs)

    def asiapump_keepActi(self, **kwargs):
        return self.call('asiapump_keepActi', kwargs=kwargs)

    def asiapump_init(self, **kwargs):
        return self.call('asiapump_init', kwargs=kwargs)

    def asiapump_status_update(self, **kwargs):
        return self.call('asiapump_status_update', kwargs=kwargs)

    def asiapump_lbl_update(self, **kwargs):
        return self.call('asiapump_lbl_update', kwargs=kwargs)

    def asiapump_filling(self, **kwargs):
        return self.call('asiapump_filling', kwargs=kwargs)

    def asiapump_emptying(self, **kwargs):
        return self.call('asiapump_emptying', kwargs=kwargs)

    def asiapump_pumping(self, **kwargs):
        return self.call('asiapump_pumping', kwargs=kwargs)

    def asiapump_stoping(self, **kwargs):
        return self.call('asiapump_stoping', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def asiapump_getlasterror(self, **kwargs):
        return self.call('asiapump_getlasterror', kwargs=kwargs)

