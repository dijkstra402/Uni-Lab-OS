from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubHelgesteinHelaoPub(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/helgestein_helao-pub', 'source_file': 'driver/pump_driver.py', 'class_name': 'pump', 'import_roots': [], 'candidate_methods': ['primePump', 'runPump', 'stopPump', 'readPump', 'askDone', 'pumpOff', 'read', 'shutdown'], 'metadata': {'repo': 'helgestein/helao-pub', 'repo_url': 'https://github.com/helgestein/helao-pub', 'unit_id': 'gh_gamry_pc6', 'source_file': 'driver/pump_driver.py', 'candidate_score': 110, 'manufacturer': 'Gamry', 'model_name': 'Gamry PC6'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def primePump(self, **kwargs):
        return self.call('primePump', kwargs=kwargs)

    def runPump(self, **kwargs):
        return self.call('runPump', kwargs=kwargs)

    def stopPump(self, **kwargs):
        return self.call('stopPump', kwargs=kwargs)

    def readPump(self, **kwargs):
        return self.call('readPump', kwargs=kwargs)

    def askDone(self, **kwargs):
        return self.call('askDone', kwargs=kwargs)

    def pumpOff(self, **kwargs):
        return self.call('pumpOff', kwargs=kwargs)

    def read(self, **kwargs):
        return self.call('read', kwargs=kwargs)

    def shutdown(self, **kwargs):
        return self.call('shutdown', kwargs=kwargs)

