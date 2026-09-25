from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubZahnerElektrikThalesRemotePython(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/Zahner-elektrik_Thales-Remote-Python', 'source_file': 'thales_remote/connection.py', 'class_name': 'ThalesRemoteConnection', 'import_roots': [], 'candidate_methods': ['connectToTerm', 'sendall', 'readall', 'getConnectionName', 'disconnectFromTerm', 'isConnectedToTerm', 'sendTelegram', 'waitForBinaryTelegram', 'waitForStringTelegram', 'sendStringAndWaitForReplyString'], 'metadata': {'repo': 'zahner-elektrik/thales-remote-python', 'repo_url': 'https://github.com/Zahner-elektrik/Thales-Remote-Python', 'unit_id': 'gh_zahner_zennium', 'source_file': 'thales_remote/connection.py', 'candidate_score': 132, 'manufacturer': 'Zahner', 'model_name': 'Zahner Zennium'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def connectToTerm(self, **kwargs):
        return self.call('connectToTerm', kwargs=kwargs)

    def sendall(self, **kwargs):
        return self.call('sendall', kwargs=kwargs)

    def readall(self, **kwargs):
        return self.call('readall', kwargs=kwargs)

    def getConnectionName(self, **kwargs):
        return self.call('getConnectionName', kwargs=kwargs)

    def disconnectFromTerm(self, **kwargs):
        return self.call('disconnectFromTerm', kwargs=kwargs)

    def isConnectedToTerm(self, **kwargs):
        return self.call('isConnectedToTerm', kwargs=kwargs)

    def sendTelegram(self, **kwargs):
        return self.call('sendTelegram', kwargs=kwargs)

    def waitForBinaryTelegram(self, **kwargs):
        return self.call('waitForBinaryTelegram', kwargs=kwargs)

    def waitForStringTelegram(self, **kwargs):
        return self.call('waitForStringTelegram', kwargs=kwargs)

    def sendStringAndWaitForReplyString(self, **kwargs):
        return self.call('sendStringAndWaitForReplyString', kwargs=kwargs)

