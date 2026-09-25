from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAbbIrb120Irb14000Yumi(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/rparak__ABB_EGM_Python', 'source_file': 'src/Lib/Transformation/Core.py', 'class_name': 'Quaternion_Cls', 'import_roots': ['src'], 'candidate_methods': ['all', 'Type', 'Shape', 'w', 'x', 'y', 'z', 'Scalar', 'Vector', 'Norm', 'Normalize', 'Conjugate', 'Inverse', 'Dot', 'Difference', 'Logarithm', 'Exponential', 'Rotate', 'Distance', 'Get_Angle_Axis', 'Get_Homogeneous_Transformation_Matrix'], 'action_targets': {}, 'metadata': {'repo': 'rparak/ABB_EGM_Python', 'repo_url': 'https://github.com/rparak/ABB_EGM_Python', 'brand': 'ABB', 'model': 'IRB 120 / IRB 14000 (YuMi)', 'device_type_cn': '协作机械臂', 'device_type_en': 'Collaborative Robot', 'source_framework': '机器人/运动控制', 'tag_id': '4402', 'tag_name': '机械臂', 'tag_name_en': 'Robotic Arm', 'candidate_score': 198, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def all(self, **kwargs):
        return self.call('all', kwargs=kwargs)

    def Type(self, **kwargs):
        return self.call('Type', kwargs=kwargs)

    def Shape(self, **kwargs):
        return self.call('Shape', kwargs=kwargs)

    def w(self, **kwargs):
        return self.call('w', kwargs=kwargs)

    def x(self, **kwargs):
        return self.call('x', kwargs=kwargs)

    def y(self, **kwargs):
        return self.call('y', kwargs=kwargs)

    def z(self, **kwargs):
        return self.call('z', kwargs=kwargs)

    def Scalar(self, **kwargs):
        return self.call('Scalar', kwargs=kwargs)

    def Vector(self, **kwargs):
        return self.call('Vector', kwargs=kwargs)

    def Norm(self, **kwargs):
        return self.call('Norm', kwargs=kwargs)

    def Normalize(self, **kwargs):
        return self.call('Normalize', kwargs=kwargs)

    def Conjugate(self, **kwargs):
        return self.call('Conjugate', kwargs=kwargs)

    def Inverse(self, **kwargs):
        return self.call('Inverse', kwargs=kwargs)

    def Dot(self, **kwargs):
        return self.call('Dot', kwargs=kwargs)

    def Difference(self, **kwargs):
        return self.call('Difference', kwargs=kwargs)

    def Logarithm(self, **kwargs):
        return self.call('Logarithm', kwargs=kwargs)

    def Exponential(self, **kwargs):
        return self.call('Exponential', kwargs=kwargs)

    def Rotate(self, **kwargs):
        return self.call('Rotate', kwargs=kwargs)

    def Distance(self, **kwargs):
        return self.call('Distance', kwargs=kwargs)

    def Get_Angle_Axis(self, **kwargs):
        return self.call('Get_Angle_Axis', kwargs=kwargs)

    def Get_Homogeneous_Transformation_Matrix(self, **kwargs):
        return self.call('Get_Homogeneous_Transformation_Matrix', kwargs=kwargs)

