from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentIviumCompactstat(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/Gnpd__pyvium', 'source_file': 'pyvium/core/direct_mode_functions.py', 'class_name': 'DirectModeFunctions', 'import_roots': [], 'candidate_methods': ['IV_getcellstatus', 'IV_setconnectionmode', 'IV_setcellon', 'IV_setpotential', 'IV_setpotentialWE2', 'IV_setcurrent', 'IV_getpotential', 'IV_setcurrentrange', 'IV_setcurrentrangeWE2', 'IV_getcurrent', 'IV_getcurrentWE2', 'IV_setfilter', 'IV_setstability', 'IV_setbistatmode', 'IV_setdac', 'IV_getadc', 'IV_setmuxchannel', 'IV_setdigout', 'IV_getdigin', 'IV_setfrequency', 'IV_setamplitude', 'IV_getcurrenttrace', 'IV_getcurrentWE2trace', 'IV_getpotentialtrace', 'get_lib', 'is_driver_open', 'set_driver_open'], 'action_targets': {}, 'metadata': {'repo': 'Gnpd/pyvium', 'repo_url': 'https://github.com/Gnpd/pyvium', 'brand': 'Ivium', 'model': 'CompactStat', 'device_type_cn': '恒电位仪', 'device_type_en': 'Potentiostat', 'source_framework': '电化学/热分析/天平', 'tag_id': '4425', 'tag_name': '电化学工作站', 'tag_name_en': 'Electrochemical Workstation', 'candidate_score': 230, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def IV_getcellstatus(self, **kwargs):
        return self.call('IV_getcellstatus', kwargs=kwargs)

    def IV_setconnectionmode(self, **kwargs):
        return self.call('IV_setconnectionmode', kwargs=kwargs)

    def IV_setcellon(self, **kwargs):
        return self.call('IV_setcellon', kwargs=kwargs)

    def IV_setpotential(self, **kwargs):
        return self.call('IV_setpotential', kwargs=kwargs)

    def IV_setpotentialWE2(self, **kwargs):
        return self.call('IV_setpotentialWE2', kwargs=kwargs)

    def IV_setcurrent(self, **kwargs):
        return self.call('IV_setcurrent', kwargs=kwargs)

    def IV_getpotential(self, **kwargs):
        return self.call('IV_getpotential', kwargs=kwargs)

    def IV_setcurrentrange(self, **kwargs):
        return self.call('IV_setcurrentrange', kwargs=kwargs)

    def IV_setcurrentrangeWE2(self, **kwargs):
        return self.call('IV_setcurrentrangeWE2', kwargs=kwargs)

    def IV_getcurrent(self, **kwargs):
        return self.call('IV_getcurrent', kwargs=kwargs)

    def IV_getcurrentWE2(self, **kwargs):
        return self.call('IV_getcurrentWE2', kwargs=kwargs)

    def IV_setfilter(self, **kwargs):
        return self.call('IV_setfilter', kwargs=kwargs)

    def IV_setstability(self, **kwargs):
        return self.call('IV_setstability', kwargs=kwargs)

    def IV_setbistatmode(self, **kwargs):
        return self.call('IV_setbistatmode', kwargs=kwargs)

    def IV_setdac(self, **kwargs):
        return self.call('IV_setdac', kwargs=kwargs)

    def IV_getadc(self, **kwargs):
        return self.call('IV_getadc', kwargs=kwargs)

    def IV_setmuxchannel(self, **kwargs):
        return self.call('IV_setmuxchannel', kwargs=kwargs)

    def IV_setdigout(self, **kwargs):
        return self.call('IV_setdigout', kwargs=kwargs)

    def IV_getdigin(self, **kwargs):
        return self.call('IV_getdigin', kwargs=kwargs)

    def IV_setfrequency(self, **kwargs):
        return self.call('IV_setfrequency', kwargs=kwargs)

    def IV_setamplitude(self, **kwargs):
        return self.call('IV_setamplitude', kwargs=kwargs)

    def IV_getcurrenttrace(self, **kwargs):
        return self.call('IV_getcurrenttrace', kwargs=kwargs)

    def IV_getcurrentWE2trace(self, **kwargs):
        return self.call('IV_getcurrentWE2trace', kwargs=kwargs)

    def IV_getpotentialtrace(self, **kwargs):
        return self.call('IV_getpotentialtrace', kwargs=kwargs)

    def get_lib(self, **kwargs):
        return self.call('get_lib', kwargs=kwargs)

    def is_driver_open(self, **kwargs):
        return self.call('is_driver_open', kwargs=kwargs)

    def set_driver_open(self, **kwargs):
        return self.call('set_driver_open', kwargs=kwargs)

