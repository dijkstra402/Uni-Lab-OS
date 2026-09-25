from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubGroundupGmbhScaleHub(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/GROUNDUP-GmbH_scale-hub', 'source_file': 'hub/core/serial_port.py', 'class_name': 'SerialPort', 'import_roots': [], 'candidate_methods': ['is_open', 'open', 'start_reader', 'write', 'close'], 'metadata': {'repo': 'groundup-gmbh/scale-hub', 'repo_url': 'https://github.com/GROUNDUP-GmbH/scale-hub', 'unit_id': 'gh_mettler_toledo_tiger', 'source_file': 'hub/core/serial_port.py', 'candidate_score': 147, 'manufacturer': 'Mettler Toledo', 'model_name': 'Mettler Toledo Tiger系列'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def is_open(self, **kwargs):
        return self.call('is_open', kwargs=kwargs)

    def open(self, **kwargs):
        return self.call('open', kwargs=kwargs)

    def start_reader(self, **kwargs):
        return self.call('start_reader', kwargs=kwargs)

    def write(self, **kwargs):
        return self.call('write', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

