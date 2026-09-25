from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentBrukerFourier80Benchtop(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/croningp__analyticallabware', 'source_file': 'AnalyticalLabware/devices/Magritek/Spinsolve/spinsolve.py', 'class_name': 'SpinsolveNMR', 'import_roots': [], 'candidate_methods': ['check_last_shimming', 'connect', 'disconnect', 'send_message', 'receive_reply', 'initialise', 'is_instrument_ready', 'load_commands', 'shim', 'shim_on_sample', 'set_user_folder', 'user_data', 'solvent', 'sample', 'get_duration', 'proton', 'proton_extended', 'carbon', 'carbon_extended', 'fluorine', 'fluorine_extended', 'wait_until_ready', 'calibrate', 'protocols_list', 'get_spectrum'], 'action_targets': {}, 'metadata': {'repo': 'croningp/analyticallabware', 'repo_url': 'https://github.com/croningp/analyticallabware', 'brand': 'Bruker', 'model': 'Fourier 80 (Benchtop)', 'device_type_cn': '台式核磁共振仪', 'device_type_en': 'Benchtop NMR', 'source_framework': 'AnalyticalLabware', 'tag_id': '4404', 'tag_name': '核磁共振波谱仪', 'tag_name_en': 'NMR Spectrometer', 'candidate_score': 250, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def check_last_shimming(self, **kwargs):
        return self.call('check_last_shimming', kwargs=kwargs)

    def connect(self, **kwargs):
        return self.call('connect', kwargs=kwargs)

    def disconnect(self, **kwargs):
        return self.call('disconnect', kwargs=kwargs)

    def send_message(self, **kwargs):
        return self.call('send_message', kwargs=kwargs)

    def receive_reply(self, **kwargs):
        return self.call('receive_reply', kwargs=kwargs)

    def initialise(self, **kwargs):
        return self.call('initialise', kwargs=kwargs)

    def is_instrument_ready(self, **kwargs):
        return self.call('is_instrument_ready', kwargs=kwargs)

    def load_commands(self, **kwargs):
        return self.call('load_commands', kwargs=kwargs)

    def shim(self, **kwargs):
        return self.call('shim', kwargs=kwargs)

    def shim_on_sample(self, **kwargs):
        return self.call('shim_on_sample', kwargs=kwargs)

    def set_user_folder(self, **kwargs):
        return self.call('set_user_folder', kwargs=kwargs)

    def user_data(self, **kwargs):
        return self.call('user_data', kwargs=kwargs)

    def solvent(self, **kwargs):
        return self.call('solvent', kwargs=kwargs)

    def sample(self, **kwargs):
        return self.call('sample', kwargs=kwargs)

    def get_duration(self, **kwargs):
        return self.call('get_duration', kwargs=kwargs)

    def proton(self, **kwargs):
        return self.call('proton', kwargs=kwargs)

    def proton_extended(self, **kwargs):
        return self.call('proton_extended', kwargs=kwargs)

    def carbon(self, **kwargs):
        return self.call('carbon', kwargs=kwargs)

    def carbon_extended(self, **kwargs):
        return self.call('carbon_extended', kwargs=kwargs)

    def fluorine(self, **kwargs):
        return self.call('fluorine', kwargs=kwargs)

    def fluorine_extended(self, **kwargs):
        return self.call('fluorine_extended', kwargs=kwargs)

    def wait_until_ready(self, **kwargs):
        return self.call('wait_until_ready', kwargs=kwargs)

    def calibrate(self, **kwargs):
        return self.call('calibrate', kwargs=kwargs)

    def protocols_list(self, **kwargs):
        return self.call('protocols_list', kwargs=kwargs)

    def get_spectrum(self, **kwargs):
        return self.call('get_spectrum', kwargs=kwargs)

