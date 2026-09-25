from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentVapourtecR2R4Flowcontrol(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/devoncallan__flowcontrol', 'source_file': 'new_code/flow.py', 'class_name': 'R2Interface', 'import_roots': [], 'candidate_methods': ['Start', 'stop_experiment', 'switch_valve', 'set_temp', 'SetFlowRate', 'send_command', 'initiate_comms271'], 'action_targets': {}, 'metadata': {'repo': 'devoncallan/flowcontrol', 'repo_url': 'https://github.com/devoncallan/flowcontrol', 'brand': 'Vapourtec', 'model': 'R2/R4 (flowcontrol)', 'device_type_cn': '反应釜', 'device_type_en': 'Flow Reactor', 'source_framework': '独立驱动', 'tag_id': '4375', 'tag_name': '反应釜', 'tag_name_en': 'Reactor Vessel', 'candidate_score': 94, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def Start(self, **kwargs):
        return self.call('Start', kwargs=kwargs)

    def stop_experiment(self, **kwargs):
        return self.call('stop_experiment', kwargs=kwargs)

    def switch_valve(self, **kwargs):
        return self.call('switch_valve', kwargs=kwargs)

    def set_temp(self, **kwargs):
        return self.call('set_temp', kwargs=kwargs)

    def SetFlowRate(self, **kwargs):
        return self.call('SetFlowRate', kwargs=kwargs)

    def send_command(self, **kwargs):
        return self.call('send_command', kwargs=kwargs)

    def initiate_comms271(self, **kwargs):
        return self.call('initiate_comms271', kwargs=kwargs)

