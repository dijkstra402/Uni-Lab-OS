from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubPalmsensMethodscriptExamples(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/PalmSens_MethodSCRIPT_Examples', 'source_file': 'Example_Python/Example_Python/palmsens/serialport.py', 'class_name': 'Serial', 'import_roots': [], 'candidate_methods': ['open', 'close', 'write', 'readline'], 'metadata': {'repo': 'palmsens/methodscript_examples', 'repo_url': 'https://github.com/PalmSens/MethodSCRIPT_Examples', 'unit_id': 'gh_palmsens_emstat_pico', 'source_file': 'Example_Python/Example_Python/palmsens/serialport.py', 'candidate_score': 82, 'manufacturer': 'PalmSens', 'model_name': 'PalmSens EmStat Pico'}}

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

