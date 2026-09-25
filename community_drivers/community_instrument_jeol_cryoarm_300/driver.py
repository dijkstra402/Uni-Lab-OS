from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentJeolCryoarm300(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/eisfabian__PACEtomo', 'source_file': 'untested/PACEtomo.py', 'class_name': '', 'import_roots': [], 'candidate_methods': ['checkFilling', 'checkColdFEG', 'checkSlit', 'checkValves', 'retryOpen', 'openOldFile', 'parseTargets', 'updateTargets', 'writeAutodoc', 'geoPlane', 'geoPara', 'parseMdoc', 'writeMdoc', 'getExtendedHeader', 'writeExtendedHeader', 'sortTS', 'bin2d', 'binStack', 'checkFrames', 'alignTo', 'realignTo', 'log', 'breakpoint', 'Tilt', 'dumpVars'], 'action_targets': {'checkFilling': 'checkFilling', 'checkColdFEG': 'checkColdFEG', 'checkSlit': 'checkSlit', 'checkValves': 'checkValves', 'retryOpen': 'retryOpen', 'openOldFile': 'openOldFile', 'parseTargets': 'parseTargets', 'updateTargets': 'updateTargets', 'writeAutodoc': 'writeAutodoc', 'geoPlane': 'geoPlane', 'geoPara': 'geoPara', 'parseMdoc': 'parseMdoc', 'writeMdoc': 'writeMdoc', 'getExtendedHeader': 'getExtendedHeader', 'writeExtendedHeader': 'writeExtendedHeader', 'sortTS': 'sortTS', 'bin2d': 'bin2d', 'binStack': 'binStack', 'checkFrames': 'checkFrames', 'alignTo': 'alignTo', 'realignTo': 'realignTo', 'log': 'log', 'breakpoint': 'breakpoint', 'Tilt': 'Tilt', 'dumpVars': 'dumpVars'}, 'metadata': {'repo': 'eisfabian/PACEtomo', 'repo_url': 'https://github.com/eisfabian/PACEtomo', 'brand': 'JEOL', 'model': 'cryoARM 300', 'device_type_cn': 'Cryo-TEM', 'device_type_en': 'Cryo Transmission Electron Microscope', 'source_framework': '显微镜/成像', 'tag_id': '4456', 'tag_name': '透射电子显微镜', 'tag_name_en': 'Transmission Electron Microscope', 'candidate_score': 195, 'parse_status': 'module_reselected', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'checkFilling': 'checkFilling', 'checkColdFEG': 'checkColdFEG', 'checkSlit': 'checkSlit', 'checkValves': 'checkValves', 'retryOpen': 'retryOpen', 'openOldFile': 'openOldFile', 'parseTargets': 'parseTargets', 'updateTargets': 'updateTargets', 'writeAutodoc': 'writeAutodoc', 'geoPlane': 'geoPlane', 'geoPara': 'geoPara', 'parseMdoc': 'parseMdoc', 'writeMdoc': 'writeMdoc', 'getExtendedHeader': 'getExtendedHeader', 'writeExtendedHeader': 'writeExtendedHeader', 'sortTS': 'sortTS', 'bin2d': 'bin2d', 'binStack': 'binStack', 'checkFrames': 'checkFrames', 'alignTo': 'alignTo', 'realignTo': 'realignTo', 'log': 'log', 'breakpoint': 'breakpoint', 'Tilt': 'Tilt', 'dumpVars': 'dumpVars'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def checkFilling(self, **kwargs):
        return self.call('checkFilling', kwargs=kwargs)

    def checkColdFEG(self, **kwargs):
        return self.call('checkColdFEG', kwargs=kwargs)

    def checkSlit(self, **kwargs):
        return self.call('checkSlit', kwargs=kwargs)

    def checkValves(self, **kwargs):
        return self.call('checkValves', kwargs=kwargs)

    def retryOpen(self, **kwargs):
        return self.call('retryOpen', kwargs=kwargs)

    def openOldFile(self, **kwargs):
        return self.call('openOldFile', kwargs=kwargs)

    def parseTargets(self, **kwargs):
        return self.call('parseTargets', kwargs=kwargs)

    def updateTargets(self, **kwargs):
        return self.call('updateTargets', kwargs=kwargs)

    def writeAutodoc(self, **kwargs):
        return self.call('writeAutodoc', kwargs=kwargs)

    def geoPlane(self, **kwargs):
        return self.call('geoPlane', kwargs=kwargs)

    def geoPara(self, **kwargs):
        return self.call('geoPara', kwargs=kwargs)

    def parseMdoc(self, **kwargs):
        return self.call('parseMdoc', kwargs=kwargs)

    def writeMdoc(self, **kwargs):
        return self.call('writeMdoc', kwargs=kwargs)

    def getExtendedHeader(self, **kwargs):
        return self.call('getExtendedHeader', kwargs=kwargs)

    def writeExtendedHeader(self, **kwargs):
        return self.call('writeExtendedHeader', kwargs=kwargs)

    def sortTS(self, **kwargs):
        return self.call('sortTS', kwargs=kwargs)

    def bin2d(self, **kwargs):
        return self.call('bin2d', kwargs=kwargs)

    def binStack(self, **kwargs):
        return self.call('binStack', kwargs=kwargs)

    def checkFrames(self, **kwargs):
        return self.call('checkFrames', kwargs=kwargs)

    def alignTo(self, **kwargs):
        return self.call('alignTo', kwargs=kwargs)

    def realignTo(self, **kwargs):
        return self.call('realignTo', kwargs=kwargs)

    def log(self, **kwargs):
        return self.call('log', kwargs=kwargs)

    def breakpoint(self, **kwargs):
        return self.call('breakpoint', kwargs=kwargs)

    def Tilt(self, **kwargs):
        return self.call('Tilt', kwargs=kwargs)

    def dumpVars(self, **kwargs):
        return self.call('dumpVars', kwargs=kwargs)

