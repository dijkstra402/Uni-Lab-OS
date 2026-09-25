from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubAndrewgyorkTools(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/AndrewGYork_tools', 'source_file': 'physik_instrumente.py', 'class_name': 'E753_Z_Piezo', 'import_roots': [], 'candidate_methods': ['send', 'get_real_position', 'get_target_position', 'move', 'set_closed_loop', 'set_analog_control_state', 'record_analog_movement', 'retrieve_data_log', 'stop', 'close'], 'metadata': {'repo': 'andrewgyork/tools', 'repo_url': 'https://github.com/AndrewGYork/tools', 'unit_id': 'gh_pco_pco_edge_4_2', 'source_file': 'physik_instrumente.py', 'candidate_score': 107, 'manufacturer': 'PCO', 'model_name': 'PCO pco.edge 4.2/5.5'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def send(self, **kwargs):
        return self.call('send', kwargs=kwargs)

    def get_real_position(self, **kwargs):
        return self.call('get_real_position', kwargs=kwargs)

    def get_target_position(self, **kwargs):
        return self.call('get_target_position', kwargs=kwargs)

    def move(self, **kwargs):
        return self.call('move', kwargs=kwargs)

    def set_closed_loop(self, **kwargs):
        return self.call('set_closed_loop', kwargs=kwargs)

    def set_analog_control_state(self, **kwargs):
        return self.call('set_analog_control_state', kwargs=kwargs)

    def record_analog_movement(self, **kwargs):
        return self.call('record_analog_movement', kwargs=kwargs)

    def retrieve_data_log(self, **kwargs):
        return self.call('retrieve_data_log', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

