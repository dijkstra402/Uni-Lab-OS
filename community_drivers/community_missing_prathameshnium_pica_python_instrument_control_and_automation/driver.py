from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityMissingPrathameshniumPicaPythonInstrumentControlAndAutomation(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/prathameshnium__PICA-Python-Instrument-Control-and-Automation', 'source_file': 'pica/lakeshore/Instrument_Control/T_Control_L350_Simple_Instrument_Control.py', 'class_name': 'Lakeshore350', 'import_roots': [], 'candidate_methods': ['reset_and_clear', 'setup_heater', 'setup_ramp', 'set_setpoint', 'set_heater_range', 'get_temperature', 'get_heater_output', 'close'], 'metadata': {'repo': 'prathameshnium/PICA-Python-Instrument-Control-and-Automation', 'repo_url': 'https://github.com/prathameshnium/PICA-Python-Instrument-Control-and-Automation', 'source_file': 'pica/keithley/k2400_2182/Instrument_Control/IV_K2400_K2182_Instrument_Control.py', 'candidate_score': 120, 'candidate_reason': '', 'manufacturers': ['Keysight'], 'models': ['E4980A精密LCR表'], 'tags': ['介电常数测定仪'], 'notes': ['PICA套件-含多种仪器自动化'], 'comm_protocols': ['pyvisa'], 'review_status': 'good', 'review_notes': ['改选 Lakeshore 350 温控仪类，覆盖温度控制核心操作。']}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def reset_and_clear(self, **kwargs):
        return self.call('reset_and_clear', kwargs=kwargs)

    def setup_heater(self, **kwargs):
        return self.call('setup_heater', kwargs=kwargs)

    def setup_ramp(self, **kwargs):
        return self.call('setup_ramp', kwargs=kwargs)

    def set_setpoint(self, **kwargs):
        return self.call('set_setpoint', kwargs=kwargs)

    def set_heater_range(self, **kwargs):
        return self.call('set_heater_range', kwargs=kwargs)

    def get_temperature(self, **kwargs):
        return self.call('get_temperature', kwargs=kwargs)

    def get_heater_output(self, **kwargs):
        return self.call('get_heater_output', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

