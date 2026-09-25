from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictThorlabspm100usb(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/pymeasure__pymeasure', 'source_file': 'pymeasure/instruments/thorlabs/thorlabspm100usb.py', 'class_name': 'ThorlabsPM100USB', 'import_roots': [], 'candidate_methods': ['wavelength', 'power', 'energy', 'check_errors', 'next_error', 'write_binary_values', 'read_binary_values'], 'action_targets': {}, 'metadata': {'repo': 'pymeasure/pymeasure', 'repo_url': 'https://github.com/pymeasure/pymeasure', 'source_url': 'https://github.com/pymeasure/pymeasure/blob/main/pymeasure/instruments/thorlabs/thorlabspm100usb.py', 'confidence': 0.9, 'quality_score': 1.12, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def wavelength(self, **kwargs):
        return self.call('wavelength', kwargs=kwargs)

    def power(self, **kwargs):
        return self.call('power', kwargs=kwargs)

    def energy(self, **kwargs):
        return self.call('energy', kwargs=kwargs)

    def check_errors(self, **kwargs):
        return self.call('check_errors', kwargs=kwargs)

    def next_error(self, **kwargs):
        return self.call('next_error', kwargs=kwargs)

    def write_binary_values(self, **kwargs):
        return self.call('write_binary_values', kwargs=kwargs)

    def read_binary_values(self, **kwargs):
        return self.call('read_binary_values', kwargs=kwargs)

