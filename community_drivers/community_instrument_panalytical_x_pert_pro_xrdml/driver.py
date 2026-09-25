from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentPanalyticalXPertProXrdml(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/FAIRmat-NFDI__pynxtools-xrd', 'source_file': 'src/pynxtools_xrd/reader.py', 'class_name': 'XRDReader', 'import_roots': ['src'], 'candidate_methods': ['convert_quantity_to_value_units', 'handle_objects', 'get_attr', 'setup_template', 'read'], 'action_targets': {}, 'metadata': {'repo': 'FAIRmat-NFDI/pynxtools-xrd', 'repo_url': 'https://github.com/FAIRmat-NFDI/pynxtools-xrd', 'brand': 'PANalytical', 'model': "X'Pert PRO (.xrdml)", 'device_type_cn': 'XRD', 'device_type_en': 'X-Ray Diffractometer', 'source_framework': '光谱分析', 'tag_id': '4362', 'tag_name': 'X射线衍射仪', 'tag_name_en': 'X-Ray Diffractometer', 'candidate_score': 98, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def convert_quantity_to_value_units(self, **kwargs):
        return self.call('convert_quantity_to_value_units', kwargs=kwargs)

    def handle_objects(self, **kwargs):
        return self.call('handle_objects', kwargs=kwargs)

    def get_attr(self, **kwargs):
        return self.call('get_attr', kwargs=kwargs)

    def setup_template(self, **kwargs):
        return self.call('setup_template', kwargs=kwargs)

    def read(self, **kwargs):
        return self.call('read', kwargs=kwargs)

