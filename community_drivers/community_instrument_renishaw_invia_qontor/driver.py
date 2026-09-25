from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentRenishawInviaQontor(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/alchem0x2A__py-wdf-reader', 'source_file': 'renishawWiRE/export.py', 'class_name': '', 'import_roots': [], 'candidate_methods': ['test_version', 'try_attr', 'get_pos', 'get_unit', 'main', 'handle_spectra', 'extract_img'], 'action_targets': {'test_version': 'test_version', 'try_attr': 'try_attr', 'get_pos': 'get_pos', 'get_unit': 'get_unit', 'main': 'main', 'handle_spectra': 'handle_spectra', 'extract_img': 'extract_img'}, 'metadata': {'repo': 'alchem0x2A/py-wdf-reader', 'repo_url': 'https://github.com/alchem0x2A/py-wdf-reader', 'brand': 'Renishaw', 'model': 'inVia Qontor', 'device_type_cn': '拉曼光谱仪', 'device_type_en': 'Raman Spectrometer', 'source_framework': '光谱分析', 'tag_id': '4392', 'tag_name': '拉曼光谱仪', 'tag_name_en': 'Raman Spectrometer', 'candidate_score': 94, 'parse_status': 'module_reselected', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'test_version': 'test_version', 'try_attr': 'try_attr', 'get_pos': 'get_pos', 'get_unit': 'get_unit', 'main': 'main', 'handle_spectra': 'handle_spectra', 'extract_img': 'extract_img'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def test_version(self, **kwargs):
        return self.call('test_version', kwargs=kwargs)

    def try_attr(self, **kwargs):
        return self.call('try_attr', kwargs=kwargs)

    def get_pos(self, **kwargs):
        return self.call('get_pos', kwargs=kwargs)

    def get_unit(self, **kwargs):
        return self.call('get_unit', kwargs=kwargs)

    def main(self, **kwargs):
        return self.call('main', kwargs=kwargs)

    def handle_spectra(self, **kwargs):
        return self.call('handle_spectra', kwargs=kwargs)

    def extract_img(self, **kwargs):
        return self.call('extract_img', kwargs=kwargs)

