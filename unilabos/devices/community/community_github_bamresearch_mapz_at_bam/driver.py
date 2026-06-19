from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubBamresearchMapzAtBam(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/BAMresearch_MAPz_at_BAM', 'source_file': 'Echem MAP/Qualification of Proxy Experiments for Accelerated Electrochemical Testing in Self-Driving Labs/Software/palmsens/serial.py', 'class_name': 'Serial', 'import_roots': [], 'candidate_methods': ['open', 'close', 'write', 'readline'], 'metadata': {'repo': 'bamresearch/mapz_at_bam', 'repo_url': 'https://github.com/BAMresearch/MAPz_at_BAM', 'unit_id': 'gh_herolab_robotcen', 'source_file': 'Echem MAP/Qualification of Proxy Experiments for Accelerated Electrochemical Testing in Self-Driving Labs/Software/palmsens/serial.py', 'candidate_score': 82, 'manufacturer': 'Herolab', 'model_name': 'Herolab RobotCen'}}

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

