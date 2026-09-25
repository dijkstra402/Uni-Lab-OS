from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentKukaIiwa7r800Iiwa14r820(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/Modi1987__iiwaPy3', 'source_file': 'python_client/iiwaPy3.py', 'class_name': 'iiwaPy3', 'import_roots': [], 'candidate_methods': ['close', 'send', 'movePTPJointSpace', 'movePTPHomeJointSpace', 'movePTPTransportPositionJointSpace', 'movePTPLineEEF', 'movePTPLineEefRelBase', 'movePTPLineEefRelEef', 'movePTPCirc1OrintationInter', 'movePTPArcYZ_AC', 'movePTPArcXZ_AC', 'movePTPArcXY_AC', 'movePTPArc_AC', 'realTime_stopImpedanceJoints', 'realTime_startDirectServoCartesian', 'realTime_stopDirectServoCartesian', 'realTime_stopDirectServoJoints', 'realTime_startDirectServoJoints', 'realTime_startImpedanceJoints', 'sendEEfPosition', 'sendJointsPositionsGetMTorque', 'sendJointsPositionsGetExTorque', 'sendJointsPositionsGetActualEEFpos', 'sendJointsPositionsGetEEF_Force_rel_EEF', 'sendJointsPositionsGetActualJpos', 'sendEEfPositionGetExTorque', 'sendEEfPositionGetActualEEFpos', 'sendEEfPositionGetActualJpos', 'sendEEfPositionGetEEF_Force_rel_EEF', 'sendEEfPositionGetMTorque', 'sendJointsPositions', 'preciseHandGuiding', 'getEEFPos', 'getEEF_Force', 'getEEFCartizianPosition', 'getEEF_Moment', 'getJointsPos', 'getJointsExternalTorques', 'getJointsMeasuredTorques', 'getMeasuredTorqueAtJoint', 'getEEFCartizianOrientation', 'getPin3State', 'getPin10State', 'getPin13State', 'getPin16State', 'setBlueOff', 'setBlueOn', 'setPin1Off', 'setPin1On', 'setPin2Off', 'setPin2On', 'setPin11Off', 'setPin11On', 'setPin12Off', 'setPin12On'], 'action_targets': {}, 'metadata': {'repo': 'Modi1987/iiwaPy3', 'repo_url': 'https://github.com/Modi1987/iiwaPy3', 'brand': 'KUKA', 'model': 'iiwa 7R800 / iiwa 14R820', 'device_type_cn': '协作机械臂', 'device_type_en': 'Collaborative Robot', 'source_framework': '机器人/运动控制', 'tag_id': '4402', 'tag_name': '机械臂', 'tag_name_en': 'Robotic Arm', 'candidate_score': 510, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def send(self, **kwargs):
        return self.call('send', kwargs=kwargs)

    def movePTPJointSpace(self, **kwargs):
        return self.call('movePTPJointSpace', kwargs=kwargs)

    def movePTPHomeJointSpace(self, **kwargs):
        return self.call('movePTPHomeJointSpace', kwargs=kwargs)

    def movePTPTransportPositionJointSpace(self, **kwargs):
        return self.call('movePTPTransportPositionJointSpace', kwargs=kwargs)

    def movePTPLineEEF(self, **kwargs):
        return self.call('movePTPLineEEF', kwargs=kwargs)

    def movePTPLineEefRelBase(self, **kwargs):
        return self.call('movePTPLineEefRelBase', kwargs=kwargs)

    def movePTPLineEefRelEef(self, **kwargs):
        return self.call('movePTPLineEefRelEef', kwargs=kwargs)

    def movePTPCirc1OrintationInter(self, **kwargs):
        return self.call('movePTPCirc1OrintationInter', kwargs=kwargs)

    def movePTPArcYZ_AC(self, **kwargs):
        return self.call('movePTPArcYZ_AC', kwargs=kwargs)

    def movePTPArcXZ_AC(self, **kwargs):
        return self.call('movePTPArcXZ_AC', kwargs=kwargs)

    def movePTPArcXY_AC(self, **kwargs):
        return self.call('movePTPArcXY_AC', kwargs=kwargs)

    def movePTPArc_AC(self, **kwargs):
        return self.call('movePTPArc_AC', kwargs=kwargs)

    def realTime_stopImpedanceJoints(self, **kwargs):
        return self.call('realTime_stopImpedanceJoints', kwargs=kwargs)

    def realTime_startDirectServoCartesian(self, **kwargs):
        return self.call('realTime_startDirectServoCartesian', kwargs=kwargs)

    def realTime_stopDirectServoCartesian(self, **kwargs):
        return self.call('realTime_stopDirectServoCartesian', kwargs=kwargs)

    def realTime_stopDirectServoJoints(self, **kwargs):
        return self.call('realTime_stopDirectServoJoints', kwargs=kwargs)

    def realTime_startDirectServoJoints(self, **kwargs):
        return self.call('realTime_startDirectServoJoints', kwargs=kwargs)

    def realTime_startImpedanceJoints(self, **kwargs):
        return self.call('realTime_startImpedanceJoints', kwargs=kwargs)

    def sendEEfPosition(self, **kwargs):
        return self.call('sendEEfPosition', kwargs=kwargs)

    def sendJointsPositionsGetMTorque(self, **kwargs):
        return self.call('sendJointsPositionsGetMTorque', kwargs=kwargs)

    def sendJointsPositionsGetExTorque(self, **kwargs):
        return self.call('sendJointsPositionsGetExTorque', kwargs=kwargs)

    def sendJointsPositionsGetActualEEFpos(self, **kwargs):
        return self.call('sendJointsPositionsGetActualEEFpos', kwargs=kwargs)

    def sendJointsPositionsGetEEF_Force_rel_EEF(self, **kwargs):
        return self.call('sendJointsPositionsGetEEF_Force_rel_EEF', kwargs=kwargs)

    def sendJointsPositionsGetActualJpos(self, **kwargs):
        return self.call('sendJointsPositionsGetActualJpos', kwargs=kwargs)

    def sendEEfPositionGetExTorque(self, **kwargs):
        return self.call('sendEEfPositionGetExTorque', kwargs=kwargs)

    def sendEEfPositionGetActualEEFpos(self, **kwargs):
        return self.call('sendEEfPositionGetActualEEFpos', kwargs=kwargs)

    def sendEEfPositionGetActualJpos(self, **kwargs):
        return self.call('sendEEfPositionGetActualJpos', kwargs=kwargs)

    def sendEEfPositionGetEEF_Force_rel_EEF(self, **kwargs):
        return self.call('sendEEfPositionGetEEF_Force_rel_EEF', kwargs=kwargs)

    def sendEEfPositionGetMTorque(self, **kwargs):
        return self.call('sendEEfPositionGetMTorque', kwargs=kwargs)

    def sendJointsPositions(self, **kwargs):
        return self.call('sendJointsPositions', kwargs=kwargs)

    def preciseHandGuiding(self, **kwargs):
        return self.call('preciseHandGuiding', kwargs=kwargs)

    def getEEFPos(self, **kwargs):
        return self.call('getEEFPos', kwargs=kwargs)

    def getEEF_Force(self, **kwargs):
        return self.call('getEEF_Force', kwargs=kwargs)

    def getEEFCartizianPosition(self, **kwargs):
        return self.call('getEEFCartizianPosition', kwargs=kwargs)

    def getEEF_Moment(self, **kwargs):
        return self.call('getEEF_Moment', kwargs=kwargs)

    def getJointsPos(self, **kwargs):
        return self.call('getJointsPos', kwargs=kwargs)

    def getJointsExternalTorques(self, **kwargs):
        return self.call('getJointsExternalTorques', kwargs=kwargs)

    def getJointsMeasuredTorques(self, **kwargs):
        return self.call('getJointsMeasuredTorques', kwargs=kwargs)

    def getMeasuredTorqueAtJoint(self, **kwargs):
        return self.call('getMeasuredTorqueAtJoint', kwargs=kwargs)

    def getEEFCartizianOrientation(self, **kwargs):
        return self.call('getEEFCartizianOrientation', kwargs=kwargs)

    def getPin3State(self, **kwargs):
        return self.call('getPin3State', kwargs=kwargs)

    def getPin10State(self, **kwargs):
        return self.call('getPin10State', kwargs=kwargs)

    def getPin13State(self, **kwargs):
        return self.call('getPin13State', kwargs=kwargs)

    def getPin16State(self, **kwargs):
        return self.call('getPin16State', kwargs=kwargs)

    def setBlueOff(self, **kwargs):
        return self.call('setBlueOff', kwargs=kwargs)

    def setBlueOn(self, **kwargs):
        return self.call('setBlueOn', kwargs=kwargs)

    def setPin1Off(self, **kwargs):
        return self.call('setPin1Off', kwargs=kwargs)

    def setPin1On(self, **kwargs):
        return self.call('setPin1On', kwargs=kwargs)

    def setPin2Off(self, **kwargs):
        return self.call('setPin2Off', kwargs=kwargs)

    def setPin2On(self, **kwargs):
        return self.call('setPin2On', kwargs=kwargs)

    def setPin11Off(self, **kwargs):
        return self.call('setPin11Off', kwargs=kwargs)

    def setPin11On(self, **kwargs):
        return self.call('setPin11On', kwargs=kwargs)

    def setPin12Off(self, **kwargs):
        return self.call('setPin12Off', kwargs=kwargs)

    def setPin12On(self, **kwargs):
        return self.call('setPin12On', kwargs=kwargs)

