from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubSfTecPyvium(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/SF-Tec_pyvium', 'source_file': 'pyvium/core/generic_functions.py', 'class_name': 'GenericFunctions', 'import_roots': [], 'candidate_methods': ['IV_open', 'IV_close', 'IV_MaxDevices', 'IV_selectdevice', 'IV_getdevicestatus', 'IV_readSN', 'IV_connect', 'IV_VersionHost', 'IV_VersionDll', 'IV_VersionCheck', 'IV_HostHandle', 'IV_VersionDllFile', 'IV_VersionDllFileStr', 'IV_SelectChannel', 'IV_SelectSn', 'IV_getDbFileName'], 'metadata': {'repo': 'sf-tec/pyvium', 'repo_url': 'https://github.com/SF-Tec/pyvium', 'unit_id': 'gh_ivium_compactstat', 'source_file': 'pyvium/core/generic_functions.py', 'candidate_score': 60, 'manufacturer': 'Ivium', 'model_name': 'Ivium CompactStat'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def IV_open(self, **kwargs):
        return self.call('IV_open', kwargs=kwargs)

    def IV_close(self, **kwargs):
        return self.call('IV_close', kwargs=kwargs)

    def IV_MaxDevices(self, **kwargs):
        return self.call('IV_MaxDevices', kwargs=kwargs)

    def IV_selectdevice(self, **kwargs):
        return self.call('IV_selectdevice', kwargs=kwargs)

    def IV_getdevicestatus(self, **kwargs):
        return self.call('IV_getdevicestatus', kwargs=kwargs)

    def IV_readSN(self, **kwargs):
        return self.call('IV_readSN', kwargs=kwargs)

    def IV_connect(self, **kwargs):
        return self.call('IV_connect', kwargs=kwargs)

    def IV_VersionHost(self, **kwargs):
        return self.call('IV_VersionHost', kwargs=kwargs)

    def IV_VersionDll(self, **kwargs):
        return self.call('IV_VersionDll', kwargs=kwargs)

    def IV_VersionCheck(self, **kwargs):
        return self.call('IV_VersionCheck', kwargs=kwargs)

    def IV_HostHandle(self, **kwargs):
        return self.call('IV_HostHandle', kwargs=kwargs)

    def IV_VersionDllFile(self, **kwargs):
        return self.call('IV_VersionDllFile', kwargs=kwargs)

    def IV_VersionDllFileStr(self, **kwargs):
        return self.call('IV_VersionDllFileStr', kwargs=kwargs)

    def IV_SelectChannel(self, **kwargs):
        return self.call('IV_SelectChannel', kwargs=kwargs)

    def IV_SelectSn(self, **kwargs):
        return self.call('IV_SelectSn', kwargs=kwargs)

    def IV_getDbFileName(self, **kwargs):
        return self.call('IV_getDbFileName', kwargs=kwargs)

