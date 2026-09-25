from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentTcPowerConversionCxn(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/tcpowerconversion/tccxn.py', 'class_name': 'CXN', 'import_roots': [], 'candidate_methods': ['values', 'read', 'write', 'request_control', 'release_control', 'ping'], 'metadata': {'source_file': 'pymeasure/instruments/tcpowerconversion/tccxn.py', 'class_name': 'CXN', 'candidate_score': 0.75, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def values(self, **kwargs):
            return self.call('values', kwargs=kwargs)

        def read(self, **kwargs):
            return self.call('read', kwargs=kwargs)

        def write(self, **kwargs):
            return self.call('write', kwargs=kwargs)

        def request_control(self, **kwargs):
            return self.call('request_control', kwargs=kwargs)

        def release_control(self, **kwargs):
            return self.call('release_control', kwargs=kwargs)

        def ping(self, **kwargs):
            return self.call('ping', kwargs=kwargs)

