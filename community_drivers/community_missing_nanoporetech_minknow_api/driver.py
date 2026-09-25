from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityMissingNanoporetechMinknowApi(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/nanoporetech__minknow_api', 'source_file': 'python/minknow_api/protocol_service.py', 'class_name': 'ProtocolService', 'import_roots': ['python'], 'candidate_methods': ['start_protocol', 'stop_protocol', 'pause_protocol', 'resume_protocol', 'get_run_info', 'list_protocol_runs', 'get_current_protocol_run', 'list_protocols', 'begin_protocol'], 'metadata': {'repo': 'nanoporetech/minknow_api', 'repo_url': 'https://github.com/nanoporetech/minknow_api', 'source_file': 'python/minknow_api/__init__.py', 'candidate_score': 54, 'candidate_reason': '', 'manufacturers': ['Oxford Nanopore Technologies'], 'models': ['MinION Mk1B, MinION Mk1D, GridION, PromethION P24, PromethION P2 Solo, PromethION P2 Integrated'], 'tags': ['DNA测序仪'], 'notes': ['官方API-控制测序运行/数据采集/设备监控'], 'comm_protocols': ['gRPC protobuf'], 'review_status': 'good', 'review_notes': ['改选 ProtocolService，覆盖 MinKNOW 测序协议核心控制接口。']}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def start_protocol(self, **kwargs):
        return self.call('start_protocol', kwargs=kwargs)

    def stop_protocol(self, **kwargs):
        return self.call('stop_protocol', kwargs=kwargs)

    def pause_protocol(self, **kwargs):
        return self.call('pause_protocol', kwargs=kwargs)

    def resume_protocol(self, **kwargs):
        return self.call('resume_protocol', kwargs=kwargs)

    def get_run_info(self, **kwargs):
        return self.call('get_run_info', kwargs=kwargs)

    def list_protocol_runs(self, **kwargs):
        return self.call('list_protocol_runs', kwargs=kwargs)

    def get_current_protocol_run(self, **kwargs):
        return self.call('get_current_protocol_run', kwargs=kwargs)

    def list_protocols(self, **kwargs):
        return self.call('list_protocols', kwargs=kwargs)

    def begin_protocol(self, **kwargs):
        return self.call('begin_protocol', kwargs=kwargs)

