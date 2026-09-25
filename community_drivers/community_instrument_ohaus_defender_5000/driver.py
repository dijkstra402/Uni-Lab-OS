from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentOhausDefender5000(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/FokkeB__serial_logger', 'source_file': 'serial_logger.py', 'class_name': 'Writer', 'import_roots': [], 'candidate_methods': ['get_filename', 'get_usb_drives', 'is_mounted', 'check_for_update', 'mount_usb_drive', 'umount_usb_drive', 'mount_if_needed', 'write_data'], 'action_targets': {}, 'metadata': {'repo': 'FokkeB/serial_logger', 'repo_url': 'https://github.com/FokkeB/serial_logger', 'brand': 'Ohaus', 'model': 'Defender 5000', 'device_type_cn': '电子天平', 'device_type_en': 'Electronic Balance', 'source_framework': '专用驱动', 'tag_id': '4426', 'tag_name': '电子天平', 'tag_name_en': 'Electronic Balance', 'candidate_score': 110, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_filename(self, **kwargs):
        return self.call('get_filename', kwargs=kwargs)

    def get_usb_drives(self, **kwargs):
        return self.call('get_usb_drives', kwargs=kwargs)

    def is_mounted(self, **kwargs):
        return self.call('is_mounted', kwargs=kwargs)

    def check_for_update(self, **kwargs):
        return self.call('check_for_update', kwargs=kwargs)

    def mount_usb_drive(self, **kwargs):
        return self.call('mount_usb_drive', kwargs=kwargs)

    def umount_usb_drive(self, **kwargs):
        return self.call('umount_usb_drive', kwargs=kwargs)

    def mount_if_needed(self, **kwargs):
        return self.call('mount_if_needed', kwargs=kwargs)

    def write_data(self, **kwargs):
        return self.call('write_data', kwargs=kwargs)

