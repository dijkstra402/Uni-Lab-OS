from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubJaneliaPythonMettlerToledoDevicePython(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/janelia-python_mettler_toledo_device_python', 'source_file': 'mettler_toledo_device/mettler_toledo_device.py', 'class_name': 'MettlerToledoDevice', 'import_roots': [], 'candidate_methods': ['close', 'get_port', 'get_commands', 'get_mtsics_level', 'get_balance_data', 'get_software_version', 'get_serial_number', 'get_software_id', 'get_weight_stable', 'get_weight', 'zero_stable', 'zero', 'reset'], 'metadata': {'repo': 'janelia-python/mettler_toledo_device_python', 'repo_url': 'https://github.com/janelia-python/mettler_toledo_device_python', 'unit_id': 'gh_mettler_toledo_xs204_mt_sics', 'source_file': 'mettler_toledo_device/mettler_toledo_device.py', 'candidate_score': 101, 'manufacturer': 'Mettler Toledo', 'model_name': 'Mettler Toledo XS204 (MT-SICS)'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def get_port(self, **kwargs):
        return self.call('get_port', kwargs=kwargs)

    def get_commands(self, **kwargs):
        return self.call('get_commands', kwargs=kwargs)

    def get_mtsics_level(self, **kwargs):
        return self.call('get_mtsics_level', kwargs=kwargs)

    def get_balance_data(self, **kwargs):
        return self.call('get_balance_data', kwargs=kwargs)

    def get_software_version(self, **kwargs):
        return self.call('get_software_version', kwargs=kwargs)

    def get_serial_number(self, **kwargs):
        return self.call('get_serial_number', kwargs=kwargs)

    def get_software_id(self, **kwargs):
        return self.call('get_software_id', kwargs=kwargs)

    def get_weight_stable(self, **kwargs):
        return self.call('get_weight_stable', kwargs=kwargs)

    def get_weight(self, **kwargs):
        return self.call('get_weight', kwargs=kwargs)

    def zero_stable(self, **kwargs):
        return self.call('zero_stable', kwargs=kwargs)

    def zero(self, **kwargs):
        return self.call('zero', kwargs=kwargs)

    def reset(self, **kwargs):
        return self.call('reset', kwargs=kwargs)

