from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentTiDlpNirscanNano(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/tidge27__NIRScan_Nano_Python', 'source_file': 'CissUsbConnectord.py', 'class_name': 'CISSNode', 'import_roots': [], 'candidate_methods': ['get_ini_config', 'connect', 'checkEventEnabled', 'disconnect', 'disable_sensors', 'enable_sensors', 'get_type', 'parse_payload', 'stream', 'config_sensors'], 'action_targets': {}, 'metadata': {'repo': 'tidge27/NIRScan_Nano_Python', 'repo_url': 'https://github.com/tidge27/NIRScan_Nano_Python', 'brand': 'TI', 'model': 'DLP NIRscan Nano', 'device_type_cn': '近红外光谱仪', 'device_type_en': 'NIR Spectrometer', 'source_framework': '光谱分析', 'tag_id': '4440', 'tag_name': '红外光谱仪', 'tag_name_en': 'Infrared Spectrometer', 'candidate_score': 110, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_ini_config(self, **kwargs):
        return self.call('get_ini_config', kwargs=kwargs)

    def connect(self, **kwargs):
        return self.call('connect', kwargs=kwargs)

    def checkEventEnabled(self, **kwargs):
        return self.call('checkEventEnabled', kwargs=kwargs)

    def disconnect(self, **kwargs):
        return self.call('disconnect', kwargs=kwargs)

    def disable_sensors(self, **kwargs):
        return self.call('disable_sensors', kwargs=kwargs)

    def enable_sensors(self, **kwargs):
        return self.call('enable_sensors', kwargs=kwargs)

    def get_type(self, **kwargs):
        return self.call('get_type', kwargs=kwargs)

    def parse_payload(self, **kwargs):
        return self.call('parse_payload', kwargs=kwargs)

    def stream(self, **kwargs):
        return self.call('stream', kwargs=kwargs)

    def config_sensors(self, **kwargs):
        return self.call('config_sensors', kwargs=kwargs)

