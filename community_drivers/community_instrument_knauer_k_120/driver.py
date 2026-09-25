from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentKnauerK120(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/richardingham__octopus', 'source_file': 'octopus/blocktopus/workspace.py', 'class_name': 'Block', 'import_roots': [], 'candidate_methods': ['state', 'disabled', 'created', 'disposed', 'emitLogMessage', 'connectNextBlock', 'disconnectNextBlock', 'getSurroundParent', 'getChildren', 'setFieldValue', 'getFieldValue', 'getInput', 'getInputValue', 'connectInput', 'disconnectInput', 'getReferencedVariables', 'getReferencedVariableNames', 'getGlobalDeclarationNames', 'getUnmatchedVariableNames', 'run', 'eval', 'pause', 'resume', 'cancel', 'reset', 'toEvents', 'root', 'abort', 'on', 'once', 'off', 'listeners', 'emit'], 'action_targets': {}, 'metadata': {'repo': 'richardingham/octopus', 'repo_url': 'https://github.com/richardingham/octopus', 'brand': 'Knauer', 'model': 'K-120', 'device_type_cn': 'HPLC泵', 'device_type_en': 'HPLC Pump', 'source_framework': '色谱/质谱', 'tag_id': '4403', 'tag_name': '柱塞泵', 'tag_name_en': 'Plunger Pump', 'candidate_score': 246, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def state(self, **kwargs):
        return self.call('state', kwargs=kwargs)

    def disabled(self, **kwargs):
        return self.call('disabled', kwargs=kwargs)

    def created(self, **kwargs):
        return self.call('created', kwargs=kwargs)

    def disposed(self, **kwargs):
        return self.call('disposed', kwargs=kwargs)

    def emitLogMessage(self, **kwargs):
        return self.call('emitLogMessage', kwargs=kwargs)

    def connectNextBlock(self, **kwargs):
        return self.call('connectNextBlock', kwargs=kwargs)

    def disconnectNextBlock(self, **kwargs):
        return self.call('disconnectNextBlock', kwargs=kwargs)

    def getSurroundParent(self, **kwargs):
        return self.call('getSurroundParent', kwargs=kwargs)

    def getChildren(self, **kwargs):
        return self.call('getChildren', kwargs=kwargs)

    def setFieldValue(self, **kwargs):
        return self.call('setFieldValue', kwargs=kwargs)

    def getFieldValue(self, **kwargs):
        return self.call('getFieldValue', kwargs=kwargs)

    def getInput(self, **kwargs):
        return self.call('getInput', kwargs=kwargs)

    def getInputValue(self, **kwargs):
        return self.call('getInputValue', kwargs=kwargs)

    def connectInput(self, **kwargs):
        return self.call('connectInput', kwargs=kwargs)

    def disconnectInput(self, **kwargs):
        return self.call('disconnectInput', kwargs=kwargs)

    def getReferencedVariables(self, **kwargs):
        return self.call('getReferencedVariables', kwargs=kwargs)

    def getReferencedVariableNames(self, **kwargs):
        return self.call('getReferencedVariableNames', kwargs=kwargs)

    def getGlobalDeclarationNames(self, **kwargs):
        return self.call('getGlobalDeclarationNames', kwargs=kwargs)

    def getUnmatchedVariableNames(self, **kwargs):
        return self.call('getUnmatchedVariableNames', kwargs=kwargs)

    def run(self, **kwargs):
        return self.call('run', kwargs=kwargs)

    def eval(self, **kwargs):
        return self.call('eval', kwargs=kwargs)

    def pause(self, **kwargs):
        return self.call('pause', kwargs=kwargs)

    def resume(self, **kwargs):
        return self.call('resume', kwargs=kwargs)

    def cancel(self, **kwargs):
        return self.call('cancel', kwargs=kwargs)

    def reset(self, **kwargs):
        return self.call('reset', kwargs=kwargs)

    def toEvents(self, **kwargs):
        return self.call('toEvents', kwargs=kwargs)

    def root(self, **kwargs):
        return self.call('root', kwargs=kwargs)

    def abort(self, **kwargs):
        return self.call('abort', kwargs=kwargs)

    def on(self, **kwargs):
        return self.call('on', kwargs=kwargs)

    def once(self, **kwargs):
        return self.call('once', kwargs=kwargs)

    def off(self, **kwargs):
        return self.call('off', kwargs=kwargs)

    def listeners(self, **kwargs):
        return self.call('listeners', kwargs=kwargs)

    def emit(self, **kwargs):
        return self.call('emit', kwargs=kwargs)

