from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityMissingMslnzMslEquipment(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/MSLNZ__msl-equipment', 'source_file': 'src/msl/equipment/config.py', 'class_name': 'Config', 'import_roots': ['src'], 'candidate_methods': ['attrib', 'equipment', 'find', 'findall', 'registers', 'value'], 'metadata': {'repo': 'MSLNZ/msl-equipment', 'repo_url': 'https://github.com/MSLNZ/msl-equipment', 'source_file': 'src/msl/equipment/interfaces/prologix.py', 'candidate_score': 157, 'candidate_reason': '', 'manufacturers': ['多品牌'], 'models': ['Sartorius, Mettler Toledo, 等ISO/IEC 17025兼容设备'], 'tags': ['固体称量工作站'], 'notes': ['新西兰计量标准实验室(MSL)出品'], 'comm_protocols': ['串口/GPIB等多接口'], 'review_status': 'needs_reselect', 'review_notes': ['框架型仓库，无单一仪器类。Config 是加载/访问设备配置的入口，非直接控制接口。']}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def attrib(self, **kwargs):
        return self.call('attrib', kwargs=kwargs)

    def equipment(self, **kwargs):
        return self.call('equipment', kwargs=kwargs)

    def find(self, **kwargs):
        return self.call('find', kwargs=kwargs)

    def findall(self, **kwargs):
        return self.call('findall', kwargs=kwargs)

    def registers(self, **kwargs):
        return self.call('registers', kwargs=kwargs)

    def value(self, **kwargs):
        return self.call('value', kwargs=kwargs)

