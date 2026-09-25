from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentVapourtecR2R43(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/cambridge-cares__TheWorldAvatar', 'source_file': 'Agents/utils/chemistry_and_robots/chemistry_and_robots/kg_operations/sparql_client.py', 'class_name': 'ChemistryAndRobotsSparqlClient', 'import_roots': [], 'candidate_methods': ['get_ontology_tbox_version', 'upload_ontology_tbox', 'get_all_chemical_reaction_iri', 'get_all_rxn_exp_given_chem_rxn', 'get_all_rxn_exp_with_target_perfind_given_chem_rxn', 'collect_triples_for_new_experiment', 'get_doe_instance', 'getDoEDomain', 'get_fixed_parameters', 'getDesignVariables', 'getSystemResponses', 'getDoEHistoricalData', 'getReactionExperiment', 'get_chemical_reaction', 'get_chemical_reaction_given_iri', 'locate_possible_input_chemical', 'get_ontokin_species_from_chem_rxn', 'get_input_chemical_of_rxn_exp', 'get_output_chemical_of_rxn_exp', 'get_chemical', 'construct_query_for_autosampler', 'get_all_autosampler_with_fill', 'getExpReactionCondition', 'getExpPerformanceIndicator', 'getDoEStrategy', 'getTSEMOSettings', 'get_newstbo_settings', 'getNewExperimentFromDoE', 'collect_triples_for_equip_settings', 'get_preferred_vapourtec_rs400', 'update_vapourtec_rs400_state', 'get_autosampler', 'get_vapourtec_rs400', 'get_vapourtec_rs400_given_autosampler', 'vapourtec_rs400_is_running_reaction', 'get_rxn_exp_assigned_to_r4_reactor', 'get_r4_reactor_rxn_exp_assigned_to', 'get_r4_reactor_given_vapourtec_rs400', 'get_r2_pump_given_vapourtec_rs400', 'get_reagent_bottle', 'assign_rxn_exp_to_r4_reactor', 'remove_rxn_exp_from_r4_reactor', 'get_prior_rxn_exp_in_queue', 'detect_new_hplc_report', 'collect_triples_for_hplc_job', 'upload_raw_hplc_report_to_kg', 'register_agent_with_hardware', 'identify_rxn_exp_when_uploading_hplc_report', 'get_raw_hplc_report_remote_path_and_extension', 'get_matching_species_from_hplc_results', 'get_internal_standard', 'get_hplc_method_given_hplc_report', 'get_hplc_method', 'get_species_molar_mass_kilogrampermole', 'get_species_density', 'get_species_material_cost', 'get_species_eco_score', 'get_reactor_volume_given_reactor', 'get_rxn_exp_associated_with_hplc_report', 'get_internal_standard_associated_with_hplc_report', 'process_raw_hplc_report', 'get_chromatogram_point_of_hplc_report', 'get_existing_hplc_report', 'get_hplc_job_given_hplc_report_iri', 'get_hplc_job_given_hplc_report_instance', 'get_hplc_job', 'download_remote_raw_hplc_report', 'connect_hplc_report_with_chemical_amount', 'get_remote_hplc_report_path_given_local_file', 'collect_triples_for_performance_indicators', 'collect_triples_for_chromatogram_point', 'collect_triples_for_output_chemical_of_chem_amount', 'update_vapourtec_autosampler_liquid_level_millilitre', 'update_waste_bottle_liquid_level_millilitre', 'update_reagent_bottle_liquid_level_millilitre', 'create_chemical_amount_for_reaction_outlet', 'create_chemical_amount_for_outlet_to_waste', 'release_vapourtec_rs400_settings', 'upload_vapourtec_input_file_to_kg', 'get_vapourtec_input_file', 'get_hplc_given_vapourtec_rs400', 'detect_new_hplc_report_from_hplc_derivation', 'get_all_laboratories', 'check_if_triple_exist'], 'action_targets': {}, 'metadata': {'repo': 'cambridge-cares/TheWorldAvatar', 'repo_url': 'https://github.com/cambridge-cares/TheWorldAvatar', 'brand': 'Vapourtec', 'model': 'R2/R4', 'device_type_cn': '微通道反应器', 'device_type_en': 'Microreactor', 'source_framework': '专用驱动', 'tag_id': '4388', 'tag_name': '微通道反应器', 'tag_name_en': 'Microreactor', 'candidate_score': 710, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_ontology_tbox_version(self, **kwargs):
        return self.call('get_ontology_tbox_version', kwargs=kwargs)

    def upload_ontology_tbox(self, **kwargs):
        return self.call('upload_ontology_tbox', kwargs=kwargs)

    def get_all_chemical_reaction_iri(self, **kwargs):
        return self.call('get_all_chemical_reaction_iri', kwargs=kwargs)

    def get_all_rxn_exp_given_chem_rxn(self, **kwargs):
        return self.call('get_all_rxn_exp_given_chem_rxn', kwargs=kwargs)

    def get_all_rxn_exp_with_target_perfind_given_chem_rxn(self, **kwargs):
        return self.call('get_all_rxn_exp_with_target_perfind_given_chem_rxn', kwargs=kwargs)

    def collect_triples_for_new_experiment(self, **kwargs):
        return self.call('collect_triples_for_new_experiment', kwargs=kwargs)

    def get_doe_instance(self, **kwargs):
        return self.call('get_doe_instance', kwargs=kwargs)

    def getDoEDomain(self, **kwargs):
        return self.call('getDoEDomain', kwargs=kwargs)

    def get_fixed_parameters(self, **kwargs):
        return self.call('get_fixed_parameters', kwargs=kwargs)

    def getDesignVariables(self, **kwargs):
        return self.call('getDesignVariables', kwargs=kwargs)

    def getSystemResponses(self, **kwargs):
        return self.call('getSystemResponses', kwargs=kwargs)

    def getDoEHistoricalData(self, **kwargs):
        return self.call('getDoEHistoricalData', kwargs=kwargs)

    def getReactionExperiment(self, **kwargs):
        return self.call('getReactionExperiment', kwargs=kwargs)

    def get_chemical_reaction(self, **kwargs):
        return self.call('get_chemical_reaction', kwargs=kwargs)

    def get_chemical_reaction_given_iri(self, **kwargs):
        return self.call('get_chemical_reaction_given_iri', kwargs=kwargs)

    def locate_possible_input_chemical(self, **kwargs):
        return self.call('locate_possible_input_chemical', kwargs=kwargs)

    def get_ontokin_species_from_chem_rxn(self, **kwargs):
        return self.call('get_ontokin_species_from_chem_rxn', kwargs=kwargs)

    def get_input_chemical_of_rxn_exp(self, **kwargs):
        return self.call('get_input_chemical_of_rxn_exp', kwargs=kwargs)

    def get_output_chemical_of_rxn_exp(self, **kwargs):
        return self.call('get_output_chemical_of_rxn_exp', kwargs=kwargs)

    def get_chemical(self, **kwargs):
        return self.call('get_chemical', kwargs=kwargs)

    def construct_query_for_autosampler(self, **kwargs):
        return self.call('construct_query_for_autosampler', kwargs=kwargs)

    def get_all_autosampler_with_fill(self, **kwargs):
        return self.call('get_all_autosampler_with_fill', kwargs=kwargs)

    def getExpReactionCondition(self, **kwargs):
        return self.call('getExpReactionCondition', kwargs=kwargs)

    def getExpPerformanceIndicator(self, **kwargs):
        return self.call('getExpPerformanceIndicator', kwargs=kwargs)

    def getDoEStrategy(self, **kwargs):
        return self.call('getDoEStrategy', kwargs=kwargs)

    def getTSEMOSettings(self, **kwargs):
        return self.call('getTSEMOSettings', kwargs=kwargs)

    def get_newstbo_settings(self, **kwargs):
        return self.call('get_newstbo_settings', kwargs=kwargs)

    def getNewExperimentFromDoE(self, **kwargs):
        return self.call('getNewExperimentFromDoE', kwargs=kwargs)

    def collect_triples_for_equip_settings(self, **kwargs):
        return self.call('collect_triples_for_equip_settings', kwargs=kwargs)

    def get_preferred_vapourtec_rs400(self, **kwargs):
        return self.call('get_preferred_vapourtec_rs400', kwargs=kwargs)

    def update_vapourtec_rs400_state(self, **kwargs):
        return self.call('update_vapourtec_rs400_state', kwargs=kwargs)

    def get_autosampler(self, **kwargs):
        return self.call('get_autosampler', kwargs=kwargs)

    def get_vapourtec_rs400(self, **kwargs):
        return self.call('get_vapourtec_rs400', kwargs=kwargs)

    def get_vapourtec_rs400_given_autosampler(self, **kwargs):
        return self.call('get_vapourtec_rs400_given_autosampler', kwargs=kwargs)

    def vapourtec_rs400_is_running_reaction(self, **kwargs):
        return self.call('vapourtec_rs400_is_running_reaction', kwargs=kwargs)

    def get_rxn_exp_assigned_to_r4_reactor(self, **kwargs):
        return self.call('get_rxn_exp_assigned_to_r4_reactor', kwargs=kwargs)

    def get_r4_reactor_rxn_exp_assigned_to(self, **kwargs):
        return self.call('get_r4_reactor_rxn_exp_assigned_to', kwargs=kwargs)

    def get_r4_reactor_given_vapourtec_rs400(self, **kwargs):
        return self.call('get_r4_reactor_given_vapourtec_rs400', kwargs=kwargs)

    def get_r2_pump_given_vapourtec_rs400(self, **kwargs):
        return self.call('get_r2_pump_given_vapourtec_rs400', kwargs=kwargs)

    def get_reagent_bottle(self, **kwargs):
        return self.call('get_reagent_bottle', kwargs=kwargs)

    def assign_rxn_exp_to_r4_reactor(self, **kwargs):
        return self.call('assign_rxn_exp_to_r4_reactor', kwargs=kwargs)

    def remove_rxn_exp_from_r4_reactor(self, **kwargs):
        return self.call('remove_rxn_exp_from_r4_reactor', kwargs=kwargs)

    def get_prior_rxn_exp_in_queue(self, **kwargs):
        return self.call('get_prior_rxn_exp_in_queue', kwargs=kwargs)

    def detect_new_hplc_report(self, **kwargs):
        return self.call('detect_new_hplc_report', kwargs=kwargs)

    def collect_triples_for_hplc_job(self, **kwargs):
        return self.call('collect_triples_for_hplc_job', kwargs=kwargs)

    def upload_raw_hplc_report_to_kg(self, **kwargs):
        return self.call('upload_raw_hplc_report_to_kg', kwargs=kwargs)

    def register_agent_with_hardware(self, **kwargs):
        return self.call('register_agent_with_hardware', kwargs=kwargs)

    def identify_rxn_exp_when_uploading_hplc_report(self, **kwargs):
        return self.call('identify_rxn_exp_when_uploading_hplc_report', kwargs=kwargs)

    def get_raw_hplc_report_remote_path_and_extension(self, **kwargs):
        return self.call('get_raw_hplc_report_remote_path_and_extension', kwargs=kwargs)

    def get_matching_species_from_hplc_results(self, **kwargs):
        return self.call('get_matching_species_from_hplc_results', kwargs=kwargs)

    def get_internal_standard(self, **kwargs):
        return self.call('get_internal_standard', kwargs=kwargs)

    def get_hplc_method_given_hplc_report(self, **kwargs):
        return self.call('get_hplc_method_given_hplc_report', kwargs=kwargs)

    def get_hplc_method(self, **kwargs):
        return self.call('get_hplc_method', kwargs=kwargs)

    def get_species_molar_mass_kilogrampermole(self, **kwargs):
        return self.call('get_species_molar_mass_kilogrampermole', kwargs=kwargs)

    def get_species_density(self, **kwargs):
        return self.call('get_species_density', kwargs=kwargs)

    def get_species_material_cost(self, **kwargs):
        return self.call('get_species_material_cost', kwargs=kwargs)

    def get_species_eco_score(self, **kwargs):
        return self.call('get_species_eco_score', kwargs=kwargs)

    def get_reactor_volume_given_reactor(self, **kwargs):
        return self.call('get_reactor_volume_given_reactor', kwargs=kwargs)

    def get_rxn_exp_associated_with_hplc_report(self, **kwargs):
        return self.call('get_rxn_exp_associated_with_hplc_report', kwargs=kwargs)

    def get_internal_standard_associated_with_hplc_report(self, **kwargs):
        return self.call('get_internal_standard_associated_with_hplc_report', kwargs=kwargs)

    def process_raw_hplc_report(self, **kwargs):
        return self.call('process_raw_hplc_report', kwargs=kwargs)

    def get_chromatogram_point_of_hplc_report(self, **kwargs):
        return self.call('get_chromatogram_point_of_hplc_report', kwargs=kwargs)

    def get_existing_hplc_report(self, **kwargs):
        return self.call('get_existing_hplc_report', kwargs=kwargs)

    def get_hplc_job_given_hplc_report_iri(self, **kwargs):
        return self.call('get_hplc_job_given_hplc_report_iri', kwargs=kwargs)

    def get_hplc_job_given_hplc_report_instance(self, **kwargs):
        return self.call('get_hplc_job_given_hplc_report_instance', kwargs=kwargs)

    def get_hplc_job(self, **kwargs):
        return self.call('get_hplc_job', kwargs=kwargs)

    def download_remote_raw_hplc_report(self, **kwargs):
        return self.call('download_remote_raw_hplc_report', kwargs=kwargs)

    def connect_hplc_report_with_chemical_amount(self, **kwargs):
        return self.call('connect_hplc_report_with_chemical_amount', kwargs=kwargs)

    def get_remote_hplc_report_path_given_local_file(self, **kwargs):
        return self.call('get_remote_hplc_report_path_given_local_file', kwargs=kwargs)

    def collect_triples_for_performance_indicators(self, **kwargs):
        return self.call('collect_triples_for_performance_indicators', kwargs=kwargs)

    def collect_triples_for_chromatogram_point(self, **kwargs):
        return self.call('collect_triples_for_chromatogram_point', kwargs=kwargs)

    def collect_triples_for_output_chemical_of_chem_amount(self, **kwargs):
        return self.call('collect_triples_for_output_chemical_of_chem_amount', kwargs=kwargs)

    def update_vapourtec_autosampler_liquid_level_millilitre(self, **kwargs):
        return self.call('update_vapourtec_autosampler_liquid_level_millilitre', kwargs=kwargs)

    def update_waste_bottle_liquid_level_millilitre(self, **kwargs):
        return self.call('update_waste_bottle_liquid_level_millilitre', kwargs=kwargs)

    def update_reagent_bottle_liquid_level_millilitre(self, **kwargs):
        return self.call('update_reagent_bottle_liquid_level_millilitre', kwargs=kwargs)

    def create_chemical_amount_for_reaction_outlet(self, **kwargs):
        return self.call('create_chemical_amount_for_reaction_outlet', kwargs=kwargs)

    def create_chemical_amount_for_outlet_to_waste(self, **kwargs):
        return self.call('create_chemical_amount_for_outlet_to_waste', kwargs=kwargs)

    def release_vapourtec_rs400_settings(self, **kwargs):
        return self.call('release_vapourtec_rs400_settings', kwargs=kwargs)

    def upload_vapourtec_input_file_to_kg(self, **kwargs):
        return self.call('upload_vapourtec_input_file_to_kg', kwargs=kwargs)

    def get_vapourtec_input_file(self, **kwargs):
        return self.call('get_vapourtec_input_file', kwargs=kwargs)

    def get_hplc_given_vapourtec_rs400(self, **kwargs):
        return self.call('get_hplc_given_vapourtec_rs400', kwargs=kwargs)

    def detect_new_hplc_report_from_hplc_derivation(self, **kwargs):
        return self.call('detect_new_hplc_report_from_hplc_derivation', kwargs=kwargs)

    def get_all_laboratories(self, **kwargs):
        return self.call('get_all_laboratories', kwargs=kwargs)

    def check_if_triple_exist(self, **kwargs):
        return self.call('check_if_triple_exist', kwargs=kwargs)

