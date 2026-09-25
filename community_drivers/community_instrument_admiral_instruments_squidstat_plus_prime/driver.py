from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAdmiralInstrumentsSquidstatPlusPrime(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/Admiral-Instruments__AdmiralSquidstatAPI', 'source_file': 'SquidstatLibrary/examples/Python/writeInCsv.py', 'class_name': 'SerialPortReader', 'import_roots': [], 'candidate_methods': ['run', 'writeData', 'closePort'], 'action_targets': {}, 'metadata': {'repo': 'Admiral-Instruments/AdmiralSquidstatAPI', 'repo_url': 'https://github.com/Admiral-Instruments/AdmiralSquidstatAPI', 'brand': 'Admiral Instruments', 'model': 'Squidstat Plus/Prime', 'device_type_cn': '电化学工作站', 'device_type_en': 'Electrochemical Workstation', 'source_framework': '官方SDK', 'tag_id': '4425', 'tag_name': '电化学工作站', 'tag_name_en': 'Electrochemical Workstation', 'candidate_score': 22, 'parse_status': 'ok', 'quality_status': 'thin', 'quality_reasons': ['test_or_example_path'], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def run(self, **kwargs):
        return self.call('run', kwargs=kwargs)

    def writeData(self, **kwargs):
        return self.call('writeData', kwargs=kwargs)

    def closePort(self, **kwargs):
        return self.call('closePort', kwargs=kwargs)

