from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubOpentronsOpentrons(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/Opentrons_opentrons', 'source_file': 'hardware-testing/hardware_testing/drivers/mitutoyo_digimatic_indicator.py', 'class_name': 'Mitutoyo_Digimatic_Indicator', 'import_roots': [], 'candidate_methods': ['connect', 'disconnect', 'read', 'read_stable'], 'metadata': {'repo': 'opentrons/opentrons', 'repo_url': 'https://github.com/Opentrons/opentrons', 'unit_id': 'gh_opentrons_ot_2', 'source_file': 'hardware-testing/hardware_testing/drivers/mitutoyo_digimatic_indicator.py', 'candidate_score': 169, 'manufacturer': 'Opentrons', 'model_name': 'Opentrons OT-2/Flex'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def connect(self, **kwargs):
        return self.call('connect', kwargs=kwargs)

    def disconnect(self, **kwargs):
        return self.call('disconnect', kwargs=kwargs)

    def read(self, **kwargs):
        return self.call('read', kwargs=kwargs)

    def read_stable(self, **kwargs):
        return self.call('read_stable', kwargs=kwargs)

