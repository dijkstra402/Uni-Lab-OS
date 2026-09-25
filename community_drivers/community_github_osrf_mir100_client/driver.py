from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubOsrfMir100Client(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/osrf_mir100-client', 'source_file': 'mir100_client/models/get_wifi_connection.py', 'class_name': 'GetWifiConnection', 'import_roots': [], 'candidate_methods': ['bssid', 'bssid', 'connected', 'connected', 'device', 'device', 'dns', 'dns', 'ip_address', 'ip_address', 'last_connected', 'last_connected', 'mac', 'mac', 'name', 'name', 'netmask', 'netmask', 'security', 'security'], 'metadata': {'repo': 'osrf/mir100-client', 'repo_url': 'https://github.com/osrf/mir100-client', 'unit_id': 'gh_mobile_industrial_robots_mir100', 'source_file': 'mir100_client/models/get_wifi_connection.py', 'candidate_score': 94, 'manufacturer': 'Mobile Industrial Robots', 'model_name': 'Mobile Industrial Robots MiR100'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def bssid(self, **kwargs):
        return self.call('bssid', kwargs=kwargs)

    def bssid(self, **kwargs):
        return self.call('bssid', kwargs=kwargs)

    def connected(self, **kwargs):
        return self.call('connected', kwargs=kwargs)

    def connected(self, **kwargs):
        return self.call('connected', kwargs=kwargs)

    def device(self, **kwargs):
        return self.call('device', kwargs=kwargs)

    def device(self, **kwargs):
        return self.call('device', kwargs=kwargs)

    def dns(self, **kwargs):
        return self.call('dns', kwargs=kwargs)

    def dns(self, **kwargs):
        return self.call('dns', kwargs=kwargs)

    def ip_address(self, **kwargs):
        return self.call('ip_address', kwargs=kwargs)

    def ip_address(self, **kwargs):
        return self.call('ip_address', kwargs=kwargs)

    def last_connected(self, **kwargs):
        return self.call('last_connected', kwargs=kwargs)

    def last_connected(self, **kwargs):
        return self.call('last_connected', kwargs=kwargs)

    def mac(self, **kwargs):
        return self.call('mac', kwargs=kwargs)

    def mac(self, **kwargs):
        return self.call('mac', kwargs=kwargs)

    def name(self, **kwargs):
        return self.call('name', kwargs=kwargs)

    def name(self, **kwargs):
        return self.call('name', kwargs=kwargs)

    def netmask(self, **kwargs):
        return self.call('netmask', kwargs=kwargs)

    def netmask(self, **kwargs):
        return self.call('netmask', kwargs=kwargs)

    def security(self, **kwargs):
        return self.call('security', kwargs=kwargs)

    def security(self, **kwargs):
        return self.call('security', kwargs=kwargs)

