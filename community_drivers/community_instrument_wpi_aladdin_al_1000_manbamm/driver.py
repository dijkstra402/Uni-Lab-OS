from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentWpiAladdinAl1000Manbamm(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/mhvwerts__MANBAMM-control', 'source_file': 'python-src/FlowInjectPilot.py', 'class_name': 'AladdinPumpSteady', 'import_roots': [], 'candidate_methods': ['main', 'idle', 'activate151', 'deactivate152', 'start211', 'stop212', 'pumprate22', 'close41', 'onclosedialog41_confirm', 'm2_check_spin3x', 'm2_getvalues_spin3x', 'm2_runprog351', 'm2_stopprog352', 'deactivate', 'activate', 'start_pump', 'stop_pump', 'updatepumprate', 'm2_activate151', 'm2_deactivate152', 'm2_euha_posA_211', 'm2_euha_posB_212', 'euha_deactivate', 'euha_activate', 'euha_posA', 'euha_posB'], 'action_targets': {}, 'metadata': {'repo': 'mhvwerts/MANBAMM-control', 'repo_url': 'https://github.com/mhvwerts/MANBAMM-control', 'brand': 'WPI', 'model': 'Aladdin AL-1000 (MANBAMM)', 'device_type_cn': '注射泵', 'device_type_en': 'Syringe Pump', 'source_framework': '独立驱动', 'tag_id': '4413', 'tag_name': '注射泵', 'tag_name_en': 'Syringe Pump', 'candidate_score': 270, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def main(self, **kwargs):
        return self.call('main', kwargs=kwargs)

    def idle(self, **kwargs):
        return self.call('idle', kwargs=kwargs)

    def activate151(self, **kwargs):
        return self.call('activate151', kwargs=kwargs)

    def deactivate152(self, **kwargs):
        return self.call('deactivate152', kwargs=kwargs)

    def start211(self, **kwargs):
        return self.call('start211', kwargs=kwargs)

    def stop212(self, **kwargs):
        return self.call('stop212', kwargs=kwargs)

    def pumprate22(self, **kwargs):
        return self.call('pumprate22', kwargs=kwargs)

    def close41(self, **kwargs):
        return self.call('close41', kwargs=kwargs)

    def onclosedialog41_confirm(self, **kwargs):
        return self.call('onclosedialog41_confirm', kwargs=kwargs)

    def m2_check_spin3x(self, **kwargs):
        return self.call('m2_check_spin3x', kwargs=kwargs)

    def m2_getvalues_spin3x(self, **kwargs):
        return self.call('m2_getvalues_spin3x', kwargs=kwargs)

    def m2_runprog351(self, **kwargs):
        return self.call('m2_runprog351', kwargs=kwargs)

    def m2_stopprog352(self, **kwargs):
        return self.call('m2_stopprog352', kwargs=kwargs)

    def deactivate(self, **kwargs):
        return self.call('deactivate', kwargs=kwargs)

    def activate(self, **kwargs):
        return self.call('activate', kwargs=kwargs)

    def start_pump(self, **kwargs):
        return self.call('start_pump', kwargs=kwargs)

    def stop_pump(self, **kwargs):
        return self.call('stop_pump', kwargs=kwargs)

    def updatepumprate(self, **kwargs):
        return self.call('updatepumprate', kwargs=kwargs)

    def m2_activate151(self, **kwargs):
        return self.call('m2_activate151', kwargs=kwargs)

    def m2_deactivate152(self, **kwargs):
        return self.call('m2_deactivate152', kwargs=kwargs)

    def m2_euha_posA_211(self, **kwargs):
        return self.call('m2_euha_posA_211', kwargs=kwargs)

    def m2_euha_posB_212(self, **kwargs):
        return self.call('m2_euha_posB_212', kwargs=kwargs)

    def euha_deactivate(self, **kwargs):
        return self.call('euha_deactivate', kwargs=kwargs)

    def euha_activate(self, **kwargs):
        return self.call('euha_activate', kwargs=kwargs)

    def euha_posA(self, **kwargs):
        return self.call('euha_posA', kwargs=kwargs)

    def euha_posB(self, **kwargs):
        return self.call('euha_posB', kwargs=kwargs)

