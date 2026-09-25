from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubAlliedvisionVimbapython(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/alliedvision_VimbaPython', 'source_file': 'vimba/interface.py', 'class_name': 'Interface', 'import_roots': [], 'candidate_methods': ['get_id', 'get_type', 'get_name', 'get_serial', 'read_memory', 'write_memory', 'read_registers', 'write_registers', 'get_all_features', 'get_features_affected_by', 'get_features_selected_by', 'get_features_by_type', 'get_features_by_category', 'get_feature_by_name'], 'metadata': {'repo': 'alliedvision/vimbapython', 'repo_url': 'https://github.com/alliedvision/VimbaPython', 'unit_id': 'gh_allied_vision_vimba', 'source_file': 'vimba/interface.py', 'candidate_score': 68, 'manufacturer': 'Allied Vision', 'model_name': 'Allied Vision Vimba/VmbPy'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def get_id(self, **kwargs):
        return self.call('get_id', kwargs=kwargs)

    def get_type(self, **kwargs):
        return self.call('get_type', kwargs=kwargs)

    def get_name(self, **kwargs):
        return self.call('get_name', kwargs=kwargs)

    def get_serial(self, **kwargs):
        return self.call('get_serial', kwargs=kwargs)

    def read_memory(self, **kwargs):
        return self.call('read_memory', kwargs=kwargs)

    def write_memory(self, **kwargs):
        return self.call('write_memory', kwargs=kwargs)

    def read_registers(self, **kwargs):
        return self.call('read_registers', kwargs=kwargs)

    def write_registers(self, **kwargs):
        return self.call('write_registers', kwargs=kwargs)

    def get_all_features(self, **kwargs):
        return self.call('get_all_features', kwargs=kwargs)

    def get_features_affected_by(self, **kwargs):
        return self.call('get_features_affected_by', kwargs=kwargs)

    def get_features_selected_by(self, **kwargs):
        return self.call('get_features_selected_by', kwargs=kwargs)

    def get_features_by_type(self, **kwargs):
        return self.call('get_features_by_type', kwargs=kwargs)

    def get_features_by_category(self, **kwargs):
        return self.call('get_features_by_category', kwargs=kwargs)

    def get_feature_by_name(self, **kwargs):
        return self.call('get_feature_by_name', kwargs=kwargs)

