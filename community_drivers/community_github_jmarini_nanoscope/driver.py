from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubJmariniNanoscope(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/jmarini_nanoscope', 'source_file': 'nanoscope/nanoscope.py', 'class_name': 'NanoscopeFile', 'import_roots': [], 'candidate_methods': ['height', 'amplitude', 'phase', 'image', 'image_types', 'describe_images'], 'metadata': {'repo': 'jmarini/nanoscope', 'repo_url': 'https://github.com/jmarini/nanoscope', 'unit_id': 'gh_bruker_dimension_nanoscope', 'source_file': 'nanoscope/nanoscope.py', 'candidate_score': 56, 'manufacturer': 'Bruker/Veeco', 'model_name': 'Bruker/Veeco Dimension (NanoScope)'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def height(self, **kwargs):
        return self.call('height', kwargs=kwargs)

    def amplitude(self, **kwargs):
        return self.call('amplitude', kwargs=kwargs)

    def phase(self, **kwargs):
        return self.call('phase', kwargs=kwargs)

    def image(self, **kwargs):
        return self.call('image', kwargs=kwargs)

    def image_types(self, **kwargs):
        return self.call('image_types', kwargs=kwargs)

    def describe_images(self, **kwargs):
        return self.call('describe_images', kwargs=kwargs)

