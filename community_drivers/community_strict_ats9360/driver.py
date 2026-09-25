from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictAts9360(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/QCoDeS__Qcodes', 'source_file': 'src/qcodes/instrument_drivers/AlazarTech/ATS9360.py', 'class_name': 'AlazarTechATS9360', 'import_roots': ['src'], 'candidate_methods': ['get_clock_source', 'get_external_sample_rate', 'get_sample_rate', 'get_clock_edge', 'get_decimation', 'get_trigger_operation', 'get_external_trigger_coupling', 'get_external_trigger_range', 'get_trigger_delay', 'get_timeout_ticks', 'get_aux_io_mode', 'get_aux_io_param', 'get_mode', 'get_samples_per_record', 'get_records_per_buffer', 'get_buffers_per_acquisition', 'get_channel_selection', 'get_transfer_offset', 'get_external_startcapture', 'get_enable_record_headers', 'get_alloc_buffers', 'get_fifo_only_streaming', 'get_interleave_samples', 'get_get_processed_data', 'get_allocated_buffers', 'get_buffer_timeout', 'get_trigger_holdoff', 'set_trigger_holdoff', 'find_boards', 'get_board_info', 'get_idn', 'syncing', 'sync_settings_to_card', 'allocate_and_post_buffer', 'acquire', 'clear_buffers', 'signal_to_volt', 'get_num_channels', 'connect_message', 'close', 'close_all', 'record_instance', 'instances', 'remove_instance', 'find_instrument', 'exist', 'is_valid', 'write_raw', 'ask_raw', 'label', 'add_parameter', 'remove_parameter', 'add_function', 'add_submodule', 'get_component', 'snapshot_base', 'print_readable_snapshot', 'invalidate_cache', 'parent', 'ancestors', 'root_instrument', 'name_parts', 'full_name', 'name', 'short_name', 'set', 'get', 'call', 'validate_status', 'load_metadata', 'snapshot'], 'action_targets': {'get_clock_source': '__qcodes_param_get__clock_source', 'get_external_sample_rate': '__qcodes_param_get__external_sample_rate', 'get_sample_rate': '__qcodes_param_get__sample_rate', 'get_clock_edge': '__qcodes_param_get__clock_edge', 'get_decimation': '__qcodes_param_get__decimation', 'get_trigger_operation': '__qcodes_param_get__trigger_operation', 'get_external_trigger_coupling': '__qcodes_param_get__external_trigger_coupling', 'get_external_trigger_range': '__qcodes_param_get__external_trigger_range', 'get_trigger_delay': '__qcodes_param_get__trigger_delay', 'get_timeout_ticks': '__qcodes_param_get__timeout_ticks', 'get_aux_io_mode': '__qcodes_param_get__aux_io_mode', 'get_aux_io_param': '__qcodes_param_get__aux_io_param', 'get_mode': '__qcodes_param_get__mode', 'get_samples_per_record': '__qcodes_param_get__samples_per_record', 'get_records_per_buffer': '__qcodes_param_get__records_per_buffer', 'get_buffers_per_acquisition': '__qcodes_param_get__buffers_per_acquisition', 'get_channel_selection': '__qcodes_param_get__channel_selection', 'get_transfer_offset': '__qcodes_param_get__transfer_offset', 'get_external_startcapture': '__qcodes_param_get__external_startcapture', 'get_enable_record_headers': '__qcodes_param_get__enable_record_headers', 'get_alloc_buffers': '__qcodes_param_get__alloc_buffers', 'get_fifo_only_streaming': '__qcodes_param_get__fifo_only_streaming', 'get_interleave_samples': '__qcodes_param_get__interleave_samples', 'get_get_processed_data': '__qcodes_param_get__get_processed_data', 'get_allocated_buffers': '__qcodes_param_get__allocated_buffers', 'get_buffer_timeout': '__qcodes_param_get__buffer_timeout', 'get_trigger_holdoff': '__qcodes_param_get__trigger_holdoff', 'set_trigger_holdoff': '__qcodes_param_set__trigger_holdoff'}, 'metadata': {'repo': 'QCoDeS/Qcodes', 'repo_url': 'https://github.com/QCoDeS/Qcodes', 'source_url': 'https://github.com/QCoDeS/Qcodes/blob/main/src/qcodes/instrument_drivers/AlazarTech/ATS9360.py', 'confidence': 0.8, 'quality_score': 0.94, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'get_clock_source': '__qcodes_param_get__clock_source', 'get_external_sample_rate': '__qcodes_param_get__external_sample_rate', 'get_sample_rate': '__qcodes_param_get__sample_rate', 'get_clock_edge': '__qcodes_param_get__clock_edge', 'get_decimation': '__qcodes_param_get__decimation', 'get_trigger_operation': '__qcodes_param_get__trigger_operation', 'get_external_trigger_coupling': '__qcodes_param_get__external_trigger_coupling', 'get_external_trigger_range': '__qcodes_param_get__external_trigger_range', 'get_trigger_delay': '__qcodes_param_get__trigger_delay', 'get_timeout_ticks': '__qcodes_param_get__timeout_ticks', 'get_aux_io_mode': '__qcodes_param_get__aux_io_mode', 'get_aux_io_param': '__qcodes_param_get__aux_io_param', 'get_mode': '__qcodes_param_get__mode', 'get_samples_per_record': '__qcodes_param_get__samples_per_record', 'get_records_per_buffer': '__qcodes_param_get__records_per_buffer', 'get_buffers_per_acquisition': '__qcodes_param_get__buffers_per_acquisition', 'get_channel_selection': '__qcodes_param_get__channel_selection', 'get_transfer_offset': '__qcodes_param_get__transfer_offset', 'get_external_startcapture': '__qcodes_param_get__external_startcapture', 'get_enable_record_headers': '__qcodes_param_get__enable_record_headers', 'get_alloc_buffers': '__qcodes_param_get__alloc_buffers', 'get_fifo_only_streaming': '__qcodes_param_get__fifo_only_streaming', 'get_interleave_samples': '__qcodes_param_get__interleave_samples', 'get_get_processed_data': '__qcodes_param_get__get_processed_data', 'get_allocated_buffers': '__qcodes_param_get__allocated_buffers', 'get_buffer_timeout': '__qcodes_param_get__buffer_timeout', 'get_trigger_holdoff': '__qcodes_param_get__trigger_holdoff', 'set_trigger_holdoff': '__qcodes_param_set__trigger_holdoff'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_clock_source(self, **kwargs):
        return self.call('get_clock_source', kwargs=kwargs)

    def get_external_sample_rate(self, **kwargs):
        return self.call('get_external_sample_rate', kwargs=kwargs)

    def get_sample_rate(self, **kwargs):
        return self.call('get_sample_rate', kwargs=kwargs)

    def get_clock_edge(self, **kwargs):
        return self.call('get_clock_edge', kwargs=kwargs)

    def get_decimation(self, **kwargs):
        return self.call('get_decimation', kwargs=kwargs)

    def get_trigger_operation(self, **kwargs):
        return self.call('get_trigger_operation', kwargs=kwargs)

    def get_external_trigger_coupling(self, **kwargs):
        return self.call('get_external_trigger_coupling', kwargs=kwargs)

    def get_external_trigger_range(self, **kwargs):
        return self.call('get_external_trigger_range', kwargs=kwargs)

    def get_trigger_delay(self, **kwargs):
        return self.call('get_trigger_delay', kwargs=kwargs)

    def get_timeout_ticks(self, **kwargs):
        return self.call('get_timeout_ticks', kwargs=kwargs)

    def get_aux_io_mode(self, **kwargs):
        return self.call('get_aux_io_mode', kwargs=kwargs)

    def get_aux_io_param(self, **kwargs):
        return self.call('get_aux_io_param', kwargs=kwargs)

    def get_mode(self, **kwargs):
        return self.call('get_mode', kwargs=kwargs)

    def get_samples_per_record(self, **kwargs):
        return self.call('get_samples_per_record', kwargs=kwargs)

    def get_records_per_buffer(self, **kwargs):
        return self.call('get_records_per_buffer', kwargs=kwargs)

    def get_buffers_per_acquisition(self, **kwargs):
        return self.call('get_buffers_per_acquisition', kwargs=kwargs)

    def get_channel_selection(self, **kwargs):
        return self.call('get_channel_selection', kwargs=kwargs)

    def get_transfer_offset(self, **kwargs):
        return self.call('get_transfer_offset', kwargs=kwargs)

    def get_external_startcapture(self, **kwargs):
        return self.call('get_external_startcapture', kwargs=kwargs)

    def get_enable_record_headers(self, **kwargs):
        return self.call('get_enable_record_headers', kwargs=kwargs)

    def get_alloc_buffers(self, **kwargs):
        return self.call('get_alloc_buffers', kwargs=kwargs)

    def get_fifo_only_streaming(self, **kwargs):
        return self.call('get_fifo_only_streaming', kwargs=kwargs)

    def get_interleave_samples(self, **kwargs):
        return self.call('get_interleave_samples', kwargs=kwargs)

    def get_get_processed_data(self, **kwargs):
        return self.call('get_get_processed_data', kwargs=kwargs)

    def get_allocated_buffers(self, **kwargs):
        return self.call('get_allocated_buffers', kwargs=kwargs)

    def get_buffer_timeout(self, **kwargs):
        return self.call('get_buffer_timeout', kwargs=kwargs)

    def get_trigger_holdoff(self, **kwargs):
        return self.call('get_trigger_holdoff', kwargs=kwargs)

    def set_trigger_holdoff(self, **kwargs):
        return self.call('set_trigger_holdoff', kwargs=kwargs)

    def find_boards(self, **kwargs):
        return self.call('find_boards', kwargs=kwargs)

    def get_board_info(self, **kwargs):
        return self.call('get_board_info', kwargs=kwargs)

    def get_idn(self, **kwargs):
        return self.call('get_idn', kwargs=kwargs)

    def syncing(self, **kwargs):
        return self.call('syncing', kwargs=kwargs)

    def sync_settings_to_card(self, **kwargs):
        return self.call('sync_settings_to_card', kwargs=kwargs)

    def allocate_and_post_buffer(self, **kwargs):
        return self.call('allocate_and_post_buffer', kwargs=kwargs)

    def acquire(self, **kwargs):
        return self.call('acquire', kwargs=kwargs)

    def clear_buffers(self, **kwargs):
        return self.call('clear_buffers', kwargs=kwargs)

    def signal_to_volt(self, **kwargs):
        return self.call('signal_to_volt', kwargs=kwargs)

    def get_num_channels(self, **kwargs):
        return self.call('get_num_channels', kwargs=kwargs)

    def connect_message(self, **kwargs):
        return self.call('connect_message', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def close_all(self, **kwargs):
        return self.call('close_all', kwargs=kwargs)

    def record_instance(self, **kwargs):
        return self.call('record_instance', kwargs=kwargs)

    def instances(self, **kwargs):
        return self.call('instances', kwargs=kwargs)

    def remove_instance(self, **kwargs):
        return self.call('remove_instance', kwargs=kwargs)

    def find_instrument(self, **kwargs):
        return self.call('find_instrument', kwargs=kwargs)

    def exist(self, **kwargs):
        return self.call('exist', kwargs=kwargs)

    def is_valid(self, **kwargs):
        return self.call('is_valid', kwargs=kwargs)

    def write_raw(self, **kwargs):
        return self.call('write_raw', kwargs=kwargs)

    def ask_raw(self, **kwargs):
        return self.call('ask_raw', kwargs=kwargs)

    def label(self, **kwargs):
        return self.call('label', kwargs=kwargs)

    def add_parameter(self, **kwargs):
        return self.call('add_parameter', kwargs=kwargs)

    def remove_parameter(self, **kwargs):
        return self.call('remove_parameter', kwargs=kwargs)

    def add_function(self, **kwargs):
        return self.call('add_function', kwargs=kwargs)

    def add_submodule(self, **kwargs):
        return self.call('add_submodule', kwargs=kwargs)

    def get_component(self, **kwargs):
        return self.call('get_component', kwargs=kwargs)

    def snapshot_base(self, **kwargs):
        return self.call('snapshot_base', kwargs=kwargs)

    def print_readable_snapshot(self, **kwargs):
        return self.call('print_readable_snapshot', kwargs=kwargs)

    def invalidate_cache(self, **kwargs):
        return self.call('invalidate_cache', kwargs=kwargs)

    def parent(self, **kwargs):
        return self.call('parent', kwargs=kwargs)

    def ancestors(self, **kwargs):
        return self.call('ancestors', kwargs=kwargs)

    def root_instrument(self, **kwargs):
        return self.call('root_instrument', kwargs=kwargs)

    def name_parts(self, **kwargs):
        return self.call('name_parts', kwargs=kwargs)

    def full_name(self, **kwargs):
        return self.call('full_name', kwargs=kwargs)

    def name(self, **kwargs):
        return self.call('name', kwargs=kwargs)

    def short_name(self, **kwargs):
        return self.call('short_name', kwargs=kwargs)

    def set(self, **kwargs):
        return self.call('set', kwargs=kwargs)

    def get(self, **kwargs):
        return self.call('get', kwargs=kwargs)

    def call(self, **kwargs):
        return self.call('call', kwargs=kwargs)

    def validate_status(self, **kwargs):
        return self.call('validate_status', kwargs=kwargs)

    def load_metadata(self, **kwargs):
        return self.call('load_metadata', kwargs=kwargs)

    def snapshot(self, **kwargs):
        return self.call('snapshot', kwargs=kwargs)

