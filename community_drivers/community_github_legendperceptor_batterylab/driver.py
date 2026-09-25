from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubLegendperceptorBatterylab(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/legendPerceptor_BatteryLab', 'source_file': 'BatteryLab/robots/SartoriusRLine.py', 'class_name': 'SartoriusRLine', 'import_roots': [], 'candidate_methods': ['parseError', 'readFeedback', 'check_connection', 'sendCmd', 'waitForReadyState', 'tellPosition', 'tellLevel', 'initiate_rline', 'aspirate', 'dispense', 'clear_and_reset', 'reset', 'blowout', 'eject', 'eject_and_home', 'disconnect'], 'metadata': {'repo': 'legendperceptor/batterylab', 'repo_url': 'https://github.com/legendPerceptor/BatteryLab', 'unit_id': 'gh_sartorius_rline', 'source_file': 'BatteryLab/robots/SartoriusRLine.py', 'candidate_score': 115, 'manufacturer': 'Sartorius', 'model_name': 'Sartorius rLINE'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def parseError(self, **kwargs):
        return self.call('parseError', kwargs=kwargs)

    def readFeedback(self, **kwargs):
        return self.call('readFeedback', kwargs=kwargs)

    def check_connection(self, **kwargs):
        return self.call('check_connection', kwargs=kwargs)

    def sendCmd(self, **kwargs):
        return self.call('sendCmd', kwargs=kwargs)

    def waitForReadyState(self, **kwargs):
        return self.call('waitForReadyState', kwargs=kwargs)

    def tellPosition(self, **kwargs):
        return self.call('tellPosition', kwargs=kwargs)

    def tellLevel(self, **kwargs):
        return self.call('tellLevel', kwargs=kwargs)

    def initiate_rline(self, **kwargs):
        return self.call('initiate_rline', kwargs=kwargs)

    def aspirate(self, **kwargs):
        return self.call('aspirate', kwargs=kwargs)

    def dispense(self, **kwargs):
        return self.call('dispense', kwargs=kwargs)

    def clear_and_reset(self, **kwargs):
        return self.call('clear_and_reset', kwargs=kwargs)

    def reset(self, **kwargs):
        return self.call('reset', kwargs=kwargs)

    def blowout(self, **kwargs):
        return self.call('blowout', kwargs=kwargs)

    def eject(self, **kwargs):
        return self.call('eject', kwargs=kwargs)

    def eject_and_home(self, **kwargs):
        return self.call('eject_and_home', kwargs=kwargs)

    def disconnect(self, **kwargs):
        return self.call('disconnect', kwargs=kwargs)

