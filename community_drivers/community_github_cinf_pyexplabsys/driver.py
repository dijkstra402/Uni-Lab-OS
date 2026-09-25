from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubCinfPyexplabsys(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/CINF_PyExpLabSys', 'source_file': 'PyExpLabSys/drivers/crowcon.py', 'class_name': 'Vortex', 'import_roots': [], 'candidate_methods': ['close', 'read_register', 'read_string', 'read_bool', 'get_type', 'get_system_status', 'get_system_power_status', 'get_serial_number', 'get_system_name', 'get_number_installed_detectors', 'get_number_installed_digital_outputs', 'detector_configuration', 'get_detector_levels', 'get_multiple_detector_levels'], 'metadata': {'repo': 'cinf/pyexplabsys', 'repo_url': 'https://github.com/CINF/PyExpLabSys', 'unit_id': 'gh_moorfield_minilab', 'source_file': 'PyExpLabSys/drivers/crowcon.py', 'candidate_score': 164, 'manufacturer': 'Moorfield', 'model_name': 'Moorfield Minilab'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def read_register(self, **kwargs):
        return self.call('read_register', kwargs=kwargs)

    def read_string(self, **kwargs):
        return self.call('read_string', kwargs=kwargs)

    def read_bool(self, **kwargs):
        return self.call('read_bool', kwargs=kwargs)

    def get_type(self, **kwargs):
        return self.call('get_type', kwargs=kwargs)

    def get_system_status(self, **kwargs):
        return self.call('get_system_status', kwargs=kwargs)

    def get_system_power_status(self, **kwargs):
        return self.call('get_system_power_status', kwargs=kwargs)

    def get_serial_number(self, **kwargs):
        return self.call('get_serial_number', kwargs=kwargs)

    def get_system_name(self, **kwargs):
        return self.call('get_system_name', kwargs=kwargs)

    def get_number_installed_detectors(self, **kwargs):
        return self.call('get_number_installed_detectors', kwargs=kwargs)

    def get_number_installed_digital_outputs(self, **kwargs):
        return self.call('get_number_installed_digital_outputs', kwargs=kwargs)

    def detector_configuration(self, **kwargs):
        return self.call('detector_configuration', kwargs=kwargs)

    def get_detector_levels(self, **kwargs):
        return self.call('get_detector_levels', kwargs=kwargs)

    def get_multiple_detector_levels(self, **kwargs):
        return self.call('get_multiple_detector_levels', kwargs=kwargs)

