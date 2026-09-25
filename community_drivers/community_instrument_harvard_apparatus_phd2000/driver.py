from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentHarvardApparatusPhd2000(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/tomwphillips__pumpy', 'source_file': 'pumpy.py', 'class_name': 'Pump', 'import_roots': [], 'candidate_methods': ['write', 'read', 'setdiameter', 'setflowrate', 'infuse', 'withdraw', 'stop', 'settargetvolume', 'waituntiltarget'], 'action_targets': {}, 'metadata': {'repo': 'tomwphillips/pumpy', 'repo_url': 'https://github.com/tomwphillips/pumpy', 'brand': 'Harvard Apparatus', 'model': 'PHD2000', 'device_type_cn': '注射泵', 'device_type_en': 'Syringe Pump', 'source_framework': 'pumpy', 'tag_id': '4413', 'tag_name': '注射泵', 'tag_name_en': 'Syringe Pump', 'candidate_score': 138, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def write(self, **kwargs):
        return self.call('write', kwargs=kwargs)

    def read(self, **kwargs):
        return self.call('read', kwargs=kwargs)

    def setdiameter(self, **kwargs):
        return self.call('setdiameter', kwargs=kwargs)

    def setflowrate(self, **kwargs):
        return self.call('setflowrate', kwargs=kwargs)

    def infuse(self, **kwargs):
        return self.call('infuse', kwargs=kwargs)

    def withdraw(self, **kwargs):
        return self.call('withdraw', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

    def settargetvolume(self, **kwargs):
        return self.call('settargetvolume', kwargs=kwargs)

    def waituntiltarget(self, **kwargs):
        return self.call('waituntiltarget', kwargs=kwargs)

