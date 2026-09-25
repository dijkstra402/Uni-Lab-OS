from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubAmsikkingPcoPixelflyUsb(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/amsikking_pco_pixelfly_usb', 'source_file': 'pco_pixelfly_usb.py', 'class_name': 'Camera', 'import_roots': [], 'candidate_methods': ['apply_settings', 'record_to_memory', 'close'], 'metadata': {'repo': 'amsikking/pco_pixelfly_usb', 'repo_url': 'https://github.com/amsikking/pco_pixelfly_usb', 'unit_id': 'gh_pco_pco_pixelfly_usb', 'source_file': 'pco_pixelfly_usb.py', 'candidate_score': 23, 'manufacturer': 'PCO', 'model_name': 'PCO pco.pixelfly USB'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def apply_settings(self, **kwargs):
        return self.call('apply_settings', kwargs=kwargs)

    def record_to_memory(self, **kwargs):
        return self.call('record_to_memory', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

