from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentZeissSmartsemRemcon32(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/ScopeFoundry__HW_zeiss_sem', 'source_file': 'remcon32.py', 'class_name': 'Remcon32', 'import_roots': [], 'candidate_methods': ['close', 'cmd_response', 'limits', 'get_kV', 'set_kV', 'set_eht_state', 'get_eht_state', 'set_blank_state', 'get_blank_state', 'set_stig', 'get_stig', 'set_ap', 'get_ap', 'set_ap_xy', 'get_ap_xy', 'set_gun_align', 'set_beam_shift', 'high_current_state', 'set_probe_current', 'scm_state', 'get_scm', 'display_focus_state', 'set_contrast_primary', 'get_contrast_primary', 'set_contrast_secondary', 'get_contrast_secondary', 'set_chan_bright', 'get_chan_bright', 'set_chan_contrast', 'get_chan_contrast', 'set_chan_detector', 'get_chan_detector', 'dual_channel_state', 'set_bright', 'get_bright', 'set_contrast', 'get_contrast', 'get_detector', 'set_detector', 'set_norm', 'run_macro', 'set_extscan_state', 'get_extscan_state', 'set_mag', 'get_mag', 'set_wd', 'get_wd', 'get_pixel_size', 'set_spot_mode', 'get_stage_position', 'get_stage_initialized_state', 'get_stage_position_dict', 'set_stage_position', 'set_stage_position_kwargs', 'set_stage_delta', 'set_stage_abs_xy_rot', 'get_stage_moving', 'check_rotation_fault'], 'action_targets': {}, 'metadata': {'repo': 'ScopeFoundry/HW_zeiss_sem', 'repo_url': 'https://github.com/ScopeFoundry/HW_zeiss_sem', 'brand': 'Zeiss', 'model': 'SmartSEM (REMCON32)', 'device_type_cn': '扫描电子显微镜', 'device_type_en': 'SEM', 'source_framework': 'ScopeFoundry', 'tag_id': '4390', 'tag_name': '扫描电子显微镜', 'tag_name_en': 'Scanning Electron Microscope', 'candidate_score': 514, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def cmd_response(self, **kwargs):
        return self.call('cmd_response', kwargs=kwargs)

    def limits(self, **kwargs):
        return self.call('limits', kwargs=kwargs)

    def get_kV(self, **kwargs):
        return self.call('get_kV', kwargs=kwargs)

    def set_kV(self, **kwargs):
        return self.call('set_kV', kwargs=kwargs)

    def set_eht_state(self, **kwargs):
        return self.call('set_eht_state', kwargs=kwargs)

    def get_eht_state(self, **kwargs):
        return self.call('get_eht_state', kwargs=kwargs)

    def set_blank_state(self, **kwargs):
        return self.call('set_blank_state', kwargs=kwargs)

    def get_blank_state(self, **kwargs):
        return self.call('get_blank_state', kwargs=kwargs)

    def set_stig(self, **kwargs):
        return self.call('set_stig', kwargs=kwargs)

    def get_stig(self, **kwargs):
        return self.call('get_stig', kwargs=kwargs)

    def set_ap(self, **kwargs):
        return self.call('set_ap', kwargs=kwargs)

    def get_ap(self, **kwargs):
        return self.call('get_ap', kwargs=kwargs)

    def set_ap_xy(self, **kwargs):
        return self.call('set_ap_xy', kwargs=kwargs)

    def get_ap_xy(self, **kwargs):
        return self.call('get_ap_xy', kwargs=kwargs)

    def set_gun_align(self, **kwargs):
        return self.call('set_gun_align', kwargs=kwargs)

    def set_beam_shift(self, **kwargs):
        return self.call('set_beam_shift', kwargs=kwargs)

    def high_current_state(self, **kwargs):
        return self.call('high_current_state', kwargs=kwargs)

    def set_probe_current(self, **kwargs):
        return self.call('set_probe_current', kwargs=kwargs)

    def scm_state(self, **kwargs):
        return self.call('scm_state', kwargs=kwargs)

    def get_scm(self, **kwargs):
        return self.call('get_scm', kwargs=kwargs)

    def display_focus_state(self, **kwargs):
        return self.call('display_focus_state', kwargs=kwargs)

    def set_contrast_primary(self, **kwargs):
        return self.call('set_contrast_primary', kwargs=kwargs)

    def get_contrast_primary(self, **kwargs):
        return self.call('get_contrast_primary', kwargs=kwargs)

    def set_contrast_secondary(self, **kwargs):
        return self.call('set_contrast_secondary', kwargs=kwargs)

    def get_contrast_secondary(self, **kwargs):
        return self.call('get_contrast_secondary', kwargs=kwargs)

    def set_chan_bright(self, **kwargs):
        return self.call('set_chan_bright', kwargs=kwargs)

    def get_chan_bright(self, **kwargs):
        return self.call('get_chan_bright', kwargs=kwargs)

    def set_chan_contrast(self, **kwargs):
        return self.call('set_chan_contrast', kwargs=kwargs)

    def get_chan_contrast(self, **kwargs):
        return self.call('get_chan_contrast', kwargs=kwargs)

    def set_chan_detector(self, **kwargs):
        return self.call('set_chan_detector', kwargs=kwargs)

    def get_chan_detector(self, **kwargs):
        return self.call('get_chan_detector', kwargs=kwargs)

    def dual_channel_state(self, **kwargs):
        return self.call('dual_channel_state', kwargs=kwargs)

    def set_bright(self, **kwargs):
        return self.call('set_bright', kwargs=kwargs)

    def get_bright(self, **kwargs):
        return self.call('get_bright', kwargs=kwargs)

    def set_contrast(self, **kwargs):
        return self.call('set_contrast', kwargs=kwargs)

    def get_contrast(self, **kwargs):
        return self.call('get_contrast', kwargs=kwargs)

    def get_detector(self, **kwargs):
        return self.call('get_detector', kwargs=kwargs)

    def set_detector(self, **kwargs):
        return self.call('set_detector', kwargs=kwargs)

    def set_norm(self, **kwargs):
        return self.call('set_norm', kwargs=kwargs)

    def run_macro(self, **kwargs):
        return self.call('run_macro', kwargs=kwargs)

    def set_extscan_state(self, **kwargs):
        return self.call('set_extscan_state', kwargs=kwargs)

    def get_extscan_state(self, **kwargs):
        return self.call('get_extscan_state', kwargs=kwargs)

    def set_mag(self, **kwargs):
        return self.call('set_mag', kwargs=kwargs)

    def get_mag(self, **kwargs):
        return self.call('get_mag', kwargs=kwargs)

    def set_wd(self, **kwargs):
        return self.call('set_wd', kwargs=kwargs)

    def get_wd(self, **kwargs):
        return self.call('get_wd', kwargs=kwargs)

    def get_pixel_size(self, **kwargs):
        return self.call('get_pixel_size', kwargs=kwargs)

    def set_spot_mode(self, **kwargs):
        return self.call('set_spot_mode', kwargs=kwargs)

    def get_stage_position(self, **kwargs):
        return self.call('get_stage_position', kwargs=kwargs)

    def get_stage_initialized_state(self, **kwargs):
        return self.call('get_stage_initialized_state', kwargs=kwargs)

    def get_stage_position_dict(self, **kwargs):
        return self.call('get_stage_position_dict', kwargs=kwargs)

    def set_stage_position(self, **kwargs):
        return self.call('set_stage_position', kwargs=kwargs)

    def set_stage_position_kwargs(self, **kwargs):
        return self.call('set_stage_position_kwargs', kwargs=kwargs)

    def set_stage_delta(self, **kwargs):
        return self.call('set_stage_delta', kwargs=kwargs)

    def set_stage_abs_xy_rot(self, **kwargs):
        return self.call('set_stage_abs_xy_rot', kwargs=kwargs)

    def get_stage_moving(self, **kwargs):
        return self.call('get_stage_moving', kwargs=kwargs)

    def check_rotation_fault(self, **kwargs):
        return self.call('check_rotation_fault', kwargs=kwargs)

