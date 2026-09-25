from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentEldexOptos(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/Waldvogel-Group__LABS-Backend', 'source_file': 'backend/setup/setup.py', 'class_name': 'Setup', 'import_roots': [], 'candidate_methods': ['current_experiment', 'current_experiment_index', 'remote_start', 'remote_stop', 'remote_pause', 'remote_shutdown', 'remote_insert_experiment_after', 'remote_add_experiment', 'remote_station_overview', 'remote_get_experiment_types', 'remote_station_run_tables', 'remote_get_updates', 'remote_station_components', 'get_device_or_channel', 'insert_experiment_after', 'add_experiment', 'start', 'execute_experiment', 'update', 'set_state', 'state', 'stateobject', 'subscribe', 'unsubscribe', 'reset_observables', 'update_subscribers', 'update_observables', 'get_updates', 'get_latest_update'], 'action_targets': {}, 'metadata': {'repo': 'Waldvogel-Group/LABS-Backend', 'repo_url': 'https://github.com/Waldvogel-Group/LABS-Backend', 'brand': 'Eldex', 'model': 'Optos', 'device_type_cn': '反应釜', 'device_type_en': 'Reactor Vessel', 'source_framework': 'LABS-Backend', 'tag_id': '4375', 'tag_name': '反应釜', 'tag_name_en': 'Reactor Vessel', 'candidate_score': 190, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def current_experiment(self, **kwargs):
        return self.call('current_experiment', kwargs=kwargs)

    def current_experiment_index(self, **kwargs):
        return self.call('current_experiment_index', kwargs=kwargs)

    def remote_start(self, **kwargs):
        return self.call('remote_start', kwargs=kwargs)

    def remote_stop(self, **kwargs):
        return self.call('remote_stop', kwargs=kwargs)

    def remote_pause(self, **kwargs):
        return self.call('remote_pause', kwargs=kwargs)

    def remote_shutdown(self, **kwargs):
        return self.call('remote_shutdown', kwargs=kwargs)

    def remote_insert_experiment_after(self, **kwargs):
        return self.call('remote_insert_experiment_after', kwargs=kwargs)

    def remote_add_experiment(self, **kwargs):
        return self.call('remote_add_experiment', kwargs=kwargs)

    def remote_station_overview(self, **kwargs):
        return self.call('remote_station_overview', kwargs=kwargs)

    def remote_get_experiment_types(self, **kwargs):
        return self.call('remote_get_experiment_types', kwargs=kwargs)

    def remote_station_run_tables(self, **kwargs):
        return self.call('remote_station_run_tables', kwargs=kwargs)

    def remote_get_updates(self, **kwargs):
        return self.call('remote_get_updates', kwargs=kwargs)

    def remote_station_components(self, **kwargs):
        return self.call('remote_station_components', kwargs=kwargs)

    def get_device_or_channel(self, **kwargs):
        return self.call('get_device_or_channel', kwargs=kwargs)

    def insert_experiment_after(self, **kwargs):
        return self.call('insert_experiment_after', kwargs=kwargs)

    def add_experiment(self, **kwargs):
        return self.call('add_experiment', kwargs=kwargs)

    def start(self, **kwargs):
        return self.call('start', kwargs=kwargs)

    def execute_experiment(self, **kwargs):
        return self.call('execute_experiment', kwargs=kwargs)

    def update(self, **kwargs):
        return self.call('update', kwargs=kwargs)

    def set_state(self, **kwargs):
        return self.call('set_state', kwargs=kwargs)

    def state(self, **kwargs):
        return self.call('state', kwargs=kwargs)

    def stateobject(self, **kwargs):
        return self.call('stateobject', kwargs=kwargs)

    def subscribe(self, **kwargs):
        return self.call('subscribe', kwargs=kwargs)

    def unsubscribe(self, **kwargs):
        return self.call('unsubscribe', kwargs=kwargs)

    def reset_observables(self, **kwargs):
        return self.call('reset_observables', kwargs=kwargs)

    def update_subscribers(self, **kwargs):
        return self.call('update_subscribers', kwargs=kwargs)

    def update_observables(self, **kwargs):
        return self.call('update_observables', kwargs=kwargs)

    def get_updates(self, **kwargs):
        return self.call('get_updates', kwargs=kwargs)

    def get_latest_update(self, **kwargs):
        return self.call('get_latest_update', kwargs=kwargs)

