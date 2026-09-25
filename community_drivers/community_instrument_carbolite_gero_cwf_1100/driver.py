from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentCarboliteGeroCwf1100(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/BAMresearch__MAPz_at_BAM', 'source_file': 'Minerva/Releases/Version_1.0.0/Hardware/OtherHardware/MolecularDevices.py', 'class_name': 'SpectraMaxM3', 'import_roots': [], 'candidate_methods': ['connect', 'disconnect', 'spectramax_error', 'spectramax_command_completed', 'spectramax_instrument_status_changed', 'close_document', 'close_all_documents', 'close_drawer', 'export_as', 'get_data_copy', 'get_drawer_status', 'get_temperature', 'get_version', 'new_document', 'new_experiment', 'new_notes', 'new_plate', 'open_drawer', 'open_file', 'quit', 'save_as', 'shake', 'shake_on', 'shake_off', 'set_temperature', 'start_read', 'stop_read', 'start_measurement', 'write_spr_file', 'parent_hardware', 'dump_configuration', 'post_load_from_config'], 'action_targets': {}, 'metadata': {'repo': 'BAMresearch/MAPz_at_BAM', 'repo_url': 'https://github.com/BAMresearch/MAPz_at_BAM', 'brand': 'Carbolite Gero', 'model': 'CWF 1100', 'device_type_cn': '箱式电阻炉', 'device_type_en': 'Box Furnace', 'source_framework': 'MAPz', 'tag_id': '4438', 'tag_name': '箱式电阻炉', 'tag_name_en': 'Box Resistance Furnace', 'candidate_score': 262, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def connect(self, **kwargs):
        return self.call('connect', kwargs=kwargs)

    def disconnect(self, **kwargs):
        return self.call('disconnect', kwargs=kwargs)

    def spectramax_error(self, **kwargs):
        return self.call('spectramax_error', kwargs=kwargs)

    def spectramax_command_completed(self, **kwargs):
        return self.call('spectramax_command_completed', kwargs=kwargs)

    def spectramax_instrument_status_changed(self, **kwargs):
        return self.call('spectramax_instrument_status_changed', kwargs=kwargs)

    def close_document(self, **kwargs):
        return self.call('close_document', kwargs=kwargs)

    def close_all_documents(self, **kwargs):
        return self.call('close_all_documents', kwargs=kwargs)

    def close_drawer(self, **kwargs):
        return self.call('close_drawer', kwargs=kwargs)

    def export_as(self, **kwargs):
        return self.call('export_as', kwargs=kwargs)

    def get_data_copy(self, **kwargs):
        return self.call('get_data_copy', kwargs=kwargs)

    def get_drawer_status(self, **kwargs):
        return self.call('get_drawer_status', kwargs=kwargs)

    def get_temperature(self, **kwargs):
        return self.call('get_temperature', kwargs=kwargs)

    def get_version(self, **kwargs):
        return self.call('get_version', kwargs=kwargs)

    def new_document(self, **kwargs):
        return self.call('new_document', kwargs=kwargs)

    def new_experiment(self, **kwargs):
        return self.call('new_experiment', kwargs=kwargs)

    def new_notes(self, **kwargs):
        return self.call('new_notes', kwargs=kwargs)

    def new_plate(self, **kwargs):
        return self.call('new_plate', kwargs=kwargs)

    def open_drawer(self, **kwargs):
        return self.call('open_drawer', kwargs=kwargs)

    def open_file(self, **kwargs):
        return self.call('open_file', kwargs=kwargs)

    def quit(self, **kwargs):
        return self.call('quit', kwargs=kwargs)

    def save_as(self, **kwargs):
        return self.call('save_as', kwargs=kwargs)

    def shake(self, **kwargs):
        return self.call('shake', kwargs=kwargs)

    def shake_on(self, **kwargs):
        return self.call('shake_on', kwargs=kwargs)

    def shake_off(self, **kwargs):
        return self.call('shake_off', kwargs=kwargs)

    def set_temperature(self, **kwargs):
        return self.call('set_temperature', kwargs=kwargs)

    def start_read(self, **kwargs):
        return self.call('start_read', kwargs=kwargs)

    def stop_read(self, **kwargs):
        return self.call('stop_read', kwargs=kwargs)

    def start_measurement(self, **kwargs):
        return self.call('start_measurement', kwargs=kwargs)

    def write_spr_file(self, **kwargs):
        return self.call('write_spr_file', kwargs=kwargs)

    def parent_hardware(self, **kwargs):
        return self.call('parent_hardware', kwargs=kwargs)

    def dump_configuration(self, **kwargs):
        return self.call('dump_configuration', kwargs=kwargs)

    def post_load_from_config(self, **kwargs):
        return self.call('post_load_from_config', kwargs=kwargs)

