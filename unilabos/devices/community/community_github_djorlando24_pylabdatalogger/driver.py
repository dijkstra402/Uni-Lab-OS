from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubDjorlando24Pylabdatalogger(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/djorlando24_pyLabDataLogger', 'source_file': 'src/device/pyvisaDevice.py', 'class_name': 'pyvisaDevice', 'import_roots': [], 'candidate_methods': ['scan', 'activate', 'deactivate', 'apply_config', 'update_config', 'updateTimestamp', 'reset', 'scope_channel_params', 'instrumentQuery', 'instrumentWrite', 'configure_device', 'convert_to_array', 'get_values', 'query'], 'metadata': {'repo': 'djorlando24/pylabdatalogger', 'repo_url': 'https://github.com/djorlando24/pyLabDataLogger', 'unit_id': 'gh_ad_g', 'source_file': 'src/device/pyvisaDevice.py', 'candidate_score': 220, 'manufacturer': 'A&D', 'model_name': 'A&D G系列'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def scan(self, **kwargs):
        return self.call('scan', kwargs=kwargs)

    def activate(self, **kwargs):
        return self.call('activate', kwargs=kwargs)

    def deactivate(self, **kwargs):
        return self.call('deactivate', kwargs=kwargs)

    def apply_config(self, **kwargs):
        return self.call('apply_config', kwargs=kwargs)

    def update_config(self, **kwargs):
        return self.call('update_config', kwargs=kwargs)

    def updateTimestamp(self, **kwargs):
        return self.call('updateTimestamp', kwargs=kwargs)

    def reset(self, **kwargs):
        return self.call('reset', kwargs=kwargs)

    def scope_channel_params(self, **kwargs):
        return self.call('scope_channel_params', kwargs=kwargs)

    def instrumentQuery(self, **kwargs):
        return self.call('instrumentQuery', kwargs=kwargs)

    def instrumentWrite(self, **kwargs):
        return self.call('instrumentWrite', kwargs=kwargs)

    def configure_device(self, **kwargs):
        return self.call('configure_device', kwargs=kwargs)

    def convert_to_array(self, **kwargs):
        return self.call('convert_to_array', kwargs=kwargs)

    def get_values(self, **kwargs):
        return self.call('get_values', kwargs=kwargs)

    def query(self, **kwargs):
        return self.call('query', kwargs=kwargs)

