from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentChInstrumentsChi760e(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/jrlLAB__hardpotato', 'source_file': 'src/hardpotato/pico_instrument.py', 'class_name': 'Instrument', 'import_roots': ['src'], 'candidate_methods': ['write', 'writelines', 'readline', 'readlines_until_end', 'get_firmware_version', 'get_device_type', 'get_mscript_version', 'get_serial_number', 'get_register', 'load_mscript_from_flash', 'run_mscript_from_flash', 'send_script', 'abort_and_sync'], 'action_targets': {}, 'metadata': {'repo': 'jrlLAB/hardpotato', 'repo_url': 'https://github.com/jrlLAB/hardpotato', 'brand': 'CH Instruments', 'model': 'CHI760E', 'device_type_cn': '恒电位仪', 'device_type_en': 'Potentiostat', 'source_framework': '电化学/热分析/天平', 'tag_id': '4425', 'tag_name': '电化学工作站', 'tag_name_en': 'Electrochemical Workstation', 'candidate_score': 150, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def write(self, **kwargs):
        return self.call('write', kwargs=kwargs)

    def writelines(self, **kwargs):
        return self.call('writelines', kwargs=kwargs)

    def readline(self, **kwargs):
        return self.call('readline', kwargs=kwargs)

    def readlines_until_end(self, **kwargs):
        return self.call('readlines_until_end', kwargs=kwargs)

    def get_firmware_version(self, **kwargs):
        return self.call('get_firmware_version', kwargs=kwargs)

    def get_device_type(self, **kwargs):
        return self.call('get_device_type', kwargs=kwargs)

    def get_mscript_version(self, **kwargs):
        return self.call('get_mscript_version', kwargs=kwargs)

    def get_serial_number(self, **kwargs):
        return self.call('get_serial_number', kwargs=kwargs)

    def get_register(self, **kwargs):
        return self.call('get_register', kwargs=kwargs)

    def load_mscript_from_flash(self, **kwargs):
        return self.call('load_mscript_from_flash', kwargs=kwargs)

    def run_mscript_from_flash(self, **kwargs):
        return self.call('run_mscript_from_flash', kwargs=kwargs)

    def send_script(self, **kwargs):
        return self.call('send_script', kwargs=kwargs)

    def abort_and_sync(self, **kwargs):
        return self.call('abort_and_sync', kwargs=kwargs)

