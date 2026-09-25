from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubPylabrobotPylabrobot(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/PyLabRobot_pylabrobot', 'source_file': 'pylabrobot/storage/inheco/incubator_shaker_backend.py', 'class_name': 'InhecoIncubatorShakerStackBackend', 'import_roots': [], 'candidate_methods': ['number_of_connected_units', 'setup', 'stop', 'send_command', 'request_firmware_version', 'request_serial_number', 'request_last_calibration_date', 'request_machine_allocation', 'request_number_of_connected_machines', 'request_labware_detection_threshold', 'request_incubator_type', 'request_plate_in_incubator', 'request_operation_time_in_hours', 'request_drawer_cycles_performed', 'request_is_initialized', 'request_plate_status_known', 'request_thermal_calibration_date', 'request_calibration_low', 'request_calibration_high', 'request_whole_calibration_data'], 'metadata': {'repo': 'pylabrobot/pylabrobot', 'repo_url': 'https://github.com/PyLabRobot/pylabrobot', 'unit_id': 'gh_biotek_cytation_5', 'source_file': 'pylabrobot/storage/inheco/incubator_shaker_backend.py', 'candidate_score': 128, 'manufacturer': 'BioTek', 'model_name': 'BioTek Cytation 5'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def number_of_connected_units(self, **kwargs):
        return self.call('number_of_connected_units', kwargs=kwargs)

    def setup(self, **kwargs):
        return self.call('setup', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

    def send_command(self, **kwargs):
        return self.call('send_command', kwargs=kwargs)

    def request_firmware_version(self, **kwargs):
        return self.call('request_firmware_version', kwargs=kwargs)

    def request_serial_number(self, **kwargs):
        return self.call('request_serial_number', kwargs=kwargs)

    def request_last_calibration_date(self, **kwargs):
        return self.call('request_last_calibration_date', kwargs=kwargs)

    def request_machine_allocation(self, **kwargs):
        return self.call('request_machine_allocation', kwargs=kwargs)

    def request_number_of_connected_machines(self, **kwargs):
        return self.call('request_number_of_connected_machines', kwargs=kwargs)

    def request_labware_detection_threshold(self, **kwargs):
        return self.call('request_labware_detection_threshold', kwargs=kwargs)

    def request_incubator_type(self, **kwargs):
        return self.call('request_incubator_type', kwargs=kwargs)

    def request_plate_in_incubator(self, **kwargs):
        return self.call('request_plate_in_incubator', kwargs=kwargs)

    def request_operation_time_in_hours(self, **kwargs):
        return self.call('request_operation_time_in_hours', kwargs=kwargs)

    def request_drawer_cycles_performed(self, **kwargs):
        return self.call('request_drawer_cycles_performed', kwargs=kwargs)

    def request_is_initialized(self, **kwargs):
        return self.call('request_is_initialized', kwargs=kwargs)

    def request_plate_status_known(self, **kwargs):
        return self.call('request_plate_status_known', kwargs=kwargs)

    def request_thermal_calibration_date(self, **kwargs):
        return self.call('request_thermal_calibration_date', kwargs=kwargs)

    def request_calibration_low(self, **kwargs):
        return self.call('request_calibration_low', kwargs=kwargs)

    def request_calibration_high(self, **kwargs):
        return self.call('request_calibration_high', kwargs=kwargs)

    def request_whole_calibration_data(self, **kwargs):
        return self.call('request_whole_calibration_data', kwargs=kwargs)

