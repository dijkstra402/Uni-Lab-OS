from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubMtoutaiOtThermocyclerStandalone(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/mtoutai_ot_thermocycler_standalone', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'metadata': {'repo': 'mtoutai/ot_thermocycler_standalone', 'repo_url': 'https://github.com/mtoutai/ot_thermocycler_standalone', 'unit_id': 'gh_opentrons_thermocycler_module_', 'source_file': '', 'candidate_score': 0, 'manufacturer': 'Opentrons', 'model_name': 'Opentrons Thermocycler Module (独立)'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


