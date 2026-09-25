from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubRichardinghamOctopus(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/richardingham_octopus', 'source_file': 'octopus/protocol/basic.py', 'class_name': 'QueuedLineReceiver', 'import_roots': [], 'candidate_methods': ['connectionMade', 'connectionLost', 'write', 'sendLine', 'dataReceived', 'lineReceived', 'processLine', 'unexpectedMessage'], 'metadata': {'repo': 'richardingham/octopus', 'repo_url': 'https://github.com/richardingham/octopus', 'unit_id': 'gh_gilson_402', 'source_file': 'octopus/protocol/basic.py', 'candidate_score': 96, 'manufacturer': 'Gilson', 'model_name': 'Gilson 402/233XL/506C'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def connectionMade(self, **kwargs):
        return self.call('connectionMade', kwargs=kwargs)

    def connectionLost(self, **kwargs):
        return self.call('connectionLost', kwargs=kwargs)

    def write(self, **kwargs):
        return self.call('write', kwargs=kwargs)

    def sendLine(self, **kwargs):
        return self.call('sendLine', kwargs=kwargs)

    def dataReceived(self, **kwargs):
        return self.call('dataReceived', kwargs=kwargs)

    def lineReceived(self, **kwargs):
        return self.call('lineReceived', kwargs=kwargs)

    def processLine(self, **kwargs):
        return self.call('processLine', kwargs=kwargs)

    def unexpectedMessage(self, **kwargs):
        return self.call('unexpectedMessage', kwargs=kwargs)

