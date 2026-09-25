from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubDavidmamUvspec(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/davidmam_UvSpec', 'source_file': 'J6305.py', 'class_name': 'Spectrometer', 'import_roots': [], 'candidate_methods': ['pause', 'set_shutter', 'printout', 'transmission', 'absorbance', 'concentration', 'voltage', 'calibrate', 'set_wavelength', 'set_conc_factor', 'scan', 'luminosity', 'scan_to_file'], 'metadata': {'repo': 'davidmam/uvspec', 'repo_url': 'https://github.com/davidmam/UvSpec', 'unit_id': 'gh_jenway_6305', 'source_file': 'J6305.py', 'candidate_score': 77, 'manufacturer': 'Jenway', 'model_name': 'Jenway 6305'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def pause(self, **kwargs):
        return self.call('pause', kwargs=kwargs)

    def set_shutter(self, **kwargs):
        return self.call('set_shutter', kwargs=kwargs)

    def printout(self, **kwargs):
        return self.call('printout', kwargs=kwargs)

    def transmission(self, **kwargs):
        return self.call('transmission', kwargs=kwargs)

    def absorbance(self, **kwargs):
        return self.call('absorbance', kwargs=kwargs)

    def concentration(self, **kwargs):
        return self.call('concentration', kwargs=kwargs)

    def voltage(self, **kwargs):
        return self.call('voltage', kwargs=kwargs)

    def calibrate(self, **kwargs):
        return self.call('calibrate', kwargs=kwargs)

    def set_wavelength(self, **kwargs):
        return self.call('set_wavelength', kwargs=kwargs)

    def set_conc_factor(self, **kwargs):
        return self.call('set_conc_factor', kwargs=kwargs)

    def scan(self, **kwargs):
        return self.call('scan', kwargs=kwargs)

    def luminosity(self, **kwargs):
        return self.call('luminosity', kwargs=kwargs)

    def scan_to_file(self, **kwargs):
        return self.call('scan_to_file', kwargs=kwargs)

