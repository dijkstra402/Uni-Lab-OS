from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentRigakuSmartlabRas(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/Traecp__Rigaku-SmartLab', 'source_file': 'SmartLab.py', 'class_name': 'RSM', 'import_roots': [], 'candidate_methods': ['get_data', 'plot_2D', 'plot_1D'], 'action_targets': {}, 'metadata': {'repo': 'Traecp/Rigaku-SmartLab', 'repo_url': 'https://github.com/Traecp/Rigaku-SmartLab', 'brand': 'Rigaku', 'model': 'SmartLab (.RAS)', 'device_type_cn': 'XRD', 'device_type_en': 'X-Ray Diffractometer', 'source_framework': '光谱分析', 'tag_id': '4362', 'tag_name': 'X射线衍射仪', 'tag_name_en': 'X-Ray Diffractometer', 'candidate_score': 62, 'parse_status': 'ok', 'quality_status': 'thin', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_data(self, **kwargs):
        return self.call('get_data', kwargs=kwargs)

    def plot_2D(self, **kwargs):
        return self.call('plot_2D', kwargs=kwargs)

    def plot_1D(self, **kwargs):
        return self.call('plot_1D', kwargs=kwargs)

