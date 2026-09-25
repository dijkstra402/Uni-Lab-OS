from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubCetoniSoftwareSilaCetoniPumps(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/CETONI-Software_sila_cetoni_pumps', 'source_file': 'sila_cetoni/pumps/syringepumps/sila/syringepump_service/feature_implementations/pumpdrivecontrolservice_impl.py', 'class_name': 'PumpDriveControlServiceImpl', 'import_roots': [], 'candidate_methods': ['start', 'stop', 'update_DrivePositionCounter', 'EnablePumpDrive', 'DisablePumpDrive', 'RestoreDrivePositionCounter', 'InitializePumpDrive'], 'metadata': {'repo': 'cetoni-software/sila_cetoni_pumps', 'repo_url': 'https://github.com/CETONI-Software/sila_cetoni_pumps', 'unit_id': 'gh_cetoni_nemesys_sila2', 'source_file': 'sila_cetoni/pumps/syringepumps/sila/syringepump_service/feature_implementations/pumpdrivecontrolservice_impl.py', 'candidate_score': 37, 'manufacturer': 'Cetoni', 'model_name': 'Cetoni neMESYS (SiLA2)'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def start(self, **kwargs):
        return self.call('start', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

    def update_DrivePositionCounter(self, **kwargs):
        return self.call('update_DrivePositionCounter', kwargs=kwargs)

    def EnablePumpDrive(self, **kwargs):
        return self.call('EnablePumpDrive', kwargs=kwargs)

    def DisablePumpDrive(self, **kwargs):
        return self.call('DisablePumpDrive', kwargs=kwargs)

    def RestoreDrivePositionCounter(self, **kwargs):
        return self.call('RestoreDrivePositionCounter', kwargs=kwargs)

    def InitializePumpDrive(self, **kwargs):
        return self.call('InitializePumpDrive', kwargs=kwargs)

