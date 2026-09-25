from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictPhasematrixfsw0020(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/instrumentkit__InstrumentKit', 'source_file': 'src/instruments/phasematrix/phasematrix_fsw0020.py', 'class_name': 'PhaseMatrixFSW0020', 'import_roots': ['src'], 'candidate_methods': ['reset', 'frequency', 'power', 'phase', 'blanking', 'ref_output', 'output', 'pulse_modulation', 'am_modulation', 'channel', 'sendcmd', 'query', 'read_raw', 'timeout', 'address', 'terminator', 'prompt', 'binblockread', 'open_from_uri', 'open_tcpip', 'open_serial', 'open_gpibusb', 'open_gpibethernet', 'open_visa', 'open_test', 'open_usbtmc', 'open_vxi11', 'open_usb', 'open_file'], 'action_targets': {}, 'metadata': {'repo': 'instrumentkit/InstrumentKit', 'repo_url': 'https://github.com/instrumentkit/InstrumentKit', 'source_url': 'https://github.com/instrumentkit/InstrumentKit/blob/main/src/instruments/phasematrix/phasematrix_fsw0020.py', 'confidence': 0.8, 'quality_score': 0.94, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def reset(self, **kwargs):
        return self.call('reset', kwargs=kwargs)

    def frequency(self, **kwargs):
        return self.call('frequency', kwargs=kwargs)

    def power(self, **kwargs):
        return self.call('power', kwargs=kwargs)

    def phase(self, **kwargs):
        return self.call('phase', kwargs=kwargs)

    def blanking(self, **kwargs):
        return self.call('blanking', kwargs=kwargs)

    def ref_output(self, **kwargs):
        return self.call('ref_output', kwargs=kwargs)

    def output(self, **kwargs):
        return self.call('output', kwargs=kwargs)

    def pulse_modulation(self, **kwargs):
        return self.call('pulse_modulation', kwargs=kwargs)

    def am_modulation(self, **kwargs):
        return self.call('am_modulation', kwargs=kwargs)

    def channel(self, **kwargs):
        return self.call('channel', kwargs=kwargs)

    def sendcmd(self, **kwargs):
        return self.call('sendcmd', kwargs=kwargs)

    def query(self, **kwargs):
        return self.call('query', kwargs=kwargs)

    def read_raw(self, **kwargs):
        return self.call('read_raw', kwargs=kwargs)

    def timeout(self, **kwargs):
        return self.call('timeout', kwargs=kwargs)

    def address(self, **kwargs):
        return self.call('address', kwargs=kwargs)

    def terminator(self, **kwargs):
        return self.call('terminator', kwargs=kwargs)

    def prompt(self, **kwargs):
        return self.call('prompt', kwargs=kwargs)

    def binblockread(self, **kwargs):
        return self.call('binblockread', kwargs=kwargs)

    def open_from_uri(self, **kwargs):
        return self.call('open_from_uri', kwargs=kwargs)

    def open_tcpip(self, **kwargs):
        return self.call('open_tcpip', kwargs=kwargs)

    def open_serial(self, **kwargs):
        return self.call('open_serial', kwargs=kwargs)

    def open_gpibusb(self, **kwargs):
        return self.call('open_gpibusb', kwargs=kwargs)

    def open_gpibethernet(self, **kwargs):
        return self.call('open_gpibethernet', kwargs=kwargs)

    def open_visa(self, **kwargs):
        return self.call('open_visa', kwargs=kwargs)

    def open_test(self, **kwargs):
        return self.call('open_test', kwargs=kwargs)

    def open_usbtmc(self, **kwargs):
        return self.call('open_usbtmc', kwargs=kwargs)

    def open_vxi11(self, **kwargs):
        return self.call('open_vxi11', kwargs=kwargs)

    def open_usb(self, **kwargs):
        return self.call('open_usb', kwargs=kwargs)

    def open_file(self, **kwargs):
        return self.call('open_file', kwargs=kwargs)

