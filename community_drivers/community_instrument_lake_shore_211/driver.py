from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentLakeShore211(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/lakeshore/lakeshore211.py', 'class_name': 'LakeShore211', 'import_roots': [], 'candidate_methods': ['get_relay_mode', 'configure_relay', 'get_alarm_status', 'configure_alarm', 'reset_alarm'], 'metadata': {'source_file': 'pymeasure/instruments/lakeshore/lakeshore211.py', 'class_name': 'LakeShore211', 'candidate_score': 0.923, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def get_relay_mode(self, **kwargs):
            return self.call('get_relay_mode', kwargs=kwargs)

        def configure_relay(self, **kwargs):
            return self.call('configure_relay', kwargs=kwargs)

        def get_alarm_status(self, **kwargs):
            return self.call('get_alarm_status', kwargs=kwargs)

        def configure_alarm(self, **kwargs):
            return self.call('configure_alarm', kwargs=kwargs)

        def reset_alarm(self, **kwargs):
            return self.call('reset_alarm', kwargs=kwargs)

