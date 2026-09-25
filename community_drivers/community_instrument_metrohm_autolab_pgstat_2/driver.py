from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentMetrohmAutolabPgstat2(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/autolab-project__autolab', 'source_file': 'autolab/core/gui/scanning/config.py', 'class_name': 'ConfigManager', 'import_roots': [], 'candidate_methods': ['ask_get_element_by_address', 'update_loaded_devices', 'getNames', 'getUniqueName', 'getUniqueNameRecipe', 'updateVariableConfig', 'addNewConfig', 'addRecipe', 'removeRecipe', 'activateRecipe', 'setRecipeOrder', 'renameRecipe', 'checkConfig', 'lastRecipeName', 'addParameter', 'removeParameter', 'setParameter', 'renameParameter', 'setNbPts', 'setStep', 'setRange', 'setLog', 'setValues', 'addRecipeStep', 'delRecipeStep', 'renameRecipeStep', 'setRecipeStepValue', 'setRecipeStepOrder', 'recipeNameList', 'getLinkedRecipe', 'getRecipeLink', 'getAllowedRecipe', 'getActive', 'getRecipeActive', 'getParameter', 'getParameterPosition', 'parameterList', 'parameterNameList', 'getParameterElement', 'getLog', 'getNbPts', 'getStep', 'getRange', 'getValues', 'hasCustomValues', 'stepList', 'getRecipeStep', 'getRecipeStepElement', 'getRecipeStepType', 'getRecipeStepValue', 'getRecipeStepPosition', 'getParamDataFrame', 'getConfigVariables', 'export', 'create_configPars', 'import_configPars', 'load_configPars', 'undoClicked', 'redoClicked', 'changeConfig', 'updateUndoRedoButtons'], 'action_targets': {}, 'metadata': {'repo': 'autolab-project/autolab', 'repo_url': 'https://github.com/autolab-project/autolab', 'brand': 'Metrohm', 'model': 'Autolab PGSTAT', 'device_type_cn': '电化学工作站', 'device_type_en': 'Potentiostat', 'source_framework': 'autolab', 'tag_id': '4425', 'tag_name': '电化学工作站', 'tag_name_en': 'Electrochemical Workstation', 'candidate_score': 501, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def ask_get_element_by_address(self, **kwargs):
        return self.call('ask_get_element_by_address', kwargs=kwargs)

    def update_loaded_devices(self, **kwargs):
        return self.call('update_loaded_devices', kwargs=kwargs)

    def getNames(self, **kwargs):
        return self.call('getNames', kwargs=kwargs)

    def getUniqueName(self, **kwargs):
        return self.call('getUniqueName', kwargs=kwargs)

    def getUniqueNameRecipe(self, **kwargs):
        return self.call('getUniqueNameRecipe', kwargs=kwargs)

    def updateVariableConfig(self, **kwargs):
        return self.call('updateVariableConfig', kwargs=kwargs)

    def addNewConfig(self, **kwargs):
        return self.call('addNewConfig', kwargs=kwargs)

    def addRecipe(self, **kwargs):
        return self.call('addRecipe', kwargs=kwargs)

    def removeRecipe(self, **kwargs):
        return self.call('removeRecipe', kwargs=kwargs)

    def activateRecipe(self, **kwargs):
        return self.call('activateRecipe', kwargs=kwargs)

    def setRecipeOrder(self, **kwargs):
        return self.call('setRecipeOrder', kwargs=kwargs)

    def renameRecipe(self, **kwargs):
        return self.call('renameRecipe', kwargs=kwargs)

    def checkConfig(self, **kwargs):
        return self.call('checkConfig', kwargs=kwargs)

    def lastRecipeName(self, **kwargs):
        return self.call('lastRecipeName', kwargs=kwargs)

    def addParameter(self, **kwargs):
        return self.call('addParameter', kwargs=kwargs)

    def removeParameter(self, **kwargs):
        return self.call('removeParameter', kwargs=kwargs)

    def setParameter(self, **kwargs):
        return self.call('setParameter', kwargs=kwargs)

    def renameParameter(self, **kwargs):
        return self.call('renameParameter', kwargs=kwargs)

    def setNbPts(self, **kwargs):
        return self.call('setNbPts', kwargs=kwargs)

    def setStep(self, **kwargs):
        return self.call('setStep', kwargs=kwargs)

    def setRange(self, **kwargs):
        return self.call('setRange', kwargs=kwargs)

    def setLog(self, **kwargs):
        return self.call('setLog', kwargs=kwargs)

    def setValues(self, **kwargs):
        return self.call('setValues', kwargs=kwargs)

    def addRecipeStep(self, **kwargs):
        return self.call('addRecipeStep', kwargs=kwargs)

    def delRecipeStep(self, **kwargs):
        return self.call('delRecipeStep', kwargs=kwargs)

    def renameRecipeStep(self, **kwargs):
        return self.call('renameRecipeStep', kwargs=kwargs)

    def setRecipeStepValue(self, **kwargs):
        return self.call('setRecipeStepValue', kwargs=kwargs)

    def setRecipeStepOrder(self, **kwargs):
        return self.call('setRecipeStepOrder', kwargs=kwargs)

    def recipeNameList(self, **kwargs):
        return self.call('recipeNameList', kwargs=kwargs)

    def getLinkedRecipe(self, **kwargs):
        return self.call('getLinkedRecipe', kwargs=kwargs)

    def getRecipeLink(self, **kwargs):
        return self.call('getRecipeLink', kwargs=kwargs)

    def getAllowedRecipe(self, **kwargs):
        return self.call('getAllowedRecipe', kwargs=kwargs)

    def getActive(self, **kwargs):
        return self.call('getActive', kwargs=kwargs)

    def getRecipeActive(self, **kwargs):
        return self.call('getRecipeActive', kwargs=kwargs)

    def getParameter(self, **kwargs):
        return self.call('getParameter', kwargs=kwargs)

    def getParameterPosition(self, **kwargs):
        return self.call('getParameterPosition', kwargs=kwargs)

    def parameterList(self, **kwargs):
        return self.call('parameterList', kwargs=kwargs)

    def parameterNameList(self, **kwargs):
        return self.call('parameterNameList', kwargs=kwargs)

    def getParameterElement(self, **kwargs):
        return self.call('getParameterElement', kwargs=kwargs)

    def getLog(self, **kwargs):
        return self.call('getLog', kwargs=kwargs)

    def getNbPts(self, **kwargs):
        return self.call('getNbPts', kwargs=kwargs)

    def getStep(self, **kwargs):
        return self.call('getStep', kwargs=kwargs)

    def getRange(self, **kwargs):
        return self.call('getRange', kwargs=kwargs)

    def getValues(self, **kwargs):
        return self.call('getValues', kwargs=kwargs)

    def hasCustomValues(self, **kwargs):
        return self.call('hasCustomValues', kwargs=kwargs)

    def stepList(self, **kwargs):
        return self.call('stepList', kwargs=kwargs)

    def getRecipeStep(self, **kwargs):
        return self.call('getRecipeStep', kwargs=kwargs)

    def getRecipeStepElement(self, **kwargs):
        return self.call('getRecipeStepElement', kwargs=kwargs)

    def getRecipeStepType(self, **kwargs):
        return self.call('getRecipeStepType', kwargs=kwargs)

    def getRecipeStepValue(self, **kwargs):
        return self.call('getRecipeStepValue', kwargs=kwargs)

    def getRecipeStepPosition(self, **kwargs):
        return self.call('getRecipeStepPosition', kwargs=kwargs)

    def getParamDataFrame(self, **kwargs):
        return self.call('getParamDataFrame', kwargs=kwargs)

    def getConfigVariables(self, **kwargs):
        return self.call('getConfigVariables', kwargs=kwargs)

    def export(self, **kwargs):
        return self.call('export', kwargs=kwargs)

    def create_configPars(self, **kwargs):
        return self.call('create_configPars', kwargs=kwargs)

    def import_configPars(self, **kwargs):
        return self.call('import_configPars', kwargs=kwargs)

    def load_configPars(self, **kwargs):
        return self.call('load_configPars', kwargs=kwargs)

    def undoClicked(self, **kwargs):
        return self.call('undoClicked', kwargs=kwargs)

    def redoClicked(self, **kwargs):
        return self.call('redoClicked', kwargs=kwargs)

    def changeConfig(self, **kwargs):
        return self.call('changeConfig', kwargs=kwargs)

    def updateUndoRedoButtons(self, **kwargs):
        return self.call('updateUndoRedoButtons', kwargs=kwargs)

