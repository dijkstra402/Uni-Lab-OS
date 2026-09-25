from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentSpectrumInstrumentationM2p5933X4(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/PyMoDAQ__pymodaq_plugins_spectrum_instrumentation', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'action_targets': {}, 'metadata': {'repo': 'PyMoDAQ/pymodaq_plugins_spectrum_instrumentation', 'repo_url': 'https://github.com/PyMoDAQ/pymodaq_plugins_spectrum_instrumentation', 'brand': 'Spectrum Instrumentation', 'model': 'M2p.5933-x4', 'device_type_cn': '数字化仪', 'device_type_en': 'Digitizer', 'source_framework': 'PyMoDAQ', 'tag_id': '4425', 'tag_name': '电化学工作站', 'tag_name_en': 'Electrochemical Workstation', 'candidate_score': -999.0, 'parse_status': 'repo_download_failed', 'quality_status': 'broken', 'quality_reasons': ['repo_download_failed'], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


