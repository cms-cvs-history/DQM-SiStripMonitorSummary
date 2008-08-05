import FWCore.ParameterSet.Config as cms

process = cms.Process("CONDOBJMON")
#-------------------------------------------------
# CALIBRATION
#-------------------------------------------------
process.load("DQM.SiStripMonitorSummary.Tags20X_cff")

#-------------------------------------------------
# DQM
#-------------------------------------------------
process.load("DQM.SiStripMonitorSummary.SiStripMonitorCondData_cfi")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/data/CRUZET3/Cosmics/RAW/v1/000/051/193/780E0842-A74E-DD11-AC94-001617C3B64C.root')
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(2)
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

