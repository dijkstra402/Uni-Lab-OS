from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentParkerGv6(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/parker/parkerGV6.py', 'class_name': 'ParkerGV6', 'import_roots': [], 'candidate_methods': ['read', 'set_defaults', 'reset', 'enable', 'disable', 'status', 'is_moving', 'angle', 'angle', 'angle_error', 'position', 'position', 'position_error', 'move', 'stop', 'kill', 'use_absolute_position', 'use_relative_position', 'set_hardware_limits', 'set_software_limits'], 'metadata': {'source_file': 'pymeasure/instruments/parker/parkerGV6.py', 'class_name': 'ParkerGV6', 'candidate_score': 0.947, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def read(self, **kwargs):
            return self.call('read', kwargs=kwargs)

        def set_defaults(self, **kwargs):
            return self.call('set_defaults', kwargs=kwargs)

        def reset(self, **kwargs):
            return self.call('reset', kwargs=kwargs)

        def enable(self, **kwargs):
            return self.call('enable', kwargs=kwargs)

        def disable(self, **kwargs):
            return self.call('disable', kwargs=kwargs)

        def status(self, **kwargs):
            return self.call('status', kwargs=kwargs)

        def is_moving(self, **kwargs):
            return self.call('is_moving', kwargs=kwargs)

        def angle(self, **kwargs):
            return self.call('angle', kwargs=kwargs)

        def angle(self, **kwargs):
            return self.call('angle', kwargs=kwargs)

        def angle_error(self, **kwargs):
            return self.call('angle_error', kwargs=kwargs)

        def position(self, **kwargs):
            return self.call('position', kwargs=kwargs)

        def position(self, **kwargs):
            return self.call('position', kwargs=kwargs)

        def position_error(self, **kwargs):
            return self.call('position_error', kwargs=kwargs)

        def move(self, **kwargs):
            return self.call('move', kwargs=kwargs)

        def stop(self, **kwargs):
            return self.call('stop', kwargs=kwargs)

        def kill(self, **kwargs):
            return self.call('kill', kwargs=kwargs)

        def use_absolute_position(self, **kwargs):
            return self.call('use_absolute_position', kwargs=kwargs)

        def use_relative_position(self, **kwargs):
            return self.call('use_relative_position', kwargs=kwargs)

        def set_hardware_limits(self, **kwargs):
            return self.call('set_hardware_limits', kwargs=kwargs)

        def set_software_limits(self, **kwargs):
            return self.call('set_software_limits', kwargs=kwargs)

