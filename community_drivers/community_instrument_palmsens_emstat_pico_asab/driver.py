from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentPalmsensEmstatPicoAsab(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/Helge-Stein-Group__ASAB', 'source_file': 'src/ASAB/utility/graph.py', 'class_name': '', 'import_roots': ['src'], 'candidate_methods': ['generateGraph', 'loadGraph', 'getGraph', 'findClosest', 'improvePath', 'findPathAB', 'findPath', 'checkConsistency', 'appendEdge', 'drawGraph', 'getValveFromName', 'getEdgedictFromNodelist', 'getTotalQuantity', 'getValveSettings', 'pathIsValid', 'getSystemStatus', 'updateSystemStatus', 'findCandidate', 'getOpenEnds', 'getDirectionality', 'pathsCompatible'], 'action_targets': {'generateGraph': 'generateGraph', 'loadGraph': 'loadGraph', 'getGraph': 'getGraph', 'findClosest': 'findClosest', 'improvePath': 'improvePath', 'findPathAB': 'findPathAB', 'findPath': 'findPath', 'checkConsistency': 'checkConsistency', 'appendEdge': 'appendEdge', 'drawGraph': 'drawGraph', 'getValveFromName': 'getValveFromName', 'getEdgedictFromNodelist': 'getEdgedictFromNodelist', 'getTotalQuantity': 'getTotalQuantity', 'getValveSettings': 'getValveSettings', 'pathIsValid': 'pathIsValid', 'getSystemStatus': 'getSystemStatus', 'updateSystemStatus': 'updateSystemStatus', 'findCandidate': 'findCandidate', 'getOpenEnds': 'getOpenEnds', 'getDirectionality': 'getDirectionality', 'pathsCompatible': 'pathsCompatible'}, 'metadata': {'repo': 'Helge-Stein-Group/ASAB', 'repo_url': 'https://github.com/Helge-Stein-Group/ASAB', 'brand': 'PalmSens', 'model': 'EmStat Pico (ASAB)', 'device_type_cn': '电化学工作站', 'device_type_en': 'Potentiostat', 'source_framework': 'ASAB', 'tag_id': '4425', 'tag_name': '电化学工作站', 'tag_name_en': 'Electrochemical Workstation', 'candidate_score': 155, 'parse_status': 'module_reselected', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'generateGraph': 'generateGraph', 'loadGraph': 'loadGraph', 'getGraph': 'getGraph', 'findClosest': 'findClosest', 'improvePath': 'improvePath', 'findPathAB': 'findPathAB', 'findPath': 'findPath', 'checkConsistency': 'checkConsistency', 'appendEdge': 'appendEdge', 'drawGraph': 'drawGraph', 'getValveFromName': 'getValveFromName', 'getEdgedictFromNodelist': 'getEdgedictFromNodelist', 'getTotalQuantity': 'getTotalQuantity', 'getValveSettings': 'getValveSettings', 'pathIsValid': 'pathIsValid', 'getSystemStatus': 'getSystemStatus', 'updateSystemStatus': 'updateSystemStatus', 'findCandidate': 'findCandidate', 'getOpenEnds': 'getOpenEnds', 'getDirectionality': 'getDirectionality', 'pathsCompatible': 'pathsCompatible'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def generateGraph(self, **kwargs):
        return self.call('generateGraph', kwargs=kwargs)

    def loadGraph(self, **kwargs):
        return self.call('loadGraph', kwargs=kwargs)

    def getGraph(self, **kwargs):
        return self.call('getGraph', kwargs=kwargs)

    def findClosest(self, **kwargs):
        return self.call('findClosest', kwargs=kwargs)

    def improvePath(self, **kwargs):
        return self.call('improvePath', kwargs=kwargs)

    def findPathAB(self, **kwargs):
        return self.call('findPathAB', kwargs=kwargs)

    def findPath(self, **kwargs):
        return self.call('findPath', kwargs=kwargs)

    def checkConsistency(self, **kwargs):
        return self.call('checkConsistency', kwargs=kwargs)

    def appendEdge(self, **kwargs):
        return self.call('appendEdge', kwargs=kwargs)

    def drawGraph(self, **kwargs):
        return self.call('drawGraph', kwargs=kwargs)

    def getValveFromName(self, **kwargs):
        return self.call('getValveFromName', kwargs=kwargs)

    def getEdgedictFromNodelist(self, **kwargs):
        return self.call('getEdgedictFromNodelist', kwargs=kwargs)

    def getTotalQuantity(self, **kwargs):
        return self.call('getTotalQuantity', kwargs=kwargs)

    def getValveSettings(self, **kwargs):
        return self.call('getValveSettings', kwargs=kwargs)

    def pathIsValid(self, **kwargs):
        return self.call('pathIsValid', kwargs=kwargs)

    def getSystemStatus(self, **kwargs):
        return self.call('getSystemStatus', kwargs=kwargs)

    def updateSystemStatus(self, **kwargs):
        return self.call('updateSystemStatus', kwargs=kwargs)

    def findCandidate(self, **kwargs):
        return self.call('findCandidate', kwargs=kwargs)

    def getOpenEnds(self, **kwargs):
        return self.call('getOpenEnds', kwargs=kwargs)

    def getDirectionality(self, **kwargs):
        return self.call('getDirectionality', kwargs=kwargs)

    def pathsCompatible(self, **kwargs):
        return self.call('pathsCompatible', kwargs=kwargs)

