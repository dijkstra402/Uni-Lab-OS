from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentBiologicSp150Sp200Sp300(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/federicoscarpioni__pyeclab', 'source_file': 'src/pyeclab/api/kbio_api.py', 'class_name': 'KBIO_api', 'import_roots': ['src'], 'candidate_methods': ['GetLibVersion', 'Connect', 'USB_DeviceInfo', 'TestConnection', 'TestComSpeed', 'Disconnect', 'PluggedChannels', 'channel_map', 'GetChannelInfo', 'LoadFirmware', 'GetHardwareConf', 'SetHardwareConf', 'OptionError', 'GetMessage', 'GetErrorMsg', 'DefineParameter', 'DefineBoolParameter', 'DefineSglParameter', 'DefineIntParameter', 'UpdateParameters', 'GetTechniqueInfos', 'GetParamInfos', 'LoadTechnique', 'StartChannel', 'StopChannel', 'StartChannels', 'StopChannels', 'GetCurrentValues', 'GetData', 'ConvertNumericIntoSingle', 'FindEChemDev', 'FindEChemEthDev', 'FindEChemUsbDev', 'SetEthernetConfig', 'bind_function'], 'action_targets': {}, 'metadata': {'repo': 'federicoscarpioni/pyeclab', 'repo_url': 'https://github.com/federicoscarpioni/pyeclab', 'brand': 'BioLogic', 'model': 'SP-150/SP-200/SP-300', 'device_type_cn': '电化学工作站', 'device_type_en': 'Electrochemical Workstation', 'source_framework': 'pyeclab', 'tag_id': '4425', 'tag_name': '电化学工作站', 'tag_name_en': 'Electrochemical Workstation', 'candidate_score': 318, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def GetLibVersion(self, **kwargs):
        return self.call('GetLibVersion', kwargs=kwargs)

    def Connect(self, **kwargs):
        return self.call('Connect', kwargs=kwargs)

    def USB_DeviceInfo(self, **kwargs):
        return self.call('USB_DeviceInfo', kwargs=kwargs)

    def TestConnection(self, **kwargs):
        return self.call('TestConnection', kwargs=kwargs)

    def TestComSpeed(self, **kwargs):
        return self.call('TestComSpeed', kwargs=kwargs)

    def Disconnect(self, **kwargs):
        return self.call('Disconnect', kwargs=kwargs)

    def PluggedChannels(self, **kwargs):
        return self.call('PluggedChannels', kwargs=kwargs)

    def channel_map(self, **kwargs):
        return self.call('channel_map', kwargs=kwargs)

    def GetChannelInfo(self, **kwargs):
        return self.call('GetChannelInfo', kwargs=kwargs)

    def LoadFirmware(self, **kwargs):
        return self.call('LoadFirmware', kwargs=kwargs)

    def GetHardwareConf(self, **kwargs):
        return self.call('GetHardwareConf', kwargs=kwargs)

    def SetHardwareConf(self, **kwargs):
        return self.call('SetHardwareConf', kwargs=kwargs)

    def OptionError(self, **kwargs):
        return self.call('OptionError', kwargs=kwargs)

    def GetMessage(self, **kwargs):
        return self.call('GetMessage', kwargs=kwargs)

    def GetErrorMsg(self, **kwargs):
        return self.call('GetErrorMsg', kwargs=kwargs)

    def DefineParameter(self, **kwargs):
        return self.call('DefineParameter', kwargs=kwargs)

    def DefineBoolParameter(self, **kwargs):
        return self.call('DefineBoolParameter', kwargs=kwargs)

    def DefineSglParameter(self, **kwargs):
        return self.call('DefineSglParameter', kwargs=kwargs)

    def DefineIntParameter(self, **kwargs):
        return self.call('DefineIntParameter', kwargs=kwargs)

    def UpdateParameters(self, **kwargs):
        return self.call('UpdateParameters', kwargs=kwargs)

    def GetTechniqueInfos(self, **kwargs):
        return self.call('GetTechniqueInfos', kwargs=kwargs)

    def GetParamInfos(self, **kwargs):
        return self.call('GetParamInfos', kwargs=kwargs)

    def LoadTechnique(self, **kwargs):
        return self.call('LoadTechnique', kwargs=kwargs)

    def StartChannel(self, **kwargs):
        return self.call('StartChannel', kwargs=kwargs)

    def StopChannel(self, **kwargs):
        return self.call('StopChannel', kwargs=kwargs)

    def StartChannels(self, **kwargs):
        return self.call('StartChannels', kwargs=kwargs)

    def StopChannels(self, **kwargs):
        return self.call('StopChannels', kwargs=kwargs)

    def GetCurrentValues(self, **kwargs):
        return self.call('GetCurrentValues', kwargs=kwargs)

    def GetData(self, **kwargs):
        return self.call('GetData', kwargs=kwargs)

    def ConvertNumericIntoSingle(self, **kwargs):
        return self.call('ConvertNumericIntoSingle', kwargs=kwargs)

    def FindEChemDev(self, **kwargs):
        return self.call('FindEChemDev', kwargs=kwargs)

    def FindEChemEthDev(self, **kwargs):
        return self.call('FindEChemEthDev', kwargs=kwargs)

    def FindEChemUsbDev(self, **kwargs):
        return self.call('FindEChemUsbDev', kwargs=kwargs)

    def SetEthernetConfig(self, **kwargs):
        return self.call('SetEthernetConfig', kwargs=kwargs)

    def bind_function(self, **kwargs):
        return self.call('bind_function', kwargs=kwargs)

