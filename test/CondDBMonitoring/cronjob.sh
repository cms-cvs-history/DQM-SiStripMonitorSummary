#!/bin/bash

export PATH=$PATH:/afs/cern.ch/cms/sw/common/
#export FRONTIER_FORCERELOAD=long # This should not be used anymore!!!

cd /afs/cern.ch/cms/tracker/sistrcalib/MonitorConditionDB/CMSSW_2_2_6/src/
eval `scramv1 runtime -sh`

cd /afs/cern.ch/cms/tracker/sistrcalib/MonitorConditionDB
./MonitorDB_NewDirStructure.sh cms_orcoff_prod CMS_COND_21X_STRIP CMS_COND_21X_GLOBALTAG FrontierProd

cd /afs/cern.ch/cms/tracker/sistrcalib/MonitorConditionDB/CMSSW_3_1_0_pre6/src/
eval `scramv1 runtime -sh`

cd /afs/cern.ch/cms/tracker/sistrcalib/MonitorConditionDB
./MonitorDB_NewDirStructure.sh cms_orcoff_prep CMS_COND_STRIP CMS_COND_30X_GLOBALTAG FrontierPrep
./MonitorDB_NewDirStructure.sh cms_orcoff_prep CMS_COND_31X_ALL CMS_COND_30X_GLOBALTAG FrontierPrep
./MonitorDB_NewDirStructure.sh cms_orcoff_prep CMS_COND_30X_STRIP CMS_COND_30X_GLOBALTAG FrontierPrep
./MonitorDB_NewDirStructure.sh cms_orcoff_prod CMS_COND_31X_STRIP CMS_COND_31X_GLOBALTAG FrontierProd
./MonitorDB_NewDirStructure.sh cms_orcoff_prod CMS_COND_31X_FROM21X CMS_COND_31X_GLOBALTAG FrontierProd
