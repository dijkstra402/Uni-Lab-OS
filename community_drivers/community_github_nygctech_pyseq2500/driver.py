from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubNygctechPyseq2500(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/nygctech_PySeq2500', 'source_file': 'pyseq/__init__.py', 'class_name': 'HiSeq', 'import_roots': [], 'candidate_methods': ['check_COM', 'initializeCams', 'initializeInstruments', 'write_metadata', 'take_picture', 'obj_stack', 'reset_stage', 'move_stage_out', 'move_inlet', 'expose', 'autofocus', 'autolevel', 'zstack', 'scan', 'twoscan', 'position', 'px_to_step', 'optimize_filter', 'message'], 'metadata': {'repo': 'nygctech/pyseq2500', 'repo_url': 'https://github.com/nygctech/PySeq2500', 'unit_id': 'gh_illumina_hiseq_2500', 'source_file': 'pyseq/__init__.py', 'candidate_score': 87, 'manufacturer': 'Illumina', 'model_name': 'Illumina HiSeq 2500'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def check_COM(self, **kwargs):
        return self.call('check_COM', kwargs=kwargs)

    def initializeCams(self, **kwargs):
        return self.call('initializeCams', kwargs=kwargs)

    def initializeInstruments(self, **kwargs):
        return self.call('initializeInstruments', kwargs=kwargs)

    def write_metadata(self, **kwargs):
        return self.call('write_metadata', kwargs=kwargs)

    def take_picture(self, **kwargs):
        return self.call('take_picture', kwargs=kwargs)

    def obj_stack(self, **kwargs):
        return self.call('obj_stack', kwargs=kwargs)

    def reset_stage(self, **kwargs):
        return self.call('reset_stage', kwargs=kwargs)

    def move_stage_out(self, **kwargs):
        return self.call('move_stage_out', kwargs=kwargs)

    def move_inlet(self, **kwargs):
        return self.call('move_inlet', kwargs=kwargs)

    def expose(self, **kwargs):
        return self.call('expose', kwargs=kwargs)

    def autofocus(self, **kwargs):
        return self.call('autofocus', kwargs=kwargs)

    def autolevel(self, **kwargs):
        return self.call('autolevel', kwargs=kwargs)

    def zstack(self, **kwargs):
        return self.call('zstack', kwargs=kwargs)

    def scan(self, **kwargs):
        return self.call('scan', kwargs=kwargs)

    def twoscan(self, **kwargs):
        return self.call('twoscan', kwargs=kwargs)

    def position(self, **kwargs):
        return self.call('position', kwargs=kwargs)

    def px_to_step(self, **kwargs):
        return self.call('px_to_step', kwargs=kwargs)

    def optimize_filter(self, **kwargs):
        return self.call('optimize_filter', kwargs=kwargs)

    def message(self, **kwargs):
        return self.call('message', kwargs=kwargs)

