from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubMintttPymmc(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/MinTTT_pymmc', 'source_file': 'device/arduino.py', 'class_name': 'ARDUINO', 'import_roots': [], 'candidate_methods': ['trigger_pattern', 'trigger_pattern', 'OutPutPinMap', 'OutPutPinMap', 'get_current_pattern', 'connect', 'cmd', 'start_trigger_mode', 'stop_trigger_mode', 'start_blanking_mode', 'stop_blanking_mode', 'blanking_positive', 'trigger', 'close_session', 'trigger_continuously', 'stop_trigger_continuously', 'trigger_one_pulse', 'ONTime', 'ONTime', 'OFFTime'], 'metadata': {'repo': 'minttt/pymmc', 'repo_url': 'https://github.com/MinTTT/pymmc', 'unit_id': 'gh_nikon_ti2', 'source_file': 'device/arduino.py', 'candidate_score': 105, 'manufacturer': 'Nikon', 'model_name': 'Nikon Ti2'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def trigger_pattern(self, **kwargs):
        return self.call('trigger_pattern', kwargs=kwargs)

    def trigger_pattern(self, **kwargs):
        return self.call('trigger_pattern', kwargs=kwargs)

    def OutPutPinMap(self, **kwargs):
        return self.call('OutPutPinMap', kwargs=kwargs)

    def OutPutPinMap(self, **kwargs):
        return self.call('OutPutPinMap', kwargs=kwargs)

    def get_current_pattern(self, **kwargs):
        return self.call('get_current_pattern', kwargs=kwargs)

    def connect(self, **kwargs):
        return self.call('connect', kwargs=kwargs)

    def cmd(self, **kwargs):
        return self.call('cmd', kwargs=kwargs)

    def start_trigger_mode(self, **kwargs):
        return self.call('start_trigger_mode', kwargs=kwargs)

    def stop_trigger_mode(self, **kwargs):
        return self.call('stop_trigger_mode', kwargs=kwargs)

    def start_blanking_mode(self, **kwargs):
        return self.call('start_blanking_mode', kwargs=kwargs)

    def stop_blanking_mode(self, **kwargs):
        return self.call('stop_blanking_mode', kwargs=kwargs)

    def blanking_positive(self, **kwargs):
        return self.call('blanking_positive', kwargs=kwargs)

    def trigger(self, **kwargs):
        return self.call('trigger', kwargs=kwargs)

    def close_session(self, **kwargs):
        return self.call('close_session', kwargs=kwargs)

    def trigger_continuously(self, **kwargs):
        return self.call('trigger_continuously', kwargs=kwargs)

    def stop_trigger_continuously(self, **kwargs):
        return self.call('stop_trigger_continuously', kwargs=kwargs)

    def trigger_one_pulse(self, **kwargs):
        return self.call('trigger_one_pulse', kwargs=kwargs)

    def ONTime(self, **kwargs):
        return self.call('ONTime', kwargs=kwargs)

    def ONTime(self, **kwargs):
        return self.call('ONTime', kwargs=kwargs)

    def OFFTime(self, **kwargs):
        return self.call('OFFTime', kwargs=kwargs)

