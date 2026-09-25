from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentMobileIndustrialRobotsMir100200250(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/DFKI-NI__mir_robot', 'source_file': 'mir_driver/src/mir_driver/rosbridge.py', 'class_name': 'RosbridgeSetup', 'import_roots': [], 'candidate_methods': ['publish', 'subscribe', 'unhook', 'unsubscribe', 'callService', 'send', 'generate_id', 'addServiceCallback', 'addCallback', 'is_connected', 'is_errored', 'onMessageReceived'], 'action_targets': {}, 'metadata': {'repo': 'DFKI-NI/mir_robot', 'repo_url': 'https://github.com/DFKI-NI/mir_robot', 'brand': 'Mobile Industrial Robots', 'model': 'MiR100/200/250', 'device_type_cn': 'AGV自动导引车', 'device_type_en': 'AGV', 'source_framework': 'ROS', 'tag_id': '4360', 'tag_name': 'AGV', 'tag_name_en': 'AGV', 'candidate_score': 154, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def publish(self, **kwargs):
        return self.call('publish', kwargs=kwargs)

    def subscribe(self, **kwargs):
        return self.call('subscribe', kwargs=kwargs)

    def unhook(self, **kwargs):
        return self.call('unhook', kwargs=kwargs)

    def unsubscribe(self, **kwargs):
        return self.call('unsubscribe', kwargs=kwargs)

    def callService(self, **kwargs):
        return self.call('callService', kwargs=kwargs)

    def send(self, **kwargs):
        return self.call('send', kwargs=kwargs)

    def generate_id(self, **kwargs):
        return self.call('generate_id', kwargs=kwargs)

    def addServiceCallback(self, **kwargs):
        return self.call('addServiceCallback', kwargs=kwargs)

    def addCallback(self, **kwargs):
        return self.call('addCallback', kwargs=kwargs)

    def is_connected(self, **kwargs):
        return self.call('is_connected', kwargs=kwargs)

    def is_errored(self, **kwargs):
        return self.call('is_errored', kwargs=kwargs)

    def onMessageReceived(self, **kwargs):
        return self.call('onMessageReceived', kwargs=kwargs)

