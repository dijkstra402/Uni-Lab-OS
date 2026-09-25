from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubBenpruittTecancavro(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/benpruitt_tecancavro', 'source_file': 'tecancavro/transport.py', 'class_name': 'TecanAPISerial', 'import_roots': [], 'candidate_methods': ['findSerialPumps', 'sendRcv'], 'metadata': {'repo': 'benpruitt/tecancavro', 'repo_url': 'https://github.com/benpruitt/tecancavro', 'unit_id': 'gh_tecan_cavro_xcalibur_d', 'source_file': 'tecancavro/transport.py', 'candidate_score': 97, 'manufacturer': 'Tecan Cavro', 'model_name': 'Tecan Cavro XCalibur D'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def findSerialPumps(self, **kwargs):
        return self.call('findSerialPumps', kwargs=kwargs)

    def sendRcv(self, **kwargs):
        return self.call('sendRcv', kwargs=kwargs)

