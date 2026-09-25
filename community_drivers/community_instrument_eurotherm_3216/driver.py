from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentEurotherm3216(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/hailegroup__nupylab', 'source_file': 'nupylab/drivers/labjack_u12.py', 'class_name': 'U12', 'import_roots': [], 'candidate_methods': ['open', 'close', 'write', 'read', 'rawReadSerial', 'rawReadLocalId', 'rawAISample', 'rawDIO', 'rawCounter', 'rawCounterPWMDIO', 'rawAIBurst', 'rawAIContinuous', 'rawPulseout', 'rawReset', 'rawReenumerate', 'rawWatchdog', 'rawReadRAM', 'rawWriteRAM', 'rawAsynch', 'rawSPI', 'rawSHT1X', 'eAnalogIn', 'eAnalogOut', 'eCount', 'eDigitalIn', 'eDigitalOut', 'aiSample', 'aiBurst', 'aiStreamStart', 'aiStreamRead', 'aiStreamClear', 'aoUpdate', 'asynchConfig', 'asynch', 'bitsToVolts', 'voltsToBits', 'counter', 'digitalIO', 'getDriverVersion', 'getFirmwareVersion', 'getWinVersion', 'listAll', 'localID', 'noThread', 'pulseOut', 'pulseOutStart', 'pulseOutFinish', 'pulseOutCalc', 'reEnum', 'reset', 'resetLJ', 'sht1X', 'shtComm', 'shtCRC', 'synch', 'watchdog', 'readMem', 'writeMem', 'LJHash', 'getErrorString'], 'action_targets': {}, 'metadata': {'repo': 'hailegroup/nupylab', 'repo_url': 'https://github.com/hailegroup/nupylab', 'brand': 'Eurotherm', 'model': '3216', 'device_type_cn': '箱式电阻炉', 'device_type_en': 'Box Resistance Furnace', 'source_framework': 'nupylab', 'tag_id': '4438', 'tag_name': '箱式电阻炉', 'tag_name_en': 'Box Resistance Furnace', 'candidate_score': 518, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def open(self, **kwargs):
        return self.call('open', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def write(self, **kwargs):
        return self.call('write', kwargs=kwargs)

    def read(self, **kwargs):
        return self.call('read', kwargs=kwargs)

    def rawReadSerial(self, **kwargs):
        return self.call('rawReadSerial', kwargs=kwargs)

    def rawReadLocalId(self, **kwargs):
        return self.call('rawReadLocalId', kwargs=kwargs)

    def rawAISample(self, **kwargs):
        return self.call('rawAISample', kwargs=kwargs)

    def rawDIO(self, **kwargs):
        return self.call('rawDIO', kwargs=kwargs)

    def rawCounter(self, **kwargs):
        return self.call('rawCounter', kwargs=kwargs)

    def rawCounterPWMDIO(self, **kwargs):
        return self.call('rawCounterPWMDIO', kwargs=kwargs)

    def rawAIBurst(self, **kwargs):
        return self.call('rawAIBurst', kwargs=kwargs)

    def rawAIContinuous(self, **kwargs):
        return self.call('rawAIContinuous', kwargs=kwargs)

    def rawPulseout(self, **kwargs):
        return self.call('rawPulseout', kwargs=kwargs)

    def rawReset(self, **kwargs):
        return self.call('rawReset', kwargs=kwargs)

    def rawReenumerate(self, **kwargs):
        return self.call('rawReenumerate', kwargs=kwargs)

    def rawWatchdog(self, **kwargs):
        return self.call('rawWatchdog', kwargs=kwargs)

    def rawReadRAM(self, **kwargs):
        return self.call('rawReadRAM', kwargs=kwargs)

    def rawWriteRAM(self, **kwargs):
        return self.call('rawWriteRAM', kwargs=kwargs)

    def rawAsynch(self, **kwargs):
        return self.call('rawAsynch', kwargs=kwargs)

    def rawSPI(self, **kwargs):
        return self.call('rawSPI', kwargs=kwargs)

    def rawSHT1X(self, **kwargs):
        return self.call('rawSHT1X', kwargs=kwargs)

    def eAnalogIn(self, **kwargs):
        return self.call('eAnalogIn', kwargs=kwargs)

    def eAnalogOut(self, **kwargs):
        return self.call('eAnalogOut', kwargs=kwargs)

    def eCount(self, **kwargs):
        return self.call('eCount', kwargs=kwargs)

    def eDigitalIn(self, **kwargs):
        return self.call('eDigitalIn', kwargs=kwargs)

    def eDigitalOut(self, **kwargs):
        return self.call('eDigitalOut', kwargs=kwargs)

    def aiSample(self, **kwargs):
        return self.call('aiSample', kwargs=kwargs)

    def aiBurst(self, **kwargs):
        return self.call('aiBurst', kwargs=kwargs)

    def aiStreamStart(self, **kwargs):
        return self.call('aiStreamStart', kwargs=kwargs)

    def aiStreamRead(self, **kwargs):
        return self.call('aiStreamRead', kwargs=kwargs)

    def aiStreamClear(self, **kwargs):
        return self.call('aiStreamClear', kwargs=kwargs)

    def aoUpdate(self, **kwargs):
        return self.call('aoUpdate', kwargs=kwargs)

    def asynchConfig(self, **kwargs):
        return self.call('asynchConfig', kwargs=kwargs)

    def asynch(self, **kwargs):
        return self.call('asynch', kwargs=kwargs)

    def bitsToVolts(self, **kwargs):
        return self.call('bitsToVolts', kwargs=kwargs)

    def voltsToBits(self, **kwargs):
        return self.call('voltsToBits', kwargs=kwargs)

    def counter(self, **kwargs):
        return self.call('counter', kwargs=kwargs)

    def digitalIO(self, **kwargs):
        return self.call('digitalIO', kwargs=kwargs)

    def getDriverVersion(self, **kwargs):
        return self.call('getDriverVersion', kwargs=kwargs)

    def getFirmwareVersion(self, **kwargs):
        return self.call('getFirmwareVersion', kwargs=kwargs)

    def getWinVersion(self, **kwargs):
        return self.call('getWinVersion', kwargs=kwargs)

    def listAll(self, **kwargs):
        return self.call('listAll', kwargs=kwargs)

    def localID(self, **kwargs):
        return self.call('localID', kwargs=kwargs)

    def noThread(self, **kwargs):
        return self.call('noThread', kwargs=kwargs)

    def pulseOut(self, **kwargs):
        return self.call('pulseOut', kwargs=kwargs)

    def pulseOutStart(self, **kwargs):
        return self.call('pulseOutStart', kwargs=kwargs)

    def pulseOutFinish(self, **kwargs):
        return self.call('pulseOutFinish', kwargs=kwargs)

    def pulseOutCalc(self, **kwargs):
        return self.call('pulseOutCalc', kwargs=kwargs)

    def reEnum(self, **kwargs):
        return self.call('reEnum', kwargs=kwargs)

    def reset(self, **kwargs):
        return self.call('reset', kwargs=kwargs)

    def resetLJ(self, **kwargs):
        return self.call('resetLJ', kwargs=kwargs)

    def sht1X(self, **kwargs):
        return self.call('sht1X', kwargs=kwargs)

    def shtComm(self, **kwargs):
        return self.call('shtComm', kwargs=kwargs)

    def shtCRC(self, **kwargs):
        return self.call('shtCRC', kwargs=kwargs)

    def synch(self, **kwargs):
        return self.call('synch', kwargs=kwargs)

    def watchdog(self, **kwargs):
        return self.call('watchdog', kwargs=kwargs)

    def readMem(self, **kwargs):
        return self.call('readMem', kwargs=kwargs)

    def writeMem(self, **kwargs):
        return self.call('writeMem', kwargs=kwargs)

    def LJHash(self, **kwargs):
        return self.call('LJHash', kwargs=kwargs)

    def getErrorString(self, **kwargs):
        return self.call('getErrorString', kwargs=kwargs)

