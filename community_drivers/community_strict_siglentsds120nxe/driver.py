from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictSiglentsds120nxe(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/QCoDeS__Qcodes_contrib_drivers', 'source_file': 'src/qcodes_contrib_drivers/drivers/Siglent/sds.py', 'class_name': 'Siglent_SDS_120NxE', 'import_roots': ['src'], 'candidate_methods': ['get_time_base', 'get_num_samples', 'get_sample_rate', 'get_vdiv', 'get_ofst', 'get_raw_analog_waveform_data', 'get_math_vdiv', 'get_raw_math_waveform_data', 'get_raw_digital_waveform_data', 'get_channel_waveform_data', 'get_channel_waveform', 'get_math_waveform', 'set_to_fft', 'get_trig_mode', 'set_trig_mode', 'get_waveform_setup', 'set_waveform_setup', 'screen_dump_bmp', 'scdp_bmp_bytes'], 'action_targets': {}, 'metadata': {'repo': 'QCoDeS/Qcodes_contrib_drivers', 'repo_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers', 'source_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers/blob/main/src/qcodes_contrib_drivers/drivers/Siglent/sds.py', 'confidence': 0.8, 'quality_score': 0.88, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_time_base(self, **kwargs):
        return self.call('get_time_base', kwargs=kwargs)

    def get_num_samples(self, **kwargs):
        return self.call('get_num_samples', kwargs=kwargs)

    def get_sample_rate(self, **kwargs):
        return self.call('get_sample_rate', kwargs=kwargs)

    def get_vdiv(self, **kwargs):
        return self.call('get_vdiv', kwargs=kwargs)

    def get_ofst(self, **kwargs):
        return self.call('get_ofst', kwargs=kwargs)

    def get_raw_analog_waveform_data(self, **kwargs):
        return self.call('get_raw_analog_waveform_data', kwargs=kwargs)

    def get_math_vdiv(self, **kwargs):
        return self.call('get_math_vdiv', kwargs=kwargs)

    def get_raw_math_waveform_data(self, **kwargs):
        return self.call('get_raw_math_waveform_data', kwargs=kwargs)

    def get_raw_digital_waveform_data(self, **kwargs):
        return self.call('get_raw_digital_waveform_data', kwargs=kwargs)

    def get_channel_waveform_data(self, **kwargs):
        return self.call('get_channel_waveform_data', kwargs=kwargs)

    def get_channel_waveform(self, **kwargs):
        return self.call('get_channel_waveform', kwargs=kwargs)

    def get_math_waveform(self, **kwargs):
        return self.call('get_math_waveform', kwargs=kwargs)

    def set_to_fft(self, **kwargs):
        return self.call('set_to_fft', kwargs=kwargs)

    def get_trig_mode(self, **kwargs):
        return self.call('get_trig_mode', kwargs=kwargs)

    def set_trig_mode(self, **kwargs):
        return self.call('set_trig_mode', kwargs=kwargs)

    def get_waveform_setup(self, **kwargs):
        return self.call('get_waveform_setup', kwargs=kwargs)

    def set_waveform_setup(self, **kwargs):
        return self.call('set_waveform_setup', kwargs=kwargs)

    def screen_dump_bmp(self, **kwargs):
        return self.call('screen_dump_bmp', kwargs=kwargs)

    def scdp_bmp_bytes(self, **kwargs):
        return self.call('scdp_bmp_bytes', kwargs=kwargs)

