from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentWatsonMarlow323(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/DiamondLightSource__dodal', 'source_file': 'src/dodal/devices/eiger.py', 'class_name': 'EigerDetector', 'import_roots': ['src'], 'candidate_methods': ['with_params', 'set_detector_parameters', 'async_stage', 'is_armed', 'wait_on_arming_if_started', 'stage', 'stop_odin_when_all_frames_collected', 'unstage', 'stop', 'disable_roi_mode', 'enable_roi_mode', 'change_roi_mode', 'set_cam_pvs', 'set_odin_number_of_frame_chunks', 'set_odin_pvs', 'set_mx_settings_pvs', 'set_detector_threshold', 'set_num_triggers_and_captures', 'forward_bit_depth_to_filewriter', 'change_dev_shm', 'disarm_detector', 'wait_for_stale_params', 'set_cam_acquire', 'do_arming_chain'], 'action_targets': {}, 'metadata': {'repo': 'DiamondLightSource/dodal', 'repo_url': 'https://github.com/DiamondLightSource/dodal', 'brand': 'Watson-Marlow', 'model': '323', 'device_type_cn': '蠕动泵', 'device_type_en': 'Peristaltic Pump', 'source_framework': 'dodal/ophyd', 'tag_id': '4451', 'tag_name': '蠕动泵', 'tag_name_en': 'Peristaltic Pump', 'candidate_score': 230, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def with_params(self, **kwargs):
        return self.call('with_params', kwargs=kwargs)

    def set_detector_parameters(self, **kwargs):
        return self.call('set_detector_parameters', kwargs=kwargs)

    def async_stage(self, **kwargs):
        return self.call('async_stage', kwargs=kwargs)

    def is_armed(self, **kwargs):
        return self.call('is_armed', kwargs=kwargs)

    def wait_on_arming_if_started(self, **kwargs):
        return self.call('wait_on_arming_if_started', kwargs=kwargs)

    def stage(self, **kwargs):
        return self.call('stage', kwargs=kwargs)

    def stop_odin_when_all_frames_collected(self, **kwargs):
        return self.call('stop_odin_when_all_frames_collected', kwargs=kwargs)

    def unstage(self, **kwargs):
        return self.call('unstage', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

    def disable_roi_mode(self, **kwargs):
        return self.call('disable_roi_mode', kwargs=kwargs)

    def enable_roi_mode(self, **kwargs):
        return self.call('enable_roi_mode', kwargs=kwargs)

    def change_roi_mode(self, **kwargs):
        return self.call('change_roi_mode', kwargs=kwargs)

    def set_cam_pvs(self, **kwargs):
        return self.call('set_cam_pvs', kwargs=kwargs)

    def set_odin_number_of_frame_chunks(self, **kwargs):
        return self.call('set_odin_number_of_frame_chunks', kwargs=kwargs)

    def set_odin_pvs(self, **kwargs):
        return self.call('set_odin_pvs', kwargs=kwargs)

    def set_mx_settings_pvs(self, **kwargs):
        return self.call('set_mx_settings_pvs', kwargs=kwargs)

    def set_detector_threshold(self, **kwargs):
        return self.call('set_detector_threshold', kwargs=kwargs)

    def set_num_triggers_and_captures(self, **kwargs):
        return self.call('set_num_triggers_and_captures', kwargs=kwargs)

    def forward_bit_depth_to_filewriter(self, **kwargs):
        return self.call('forward_bit_depth_to_filewriter', kwargs=kwargs)

    def change_dev_shm(self, **kwargs):
        return self.call('change_dev_shm', kwargs=kwargs)

    def disarm_detector(self, **kwargs):
        return self.call('disarm_detector', kwargs=kwargs)

    def wait_for_stale_params(self, **kwargs):
        return self.call('wait_for_stale_params', kwargs=kwargs)

    def set_cam_acquire(self, **kwargs):
        return self.call('set_cam_acquire', kwargs=kwargs)

    def do_arming_chain(self, **kwargs):
        return self.call('do_arming_chain', kwargs=kwargs)

