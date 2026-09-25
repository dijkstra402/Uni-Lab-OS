from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityMissingCetoniSoftwareSilaCetoniPumps(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/CETONI-Software__sila_cetoni_pumps', 'source_file': 'sila_cetoni/pumps/__init__.py', 'class_name': 'CetoniPumpDevice', 'import_roots': [], 'candidate_methods': ['is_contiflow_pump', 'is_peristaltic_pump', 'set_operational', 'StopDosage', 'SetFillLevel', 'DoseVolume', 'GenerateFlow'], 'metadata': {'repo': 'CETONI-Software/sila_cetoni_pumps', 'repo_url': 'https://github.com/CETONI-Software/sila_cetoni_pumps', 'source_file': 'sila_cetoni/pumps/syringepumps/sila/syringepump_service/feature_implementations/pumpunitcontroller_impl.py', 'candidate_score': 24, 'candidate_reason': '', 'manufacturers': ['Cetoni'], 'models': ['Nemesys系列(官方SiLA2)'], 'tags': ['柱塞泵'], 'notes': ['CETONI官方出品'], 'comm_protocols': ['SiLA2协议 + QmixSDK'], 'review_status': 'good', 'review_notes': ['改选 CetoniPumpDevice，覆盖 SiLA2 泵业务操作接口。']}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def is_contiflow_pump(self, **kwargs):
        return self.call('is_contiflow_pump', kwargs=kwargs)

    def is_peristaltic_pump(self, **kwargs):
        return self.call('is_peristaltic_pump', kwargs=kwargs)

    def set_operational(self, **kwargs):
        return self.call('set_operational', kwargs=kwargs)

    def StopDosage(self, **kwargs):
        return self.call('StopDosage', kwargs=kwargs)

    def SetFillLevel(self, **kwargs):
        return self.call('SetFillLevel', kwargs=kwargs)

    def DoseVolume(self, **kwargs):
        return self.call('DoseVolume', kwargs=kwargs)

    def GenerateFlow(self, **kwargs):
        return self.call('GenerateFlow', kwargs=kwargs)

