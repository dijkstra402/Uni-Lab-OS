from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubJrllabHardpotato(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/jrlLAB_hardpotato', 'source_file': 'src/hardpotato/pico_serial.py', 'class_name': 'Serial', 'import_roots': [], 'candidate_methods': ['open', 'close', 'write', 'readline'], 'metadata': {'repo': 'jrllab/hardpotato', 'repo_url': 'https://github.com/jrlLAB/hardpotato', 'unit_id': 'gh_ch_instruments_chi760e', 'source_file': 'src/hardpotato/pico_serial.py', 'candidate_score': 82, 'manufacturer': 'CH Instruments', 'model_name': 'CH Instruments CHI760E'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def open(self, **kwargs):
        return self.call('open', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def write(self, **kwargs):
        return self.call('write', kwargs=kwargs)

    def readline(self, **kwargs):
        return self.call('readline', kwargs=kwargs)

