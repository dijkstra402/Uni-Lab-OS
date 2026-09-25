from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentKeithley2636b(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/microsoft__Qcodes', 'source_file': 'src/qcodes/instrument_drivers/Keysight/keysightb1500/message_builder.py', 'class_name': 'MessageBuilder', 'import_roots': ['src'], 'candidate_methods': ['message', 'clear_message_queue', 'aad', 'ab', 'ach', 'act', 'acv', 'adj', 'adj_query', 'ait', 'aitm', 'aitm_query', 'als', 'als_query', 'alw', 'alw_query', 'av', 'az', 'bc', 'bdm', 'bdt', 'bdv', 'bgi', 'bgv', 'bsi', 'bsm', 'bssi', 'bssv', 'bst', 'bsv', 'bsvm', 'ca', 'cal_query', 'cl', 'clcorr', 'cm', 'cmm', 'cn', 'cnx', 'corr_query', 'corrdt', 'corrdt_query', 'corrl', 'corrl_query', 'corrser_query', 'corrst', 'corrst_query', 'dcorr', 'dcorr_query', 'dcv', 'di', 'diag_query', 'do', 'dsmplarm', 'dsmplflush', 'dsmplsetup', 'dv', 'dz', 'emg_query', 'end', 'erc', 'ercmaa', 'ercmaa_query', 'ercmagrd', 'ercmagrd_query', 'ercmaio', 'ercmaio_query', 'ercmapfgd', 'erhpa', 'erhpa_query', 'erhpe', 'erhpe_query', 'erhpl', 'erhpl_query', 'erhpp', 'erhpp_query', 'erhpqg', 'erhpqg_query', 'erhpr', 'erhpr_query', 'erhps', 'erhps_query', 'erhvca', 'erhvca_query', 'erhvctst_query', 'erhvp', 'erhvp_query', 'erhvpv', 'erhvs', 'erhvs_query', 'erm', 'ermod', 'ermod_query', 'erpfda', 'erpfda_query', 'erpfdp', 'erpfdp_query', 'erpfds', 'erpfds_query', 'erpfga', 'erpfga_query', 'erpfgp', 'erpfgp_query', 'erpfgr', 'erpfgr_query', 'erpfqg', 'erpfqg_query', 'erpftemp_query', 'erpfuhca', 'erpfuhca_query', 'erpfuhccal_query', 'erpfuhcmax_query', 'erpfuhctst', 'err_query', 'errx_query', 'ers_query', 'erssp', 'erssp_query', 'eruhva', 'eruhva_query', 'fc', 'fl', 'fmt', 'hvsmuop', 'hvsmuop_query', 'idn_query', 'imp', 'in_', 'intlkvth', 'intlkvth_query', 'lgi', 'lgv', 'lim', 'lim_query', 'lmn', 'lop_query', 'lrn_query', 'lsi', 'lsm', 'lssi', 'lssv', 'lst_query', 'lstm', 'lsv', 'lsvm', 'mcc', 'mcpnt', 'mcpnx', 'mcpt', 'mcpws', 'mcpwnx', 'mdcv', 'mi', 'ml', 'mm', 'msc', 'msp', 'mt', 'mtdcv', 'mv', 'nub_query', 'odsw', 'odsw_query', 'opc_query', 'os', 'osx', 'pa', 'pad', 'pax', 'pch', 'pch_query', 'pdcv', 'pi', 'pt', 'ptdcv', 'pv', 'pwdcv', 'pwi', 'pwv', 'qsc', 'qsl', 'qsm', 'qso', 'qsr', 'qst', 'qsv', 'qsz', 'rc', 'rcv', 'ri', 'rm', 'rst', 'ru', 'rv', 'rz', 'sal', 'sap', 'sar', 'scr', 'ser', 'ser_query', 'sim', 'sim_query', 'sopc', 'sopc_query', 'sovc', 'sovc_query', 'spm', 'spm_query', 'spp', 'spper', 'spper_query', 'sprm', 'sprm_query', 'spst_query', 'spt', 'spt_query', 'spupd', 'spv', 'spv_query', 'sre', 'sre_query', 'srp', 'ssl', 'ssp', 'ssr', 'st', 'stb_query', 'stgp', 'stgp_query', 'tacv', 'tc', 'tdcv', 'tdi', 'tdv', 'tgmo', 'tgp', 'tgpc', 'tgsi', 'tgso', 'tgxo', 'ti', 'tiv', 'tm', 'tmacv', 'tmdcv', 'tsc', 'tsq', 'tsr', 'tst', 'ttc', 'tti', 'ttiv', 'ttv', 'tv', 'unt_query', 'var', 'var_query', 'wacv', 'wat', 'wdcv', 'wfc', 'wi', 'wm', 'wmacv', 'wmdcv', 'wmfc', 'wncc', 'wnu_query', 'wnx', 'ws', 'wsi', 'wsv', 'wt', 'wtacv', 'wtdcv', 'wtfc', 'wv', 'wz_query', 'xe'], 'action_targets': {}, 'metadata': {'repo': 'microsoft/Qcodes', 'repo_url': 'https://github.com/microsoft/Qcodes', 'brand': 'Keithley', 'model': '2636B', 'device_type_cn': '源表', 'device_type_en': 'SourceMeter', 'source_framework': 'QCoDeS', 'tag_id': '4425', 'tag_name': '电化学工作站', 'tag_name_en': 'Electrochemical Workstation', 'candidate_score': 2278, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def message(self, **kwargs):
        return self.call('message', kwargs=kwargs)

    def clear_message_queue(self, **kwargs):
        return self.call('clear_message_queue', kwargs=kwargs)

    def aad(self, **kwargs):
        return self.call('aad', kwargs=kwargs)

    def ab(self, **kwargs):
        return self.call('ab', kwargs=kwargs)

    def ach(self, **kwargs):
        return self.call('ach', kwargs=kwargs)

    def act(self, **kwargs):
        return self.call('act', kwargs=kwargs)

    def acv(self, **kwargs):
        return self.call('acv', kwargs=kwargs)

    def adj(self, **kwargs):
        return self.call('adj', kwargs=kwargs)

    def adj_query(self, **kwargs):
        return self.call('adj_query', kwargs=kwargs)

    def ait(self, **kwargs):
        return self.call('ait', kwargs=kwargs)

    def aitm(self, **kwargs):
        return self.call('aitm', kwargs=kwargs)

    def aitm_query(self, **kwargs):
        return self.call('aitm_query', kwargs=kwargs)

    def als(self, **kwargs):
        return self.call('als', kwargs=kwargs)

    def als_query(self, **kwargs):
        return self.call('als_query', kwargs=kwargs)

    def alw(self, **kwargs):
        return self.call('alw', kwargs=kwargs)

    def alw_query(self, **kwargs):
        return self.call('alw_query', kwargs=kwargs)

    def av(self, **kwargs):
        return self.call('av', kwargs=kwargs)

    def az(self, **kwargs):
        return self.call('az', kwargs=kwargs)

    def bc(self, **kwargs):
        return self.call('bc', kwargs=kwargs)

    def bdm(self, **kwargs):
        return self.call('bdm', kwargs=kwargs)

    def bdt(self, **kwargs):
        return self.call('bdt', kwargs=kwargs)

    def bdv(self, **kwargs):
        return self.call('bdv', kwargs=kwargs)

    def bgi(self, **kwargs):
        return self.call('bgi', kwargs=kwargs)

    def bgv(self, **kwargs):
        return self.call('bgv', kwargs=kwargs)

    def bsi(self, **kwargs):
        return self.call('bsi', kwargs=kwargs)

    def bsm(self, **kwargs):
        return self.call('bsm', kwargs=kwargs)

    def bssi(self, **kwargs):
        return self.call('bssi', kwargs=kwargs)

    def bssv(self, **kwargs):
        return self.call('bssv', kwargs=kwargs)

    def bst(self, **kwargs):
        return self.call('bst', kwargs=kwargs)

    def bsv(self, **kwargs):
        return self.call('bsv', kwargs=kwargs)

    def bsvm(self, **kwargs):
        return self.call('bsvm', kwargs=kwargs)

    def ca(self, **kwargs):
        return self.call('ca', kwargs=kwargs)

    def cal_query(self, **kwargs):
        return self.call('cal_query', kwargs=kwargs)

    def cl(self, **kwargs):
        return self.call('cl', kwargs=kwargs)

    def clcorr(self, **kwargs):
        return self.call('clcorr', kwargs=kwargs)

    def cm(self, **kwargs):
        return self.call('cm', kwargs=kwargs)

    def cmm(self, **kwargs):
        return self.call('cmm', kwargs=kwargs)

    def cn(self, **kwargs):
        return self.call('cn', kwargs=kwargs)

    def cnx(self, **kwargs):
        return self.call('cnx', kwargs=kwargs)

    def corr_query(self, **kwargs):
        return self.call('corr_query', kwargs=kwargs)

    def corrdt(self, **kwargs):
        return self.call('corrdt', kwargs=kwargs)

    def corrdt_query(self, **kwargs):
        return self.call('corrdt_query', kwargs=kwargs)

    def corrl(self, **kwargs):
        return self.call('corrl', kwargs=kwargs)

    def corrl_query(self, **kwargs):
        return self.call('corrl_query', kwargs=kwargs)

    def corrser_query(self, **kwargs):
        return self.call('corrser_query', kwargs=kwargs)

    def corrst(self, **kwargs):
        return self.call('corrst', kwargs=kwargs)

    def corrst_query(self, **kwargs):
        return self.call('corrst_query', kwargs=kwargs)

    def dcorr(self, **kwargs):
        return self.call('dcorr', kwargs=kwargs)

    def dcorr_query(self, **kwargs):
        return self.call('dcorr_query', kwargs=kwargs)

    def dcv(self, **kwargs):
        return self.call('dcv', kwargs=kwargs)

    def di(self, **kwargs):
        return self.call('di', kwargs=kwargs)

    def diag_query(self, **kwargs):
        return self.call('diag_query', kwargs=kwargs)

    def do(self, **kwargs):
        return self.call('do', kwargs=kwargs)

    def dsmplarm(self, **kwargs):
        return self.call('dsmplarm', kwargs=kwargs)

    def dsmplflush(self, **kwargs):
        return self.call('dsmplflush', kwargs=kwargs)

    def dsmplsetup(self, **kwargs):
        return self.call('dsmplsetup', kwargs=kwargs)

    def dv(self, **kwargs):
        return self.call('dv', kwargs=kwargs)

    def dz(self, **kwargs):
        return self.call('dz', kwargs=kwargs)

    def emg_query(self, **kwargs):
        return self.call('emg_query', kwargs=kwargs)

    def end(self, **kwargs):
        return self.call('end', kwargs=kwargs)

    def erc(self, **kwargs):
        return self.call('erc', kwargs=kwargs)

    def ercmaa(self, **kwargs):
        return self.call('ercmaa', kwargs=kwargs)

    def ercmaa_query(self, **kwargs):
        return self.call('ercmaa_query', kwargs=kwargs)

    def ercmagrd(self, **kwargs):
        return self.call('ercmagrd', kwargs=kwargs)

    def ercmagrd_query(self, **kwargs):
        return self.call('ercmagrd_query', kwargs=kwargs)

    def ercmaio(self, **kwargs):
        return self.call('ercmaio', kwargs=kwargs)

    def ercmaio_query(self, **kwargs):
        return self.call('ercmaio_query', kwargs=kwargs)

    def ercmapfgd(self, **kwargs):
        return self.call('ercmapfgd', kwargs=kwargs)

    def erhpa(self, **kwargs):
        return self.call('erhpa', kwargs=kwargs)

    def erhpa_query(self, **kwargs):
        return self.call('erhpa_query', kwargs=kwargs)

    def erhpe(self, **kwargs):
        return self.call('erhpe', kwargs=kwargs)

    def erhpe_query(self, **kwargs):
        return self.call('erhpe_query', kwargs=kwargs)

    def erhpl(self, **kwargs):
        return self.call('erhpl', kwargs=kwargs)

    def erhpl_query(self, **kwargs):
        return self.call('erhpl_query', kwargs=kwargs)

    def erhpp(self, **kwargs):
        return self.call('erhpp', kwargs=kwargs)

    def erhpp_query(self, **kwargs):
        return self.call('erhpp_query', kwargs=kwargs)

    def erhpqg(self, **kwargs):
        return self.call('erhpqg', kwargs=kwargs)

    def erhpqg_query(self, **kwargs):
        return self.call('erhpqg_query', kwargs=kwargs)

    def erhpr(self, **kwargs):
        return self.call('erhpr', kwargs=kwargs)

    def erhpr_query(self, **kwargs):
        return self.call('erhpr_query', kwargs=kwargs)

    def erhps(self, **kwargs):
        return self.call('erhps', kwargs=kwargs)

    def erhps_query(self, **kwargs):
        return self.call('erhps_query', kwargs=kwargs)

    def erhvca(self, **kwargs):
        return self.call('erhvca', kwargs=kwargs)

    def erhvca_query(self, **kwargs):
        return self.call('erhvca_query', kwargs=kwargs)

    def erhvctst_query(self, **kwargs):
        return self.call('erhvctst_query', kwargs=kwargs)

    def erhvp(self, **kwargs):
        return self.call('erhvp', kwargs=kwargs)

    def erhvp_query(self, **kwargs):
        return self.call('erhvp_query', kwargs=kwargs)

    def erhvpv(self, **kwargs):
        return self.call('erhvpv', kwargs=kwargs)

    def erhvs(self, **kwargs):
        return self.call('erhvs', kwargs=kwargs)

    def erhvs_query(self, **kwargs):
        return self.call('erhvs_query', kwargs=kwargs)

    def erm(self, **kwargs):
        return self.call('erm', kwargs=kwargs)

    def ermod(self, **kwargs):
        return self.call('ermod', kwargs=kwargs)

    def ermod_query(self, **kwargs):
        return self.call('ermod_query', kwargs=kwargs)

    def erpfda(self, **kwargs):
        return self.call('erpfda', kwargs=kwargs)

    def erpfda_query(self, **kwargs):
        return self.call('erpfda_query', kwargs=kwargs)

    def erpfdp(self, **kwargs):
        return self.call('erpfdp', kwargs=kwargs)

    def erpfdp_query(self, **kwargs):
        return self.call('erpfdp_query', kwargs=kwargs)

    def erpfds(self, **kwargs):
        return self.call('erpfds', kwargs=kwargs)

    def erpfds_query(self, **kwargs):
        return self.call('erpfds_query', kwargs=kwargs)

    def erpfga(self, **kwargs):
        return self.call('erpfga', kwargs=kwargs)

    def erpfga_query(self, **kwargs):
        return self.call('erpfga_query', kwargs=kwargs)

    def erpfgp(self, **kwargs):
        return self.call('erpfgp', kwargs=kwargs)

    def erpfgp_query(self, **kwargs):
        return self.call('erpfgp_query', kwargs=kwargs)

    def erpfgr(self, **kwargs):
        return self.call('erpfgr', kwargs=kwargs)

    def erpfgr_query(self, **kwargs):
        return self.call('erpfgr_query', kwargs=kwargs)

    def erpfqg(self, **kwargs):
        return self.call('erpfqg', kwargs=kwargs)

    def erpfqg_query(self, **kwargs):
        return self.call('erpfqg_query', kwargs=kwargs)

    def erpftemp_query(self, **kwargs):
        return self.call('erpftemp_query', kwargs=kwargs)

    def erpfuhca(self, **kwargs):
        return self.call('erpfuhca', kwargs=kwargs)

    def erpfuhca_query(self, **kwargs):
        return self.call('erpfuhca_query', kwargs=kwargs)

    def erpfuhccal_query(self, **kwargs):
        return self.call('erpfuhccal_query', kwargs=kwargs)

    def erpfuhcmax_query(self, **kwargs):
        return self.call('erpfuhcmax_query', kwargs=kwargs)

    def erpfuhctst(self, **kwargs):
        return self.call('erpfuhctst', kwargs=kwargs)

    def err_query(self, **kwargs):
        return self.call('err_query', kwargs=kwargs)

    def errx_query(self, **kwargs):
        return self.call('errx_query', kwargs=kwargs)

    def ers_query(self, **kwargs):
        return self.call('ers_query', kwargs=kwargs)

    def erssp(self, **kwargs):
        return self.call('erssp', kwargs=kwargs)

    def erssp_query(self, **kwargs):
        return self.call('erssp_query', kwargs=kwargs)

    def eruhva(self, **kwargs):
        return self.call('eruhva', kwargs=kwargs)

    def eruhva_query(self, **kwargs):
        return self.call('eruhva_query', kwargs=kwargs)

    def fc(self, **kwargs):
        return self.call('fc', kwargs=kwargs)

    def fl(self, **kwargs):
        return self.call('fl', kwargs=kwargs)

    def fmt(self, **kwargs):
        return self.call('fmt', kwargs=kwargs)

    def hvsmuop(self, **kwargs):
        return self.call('hvsmuop', kwargs=kwargs)

    def hvsmuop_query(self, **kwargs):
        return self.call('hvsmuop_query', kwargs=kwargs)

    def idn_query(self, **kwargs):
        return self.call('idn_query', kwargs=kwargs)

    def imp(self, **kwargs):
        return self.call('imp', kwargs=kwargs)

    def in_(self, **kwargs):
        return self.call('in_', kwargs=kwargs)

    def intlkvth(self, **kwargs):
        return self.call('intlkvth', kwargs=kwargs)

    def intlkvth_query(self, **kwargs):
        return self.call('intlkvth_query', kwargs=kwargs)

    def lgi(self, **kwargs):
        return self.call('lgi', kwargs=kwargs)

    def lgv(self, **kwargs):
        return self.call('lgv', kwargs=kwargs)

    def lim(self, **kwargs):
        return self.call('lim', kwargs=kwargs)

    def lim_query(self, **kwargs):
        return self.call('lim_query', kwargs=kwargs)

    def lmn(self, **kwargs):
        return self.call('lmn', kwargs=kwargs)

    def lop_query(self, **kwargs):
        return self.call('lop_query', kwargs=kwargs)

    def lrn_query(self, **kwargs):
        return self.call('lrn_query', kwargs=kwargs)

    def lsi(self, **kwargs):
        return self.call('lsi', kwargs=kwargs)

    def lsm(self, **kwargs):
        return self.call('lsm', kwargs=kwargs)

    def lssi(self, **kwargs):
        return self.call('lssi', kwargs=kwargs)

    def lssv(self, **kwargs):
        return self.call('lssv', kwargs=kwargs)

    def lst_query(self, **kwargs):
        return self.call('lst_query', kwargs=kwargs)

    def lstm(self, **kwargs):
        return self.call('lstm', kwargs=kwargs)

    def lsv(self, **kwargs):
        return self.call('lsv', kwargs=kwargs)

    def lsvm(self, **kwargs):
        return self.call('lsvm', kwargs=kwargs)

    def mcc(self, **kwargs):
        return self.call('mcc', kwargs=kwargs)

    def mcpnt(self, **kwargs):
        return self.call('mcpnt', kwargs=kwargs)

    def mcpnx(self, **kwargs):
        return self.call('mcpnx', kwargs=kwargs)

    def mcpt(self, **kwargs):
        return self.call('mcpt', kwargs=kwargs)

    def mcpws(self, **kwargs):
        return self.call('mcpws', kwargs=kwargs)

    def mcpwnx(self, **kwargs):
        return self.call('mcpwnx', kwargs=kwargs)

    def mdcv(self, **kwargs):
        return self.call('mdcv', kwargs=kwargs)

    def mi(self, **kwargs):
        return self.call('mi', kwargs=kwargs)

    def ml(self, **kwargs):
        return self.call('ml', kwargs=kwargs)

    def mm(self, **kwargs):
        return self.call('mm', kwargs=kwargs)

    def msc(self, **kwargs):
        return self.call('msc', kwargs=kwargs)

    def msp(self, **kwargs):
        return self.call('msp', kwargs=kwargs)

    def mt(self, **kwargs):
        return self.call('mt', kwargs=kwargs)

    def mtdcv(self, **kwargs):
        return self.call('mtdcv', kwargs=kwargs)

    def mv(self, **kwargs):
        return self.call('mv', kwargs=kwargs)

    def nub_query(self, **kwargs):
        return self.call('nub_query', kwargs=kwargs)

    def odsw(self, **kwargs):
        return self.call('odsw', kwargs=kwargs)

    def odsw_query(self, **kwargs):
        return self.call('odsw_query', kwargs=kwargs)

    def opc_query(self, **kwargs):
        return self.call('opc_query', kwargs=kwargs)

    def os(self, **kwargs):
        return self.call('os', kwargs=kwargs)

    def osx(self, **kwargs):
        return self.call('osx', kwargs=kwargs)

    def pa(self, **kwargs):
        return self.call('pa', kwargs=kwargs)

    def pad(self, **kwargs):
        return self.call('pad', kwargs=kwargs)

    def pax(self, **kwargs):
        return self.call('pax', kwargs=kwargs)

    def pch(self, **kwargs):
        return self.call('pch', kwargs=kwargs)

    def pch_query(self, **kwargs):
        return self.call('pch_query', kwargs=kwargs)

    def pdcv(self, **kwargs):
        return self.call('pdcv', kwargs=kwargs)

    def pi(self, **kwargs):
        return self.call('pi', kwargs=kwargs)

    def pt(self, **kwargs):
        return self.call('pt', kwargs=kwargs)

    def ptdcv(self, **kwargs):
        return self.call('ptdcv', kwargs=kwargs)

    def pv(self, **kwargs):
        return self.call('pv', kwargs=kwargs)

    def pwdcv(self, **kwargs):
        return self.call('pwdcv', kwargs=kwargs)

    def pwi(self, **kwargs):
        return self.call('pwi', kwargs=kwargs)

    def pwv(self, **kwargs):
        return self.call('pwv', kwargs=kwargs)

    def qsc(self, **kwargs):
        return self.call('qsc', kwargs=kwargs)

    def qsl(self, **kwargs):
        return self.call('qsl', kwargs=kwargs)

    def qsm(self, **kwargs):
        return self.call('qsm', kwargs=kwargs)

    def qso(self, **kwargs):
        return self.call('qso', kwargs=kwargs)

    def qsr(self, **kwargs):
        return self.call('qsr', kwargs=kwargs)

    def qst(self, **kwargs):
        return self.call('qst', kwargs=kwargs)

    def qsv(self, **kwargs):
        return self.call('qsv', kwargs=kwargs)

    def qsz(self, **kwargs):
        return self.call('qsz', kwargs=kwargs)

    def rc(self, **kwargs):
        return self.call('rc', kwargs=kwargs)

    def rcv(self, **kwargs):
        return self.call('rcv', kwargs=kwargs)

    def ri(self, **kwargs):
        return self.call('ri', kwargs=kwargs)

    def rm(self, **kwargs):
        return self.call('rm', kwargs=kwargs)

    def rst(self, **kwargs):
        return self.call('rst', kwargs=kwargs)

    def ru(self, **kwargs):
        return self.call('ru', kwargs=kwargs)

    def rv(self, **kwargs):
        return self.call('rv', kwargs=kwargs)

    def rz(self, **kwargs):
        return self.call('rz', kwargs=kwargs)

    def sal(self, **kwargs):
        return self.call('sal', kwargs=kwargs)

    def sap(self, **kwargs):
        return self.call('sap', kwargs=kwargs)

    def sar(self, **kwargs):
        return self.call('sar', kwargs=kwargs)

    def scr(self, **kwargs):
        return self.call('scr', kwargs=kwargs)

    def ser(self, **kwargs):
        return self.call('ser', kwargs=kwargs)

    def ser_query(self, **kwargs):
        return self.call('ser_query', kwargs=kwargs)

    def sim(self, **kwargs):
        return self.call('sim', kwargs=kwargs)

    def sim_query(self, **kwargs):
        return self.call('sim_query', kwargs=kwargs)

    def sopc(self, **kwargs):
        return self.call('sopc', kwargs=kwargs)

    def sopc_query(self, **kwargs):
        return self.call('sopc_query', kwargs=kwargs)

    def sovc(self, **kwargs):
        return self.call('sovc', kwargs=kwargs)

    def sovc_query(self, **kwargs):
        return self.call('sovc_query', kwargs=kwargs)

    def spm(self, **kwargs):
        return self.call('spm', kwargs=kwargs)

    def spm_query(self, **kwargs):
        return self.call('spm_query', kwargs=kwargs)

    def spp(self, **kwargs):
        return self.call('spp', kwargs=kwargs)

    def spper(self, **kwargs):
        return self.call('spper', kwargs=kwargs)

    def spper_query(self, **kwargs):
        return self.call('spper_query', kwargs=kwargs)

    def sprm(self, **kwargs):
        return self.call('sprm', kwargs=kwargs)

    def sprm_query(self, **kwargs):
        return self.call('sprm_query', kwargs=kwargs)

    def spst_query(self, **kwargs):
        return self.call('spst_query', kwargs=kwargs)

    def spt(self, **kwargs):
        return self.call('spt', kwargs=kwargs)

    def spt_query(self, **kwargs):
        return self.call('spt_query', kwargs=kwargs)

    def spupd(self, **kwargs):
        return self.call('spupd', kwargs=kwargs)

    def spv(self, **kwargs):
        return self.call('spv', kwargs=kwargs)

    def spv_query(self, **kwargs):
        return self.call('spv_query', kwargs=kwargs)

    def sre(self, **kwargs):
        return self.call('sre', kwargs=kwargs)

    def sre_query(self, **kwargs):
        return self.call('sre_query', kwargs=kwargs)

    def srp(self, **kwargs):
        return self.call('srp', kwargs=kwargs)

    def ssl(self, **kwargs):
        return self.call('ssl', kwargs=kwargs)

    def ssp(self, **kwargs):
        return self.call('ssp', kwargs=kwargs)

    def ssr(self, **kwargs):
        return self.call('ssr', kwargs=kwargs)

    def st(self, **kwargs):
        return self.call('st', kwargs=kwargs)

    def stb_query(self, **kwargs):
        return self.call('stb_query', kwargs=kwargs)

    def stgp(self, **kwargs):
        return self.call('stgp', kwargs=kwargs)

    def stgp_query(self, **kwargs):
        return self.call('stgp_query', kwargs=kwargs)

    def tacv(self, **kwargs):
        return self.call('tacv', kwargs=kwargs)

    def tc(self, **kwargs):
        return self.call('tc', kwargs=kwargs)

    def tdcv(self, **kwargs):
        return self.call('tdcv', kwargs=kwargs)

    def tdi(self, **kwargs):
        return self.call('tdi', kwargs=kwargs)

    def tdv(self, **kwargs):
        return self.call('tdv', kwargs=kwargs)

    def tgmo(self, **kwargs):
        return self.call('tgmo', kwargs=kwargs)

    def tgp(self, **kwargs):
        return self.call('tgp', kwargs=kwargs)

    def tgpc(self, **kwargs):
        return self.call('tgpc', kwargs=kwargs)

    def tgsi(self, **kwargs):
        return self.call('tgsi', kwargs=kwargs)

    def tgso(self, **kwargs):
        return self.call('tgso', kwargs=kwargs)

    def tgxo(self, **kwargs):
        return self.call('tgxo', kwargs=kwargs)

    def ti(self, **kwargs):
        return self.call('ti', kwargs=kwargs)

    def tiv(self, **kwargs):
        return self.call('tiv', kwargs=kwargs)

    def tm(self, **kwargs):
        return self.call('tm', kwargs=kwargs)

    def tmacv(self, **kwargs):
        return self.call('tmacv', kwargs=kwargs)

    def tmdcv(self, **kwargs):
        return self.call('tmdcv', kwargs=kwargs)

    def tsc(self, **kwargs):
        return self.call('tsc', kwargs=kwargs)

    def tsq(self, **kwargs):
        return self.call('tsq', kwargs=kwargs)

    def tsr(self, **kwargs):
        return self.call('tsr', kwargs=kwargs)

    def tst(self, **kwargs):
        return self.call('tst', kwargs=kwargs)

    def ttc(self, **kwargs):
        return self.call('ttc', kwargs=kwargs)

    def tti(self, **kwargs):
        return self.call('tti', kwargs=kwargs)

    def ttiv(self, **kwargs):
        return self.call('ttiv', kwargs=kwargs)

    def ttv(self, **kwargs):
        return self.call('ttv', kwargs=kwargs)

    def tv(self, **kwargs):
        return self.call('tv', kwargs=kwargs)

    def unt_query(self, **kwargs):
        return self.call('unt_query', kwargs=kwargs)

    def var(self, **kwargs):
        return self.call('var', kwargs=kwargs)

    def var_query(self, **kwargs):
        return self.call('var_query', kwargs=kwargs)

    def wacv(self, **kwargs):
        return self.call('wacv', kwargs=kwargs)

    def wat(self, **kwargs):
        return self.call('wat', kwargs=kwargs)

    def wdcv(self, **kwargs):
        return self.call('wdcv', kwargs=kwargs)

    def wfc(self, **kwargs):
        return self.call('wfc', kwargs=kwargs)

    def wi(self, **kwargs):
        return self.call('wi', kwargs=kwargs)

    def wm(self, **kwargs):
        return self.call('wm', kwargs=kwargs)

    def wmacv(self, **kwargs):
        return self.call('wmacv', kwargs=kwargs)

    def wmdcv(self, **kwargs):
        return self.call('wmdcv', kwargs=kwargs)

    def wmfc(self, **kwargs):
        return self.call('wmfc', kwargs=kwargs)

    def wncc(self, **kwargs):
        return self.call('wncc', kwargs=kwargs)

    def wnu_query(self, **kwargs):
        return self.call('wnu_query', kwargs=kwargs)

    def wnx(self, **kwargs):
        return self.call('wnx', kwargs=kwargs)

    def ws(self, **kwargs):
        return self.call('ws', kwargs=kwargs)

    def wsi(self, **kwargs):
        return self.call('wsi', kwargs=kwargs)

    def wsv(self, **kwargs):
        return self.call('wsv', kwargs=kwargs)

    def wt(self, **kwargs):
        return self.call('wt', kwargs=kwargs)

    def wtacv(self, **kwargs):
        return self.call('wtacv', kwargs=kwargs)

    def wtdcv(self, **kwargs):
        return self.call('wtdcv', kwargs=kwargs)

    def wtfc(self, **kwargs):
        return self.call('wtfc', kwargs=kwargs)

    def wv(self, **kwargs):
        return self.call('wv', kwargs=kwargs)

    def wz_query(self, **kwargs):
        return self.call('wz_query', kwargs=kwargs)

    def xe(self, **kwargs):
        return self.call('xe', kwargs=kwargs)

