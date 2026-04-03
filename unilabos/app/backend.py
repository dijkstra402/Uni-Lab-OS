import threading
import time

from unilabos.resources.resource_tracker import ResourceTreeSet
from unilabos.utils import logger


def _simple_main(
    devices_config: ResourceTreeSet,
    resources_config: ResourceTreeSet,
    resources_edge_config: list[dict] = [],
    graph=None,
    controllers_config: dict = {},
    bridges=[],
    visual: str = "None",
    resources_mesh_config: dict = {},
):
    """Minimal backend that keeps the process alive for WebSocket / HTTP bridges."""
    logger.info("[SimpleBackend] Running (no ROS). Bridges and WebSocket handle all communication.")
    while True:
        time.sleep(1)


# 根据选择的 backend 启动相应的功能
def start_backend(
    backend: str,
    devices_config: ResourceTreeSet,
    resources_config: ResourceTreeSet,
    resources_edge_config: list[dict] = [],
    graph=None,
    controllers_config: dict = {},
    bridges=[],
    is_slave: bool = False,
    visual: str = "None",
    resources_mesh_config: dict = {},
    **kwargs,
):
    if backend == "ros":
        from unilabos.ros.main_slave_run import main, slave
    elif backend == "simple":
        main = _simple_main
        slave = _simple_main
    elif backend == "automancer":
        main = _simple_main
        slave = _simple_main
    else:
        raise ValueError(f"Unsupported backend: {backend}")

    backend_thread = threading.Thread(
        target=main if not is_slave else slave,
        args=(
            devices_config,
            resources_config,
            resources_edge_config,
            graph,
            controllers_config,
            bridges,
            visual,
            resources_mesh_config,
        ),
        name="backend_thread",
        daemon=True,
    )
    backend_thread.start()
    logger.info(f"Backend {backend} started.")
