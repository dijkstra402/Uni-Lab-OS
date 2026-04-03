import json
import time
from typing import Optional, Tuple, Dict, Any, List

from unilabos.utils.log import logger
from unilabos.utils.type_check import TypeEncoder

BATCH_SIZE = 100


def _chunked(items: List[Any], size: int):
    for i in range(0, len(items), size):
        yield items[i : i + size]


def register_devices_and_resources(lab_registry, gather_only=False) -> Optional[Tuple[Dict[str, Any], Dict[str, Any]]]:
    """
    注册设备和资源到服务器（仅支持HTTP）
    """

    # 注册资源信息 - 使用HTTP方式
    from unilabos.app.web.client import http_client

    logger.info("[UniLab Register] 开始注册设备和资源...")

    # 注册设备信息 — 以原始 id（设备类名）为主键去重
    # id 保持设备类名（YAML key / AST key），使 startup.json 的 class 字段能正确匹配
    devices_to_register = {}
    for device_info in lab_registry.obtain_registry_device_info():
        device_data = json.loads(
            json.dumps(device_info, ensure_ascii=False, cls=TypeEncoder)
        )
        effective_id = device_data["id"]
        if effective_id in devices_to_register:
            logger.debug(f"[UniLab Register] 跳过重复设备: {effective_id}")
            continue
        devices_to_register[effective_id] = device_data
        logger.debug(f"[UniLab Register] 收集设备: {effective_id}")

    resources_to_register = {}
    for resource_info in lab_registry.obtain_registry_resource_info():
        resources_to_register[resource_info["id"]] = resource_info
        logger.debug(f"[UniLab Register] 收集资源: {resource_info['id']}")

    if gather_only:
        return devices_to_register, resources_to_register

    # 分批注册设备
    if devices_to_register:
        all_devices = list(devices_to_register.values())
        total = len(all_devices)
        registered = 0
        failed = 0
        start_time = time.time()

        for batch_idx, batch in enumerate(_chunked(all_devices, BATCH_SIZE)):
            try:
                response = http_client.resource_registry({"resources": batch}, tag=f"registry_batch_{batch_idx}")
                body_ok = True
                if response.status_code in [200, 201]:
                    try:
                        body = response.json()
                        if body.get("code", 0) != 0:
                            body_ok = False
                            logger.error(
                                f"[UniLab Register] 批次 {batch_idx + 1} 服务端错误: {body}"
                            )
                    except Exception:
                        pass
                if response.status_code in [200, 201] and body_ok:
                    registered += len(batch)
                    logger.info(
                        f"[UniLab Register] 批次 {batch_idx + 1} 注册 {len(batch)} 个设备成功 "
                        f"({registered}/{total})"
                    )
                else:
                    failed += len(batch)
                    if body_ok:
                        logger.error(
                            f"[UniLab Register] 批次 {batch_idx + 1} 注册失败: "
                            f"{response.status_code}, {response.text}"
                        )
            except Exception as e:
                failed += len(batch)
                logger.error(f"[UniLab Register] 批次 {batch_idx + 1} 注册异常: {e}")

        cost_time = time.time() - start_time
        logger.info(
            f"[UniLab Register] 设备注册完成: 成功 {registered}/{total}, "
            f"失败 {failed}, 耗时 {cost_time:.2f}s"
        )

    # 分批注册资源
    if resources_to_register:
        all_resources = list(resources_to_register.values())
        total = len(all_resources)
        registered = 0
        failed = 0
        start_time = time.time()

        for batch_idx, batch in enumerate(_chunked(all_resources, BATCH_SIZE)):
            try:
                response = http_client.resource_registry({"resources": batch}, tag=f"resource_registry_batch_{batch_idx}")
                if response.status_code in [200, 201]:
                    registered += len(batch)
                    logger.info(
                        f"[UniLab Register] 资源批次 {batch_idx + 1} 注册 {len(batch)} 个成功 "
                        f"({registered}/{total})"
                    )
                else:
                    failed += len(batch)
                    logger.error(
                        f"[UniLab Register] 资源批次 {batch_idx + 1} 注册失败: "
                        f"{response.status_code}, {response.text}"
                    )
            except Exception as e:
                failed += len(batch)
                logger.error(f"[UniLab Register] 资源批次 {batch_idx + 1} 注册异常: {e}")

        cost_time = time.time() - start_time
        logger.info(
            f"[UniLab Register] 资源注册完成: 成功 {registered}/{total}, "
            f"失败 {failed}, 耗时 {cost_time:.2f}s"
        )

    logger.info("[UniLab Register] 设备和资源注册完成.")
