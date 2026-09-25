from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentCetoniNemesysSila2(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/CETONI-Software__sila_cetoni_pumps', 'source_file': 'sila_cetoni/pumps/syringepumps/sila/syringepump_service/generated/forcemonitoringservice/forcemonitoringservice_base.py', 'class_name': 'ForceMonitoringServiceBase', 'import_roots': [], 'candidate_methods': ['update_ForceSensorValue', 'ForceSensorValue_on_subscription', 'abort_ForceSensorValue_subscriptions', 'current_ForceSensorValue', 'update_ForceLimit', 'ForceLimit_on_subscription', 'abort_ForceLimit_subscriptions', 'current_ForceLimit', 'update_MaxDeviceForce', 'MaxDeviceForce_on_subscription', 'abort_MaxDeviceForce_subscriptions', 'current_MaxDeviceForce', 'update_ForceMonitoringEnabled', 'ForceMonitoringEnabled_on_subscription', 'abort_ForceMonitoringEnabled_subscriptions', 'current_ForceMonitoringEnabled', 'update_ForceSafetyStopActive', 'ForceSafetyStopActive_on_subscription', 'abort_ForceSafetyStopActive_subscriptions', 'current_ForceSafetyStopActive', 'ClearForceSafetyStop', 'EnableForceMonitoring', 'DisableForceMonitoring', 'SetForceLimit'], 'action_targets': {}, 'metadata': {'repo': 'CETONI-Software/sila_cetoni_pumps', 'repo_url': 'https://github.com/CETONI-Software/sila_cetoni_pumps', 'brand': 'Cetoni', 'model': 'neMESYS (SiLA2)', 'device_type_cn': '注射泵', 'device_type_en': 'Syringe Pump', 'source_framework': '泵阀/液体处理', 'tag_id': '4413', 'tag_name': '注射泵', 'tag_name_en': 'Syringe Pump', 'candidate_score': 237, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def update_ForceSensorValue(self, **kwargs):
        return self.call('update_ForceSensorValue', kwargs=kwargs)

    def ForceSensorValue_on_subscription(self, **kwargs):
        return self.call('ForceSensorValue_on_subscription', kwargs=kwargs)

    def abort_ForceSensorValue_subscriptions(self, **kwargs):
        return self.call('abort_ForceSensorValue_subscriptions', kwargs=kwargs)

    def current_ForceSensorValue(self, **kwargs):
        return self.call('current_ForceSensorValue', kwargs=kwargs)

    def update_ForceLimit(self, **kwargs):
        return self.call('update_ForceLimit', kwargs=kwargs)

    def ForceLimit_on_subscription(self, **kwargs):
        return self.call('ForceLimit_on_subscription', kwargs=kwargs)

    def abort_ForceLimit_subscriptions(self, **kwargs):
        return self.call('abort_ForceLimit_subscriptions', kwargs=kwargs)

    def current_ForceLimit(self, **kwargs):
        return self.call('current_ForceLimit', kwargs=kwargs)

    def update_MaxDeviceForce(self, **kwargs):
        return self.call('update_MaxDeviceForce', kwargs=kwargs)

    def MaxDeviceForce_on_subscription(self, **kwargs):
        return self.call('MaxDeviceForce_on_subscription', kwargs=kwargs)

    def abort_MaxDeviceForce_subscriptions(self, **kwargs):
        return self.call('abort_MaxDeviceForce_subscriptions', kwargs=kwargs)

    def current_MaxDeviceForce(self, **kwargs):
        return self.call('current_MaxDeviceForce', kwargs=kwargs)

    def update_ForceMonitoringEnabled(self, **kwargs):
        return self.call('update_ForceMonitoringEnabled', kwargs=kwargs)

    def ForceMonitoringEnabled_on_subscription(self, **kwargs):
        return self.call('ForceMonitoringEnabled_on_subscription', kwargs=kwargs)

    def abort_ForceMonitoringEnabled_subscriptions(self, **kwargs):
        return self.call('abort_ForceMonitoringEnabled_subscriptions', kwargs=kwargs)

    def current_ForceMonitoringEnabled(self, **kwargs):
        return self.call('current_ForceMonitoringEnabled', kwargs=kwargs)

    def update_ForceSafetyStopActive(self, **kwargs):
        return self.call('update_ForceSafetyStopActive', kwargs=kwargs)

    def ForceSafetyStopActive_on_subscription(self, **kwargs):
        return self.call('ForceSafetyStopActive_on_subscription', kwargs=kwargs)

    def abort_ForceSafetyStopActive_subscriptions(self, **kwargs):
        return self.call('abort_ForceSafetyStopActive_subscriptions', kwargs=kwargs)

    def current_ForceSafetyStopActive(self, **kwargs):
        return self.call('current_ForceSafetyStopActive', kwargs=kwargs)

    def ClearForceSafetyStop(self, **kwargs):
        return self.call('ClearForceSafetyStop', kwargs=kwargs)

    def EnableForceMonitoring(self, **kwargs):
        return self.call('EnableForceMonitoring', kwargs=kwargs)

    def DisableForceMonitoring(self, **kwargs):
        return self.call('DisableForceMonitoring', kwargs=kwargs)

    def SetForceLimit(self, **kwargs):
        return self.call('SetForceLimit', kwargs=kwargs)

