import FWCore.ParameterSet.Config as cms

process = cms.Process("CONDOBJMON")
#-------------------------------------------------
# CALIBRATION
#-------------------------------------------------
process.load("DQM.SiStripMonitorSummary.Tags21X_cff")

#-------------------------------------------------
# DQM
#-------------------------------------------------
process.load("DQM.SiStripMonitorSummary.SiStripMonitorCondData_cfi")

process.source = cms.Source("EmptyIOVSource",
    lastRun = cms.untracked.uint32(36213),
    timetype = cms.string('runnumber'),
    firstRun = cms.untracked.uint32(36213),
    #      untracked uint32 firstRun = 8055
    #      untracked uint32 lastRun  = 8055
    interval = cms.uint32(1)
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

process.qTester = cms.EDFilter("QualityTester",
    qtList = cms.untracked.FileInPath('DQM/SiStripMonitorSummary/data/CondDBQtests.xml'),
    QualityTestPrescaler = cms.untracked.int32(1),
    getQualityTestsFromFile = cms.untracked.bool(True)
)

process.DQMStore = cms.Service("DQMStore",
    referenceFileName = cms.untracked.string(''),
    verbose = cms.untracked.int32(1)
)

process.p = cms.Path(process.CondDataMonitoring*process.qTester)
process.CondDataMonitoring.OutputMEsInRootFile = True
process.CondDataMonitoring.MonitorSiStripPedestal = True
process.CondDataMonitoring.MonitorSiStripNoise = True
process.CondDataMonitoring.MonitorSiStripQuality = False
process.CondDataMonitoring.MonitorSiStripApvGain = False
process.CondDataMonitoring.MonitorSiStripLorentzAngle = False
process.CondDataMonitoring.FillConditions_PSet.Mod_On = True
process.CondDataMonitoring.FillConditions_PSet.SummaryOnLayerLevel_On = True
process.CondDataMonitoring.FillConditions_PSet.SummaryOnStringLevel_On = False
process.CondDataMonitoring.FillConditions_PSet.StripQualityLabel = 'test1'
process.CondDataMonitoring.FillConditions_PSet.restrictModules = False
process.CondDataMonitoring.FillConditions_PSet.ModulesToBeIncluded = []
process.CondDataMonitoring.FillConditions_PSet.ModulesToBeExcluded = []
process.CondDataMonitoring.FillConditions_PSet.SubDetectorsToBeExcluded = ['none']
process.CondDataMonitoring.FillConditions_PSet.ModulesToBeFilled = 'all'
process.CondDataMonitoring.SiStripNoisesDQM_PSet.CondObj_fillId = 'ProfileAndCumul'
process.CondDataMonitoring.SiStripNoisesDQM_PSet.GainRenormalisation = False

