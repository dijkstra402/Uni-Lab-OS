from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentTeledyneIsco260d(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/octopode__spectackler', 'source_file': 'isco260D.py', 'class_name': 'ISCOController', 'import_roots': [], 'candidate_methods': ['disconnect', 'rcvd_ok', 'read_vals', 'flush', 'remote', 'local', 'run', 'stop', 'clear', 'digital', 'mode', 'mode_const_press', 'mode_const_flow', 'mode_prgm_grad', 'zero', 'maxflow', 'minflow', 'maxpress', 'minpress', 'press_set', 'integral_enable', 'integral_disable', 'units', 'gg', 'identify', 'status', 'press_get', 'flow_get', 'vol_get', 'pause', 'tune_maxflow', 'const_press_alarm'], 'action_targets': {}, 'metadata': {'repo': 'octopode/spectackler', 'repo_url': 'https://github.com/octopode/spectackler', 'brand': 'Teledyne Isco', 'model': '260D', 'device_type_cn': '高压注射泵', 'device_type_en': 'High Pressure Syringe Pump', 'source_framework': '泵阀/液体处理', 'tag_id': '4413', 'tag_name': '注射泵', 'tag_name_en': 'Syringe Pump', 'candidate_score': 322, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def disconnect(self, **kwargs):
        return self.call('disconnect', kwargs=kwargs)

    def rcvd_ok(self, **kwargs):
        return self.call('rcvd_ok', kwargs=kwargs)

    def read_vals(self, **kwargs):
        return self.call('read_vals', kwargs=kwargs)

    def flush(self, **kwargs):
        return self.call('flush', kwargs=kwargs)

    def remote(self, **kwargs):
        return self.call('remote', kwargs=kwargs)

    def local(self, **kwargs):
        return self.call('local', kwargs=kwargs)

    def run(self, **kwargs):
        return self.call('run', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

    def clear(self, **kwargs):
        return self.call('clear', kwargs=kwargs)

    def digital(self, **kwargs):
        return self.call('digital', kwargs=kwargs)

    def mode(self, **kwargs):
        return self.call('mode', kwargs=kwargs)

    def mode_const_press(self, **kwargs):
        return self.call('mode_const_press', kwargs=kwargs)

    def mode_const_flow(self, **kwargs):
        return self.call('mode_const_flow', kwargs=kwargs)

    def mode_prgm_grad(self, **kwargs):
        return self.call('mode_prgm_grad', kwargs=kwargs)

    def zero(self, **kwargs):
        return self.call('zero', kwargs=kwargs)

    def maxflow(self, **kwargs):
        return self.call('maxflow', kwargs=kwargs)

    def minflow(self, **kwargs):
        return self.call('minflow', kwargs=kwargs)

    def maxpress(self, **kwargs):
        return self.call('maxpress', kwargs=kwargs)

    def minpress(self, **kwargs):
        return self.call('minpress', kwargs=kwargs)

    def press_set(self, **kwargs):
        return self.call('press_set', kwargs=kwargs)

    def integral_enable(self, **kwargs):
        return self.call('integral_enable', kwargs=kwargs)

    def integral_disable(self, **kwargs):
        return self.call('integral_disable', kwargs=kwargs)

    def units(self, **kwargs):
        return self.call('units', kwargs=kwargs)

    def gg(self, **kwargs):
        return self.call('gg', kwargs=kwargs)

    def identify(self, **kwargs):
        return self.call('identify', kwargs=kwargs)

    def status(self, **kwargs):
        return self.call('status', kwargs=kwargs)

    def press_get(self, **kwargs):
        return self.call('press_get', kwargs=kwargs)

    def flow_get(self, **kwargs):
        return self.call('flow_get', kwargs=kwargs)

    def vol_get(self, **kwargs):
        return self.call('vol_get', kwargs=kwargs)

    def pause(self, **kwargs):
        return self.call('pause', kwargs=kwargs)

    def tune_maxflow(self, **kwargs):
        return self.call('tune_maxflow', kwargs=kwargs)

    def const_press_alarm(self, **kwargs):
        return self.call('const_press_alarm', kwargs=kwargs)

