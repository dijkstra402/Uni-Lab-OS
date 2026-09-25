from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubCzbiohubSfOtTempdeckControl(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/czbiohub-sf_ot-tempdeck-control', 'source_file': 'ot_tempdeck/_driver.py', 'class_name': 'TempdeckControl', 'import_roots': [], 'candidate_methods': ['open_first_device', 'from_usb_location', 'from_serial_portname', 'list_connected_devices', 'set_target_temp', 'get_temps', 'get_target_temp', 'get_current_temp', 'deactivate', 'model_name', 'serial_no', 'fw_version'], 'metadata': {'repo': 'czbiohub-sf/ot-tempdeck-control', 'repo_url': 'https://github.com/czbiohub-sf/ot-tempdeck-control', 'unit_id': 'gh_opentrons_temperature_module', 'source_file': 'ot_tempdeck/_driver.py', 'candidate_score': 146, 'manufacturer': 'Opentrons', 'model_name': 'Opentrons Temperature Module'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def open_first_device(self, **kwargs):
        return self.call('open_first_device', kwargs=kwargs)

    def from_usb_location(self, **kwargs):
        return self.call('from_usb_location', kwargs=kwargs)

    def from_serial_portname(self, **kwargs):
        return self.call('from_serial_portname', kwargs=kwargs)

    def list_connected_devices(self, **kwargs):
        return self.call('list_connected_devices', kwargs=kwargs)

    def set_target_temp(self, **kwargs):
        return self.call('set_target_temp', kwargs=kwargs)

    def get_temps(self, **kwargs):
        return self.call('get_temps', kwargs=kwargs)

    def get_target_temp(self, **kwargs):
        return self.call('get_target_temp', kwargs=kwargs)

    def get_current_temp(self, **kwargs):
        return self.call('get_current_temp', kwargs=kwargs)

    def deactivate(self, **kwargs):
        return self.call('deactivate', kwargs=kwargs)

    def model_name(self, **kwargs):
        return self.call('model_name', kwargs=kwargs)

    def serial_no(self, **kwargs):
        return self.call('serial_no', kwargs=kwargs)

    def fw_version(self, **kwargs):
        return self.call('fw_version', kwargs=kwargs)

