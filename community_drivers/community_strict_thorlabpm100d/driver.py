from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictThorlabpm100d(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/QCoDeS__Qcodes_contrib_drivers', 'source_file': 'src/qcodes_contrib_drivers/drivers/Thorlabs/PM100D.py', 'class_name': 'Thorlab_PM100D', 'import_roots': ['src'], 'candidate_methods': ['get_averaging', 'set_averaging', 'get_wavelength', 'set_wavelength', 'get_power', 'get_attenuation', 'set_attenuation', 'get_power_range', 'set_power_range', 'get_auto_range', 'set_auto_range', 'get_frequency', 'get_current', 'get_current_range', 'get_zero_value', 'get_beam_diameter', 'set_beam_diameter'], 'action_targets': {'get_averaging': '__qcodes_param_get__averaging', 'set_averaging': '__qcodes_param_set__averaging', 'get_wavelength': '__qcodes_param_get__wavelength', 'set_wavelength': '__qcodes_param_set__wavelength', 'get_power': '__qcodes_param_get__power', 'get_attenuation': '__qcodes_param_get__attenuation', 'set_attenuation': '__qcodes_param_set__attenuation', 'get_power_range': '__qcodes_param_get__power_range', 'set_power_range': '__qcodes_param_set__power_range', 'get_auto_range': '__qcodes_param_get__auto_range', 'set_auto_range': '__qcodes_param_set__auto_range', 'get_frequency': '__qcodes_param_get__frequency', 'get_current': '__qcodes_param_get__current', 'get_current_range': '__qcodes_param_get__current_range', 'get_zero_value': '__qcodes_param_get__zero_value', 'get_beam_diameter': '__qcodes_param_get__beam_diameter', 'set_beam_diameter': '__qcodes_param_set__beam_diameter'}, 'metadata': {'repo': 'QCoDeS/Qcodes_contrib_drivers', 'repo_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers', 'source_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers/blob/main/src/qcodes_contrib_drivers/drivers/Thorlabs/PM100D.py', 'confidence': 0.95, 'quality_score': 1.11, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'get_averaging': '__qcodes_param_get__averaging', 'set_averaging': '__qcodes_param_set__averaging', 'get_wavelength': '__qcodes_param_get__wavelength', 'set_wavelength': '__qcodes_param_set__wavelength', 'get_power': '__qcodes_param_get__power', 'get_attenuation': '__qcodes_param_get__attenuation', 'set_attenuation': '__qcodes_param_set__attenuation', 'get_power_range': '__qcodes_param_get__power_range', 'set_power_range': '__qcodes_param_set__power_range', 'get_auto_range': '__qcodes_param_get__auto_range', 'set_auto_range': '__qcodes_param_set__auto_range', 'get_frequency': '__qcodes_param_get__frequency', 'get_current': '__qcodes_param_get__current', 'get_current_range': '__qcodes_param_get__current_range', 'get_zero_value': '__qcodes_param_get__zero_value', 'get_beam_diameter': '__qcodes_param_get__beam_diameter', 'set_beam_diameter': '__qcodes_param_set__beam_diameter'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_averaging(self, **kwargs):
        return self.call('get_averaging', kwargs=kwargs)

    def set_averaging(self, **kwargs):
        return self.call('set_averaging', kwargs=kwargs)

    def get_wavelength(self, **kwargs):
        return self.call('get_wavelength', kwargs=kwargs)

    def set_wavelength(self, **kwargs):
        return self.call('set_wavelength', kwargs=kwargs)

    def get_power(self, **kwargs):
        return self.call('get_power', kwargs=kwargs)

    def get_attenuation(self, **kwargs):
        return self.call('get_attenuation', kwargs=kwargs)

    def set_attenuation(self, **kwargs):
        return self.call('set_attenuation', kwargs=kwargs)

    def get_power_range(self, **kwargs):
        return self.call('get_power_range', kwargs=kwargs)

    def set_power_range(self, **kwargs):
        return self.call('set_power_range', kwargs=kwargs)

    def get_auto_range(self, **kwargs):
        return self.call('get_auto_range', kwargs=kwargs)

    def set_auto_range(self, **kwargs):
        return self.call('set_auto_range', kwargs=kwargs)

    def get_frequency(self, **kwargs):
        return self.call('get_frequency', kwargs=kwargs)

    def get_current(self, **kwargs):
        return self.call('get_current', kwargs=kwargs)

    def get_current_range(self, **kwargs):
        return self.call('get_current_range', kwargs=kwargs)

    def get_zero_value(self, **kwargs):
        return self.call('get_zero_value', kwargs=kwargs)

    def get_beam_diameter(self, **kwargs):
        return self.call('get_beam_diameter', kwargs=kwargs)

    def set_beam_diameter(self, **kwargs):
        return self.call('set_beam_diameter', kwargs=kwargs)

