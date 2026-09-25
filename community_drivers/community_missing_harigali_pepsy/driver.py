from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityMissingHarigaliPepsy(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/harigali__PepSy', 'source_file': 'PepSy.py', 'class_name': '', 'import_roots': [], 'candidate_methods': ['positions', 'pspos', 'pumpon', 'presyn', 'syn', 'washing', 'initialization', 'priming', 'swelling', 'coupling', 'doublecoupling', 'fmocdeprotection'], 'metadata': {'repo': 'harigali/PepSy', 'repo_url': 'https://github.com/harigali/PepSy', 'review_status': 'good', 'review_notes': ['多肽合成工艺方法明确。']}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def positions(self, **kwargs):
        return self.call('positions', kwargs=kwargs)

    def pspos(self, **kwargs):
        return self.call('pspos', kwargs=kwargs)

    def pumpon(self, **kwargs):
        return self.call('pumpon', kwargs=kwargs)

    def presyn(self, **kwargs):
        return self.call('presyn', kwargs=kwargs)

    def syn(self, **kwargs):
        return self.call('syn', kwargs=kwargs)

    def washing(self, **kwargs):
        return self.call('washing', kwargs=kwargs)

    def initialization(self, **kwargs):
        return self.call('initialization', kwargs=kwargs)

    def priming(self, **kwargs):
        return self.call('priming', kwargs=kwargs)

    def swelling(self, **kwargs):
        return self.call('swelling', kwargs=kwargs)

    def coupling(self, **kwargs):
        return self.call('coupling', kwargs=kwargs)

    def doublecoupling(self, **kwargs):
        return self.call('doublecoupling', kwargs=kwargs)

    def fmocdeprotection(self, **kwargs):
        return self.call('fmocdeprotection', kwargs=kwargs)

