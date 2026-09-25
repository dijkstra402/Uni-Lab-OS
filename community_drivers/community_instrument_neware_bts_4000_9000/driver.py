from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentNewareBts40009000(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/EmpaEconversion__aurora-neware', 'source_file': 'aurora_neware/neware.py', 'class_name': 'NewareAPI', 'import_roots': [], 'candidate_methods': ['connect', 'disconnect', 'get_pipeline', 'command', 'start', 'stop', 'getchlstatus', 'inquire', 'inquiredf', 'downloadlog', 'download', 'getdevinfo', 'light', 'clearflag', 'get_steps', 'get_testid'], 'action_targets': {}, 'metadata': {'repo': 'EmpaEconversion/aurora-neware', 'repo_url': 'https://github.com/EmpaEconversion/aurora-neware', 'brand': 'Neware', 'model': 'BTS 4000/9000', 'device_type_cn': '电池测试柜', 'device_type_en': 'Battery Cycler', 'source_framework': 'aurora-neware', 'tag_id': '4427', 'tag_name': '电池测试柜', 'tag_name_en': 'Battery Test Cabinet', 'candidate_score': 186, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def connect(self, **kwargs):
        return self.call('connect', kwargs=kwargs)

    def disconnect(self, **kwargs):
        return self.call('disconnect', kwargs=kwargs)

    def get_pipeline(self, **kwargs):
        return self.call('get_pipeline', kwargs=kwargs)

    def command(self, **kwargs):
        return self.call('command', kwargs=kwargs)

    def start(self, **kwargs):
        return self.call('start', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

    def getchlstatus(self, **kwargs):
        return self.call('getchlstatus', kwargs=kwargs)

    def inquire(self, **kwargs):
        return self.call('inquire', kwargs=kwargs)

    def inquiredf(self, **kwargs):
        return self.call('inquiredf', kwargs=kwargs)

    def downloadlog(self, **kwargs):
        return self.call('downloadlog', kwargs=kwargs)

    def download(self, **kwargs):
        return self.call('download', kwargs=kwargs)

    def getdevinfo(self, **kwargs):
        return self.call('getdevinfo', kwargs=kwargs)

    def light(self, **kwargs):
        return self.call('light', kwargs=kwargs)

    def clearflag(self, **kwargs):
        return self.call('clearflag', kwargs=kwargs)

    def get_steps(self, **kwargs):
        return self.call('get_steps', kwargs=kwargs)

    def get_testid(self, **kwargs):
        return self.call('get_testid', kwargs=kwargs)

