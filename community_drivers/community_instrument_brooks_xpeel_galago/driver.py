from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentBrooksXpeelGalago(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/sciencecorp__galago-tools', 'source_file': 'tools/pf400/server.py', 'class_name': 'Pf400Server', 'import_roots': [], 'candidate_methods': ['LoadWaypoints', 'LoadLabware', 'Unwind', 'Release', 'Engage', 'moveTo', 'Move', 'GraspPlate', 'ReleasePlate', 'retrieve_plate', 'dropoff_plate', 'RetrievePlate', 'DropOffPlate', 'Jog', 'Transfer', 'PickLid', 'PlaceLid', 'GetCurrentLocation', 'command_instance_from_name', 'RunSequence', 'estimateRelease', 'estimateEngage', 'estimateUnwind', 'estimateGraspPlate', 'estimateReleasePlate', 'estimateRunSequence', 'EstimateGetCurrentLocation', 'EstimateMove', 'EstimateTransfer', 'EstimateJog', 'EstimatePickLid', 'EstimatePlaceLid', 'EstimateLoadWaypoints', 'EstimateLoadLabware', 'GetStatus', 'setSimulated', 'setStatus', 'Configure', 'runSequence', 'isReady', 'parseCommand', 'ExecuteCommand', 'EstimateDuration'], 'action_targets': {}, 'metadata': {'repo': 'sciencecorp/galago-tools', 'repo_url': 'https://github.com/sciencecorp/galago-tools', 'brand': 'Brooks', 'model': 'XPeel (galago)', 'device_type_cn': '撕膜仪', 'device_type_en': 'Plate Desealer', 'source_framework': 'galago-tools', 'tag_id': '4396', 'tag_name': '撕膜仪', 'tag_name_en': 'Plate Desealer', 'candidate_score': 310, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def LoadWaypoints(self, **kwargs):
        return self.call('LoadWaypoints', kwargs=kwargs)

    def LoadLabware(self, **kwargs):
        return self.call('LoadLabware', kwargs=kwargs)

    def Unwind(self, **kwargs):
        return self.call('Unwind', kwargs=kwargs)

    def Release(self, **kwargs):
        return self.call('Release', kwargs=kwargs)

    def Engage(self, **kwargs):
        return self.call('Engage', kwargs=kwargs)

    def moveTo(self, **kwargs):
        return self.call('moveTo', kwargs=kwargs)

    def Move(self, **kwargs):
        return self.call('Move', kwargs=kwargs)

    def GraspPlate(self, **kwargs):
        return self.call('GraspPlate', kwargs=kwargs)

    def ReleasePlate(self, **kwargs):
        return self.call('ReleasePlate', kwargs=kwargs)

    def retrieve_plate(self, **kwargs):
        return self.call('retrieve_plate', kwargs=kwargs)

    def dropoff_plate(self, **kwargs):
        return self.call('dropoff_plate', kwargs=kwargs)

    def RetrievePlate(self, **kwargs):
        return self.call('RetrievePlate', kwargs=kwargs)

    def DropOffPlate(self, **kwargs):
        return self.call('DropOffPlate', kwargs=kwargs)

    def Jog(self, **kwargs):
        return self.call('Jog', kwargs=kwargs)

    def Transfer(self, **kwargs):
        return self.call('Transfer', kwargs=kwargs)

    def PickLid(self, **kwargs):
        return self.call('PickLid', kwargs=kwargs)

    def PlaceLid(self, **kwargs):
        return self.call('PlaceLid', kwargs=kwargs)

    def GetCurrentLocation(self, **kwargs):
        return self.call('GetCurrentLocation', kwargs=kwargs)

    def command_instance_from_name(self, **kwargs):
        return self.call('command_instance_from_name', kwargs=kwargs)

    def RunSequence(self, **kwargs):
        return self.call('RunSequence', kwargs=kwargs)

    def estimateRelease(self, **kwargs):
        return self.call('estimateRelease', kwargs=kwargs)

    def estimateEngage(self, **kwargs):
        return self.call('estimateEngage', kwargs=kwargs)

    def estimateUnwind(self, **kwargs):
        return self.call('estimateUnwind', kwargs=kwargs)

    def estimateGraspPlate(self, **kwargs):
        return self.call('estimateGraspPlate', kwargs=kwargs)

    def estimateReleasePlate(self, **kwargs):
        return self.call('estimateReleasePlate', kwargs=kwargs)

    def estimateRunSequence(self, **kwargs):
        return self.call('estimateRunSequence', kwargs=kwargs)

    def EstimateGetCurrentLocation(self, **kwargs):
        return self.call('EstimateGetCurrentLocation', kwargs=kwargs)

    def EstimateMove(self, **kwargs):
        return self.call('EstimateMove', kwargs=kwargs)

    def EstimateTransfer(self, **kwargs):
        return self.call('EstimateTransfer', kwargs=kwargs)

    def EstimateJog(self, **kwargs):
        return self.call('EstimateJog', kwargs=kwargs)

    def EstimatePickLid(self, **kwargs):
        return self.call('EstimatePickLid', kwargs=kwargs)

    def EstimatePlaceLid(self, **kwargs):
        return self.call('EstimatePlaceLid', kwargs=kwargs)

    def EstimateLoadWaypoints(self, **kwargs):
        return self.call('EstimateLoadWaypoints', kwargs=kwargs)

    def EstimateLoadLabware(self, **kwargs):
        return self.call('EstimateLoadLabware', kwargs=kwargs)

    def GetStatus(self, **kwargs):
        return self.call('GetStatus', kwargs=kwargs)

    def setSimulated(self, **kwargs):
        return self.call('setSimulated', kwargs=kwargs)

    def setStatus(self, **kwargs):
        return self.call('setStatus', kwargs=kwargs)

    def Configure(self, **kwargs):
        return self.call('Configure', kwargs=kwargs)

    def runSequence(self, **kwargs):
        return self.call('runSequence', kwargs=kwargs)

    def isReady(self, **kwargs):
        return self.call('isReady', kwargs=kwargs)

    def parseCommand(self, **kwargs):
        return self.call('parseCommand', kwargs=kwargs)

    def ExecuteCommand(self, **kwargs):
        return self.call('ExecuteCommand', kwargs=kwargs)

    def EstimateDuration(self, **kwargs):
        return self.call('EstimateDuration', kwargs=kwargs)

