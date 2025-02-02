import argparse
from coffea.dataset_tools import rucio_utils
from coffea.dataset_tools.dataset_query import print_dataset_query
from rich.console import Console
from rich.table import Table
from coffea.dataset_tools.dataset_query import DataDiscoveryCLI

2018_dataset = {
    "/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM": {"mc_campaign": "UL18", "lumi": 59.74, "process": "DYJets", "dataset": "DYJetsToLL_M-50_HT-70to100", "xsec": 208.977},
    "/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM": {"mc_campaign": "UL18", "lumi": 59.74, "process": "DYJets", "dataset": "DYJetsToLL_M-50_HT-100to200", "xsec": 181.30},
    "/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM": {"mc_campaign": "UL18", "lumi": 59.74, "process": "DYJets", "dataset": "DYJetsToLL_M-50_HT-200to400", "xsec": 50.4177},
    "/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM": {"mc_campaign": "UL18", "lumi": 59.74, "process": "DYJets", "dataset": "DYJetsToLL_M-50_HT-400to600", "xsec": 6.98394},
    "/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM": {"mc_campaign": "UL18", "lumi": 59.74, "process": "DYJets", "dataset": "DYJetsToLL_M-50_HT-600to800", "xsec": 1.68141},
    "/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM": {"mc_campaign": "UL18", "lumi": 59.74, "process": "DYJets", "dataset": "DYJetsToLL_M-50_HT-800to1200", "xsec": 0.775392},
    "/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM": {"mc_campaign": "UL18", "lumi": 59.74, "process": "DYJets", "dataset": "DYJetsToLL_M-50_HT-1200to2500", "xsec": 0.186222},
    "/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM": {"mc_campaign": "UL18", "lumi": 59.74, "process": "DYJets", "dataset": "DYJetsToLL_M-50_HT-2500toInf", "xsec": 0.00438495},
    "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM": {"mc_campaign": "UL18", "lumi": 59.74, "process": "tt+tW", "dataset": "TTTo2L2Nu", "xsec": 88.29},
    "/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM": {"mc_campaign": "UL18", "lumi": 59.74, "process": "tt+tW", "dataset": "ST_tW_antitop", "xsec": 19.20},
    "/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM": {"mc_campaign": "UL18", "lumi": 59.74, "process": "tt+tW", "dataset": "ST_tW_top", "xsec": 19.20},
    "/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM": {"mc_campaign": "UL18", "lumi": 59.74, "process": "WJets", "dataset": "WJetsToLNu_HT-70To100", "xsec": 1637.1},
    "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM": {"mc_campaign": "UL18", "lumi": 59.74, "process": "WJets", "dataset": "WJetsToLNu_HT-100To200", "xsec": 1627.45},
    "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM": {"mc_campaign": "UL18", "lumi": 59.74, "process": "WJets", "dataset": "WJetsToLNu_HT-200To400", "xsec": 435.237},
    "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM": {"mc_campaign": "UL18", "lumi": 59.74, "process": "WJets", "dataset": "WJetsToLNu_HT-400To600", "xsec": 59.1811},
    "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM": {"mc_campaign": "UL18", "lumi": 59.74, "process": "WJets", "dataset": "WJetsToLNu_HT-600To800", "xsec": 14.5805},
    "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM": {"mc_campaign": "UL18", "lumi": 59.74, "process": "WJets", "dataset": "WJetsToLNu_HT-800To1200", "xsec": 6.65621},
    "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM": {"mc_campaign": "UL18", "lumi": 59.74, "process": "WJets", "dataset": "WJetsToLNu_HT-1200To2500", "xsec": 1.60809},
    "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM": {"mc_campaign": "UL18", "lumi": 59.74, "process": "WJets", "dataset": "WJetsToLNu_HT-2500ToInf", "xsec": 0.0389136},
    "/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM": {"mc_campaign": "UL18", "lumi": 59.74, "process": "Diboson", "dataset": "WW", "xsec": 118.7},
    "/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM": {"mc_campaign": "UL18", "lumi": 59.74, "process": "Diboson", "dataset": "WZ", "xsec": 47.13},
    "/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM": {"mc_campaign": "UL18", "lumi": 59.74, "process": "Diboson", "dataset": "ZZ", "xsec": 16.523},
    "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM": {"mc_campaign": "UL18", "lumi": 59.74, "process": "Triboson", "dataset": "WWW", "xsec": 0.2086},
    "/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM": {"mc_campaign": "UL18", "lumi": 59.74, "process": "Triboson", "dataset": "WWZ", "xsec": 0.1651},
    "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM": {"mc_campaign": "UL18", "lumi": 59.74, "process": "Triboson", "dataset": "WZZ", "xsec": 0.05565},
    "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM": {"mc_campaign": "UL18", "lumi": 59.74, "process": "Triboson", "dataset": "ZZZ", "xsec": 0.01398},
    "/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM": {"mc_campaign": "UL18", "lumi": 59.74, "process": "ttX", "dataset": "ttWJets", "xsec": 0.4611},
    "/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM": {"mc_campaign": "UL18", "lumi": 59.74, "process": "ttX", "dataset": "ttZJets", "xsec": 0.5407},
    "/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM": {"mc_campaign": "UL18", "lumi": 59.74, "process": "SingleTop", "dataset": "ST_s-channel", "xsec": 3.36},
    "/ST_t-channel_antitop_5f_InclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM": {"mc_campaign": "UL18", "lumi": 59.74, "process": "SingleTop", "dataset": "ST_t-channel_antitop", "xsec": 80.95},
    "/ST_t-channel_top_5f_InclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM": {"mc_campaign": "UL18", "lumi": 59.74, "process": "SingleTop", "dataset": "ST_t-channel_top", "xsec": 136.02},
    "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM": {"mc_campaign": "UL18", "lumi": 59.74, "process": "tt_semileptonic", "dataset": "TTToSemiLeptonic", "xsec": 365.34},
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Construct fileset from list of datasets.')
    parser.add_argument('year', choices=['2018', '2017', '2016'], help='Choose the year to query.')
    args = parser.parse_args()

    if args.year != '2018':
        raise NotImplementedError

    ddc = DataDiscoveryCLI()
    ddc.do_allowlist_sites(["T2_DE_DESY", "T2_US_Wisconsin", "T2_US_Nebraska"])
    
    datasets = '{}_dataset'.format(args.year)

    ddc.load_dataset_definition(datasets, query_results_strategy="all",replicas_strategy="round-robin")

    ddc.do_save(f"UL{args.year}Bkg.json") #Use this to do manual preprocessing instead

    fileset_total = ddc.do_preprocess(output_file=f'UL{args.year}Bkg',
                  step_size=70000,
                  align_to_clusters=False,
                  scheduler_url=None)
