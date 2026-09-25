from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubInstrumentkitInstrumentkit(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/instrumentkit_InstrumentKit', 'source_file': 'src/instruments/abstract_instruments/instrument.py', 'class_name': 'Instrument', 'import_roots': [], 'candidate_methods': ['sendcmd', 'query', 'read', 'read_raw', 'timeout', 'timeout', 'address', 'address', 'terminator', 'terminator', 'prompt', 'prompt', 'write', 'binblockread', 'open_from_uri', 'open_tcpip', 'open_serial', 'open_gpibusb', 'open_gpibethernet', 'open_visa'], 'metadata': {'repo': 'instrumentkit/instrumentkit', 'repo_url': 'https://github.com/instrumentkit/InstrumentKit', 'unit_id': 'gh_keithley_6220', 'source_file': 'src/instruments/abstract_instruments/instrument.py', 'candidate_score': 232, 'manufacturer': 'Keithley', 'model_name': 'Keithley 6220'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def sendcmd(self, **kwargs):
        return self.call('sendcmd', kwargs=kwargs)

    def query(self, **kwargs):
        return self.call('query', kwargs=kwargs)

    def read(self, **kwargs):
        return self.call('read', kwargs=kwargs)

    def read_raw(self, **kwargs):
        return self.call('read_raw', kwargs=kwargs)

    def timeout(self, **kwargs):
        return self.call('timeout', kwargs=kwargs)

    def timeout(self, **kwargs):
        return self.call('timeout', kwargs=kwargs)

    def address(self, **kwargs):
        return self.call('address', kwargs=kwargs)

    def address(self, **kwargs):
        return self.call('address', kwargs=kwargs)

    def terminator(self, **kwargs):
        return self.call('terminator', kwargs=kwargs)

    def terminator(self, **kwargs):
        return self.call('terminator', kwargs=kwargs)

    def prompt(self, **kwargs):
        return self.call('prompt', kwargs=kwargs)

    def prompt(self, **kwargs):
        return self.call('prompt', kwargs=kwargs)

    def write(self, **kwargs):
        return self.call('write', kwargs=kwargs)

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

