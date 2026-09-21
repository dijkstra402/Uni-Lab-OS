"""
注射泵 — 标准设备类模板 (Device Class Template)

定义「注射泵」这一设备大类的标准动作(action)与状态属性(property)。
同一大类下不同品牌的设备都应实现这套统一接口，使一套工作流可跨品牌控制整类设备。

ponytail: 无硬件时用内存 mock，便于卡片/调试台下发动作；接真机时换品牌驱动实现。
来源: 电气通讯协议标准化 device_action_spec.json
"""

from typing import Any, Dict, Optional

from unilabos.registry.decorators import device, action, topic_config


@device(
    id="syringe_pump",
    category=["注射泵"],
    description="注射泵标准接口：同一大类跨品牌统一的动作与参数。",
    display_name="注射泵",
)
class SyringePump:

    def __init__(self, device_id: Optional[str] = None, config: Optional[Dict[str, Any]] = None, **kwargs):
        """
        初始化设备。

        Args:
            device_id[设备ID]: 设备实例 ID。
            config[设备配置]: 设备启动配置。
        """
        self.device_id = device_id or "syringe_pump"
        self.config = config or {}
        self.data: Dict[str, Any] = {
            "status": "idle",
            "idle": True,
            "fault": False,
            "fault_code": 0,
            "current_position": 0.0,
            "aspirate_position": 0.0,
            "dispense_position": 0.0,
        }
        self._aspirate_set = False
        self._dispense_set = False

    def _snapshot(self, **updates: Any) -> Dict[str, Any]:
        if updates:
            self.data.update(updates)
        self.data["idle"] = True
        self.data.setdefault("fault", False)
        self.data.setdefault("fault_code", 0)
        return dict(self.data)

    @action(description="初始化")
    def initialize(self) -> Dict[str, Any]:
        """初始化。"""
        self._aspirate_set = False
        self._dispense_set = False
        return self._snapshot(
            status="idle",
            fault=False,
            fault_code=0,
            current_position=0.0,
            aspirate_position=0.0,
            dispense_position=0.0,
        )

    @action(description="设置绝对位置")
    def set_position(self, position: float = 0.0) -> Dict[str, Any]:
        """
        设置绝对位置。

        Args:
            position[绝对位置]: 目标绝对位置（单位依设备量程而定）。
        """
        return self._snapshot(status="idle", current_position=float(position))

    @action(description="设置抽液位置")
    def set_aspirate_position(self, aspirate_position: float = 0.0) -> Dict[str, Any]:
        """
        设置抽液位置。

        Args:
            aspirate_position[抽液位置]: 目标抽液位置（单位依设备量程而定）。
        """
        self._aspirate_set = True
        pos = float(aspirate_position)
        return self._snapshot(
            status="idle",
            aspirate_position=pos,
            current_position=pos,
        )

    @action(description="设置排液位置")
    def set_dispense_position(self, dispense_position: float = 0.0) -> Dict[str, Any]:
        """
        设置排液位置。

        Args:
            dispense_position[排液位置]: 目标排液位置（单位依设备量程而定）。
        """
        self._dispense_set = True
        pos = float(dispense_position)
        return self._snapshot(
            status="idle",
            dispense_position=pos,
            current_position=pos,
        )

    @action(description="绝对控制")
    def move_absolute(self) -> Dict[str, Any]:
        """绝对控制：确认当前绝对位置（mock）。"""
        return self._snapshot(
            status="idle",
            current_position=float(self.data.get("current_position", 0.0)),
        )

    @action(description="抽液")
    def aspirate(self) -> Dict[str, Any]:
        """抽液：已设抽液位则移到该位，否则当前位置 +5。"""
        if self._aspirate_set:
            pos = float(self.data["aspirate_position"])
        else:
            pos = float(self.data.get("current_position", 0.0)) + 5.0
        return self._snapshot(status="idle", current_position=pos)

    @action(description="排液")
    def dispense(self) -> Dict[str, Any]:
        """排液：已设排液位则移到该位，否则当前位置 -5（不低于 0）。"""
        if self._dispense_set:
            pos = float(self.data["dispense_position"])
        else:
            pos = max(0.0, float(self.data.get("current_position", 0.0)) - 5.0)
        return self._snapshot(status="idle", current_position=pos)

    @property
    @topic_config()
    def status(self) -> str:
        """设备运行状态。"""
        return self.data.get("status", "idle")

    @property
    @topic_config()
    def fault(self) -> bool:
        """故障。"""
        return bool(self.data.get("fault", False))

    @property
    @topic_config()
    def idle(self) -> bool:
        """空闲。"""
        return bool(self.data.get("idle", True))

    @property
    @topic_config()
    def fault_code(self) -> int:
        """故障代码。"""
        return int(self.data.get("fault_code", 0))

    @property
    @topic_config()
    def current_position(self) -> float:
        """当前位置显示。"""
        return float(self.data.get("current_position", 0.0))

    @property
    @topic_config()
    def aspirate_position(self) -> float:
        """已设置的抽液位置。"""
        return float(self.data.get("aspirate_position", 0.0))

    @property
    @topic_config()
    def dispense_position(self) -> float:
        """已设置的排液位置。"""
        return float(self.data.get("dispense_position", 0.0))
