from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAvantesAvaspec20482(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/tspspi__pyavaspec', 'source_file': 'src/pyavaspec/avacli.py', 'class_name': 'PyAvaSpecCli', 'import_roots': ['src'], 'candidate_methods': ['parsevalidate_inttime', 'parsevalidate_avgcount_soft', 'parsevalidate_avgcount_hard', 'parsevalidate_avgcount', 'parsevalidate_peakmaxcount', 'parsevalidate_peakavgwindow', 'parsevalidate_plotformat', 'parsevalidate_sdg1032xCh', 'parsevalidate_sdg1032xFrq', 'parsevalidate_sdg1032xPeriod', 'parsevalidate_sleep', 'exec_inttime', 'exec_avgsoft', 'exec_avghard', 'exec_avg', 'exec_maxpeaks', 'exec_peakavgwindow', 'exec_measure', 'exec_measurebg', 'exec_dump', 'exec_dumpbg', 'exec_dumpf', 'exec_dumppeak', 'exec_dumpfpeak', 'exec_loadfpeak', 'exec_loadf', 'exec_loadfbg', 'exec_dumpfbg', 'exec_plotfmt', 'exec_plot', 'exec_plotf', 'exec_plotbg', 'exec_plotfbg', 'exec_subbg', 'exec_moveavg', 'exec_peaks', 'exec_SDG1032XDEV', 'exec_SDG1032XChannel', 'exec_SDG1032XFrequency', 'exec_SDG1032XPeriod', 'exec_GateOn', 'exec_GateOff', 'exec_sleep', 'printUsage', 'getDefaultConfiguration', 'initializeState', 'parseCommandOptions_Validation', 'executeCommands', 'close'], 'action_targets': {}, 'metadata': {'repo': 'tspspi/pyavaspec', 'repo_url': 'https://github.com/tspspi/pyavaspec', 'brand': 'Avantes', 'model': 'AvaSpec-2048-2', 'device_type_cn': 'UV-Vis光谱仪', 'device_type_en': 'UV-Vis Spectrometer', 'source_framework': '光谱分析', 'tag_id': '4439', 'tag_name': '紫外-可见分光光谱仪', 'tag_name_en': 'UV-Vis Spectrophotometer', 'candidate_score': 462, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def parsevalidate_inttime(self, **kwargs):
        return self.call('parsevalidate_inttime', kwargs=kwargs)

    def parsevalidate_avgcount_soft(self, **kwargs):
        return self.call('parsevalidate_avgcount_soft', kwargs=kwargs)

    def parsevalidate_avgcount_hard(self, **kwargs):
        return self.call('parsevalidate_avgcount_hard', kwargs=kwargs)

    def parsevalidate_avgcount(self, **kwargs):
        return self.call('parsevalidate_avgcount', kwargs=kwargs)

    def parsevalidate_peakmaxcount(self, **kwargs):
        return self.call('parsevalidate_peakmaxcount', kwargs=kwargs)

    def parsevalidate_peakavgwindow(self, **kwargs):
        return self.call('parsevalidate_peakavgwindow', kwargs=kwargs)

    def parsevalidate_plotformat(self, **kwargs):
        return self.call('parsevalidate_plotformat', kwargs=kwargs)

    def parsevalidate_sdg1032xCh(self, **kwargs):
        return self.call('parsevalidate_sdg1032xCh', kwargs=kwargs)

    def parsevalidate_sdg1032xFrq(self, **kwargs):
        return self.call('parsevalidate_sdg1032xFrq', kwargs=kwargs)

    def parsevalidate_sdg1032xPeriod(self, **kwargs):
        return self.call('parsevalidate_sdg1032xPeriod', kwargs=kwargs)

    def parsevalidate_sleep(self, **kwargs):
        return self.call('parsevalidate_sleep', kwargs=kwargs)

    def exec_inttime(self, **kwargs):
        return self.call('exec_inttime', kwargs=kwargs)

    def exec_avgsoft(self, **kwargs):
        return self.call('exec_avgsoft', kwargs=kwargs)

    def exec_avghard(self, **kwargs):
        return self.call('exec_avghard', kwargs=kwargs)

    def exec_avg(self, **kwargs):
        return self.call('exec_avg', kwargs=kwargs)

    def exec_maxpeaks(self, **kwargs):
        return self.call('exec_maxpeaks', kwargs=kwargs)

    def exec_peakavgwindow(self, **kwargs):
        return self.call('exec_peakavgwindow', kwargs=kwargs)

    def exec_measure(self, **kwargs):
        return self.call('exec_measure', kwargs=kwargs)

    def exec_measurebg(self, **kwargs):
        return self.call('exec_measurebg', kwargs=kwargs)

    def exec_dump(self, **kwargs):
        return self.call('exec_dump', kwargs=kwargs)

    def exec_dumpbg(self, **kwargs):
        return self.call('exec_dumpbg', kwargs=kwargs)

    def exec_dumpf(self, **kwargs):
        return self.call('exec_dumpf', kwargs=kwargs)

    def exec_dumppeak(self, **kwargs):
        return self.call('exec_dumppeak', kwargs=kwargs)

    def exec_dumpfpeak(self, **kwargs):
        return self.call('exec_dumpfpeak', kwargs=kwargs)

    def exec_loadfpeak(self, **kwargs):
        return self.call('exec_loadfpeak', kwargs=kwargs)

    def exec_loadf(self, **kwargs):
        return self.call('exec_loadf', kwargs=kwargs)

    def exec_loadfbg(self, **kwargs):
        return self.call('exec_loadfbg', kwargs=kwargs)

    def exec_dumpfbg(self, **kwargs):
        return self.call('exec_dumpfbg', kwargs=kwargs)

    def exec_plotfmt(self, **kwargs):
        return self.call('exec_plotfmt', kwargs=kwargs)

    def exec_plot(self, **kwargs):
        return self.call('exec_plot', kwargs=kwargs)

    def exec_plotf(self, **kwargs):
        return self.call('exec_plotf', kwargs=kwargs)

    def exec_plotbg(self, **kwargs):
        return self.call('exec_plotbg', kwargs=kwargs)

    def exec_plotfbg(self, **kwargs):
        return self.call('exec_plotfbg', kwargs=kwargs)

    def exec_subbg(self, **kwargs):
        return self.call('exec_subbg', kwargs=kwargs)

    def exec_moveavg(self, **kwargs):
        return self.call('exec_moveavg', kwargs=kwargs)

    def exec_peaks(self, **kwargs):
        return self.call('exec_peaks', kwargs=kwargs)

    def exec_SDG1032XDEV(self, **kwargs):
        return self.call('exec_SDG1032XDEV', kwargs=kwargs)

    def exec_SDG1032XChannel(self, **kwargs):
        return self.call('exec_SDG1032XChannel', kwargs=kwargs)

    def exec_SDG1032XFrequency(self, **kwargs):
        return self.call('exec_SDG1032XFrequency', kwargs=kwargs)

    def exec_SDG1032XPeriod(self, **kwargs):
        return self.call('exec_SDG1032XPeriod', kwargs=kwargs)

    def exec_GateOn(self, **kwargs):
        return self.call('exec_GateOn', kwargs=kwargs)

    def exec_GateOff(self, **kwargs):
        return self.call('exec_GateOff', kwargs=kwargs)

    def exec_sleep(self, **kwargs):
        return self.call('exec_sleep', kwargs=kwargs)

    def printUsage(self, **kwargs):
        return self.call('printUsage', kwargs=kwargs)

    def getDefaultConfiguration(self, **kwargs):
        return self.call('getDefaultConfiguration', kwargs=kwargs)

    def initializeState(self, **kwargs):
        return self.call('initializeState', kwargs=kwargs)

    def parseCommandOptions_Validation(self, **kwargs):
        return self.call('parseCommandOptions_Validation', kwargs=kwargs)

    def executeCommands(self, **kwargs):
        return self.call('executeCommands', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

