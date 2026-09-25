from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictZihdawg8(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/QCoDeS__Qcodes_contrib_drivers', 'source_file': 'src/qcodes_contrib_drivers/drivers/ZurichInstruments/ZIHDAWG8.py', 'class_name': 'ZIHDAWG8', 'import_roots': ['src'], 'candidate_methods': ['snapshot_base', 'snapshot', 'enable_channel', 'disable_channel', 'start_awg', 'stop_awg', 'waveform_to_wave', 'waveform_to_csv', 'generate_csv_sequence_program', 'upload_sequence_program', 'upload_waveform', 'set_channel_grouping', 'create_parameters_from_node_tree', 'download_device_node_tree'], 'action_targets': {}, 'metadata': {'repo': 'QCoDeS/Qcodes_contrib_drivers', 'repo_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers', 'source_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers/blob/main/src/qcodes_contrib_drivers/drivers/ZurichInstruments/ZIHDAWG8.py', 'confidence': 0.9, 'quality_score': 1.06, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def snapshot_base(self, **kwargs):
        return self.call('snapshot_base', kwargs=kwargs)

    def snapshot(self, **kwargs):
        return self.call('snapshot', kwargs=kwargs)

    def enable_channel(self, **kwargs):
        return self.call('enable_channel', kwargs=kwargs)

    def disable_channel(self, **kwargs):
        return self.call('disable_channel', kwargs=kwargs)

    def start_awg(self, **kwargs):
        return self.call('start_awg', kwargs=kwargs)

    def stop_awg(self, **kwargs):
        return self.call('stop_awg', kwargs=kwargs)

    def waveform_to_wave(self, **kwargs):
        return self.call('waveform_to_wave', kwargs=kwargs)

    def waveform_to_csv(self, **kwargs):
        return self.call('waveform_to_csv', kwargs=kwargs)

    def generate_csv_sequence_program(self, **kwargs):
        return self.call('generate_csv_sequence_program', kwargs=kwargs)

    def upload_sequence_program(self, **kwargs):
        return self.call('upload_sequence_program', kwargs=kwargs)

    def upload_waveform(self, **kwargs):
        return self.call('upload_waveform', kwargs=kwargs)

    def set_channel_grouping(self, **kwargs):
        return self.call('set_channel_grouping', kwargs=kwargs)

    def create_parameters_from_node_tree(self, **kwargs):
        return self.call('create_parameters_from_node_tree', kwargs=kwargs)

    def download_device_node_tree(self, **kwargs):
        return self.call('download_device_node_tree', kwargs=kwargs)

