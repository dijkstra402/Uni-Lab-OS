from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentInficonSqm160Sqc310(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/PABausson__pymodaq_plugins_inficon', 'source_file': 'src/pymodaq_plugins_inficon/daq_viewer_plugins/plugins_0D/daq_0Dviewer_SQM160.py', 'class_name': 'DAQ_0DViewer_SQM160', 'import_roots': ['src'], 'candidate_methods': ['ini_attributes', 'commit_settings', 'ini_detector', 'close', 'grab_data', 'callback', 'stop'], 'action_targets': {}, 'metadata': {'repo': 'PABausson/pymodaq_plugins_inficon', 'repo_url': 'https://github.com/PABausson/pymodaq_plugins_inficon', 'brand': 'Inficon', 'model': 'SQM-160/SQC-310', 'device_type_cn': '蒸镀仪', 'device_type_en': 'Evaporation Coater', 'source_framework': 'PyMoDAQ', 'tag_id': '4449', 'tag_name': '蒸镀仪', 'tag_name_en': 'Evaporation Coater', 'candidate_score': 150, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def ini_attributes(self, **kwargs):
        return self.call('ini_attributes', kwargs=kwargs)

    def commit_settings(self, **kwargs):
        return self.call('commit_settings', kwargs=kwargs)

    def ini_detector(self, **kwargs):
        return self.call('ini_detector', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def grab_data(self, **kwargs):
        return self.call('grab_data', kwargs=kwargs)

    def callback(self, **kwargs):
        return self.call('callback', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

