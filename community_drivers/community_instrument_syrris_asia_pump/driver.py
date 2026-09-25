from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentSyrrisAsiaPump(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/fungos34__auto_condition_screening', 'source_file': 'protocol_power_supply.py', 'class_name': 'BKPrecisionRS232', 'import_roots': [], 'candidate_methods': ['initialize_connection', 'close_port', 'send_encoded_command', 'receive_one_byte', 'verify_connected', 'verify_device_active', 'encode_command', 'collect_response', 'format_response', 'verify_response', 'interpret_response', 'send_command', 'send_commands', 'start_monitoring', 'stop_monitoring'], 'action_targets': {}, 'metadata': {'repo': 'fungos34/auto_condition_screening', 'repo_url': 'https://github.com/fungos34/auto_condition_screening', 'brand': 'Syrris', 'model': 'Asia Pump', 'device_type_cn': '注射泵', 'device_type_en': 'Syringe Pump', 'source_framework': '独立驱动', 'tag_id': '4413', 'tag_name': '注射泵', 'tag_name_en': 'Syringe Pump', 'candidate_score': 150, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def initialize_connection(self, **kwargs):
        return self.call('initialize_connection', kwargs=kwargs)

    def close_port(self, **kwargs):
        return self.call('close_port', kwargs=kwargs)

    def send_encoded_command(self, **kwargs):
        return self.call('send_encoded_command', kwargs=kwargs)

    def receive_one_byte(self, **kwargs):
        return self.call('receive_one_byte', kwargs=kwargs)

    def verify_connected(self, **kwargs):
        return self.call('verify_connected', kwargs=kwargs)

    def verify_device_active(self, **kwargs):
        return self.call('verify_device_active', kwargs=kwargs)

    def encode_command(self, **kwargs):
        return self.call('encode_command', kwargs=kwargs)

    def collect_response(self, **kwargs):
        return self.call('collect_response', kwargs=kwargs)

    def format_response(self, **kwargs):
        return self.call('format_response', kwargs=kwargs)

    def verify_response(self, **kwargs):
        return self.call('verify_response', kwargs=kwargs)

    def interpret_response(self, **kwargs):
        return self.call('interpret_response', kwargs=kwargs)

    def send_command(self, **kwargs):
        return self.call('send_command', kwargs=kwargs)

    def send_commands(self, **kwargs):
        return self.call('send_commands', kwargs=kwargs)

    def start_monitoring(self, **kwargs):
        return self.call('start_monitoring', kwargs=kwargs)

    def stop_monitoring(self, **kwargs):
        return self.call('stop_monitoring', kwargs=kwargs)

