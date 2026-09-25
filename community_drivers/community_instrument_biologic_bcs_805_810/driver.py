from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentBiologicBcs805810(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/dgbowl__tomato', 'source_file': 'src/tomato/driverinterface_2_0/__init__.py', 'class_name': 'ModelInterface', 'import_roots': ['src'], 'candidate_methods': ['DeviceFactory', 'cmp_register', 'cmp_teardown', 'cmp_reset', 'cmp_set_attr', 'cmp_get_attr', 'cmp_status', 'cmp_capabilities', 'cmp_attrs', 'cmp_constants', 'cmp_last_data', 'cmp_measure', 'task_start', 'task_status', 'task_stop', 'task_data', 'task_validate', 'status', 'quit', 'reset'], 'action_targets': {}, 'metadata': {'repo': 'dgbowl/tomato', 'repo_url': 'https://github.com/dgbowl/tomato', 'brand': 'BioLogic', 'model': 'BCS-805/810', 'device_type_cn': '电池测试柜', 'device_type_en': 'Battery Test Cabinet', 'source_framework': 'tomato', 'tag_id': '4427', 'tag_name': '电池测试柜', 'tag_name_en': 'Battery Test Cabinet', 'candidate_score': 198, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def DeviceFactory(self, **kwargs):
        return self.call('DeviceFactory', kwargs=kwargs)

    def cmp_register(self, **kwargs):
        return self.call('cmp_register', kwargs=kwargs)

    def cmp_teardown(self, **kwargs):
        return self.call('cmp_teardown', kwargs=kwargs)

    def cmp_reset(self, **kwargs):
        return self.call('cmp_reset', kwargs=kwargs)

    def cmp_set_attr(self, **kwargs):
        return self.call('cmp_set_attr', kwargs=kwargs)

    def cmp_get_attr(self, **kwargs):
        return self.call('cmp_get_attr', kwargs=kwargs)

    def cmp_status(self, **kwargs):
        return self.call('cmp_status', kwargs=kwargs)

    def cmp_capabilities(self, **kwargs):
        return self.call('cmp_capabilities', kwargs=kwargs)

    def cmp_attrs(self, **kwargs):
        return self.call('cmp_attrs', kwargs=kwargs)

    def cmp_constants(self, **kwargs):
        return self.call('cmp_constants', kwargs=kwargs)

    def cmp_last_data(self, **kwargs):
        return self.call('cmp_last_data', kwargs=kwargs)

    def cmp_measure(self, **kwargs):
        return self.call('cmp_measure', kwargs=kwargs)

    def task_start(self, **kwargs):
        return self.call('task_start', kwargs=kwargs)

    def task_status(self, **kwargs):
        return self.call('task_status', kwargs=kwargs)

    def task_stop(self, **kwargs):
        return self.call('task_stop', kwargs=kwargs)

    def task_data(self, **kwargs):
        return self.call('task_data', kwargs=kwargs)

    def task_validate(self, **kwargs):
        return self.call('task_validate', kwargs=kwargs)

    def status(self, **kwargs):
        return self.call('status', kwargs=kwargs)

    def quit(self, **kwargs):
        return self.call('quit', kwargs=kwargs)

    def reset(self, **kwargs):
        return self.call('reset', kwargs=kwargs)

