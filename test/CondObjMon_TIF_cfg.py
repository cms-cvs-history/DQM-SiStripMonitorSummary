import FWCore.ParameterSet.Config as cms

process = cms.Process("CONDOBJMON")
#-------------------------------------------------
# CALIBRATION
#-------------------------------------------------
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")

#calibrated conditions (as obtained with 10pb-1 data)
#replace GlobalTag.globaltag = "CSA08_S156::All"
#ideal conditions (one value for all TIB modules and one value for all TOB modules)
#replace GlobalTag.globaltag = "1PB_V2_RECO::All"
#
#include "CalibTracker/Configuration/data/Tracker_FrontierConditions_TIF_20X.cff"
#-------------------------------------------------
# DQM
#-------------------------------------------------
process.load("DQM.SiStripMonitorSummary.SiStripMonitorCondDataOffline_cfi")

process.source = cms.Source("EmptyIOVSource",
    lastValue = cms.uint64(8055),
    timetype = cms.string('runnumber'),
    firstValue = cms.uint64(8055),
    interval = cms.uint64(1)
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)
process.MessageLogger = cms.Service("MessageLogger",
    debugModules = cms.untracked.vstring('SiStripMonitorCondData'),
    cout = cms.untracked.PSet(
        threshold = cms.untracked.string('Error')
    ),
    destinations = cms.untracked.vstring('error.log', 
        'cout')
)

process.DQMStore = cms.Service("DQMStore",
    referenceFileName = cms.untracked.string(''),
    verbose = cms.untracked.int32(0)
)

process.p = cms.Path(process.CondDataMonitoring)
process.GlobalTag.globaltag = 'STARTUP_V2::All'
process.CondDataMonitoring.MonitorSiStripQuality = False
process.CondDataMonitoring.MonitorSiStripApvGain = True
process.CondDataMonitoring.FillConditions_PSet.Mod_On = True
process.CondDataMonitoring.FillConditions_PSet.SummaryOnLayerLevel_On = True
process.CondDataMonitoring.FillConditions_PSet.SummaryOnStringLevel_On = False
process.CondDataMonitoring.FillConditions_PSet.StripQualityLabel = 'test1'
process.CondDataMonitoring.FillConditions_PSet.restrictModules = False
process.CondDataMonitoring.FillConditions_PSet.ModulesToBeIncluded = []
process.CondDataMonitoring.FillConditions_PSet.ModulesToBeExcluded = []
process.CondDataMonitoring.FillConditions_PSet.SubDetectorsToBeExcluded = ['TEC', 'TID']
process.CondDataMonitoring.FillConditions_PSet.ModulesToBeFilled = 'all'
process.CondDataMonitoring.SiStripNoisesDQM_PSet.CondObj_fillId = 'ProfileAndCumul'
process.CondDataMonitoring.SiStripNoisesDQM_PSet.GainRenormalisation = True
process.CondDataMonitoring.SiStripApvGainsDQM_PSet.CondObj_fillId = 'ProfileAndCumul'
process.CondDataMonitoring.SiStripLorentzAngleDQM_PSet.CondObj_fillId = 'ProfileAndCumul'

