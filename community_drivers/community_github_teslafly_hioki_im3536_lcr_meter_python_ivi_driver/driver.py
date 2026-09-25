from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubTeslaflyHiokiIm3536LcrMeterPythonIviDriver(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/Teslafly_Hioki-IM3536-Lcr-meter-python-IVI-driver', 'source_file': 'hioki/hiokiIM3536.py', 'class_name': 'hiokiIM3536', 'import_roots': [], 'candidate_methods': ['do_lcr_measurement', 'set_display_items'], 'metadata': {'repo': 'teslafly/hioki-im3536-lcr-meter-python-ivi-driver', 'repo_url': 'https://github.com/Teslafly/Hioki-IM3536-Lcr-meter-python-IVI-driver', 'unit_id': 'gh_hioki_im3536', 'source_file': 'hioki/hiokiIM3536.py', 'candidate_score': 137, 'manufacturer': 'Hioki', 'model_name': 'Hioki IM3536'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def do_lcr_measurement(self, **kwargs):
        return self.call('do_lcr_measurement', kwargs=kwargs)

    def set_display_items(self, **kwargs):
        return self.call('set_display_items', kwargs=kwargs)

