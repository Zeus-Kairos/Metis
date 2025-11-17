[File](FileTopic.md) | [Instrument](XTraceChanTopic.md) | [Response](XResponseTopic.md) | [Stimulus](XStimulusTopic.md) | [Utility](XUtilityTopic.md) | [Cal](CalTopic.md) | [Apps](MixerTopic.md) | [Remote ONLY](DataTopic.md)

* * *

[Unguided](CalTopic.md#Unguided) | [SmartCal (Guided](CalTopic.md#guid)) | [ECAL](CalTopic.md#ECAL) | [Guided Power Cal](CalTopic.md#EnhancedPowerCal) | [Cal All](CalTopic.md#CalAll) | [Save-Recall](CalTopic.md#Recall) | [Cal Sets](CalTopic.md#sets) | [Cal Types](CalTopic.md#CalType) | [Prefer's](CalTopic.md#Preferences) |[Correction](CalTopic.md#Correction) | [Port Ext](CalTopic.md#PortExt) | [Fixturing](CalTopic.md#Fixturing) | [CPM](CalTopic.md#cpm) | [Delta Match](CalTopic.md#GlobalDMC) | [Cal Kits](CalTopic.md#kit) | [Standards](CalTopic.md#stand) | [Real-time Uncertainty](CalTopic.md#uncertainty) | [Multiple Sensors](CalTopic.md#MultiplePsensors) | [Source Pwr Cal](CalTopic.md#power) | [Power Sensors](CalTopic.md#Sensors) | [Receiver Cal](CalTopic.md#Receiver) [| Cal Data](CalTopic.md#Retrieve) | [CalPod](CalTopic.md#Calpod) | [Custom Cal Window](CalTopic.md#CustomWindow) | AFR | Cal Update

Description |  SCPI See Also: [Calibration commands for Apps](MixerTopic.md) |  COM  
---|---|---  
Perform an Unguided Calibration  
Launch Cal Wizard |  [SYSTem:CORRection:WIZard](GP-IB_Command_Finder/System.md#wiz) |  [app.LaunchCalWizard](COM_Reference/Methods/LaunchCalWizard_Method.md)  
Set Cal Type |  [SENSe:CORRection:COLLect:METHod](GP-IB_Command_Finder/Sense/Sense_Correction.md#sccm) |  [cal.SetCalInfo](COM_Reference/Methods/SetCalInfo_Method.md)  
Select a Cal Kit |  [SENSe:CORRection:COLLect:CKIT](GP-IB_Command_Finder/Sense/CorrCollCKIT.md#scccs) |  [app.CalKitType](COM_Reference/Properties/CalKitType_Property.md)  
Get a Handle to the Active Cal Kit |  None |  [app.ActiveCalKit](COM_Reference/Properties/Active_Cal_Kit_Property.md)  
Simultaneous 2-Port Calibration |  [SENSe:CORRection:TSTandards](GP-IB_Command_Finder/Sense/Sense_Correction.md#2STDS1) |  [cal.Simultaneous2PortAcquisition](COM_Reference/Properties/Simultaneous2PortAcquisition_Property.md)  
Acquisition Direction |  [SENSe:CORRection:SFORward](GP-IB_Command_Finder/Sense/Sense_Correction.md#sforward) |  [cal.AcquisitionDirection](COM_Reference/Properties/AcquisitionDirection_Property.md)  
Measure a Standard |  [SENSe:CORRection:COLLect](GP-IB_Command_Finder/Sense/Sense_Correction.md#scca) |  [cal.AcquireCalStandard](COM_Reference/Methods/Acquire_Cal_Standard_Method.md)  
Calculate Errors |  [SENSe:CORRection:COLLect:SAVE](GP-IB_Command_Finder/Sense/Sense_Correction.md#sccs) |  [cal.CalculateErrorCoeffecients](COM_Reference/Methods/Calculate_Error_Coefficients_Method.md)  
Do Isolation |  [SENSe:CORRection:COLLect](GP-IB_Command_Finder/Sense/Sense_Correction.md#scca) |  [cal.AcquireCalStandard](COM_Reference/Methods/Acquire_Cal_Standard_Method.md)  
Perform and apply Response (Normalization) cal |  [SENSe:CORRection:COLLect:METHod](GP-IB_Command_Finder/Sense/Sense_Correction.md#sccm) |  [DoResponseCal](COM_Reference/Methods/DoResponseCal_Method.md)  
  
Perform a Guided Cal  
---  
Initiate a Guided Cal |  [SENSe:CORRection:COLLect:GUIDed:INITiate](GP-IB_Command_Finder/Sense/CorrGuided.md#gInit) |  [Initialize](COM_Reference/Methods/Initialize_Method.md)  
List valid Connector Types for a Port |  [SENSe:CORRection:COLLect:GUIDed:CONNector:CATalog?](GP-IB_Command_Finder/Sense/CorrGuided.md#gConnCat) |  [ValidConnectorTypes](COM_Reference/Properties/ValidConnectorType_Property.md)  
List valid Cal Kits for a Connector type. |  [SENSe:CORRection:COLLect:GUIDed:CKIT:CATalog?](GP-IB_Command_Finder/Sense/CorrGuided.md#ckitCatConn) |  [GetCompatibleCalKits](COM_Reference/Methods/GetCompatibleCalKits_Method.md)  
Select a Connector Type |  [SENSe:CORRection:COLLect:GUIDed:CONNector:PORT](GP-IB_Command_Finder/Sense/CorrGuided.md#gConSelect) |  [ConnectorType](COM_Reference/Properties/ConnectorType_Property.md)  
Select a Cal Kit |  [SENSe:CORRection:COLLect:GUIDed:CKIT:PORT](GP-IB_Command_Finder/Sense/CorrGuided.md#gKit) |  [CalKitType](COM_Reference/Properties/CalKitType_Property.md)  
Set cal method for each port pair. |  [SENSe:CORRection:COLLect:GUIDed:PATH:CMEThod](GP-IB_Command_Finder/Sense/CorrGuided.md#PathCmethod) |  [PathCalMethod](COM_Reference/Properties/PathCalMethod_Property.md)  
Set Thru Method for each port pair. |  [SENSe:CORRection:COLLect:GUIDed:PATH:TMEThod](GP-IB_Command_Finder/Sense/CorrGuided.md#PathTMethod) |  [PathThruMethod](COM_Reference/Properties/PathThruMethod_Property.md)  
Set Thru Port Pairs |  [SENSe:CORRection:COLLect:GUIDed:THRU:PORTs](GP-IB_Command_Finder/Sense/CorrGuided.md#pairs) |  [ThruPortList](COM_Reference/Properties/ThruPortList_Property.md)  
Return Number of Steps in a Cal |  [SENSe:CORRection:COLLect:GUIDed:STEPs?](GP-IB_Command_Finder/Sense/CorrGuided.md#gSteps) |  [GenerateSteps](COM_Reference/Methods/GenerateSteps_Method.md)  
Return a Description of a Cal Step |  [SENSe:CORRection:COLLect:GUIDed:DESCription?](GP-IB_Command_Finder/Sense/CorrGuided.md#gDesc) |  [GetStepDescription](COM_Reference/Methods/Get_StepDescription_Method.md)  
Measure a Cal Standard in a Guided Cal |  [SENSe:CORRection:COLLect:GUIDed:STAN](GP-IB_Command_Finder/Sense/CorrGuided.md#gAcquire) |  [AcquireStep](COM_Reference/Methods/AcquireStep_Method.md)  
Save Cal |  [SENSe:CORRection:COLLect:GUIDed:SAVE](GP-IB_Command_Finder/Sense/CorrGuided.md#gSave) |  [GenerateErrorTerms](COM_Reference/Methods/GenerateErrorTerms_Method.md)  
Return Number of Steps in a Cal |  [SENSe:CORRection:COLLect:GUIDed:LIST:COUNt?](GP-IB_Command_Finder/Sense/CorrGuided.md#SENSe:CORRection:COLLect:GUIDed:LIST:COUNt) |  None  
Return number of standards for step[n] |  [SENSe:CORRection:COLLect:GUIDed:LIST:STEP:COUNt?](GP-IB_Command_Finder/Sense/CorrGuided.md#SENSe:CORRection:COLLect:GUIDed:LIST:STEP:COUNt) |  None  
Return step description |  [SENSe:CORRection:COLLect:GUIDed:LIST:STEP:DESCription?](GP-IB_Command_Finder/Sense/CorrGuided.md#SENSe:CORRection:COLLect:GUIDed:LIST:STEP:DESCription) |  None  
Return label for complete standard |  [SENSe:CORRection:COLLect:GUIDed:LIST:STEP:LABel?](GP-IB_Command_Finder/Sense/CorrGuided.md#SENSe:CORRection:COLLect:GUIDed:LIST:STEP:LABel) |  None  
Return number of ports on standard used in the step |  [SENSe:CORRection:COLLect:GUIDed:LIST:STEP:PORTs?](GP-IB_Command_Finder/Sense/CorrGuided.md#SENSe:CORRection:COLLect:GUIDed:LIST:STEP:PORTs) |  None  
Return label for one of the standards in the step |  [SENSe:CORRection:COLLect:GUIDed:LIST:STEP:STANdard:LABel?](GP-IB_Command_Finder/Sense/CorrGuided.md#SENSe:CORRection:COLLect:GUIDed:LIST:STEP:STANdard:LABel) |  None  
Return number of ports on one of the standards used in the step |  [SENSe:CORRection:COLLect:GUIDed:LIST:STEP:STANdard:PORTs?](GP-IB_Command_Finder/Sense/CorrGuided.md#SENSe:CORRection:COLLect:GUIDed:LIST:STEP:STANdard:PORTs) |  None  
Return the enumeration for the type of standard |  [SENSe:CORRection:COLLect:GUIDed:LIST:STEP:STANdard:STYPe?](GP-IB_Command_Finder/Sense/CorrGuided.md#SENSe:CORRection:COLLect:GUIDed:LIST:STEP:STANdard:STYPe) |  None  
Return list of VNA test ports to which one of the standards is attached |  [SENSe:CORRection:COLLect:GUIDed:LIST:STEP:STANdard:TPORts?](GP-IB_Command_Finder/Sense/CorrGuided.md#SENSe:CORRection:COLLect:GUIDed:LIST:STEP:STANdard:TPORts) |  None  
Return enumeration for the type of standard device used in the step |  [SENSe:CORRection:COLLect:GUIDed:LIST:STEP:STYPe?](GP-IB_Command_Finder/Sense/CorrGuided.md#SENSe:CORRection:COLLect:GUIDed:LIST:STEP:STYPe) |  None  
Return list of VNA test ports to which the standard(s) in this step is attached |  [SENSe:CORRection:COLLect:GUIDed:LIST:STEP:TPORts?](GP-IB_Command_Finder/Sense/CorrGuided.md#SENSe:CORRection:COLLect:GUIDed:LIST:STEP:TPORts) |  None  
Return measurement parameters measured in the specified step number of a guided calibration |  [SENSe:CORRection:COLLect:GUIDed:DATA:CATalog?](GP-IB_Command_Finder/Sense/CorrGuided.md#SENSe:CORRection:COLLect:GUIDed:MEASurement:CATalog) |  None  
Set and return measurement data for a specified measurement parameter of a particular step of a guided cal |  [SENSe:CORRection:COLLect:GUIDed:DATA](GP-IB_Command_Finder/Sense/CorrGuided.md#SENSe:CORRection:COLLect:GUIDed:MEASurement:DATA) |  None  
Enable/disable using existing source power calibration array when acquiring calibration standard data: |  [SENSe:CORRection:COLLect:GUIDed:PCAL:APPLy](GP-IB_Command_Finder/Sense/CorrGuided.md#SENSe:CORRection:COLLect:GUIDed:PCAL:APPLy) |  None  
Return list of ports being calibrated by an active calibration session |  [SENSe:CORRection:COLLect:GUIDed:PORTs?](GP-IB_Command_Finder/Sense/CorrGuided.md#SENSe:CORRection:COLLect:GUIDed:PORTs) |  None  
  
Adapter settings for Unknown Thru or Adapter Removal  
---  
Sets use of a THRU adapter |  [SENSe:CORRection:COLLect:GUIDed:ADAPter:CREate](GP-IB_Command_Finder/Sense/CorrGuided.md#adaptCreate) |  None  
Set adapter delay |  [SENSe:CORRection:COLLect:GUIDed:ADAPter:DELay](GP-IB_Command_Finder/Sense/CorrGuided.md#adaptDelay) |  None  
Set adapter description |  [SENSe:CORRection:COLLect:GUIDed:ADAPter:DESCription](GP-IB_Command_Finder/Sense/CorrGuided.md#adaptDesc) |  None  
Set port pairs for adapter |  [SENSe:CORRection:COLLect:GUIDed:ADAPter:PATHs](GP-IB_Command_Finder/Sense/CorrGuided.md#adaptPaths) |  None  
Clear the settings |  [SENSe:CORRection:COLLect:GUIDed:ADAPter:COUNt:ZERO](GP-IB_Command_Finder/Sense/CorrGuided.md#adapterCountZero) |  None  
Return number of adapters |  [SENSe:CORRection:COLLect:GUIDed:ADAPter:COUNt?](GP-IB_Command_Finder/Sense/CorrGuided.md#adaptCount) |  None  
  
Optional Guided Cal commands  
---  
Auto-Orient ECal |  [SENSe:CORRection:PREFerence:ECAL:ORIentation](GP-IB_Command_Finder/Sense/Sense_Correction.md#Orie) |  [cal.OrientECALModule](COM_Reference/Properties/OrientECALModule_Property.md)  
Manual orient ECAL |  [SENSe:CORRection:PREFerence:ECAL:PMAP](GP-IB_Command_Finder/Sense/Sense_Correction.md#Pmap) |  [cal.ECALPortMapEx](COM_Reference/Properties/ECALPortMapEx_Property.md)  
Read orientation |  [SENSe:CORRection:CKIT:ECAL:ORIent?](GP-IB_Command_Finder/Sense/CorrCKIT_SCPI.md#Orient) |  [ECalModules](COM_Reference/Objects/ECalModules_Collection.md)  
Calculate Error Terms from a Guided Cal |  [SENSe:CORRection:COLLect:GUIDed:SAVE](GP-IB_Command_Finder/Sense/CorrGuided.md#gSave) |  [GenerateErrorTerms](COM_Reference/Methods/GenerateErrorTerms_Method.md)  
Save Cal to an existing Cal Set GUID |  [SENSe:CORRection:COLLect:GUIDed:SAVE:CSET](GP-IB_Command_Finder/Sense/CorrGuided.md#SaveCSET) |  None  
Load Eterms during a cal |  [SENSe:CORRection:COLLect:GUIDed:ETERms:LOAD](GP-IB_Command_Finder/Sense/CorrGuided.md#EtermLoad) |  None  
Perform Isolation |  [SENSe:CORRection:COLLect:GUIDed:ISOLation:PATHs](GP-IB_Command_Finder/Sense/CorrGuided.md#IsolPaths) |  [GetIsolationPaths Method](COM_Reference/Methods/GetIsolationPaths_Method.md) [SetIsolationPaths Method](COM_Reference/Methods/SetIsolationPaths_Method.md)  
Increment Avg for Isolation |  [SENSe:CORRection:COLLect:GUIDed:ISOLation:AVERage:INCRement](GP-IB_Command_Finder/Sense/CorrGuided.md#IsoAvg) |  [IsolationAveragingIncrement Property](COM_Reference/Properties/IsolationAveragingIncrement_Property.md)  
Abort Guided cal |  [SENSe:CORRection:COLLect:GUIDed:ABORt](GP-IB_Command_Finder/Sense/CorrGuided.md#abort) |  None required. Destroy the GuidedCal object to terminate a cal.  
Execute the Ecal calibration |  [SENSe:CORRection:COLLect:GUIDed:ECAL:ACQuire](GP-IB_Command_Finder/Sense/CorrGuided.md#EcalAqu) |  None  
Specifies the Ecal Kit for Ecal Calibration |  [SENSe:CORRection:COLLect:GUIDed:ECAL:SELect](GP-IB_Command_Finder/Sense/CorrGuided.md#EcalSel) |  None  
Compute Error Terms |  [SENSe:CORRection:COLLect:GUIDed:ETERms:COMPute](GP-IB_Command_Finder/Sense/CorrGuided.md#SENSe:CORRection:COLLect:ETERms:COMPute) |  None  
  
Guided Power Cal Use standard [Source Power](CalTopic.md#power) commands to
make advanced settings. Use [Power Sensor](CalTopic.md#Sensors) commands to
configure the power sensor.  
---  
Perform power cal |  [SENSe:CORRection:COLLect:GUIDed:PSENsor](GP-IB_Command_Finder/Sense/CorrCollGuidPSens.md#PerformPowerCal) |  [PerformPowerCalibration](COM_Reference/Properties/PerformPowerCalibration_Property.md)  
Power sensor connector type |  [SENSe:CORRection:COLLect:GUIDed:PSENsor:CONNector](GP-IB_Command_Finder/Sense/CorrCollGuidPSens.md#PsensorConn) |  [PowerSensorConnectorType](COM_Reference/Properties/PowerSensorConnectorType_Guided_Property.md)  
Cal Kit for power cal |  [SENSe:CORRection:COLLect:GUIDed:PSENsor:CKIT](GP-IB_Command_Finder/Sense/CorrCollGuidPSens.md#PsenCKIT) |  [PowerSensorCalKitType](COM_Reference/Properties/PowerSensorCalKitType_Guided%20Property.md)  
Power Level for cal |  [SENSe:CORRection:COLLect:GUIDed:PSENsor:POWer:LEVel](GP-IB_Command_Finder/Sense/CorrCollGuidPSens.md#PsenPowLevel) |  [PowerCalibrationPowerLevel](COM_Reference/Properties/PowerCalibrationPowerLevel_Property.md)  
Perform match-correction |  [SENSe:CORRection:METHods:MATCh](GP-IB_Command_Finder/Sense/Sense_Correction.md#methodsMatch) |  [MatchCorrectPower](COM_Reference/Properties/MatchCorrectPower_Property.md)  
Sets and returns the selected ports to include in a full NPort correction. |  [SENSe:CORRection:METHods:PORT:SUBSet:FULL[:VALue]](GP-IB_Command_Finder/Sense/Sense_Correction.md#SENSe:CORRection:METHods:PORT:SUBSet:FULL:VALue) |  [FullyCorrectedPorts](COM_Reference/Properties/FullyCorrectedPorts_Property.md)  
Resets the full and response list to their default values. |  [SENSe:CORRection:METHods:PORT:SUBSet:RESet](GP-IB_Command_Finder/Sense/Sense_Correction.md#SENSe:CORRection:METHods:PORT:SUBSet:RESet) |  [ResetPortValues](COM_Reference/Methods/ResetPortValues_Method.md)  
Sets and returns the selected ports to be corrected with enhanced response calibration. |  [SENSe:CORRection:METHods:PORT:SUBSet:RESPonse[:VALue]](GP-IB_Command_Finder/Sense/Sense_Correction.md#SENSe:CORRection:METHods:PORT:SUBSet:RESPonse:VALue) |  [ResponseCorrectedPorts](COM_Reference/Properties/ResponseCorrectedPorts_Property.md)  
Set and return the ON/OFF subset correction state. |  [SENSe:CORRection:METHods:PORT:SUBSet:[:STATe]](GP-IB_Command_Finder/Sense/Sense_Correction.md#SENSe:CORRection:METHods:PORT:SUBSet:STATe) |  [CorrectionSubsettingState](COM_Reference/Properties/CorrectionSubsettingState_Property.md)  
Load Power Table |  [SENSe:CORRection:COLLect:GUIDed:PSENsor:POWTable](GP-IB_Command_Finder/Sense/CorrCollGuidPSens.md#Powtable) Used with SMC on mmWave systems. |  [PowerTableFilename](COM_Reference/Properties/PowerTableFilename_Property.md) Used with SMC on mmWave systems.  
  
Perform Enhanced Response Cal  
---  
Set guided Cal method |  [SENSe:CORRection:COLLect:GUIDed:PATH:CMEThod](GP-IB_Command_Finder/Sense/CorrGuided.md#PathCmethod) |  [PathCalMethod](COM_Reference/Properties/PathCalMethod_Property.md)  
Set guided Thru method |  [SENSe:CORRection:COLLect:GUIDed:PATH:TMEThod](GP-IB_Command_Finder/Sense/CorrGuided.md#PathTMethod) |  [PathThruMethod](COM_Reference/Properties/PathThruMethod_Property.md)  
  
Perform Sliding Load Acquisition  
---  
Set preference to not prompt |  [SENSe:CORRection:COLLect:GUIDed:PREFerence:SLIDingload](GP-IB_Command_Finder/Sense/CorrGuided.md#PrefSliding) |  [SlidingLoadAcquisitionBehavior](COM_Reference/Properties/SlidingLoadAcquisitionBehavior_Property.md)  
Read iteration step |  [SENSe:CORRection:COLLect:GUIDed:ITERations:COUNt?](GP-IB_Command_Finder/Sense/CorrGuided.md#IterCount) |  [IterationCountForStep](COM_Reference/Properties/IterationCountForStep_Property.md)  
Read minimum iterations |  [SENSe:CORRection:COLLect:GUIDed:ITERations:MINimum?](GP-IB_Command_Finder/Sense/CorrGuided.md#iterMin) |  [MinimumIterationsForStep](COM_Reference/Properties/MinimumIterationsForStep_Property.md)  
Reset iterations |  [SENSe:CORRection:COLLect:GUIDed:ITERations:RESet](GP-IB_Command_Finder/Sense/CorrGuided.md#IterReset) |  [ResetStep](COM_Reference/Methods/ResetStep_Method.md)  
  
Perform an ECAL  
---  
Specify Module and Characterization |  [SENSe:CORRection:COLLect:ACQuire](GP-IB_Command_Finder/Sense/Sense_Correction.md#scca) |  [cal.ECALCharacterizationEx](COM_Reference/Properties/ECALCharacterizationEx_Property.md)  
Do ECAL 1-Port |  [SENSe:CORRection:COLLect:CKIT 99](GP-IB_Command_Finder/Sense/CorrCollCKIT.md#scccs) |  [cal.DoECAL1PortEx](COM_Reference/Methods/DoECAL1PortEx_Method.md)  
Do ECAL 2-Port |  [SENSe:CORRection:COLLect:CKIT 99](GP-IB_Command_Finder/Sense/CorrCollCKIT.md#scccs) |  [cal.DoECAL2PortEx](COM_Reference/Methods/DoECAL2PortEx_Method.md)  
Get ECAL Module Info |  [SENSe:CORRection:COLLect:CKIT:INFormation?](GP-IB_Command_Finder/Sense/CorrCollCKIT.md#Inf) [SENSe:CORRection:CKIT:ECAL:INFormation?](GP-IB_Command_Finder/Sense/CorrCKIT_SCPI.md#ECALInf) |  cal.[GetCalKitTypeString](COM_Reference/Methods/GetCalKitTypeString_Method.md) [cal.GetECALModuleInfoEx](COM_Reference/Methods/Get_ECALModuleInfoEx_Method.md)  
Get list of ECal Modules attached to PNA |  [SENSe:CORRection:CKIT:ECAL:LIST?](GP-IB_Command_Finder/Sense/CorrCKIT_SCPI.md#List) |  [cal.ECALModuleNumberList](COM_Reference/Properties/ECALModuleNumberList_Property.md)  
Get list of characterizations in ECal module |  [SENSe:CORRection:CKIT:ECAL:CLISt?](GP-IB_Command_Finder/Sense/CorrCKIT_SCPI.md#Clist) |  [cal.ECALCharacterizationIndexList](COM_Reference/Properties/ECALCharacterizationIndexList_Property.md)  
Perform Module Orientation during calibration |  [SENSe:CORRection:PREFerence:ECAL:ORIentation](GP-IB_Command_Finder/Sense/Sense_Correction.md#Orie) |  [cal.OrientECALModule](COM_Reference/Properties/OrientECALModule_Property.md)  
Maps ECAL Module to PNA Ports |  [SENSe:CORRection:PREFerence:ECAL:PMAP](GP-IB_Command_Finder/Sense/Sense_Correction.md#Pmap) |  [cal.ECALPortMapEx](COM_Reference/Properties/ECALPortMapEx_Property.md)  
Reads ECal orientation |  [SENSe:CORRection:CKIT:ECAL:ORIent?](GP-IB_Command_Finder/Sense/CorrCKIT_SCPI.md#Orient) |  [ECalModules](COM_Reference/Objects/ECalModules_Collection.md)  
Perform ECal Isolation |  [SENSe:CORRection:COLLect:ISOLation:ECAL](GP-IB_Command_Finder/Sense/Sense_Correction.md#IsoEcal) |  [ECALIsolation](COM_Reference/Properties/ECALIsolation_Property.md)  
Increment Avg for ECal Isolation |  [SENSe:CORRection:COLLect:ISOLation:AVERage:INCRement](GP-IB_Command_Finder/Sense/Sense_Correction.md#IsolAvg) |  [IsolationAveragingIncrement](COM_Reference/Properties/IsolationAveragingIncrement_Property.md)  
Return the ID string of ECals |  [SYSTem:COMMunicate:ECAL:CATalog?](GP-IB_Command_Finder/SystCommunicate.md#EcalCat) |  None  
Return a list of characterizations |  [SYSTem:COMMunicate:ECAL:CLISt?](GP-IB_Command_Finder/SystCommunicate.md#SYSTem:COMMunicate:ECAL:CLISt) |  None  
Return the number of installed cal kits |  [SYSTem:COMMunicate:ECAL:COUNt?](GP-IB_Command_Finder/SystCommunicate.md#SYSTem:COMMunicate:ECAL:COUNt) |  None  
Delete user characterizations from VNA disk memory |  [SYSTem:COMMunicate:ECAL:DMEMory:CLEar](GP-IB_Command_Finder/SystCommunicate.md#SYSTem:COMMunicate:ECAL:DMEMory:CLEar) |  None  
Import file into VNA disk memory |  [SYSTem:COMMunicate:ECAL:DMEMory:IMPort](GP-IB_Command_Finder/SystCommunicate.md#SYSTem:COMMunicate:ECAL:DMEMory:IMPort) |  None  
Save existing ECal characterization to a file |  [SYSTem:COMMunicate:ECAL:EXPort](GP-IB_Command_Finder/SystCommunicate.md#SYSTem:COMMunicate:ECAL:EXPort) |  None  
Read identification and characterization information for ECal module |  [SYSTem:COMMunicate:ECAL:INFormation?](GP-IB_Command_Finder/SystCommunicate.md#SYSTem:COMMunicate:ECAL:INFormation) |  None  
Read identification and characterization information from ECal module or VNA disk memory |  [SYSTem:COMMunicate:ECAL:KNAMe:INFormation?](GP-IB_Command_Finder/SystCommunicate.md#SYSTem:COMMunicate:ECAL:KNAMe:INFormation) |  None  
Return list of index numbers for ECal modules |  [SYSTem:COMMunicate:ECAL:LIST?](GP-IB_Command_Finder/SystCommunicate.md#SYSTem:COMMunicate:ECAL:LIST) |  None  
Return number of unique states for specified path name on selected ECal module |  [SYSTem:COMMunicate:ECAL:PATH:COUNt?](GP-IB_Command_Finder/SystCommunicate.md#SYSTem:COMMunicate:ECAL:PATH:COUNt) |  None  
  
Perform ECal User Characterizations  
---  
Perform User ECal Characterization |  [All SCPI commands](GP-IB_Command_Finder/Sense/ECalCharacterize.md) |  [All COM commands](COM_Reference/Objects/ECalUserCharacterizer_Object.md)  
Manage PNA Disk Memory Characterizations  
Delete disk memory characterizations. |  [SENSe:CORRection:CKIT:ECAL:DMEMory:CLEar](GP-IB_Command_Finder/Sense/CorrCKIT_SCPI.md#dmemClear) |  None  
Saves a disk memory characterization to an archive file. |  [SENSe:CORRection:CKIT:ECAL:EXPort](GP-IB_Command_Finder/Sense/CorrCKIT_SCPI.md#EcalExport) |  None  
Imports the ECal characterization from the specified archive file. |  [SENSe:CORRection:CKIT:ECAL:DMEMory:IMPort](GP-IB_Command_Finder/Sense/CorrCKIT_SCPI.md#dmemImport) |  None  
Reads the user-characterization info from ECal module or PNA disk memory. |  [SENSe:CORRection:CKIT:ECAL:KNAMe:INFormation?](GP-IB_Command_Finder/Sense/CorrCKIT_SCPI.md#knameInf) |  None  
  
ECal Confidence Check  
---  
Confidence Check Parameter |  [SENSe:CORRection:CCHeck:PARameter](GP-IB_Command_Finder/Sense/Sense_Correction.md#chkPar) |  [cal.AcquireCalConfidenceCheckECALEx](COM_Reference/Methods/AcquireCalConfidenceCheckECALex_Method.md)  
Confidence Check Acquire |  [SENSe:CORRection:CCHeck](GP-IB_Command_Finder/Sense/Sense_Correction.md#chkAcq) |  [cal.AcquireCalConfidenceCheckECALEx](COM_Reference/Methods/AcquireCalConfidenceCheckECALex_Method.md)  
Confidence Check Done |  [SENSe:CORRection:CCHeck:DONE](GP-IB_Command_Finder/Sense/Sense_Correction.md#chkDone) |  [cal.DoneCalConfidenceCheckECAL](COM_Reference/Methods/DoneCalConfidenceCheckECAL.md)  
Set/Read ECal State  
Sets the state of an ECAL module |  [CONTrol:ECAL:MODule:PATH:STATe](GP-IB_Command_Finder/Control.md#EcalPathState) |  None  
Read ECal state data |  [SENSe:CORRection:CKIT:ECAL:PATH:DATA?](GP-IB_Command_Finder/Sense/CorrCKIT_SCPI.md#EcalPathData) |  None  
Read number of ECal states for specified path |  [CONTrol:ECAL:MODule:PATH:COUNt?](GP-IB_Command_Finder/Control.md#ECalPathCount) [SENSe:CORRection:CKIT:ECAL:PATH:COUNt?](GP-IB_Command_Finder/Sense/CorrCKIT_SCPI.md#ECalPathCount) |  None  
  
Calibrate All Channels  
---  
Select the channels to be calibrated. |  [SYSTem:CALibrate:ALL:SELect](GP-IB_Command_Finder/SystCalAll.md#ChanSelect) |  [Channels](COM_Reference/Properties/Channels_Property.md)  
Set the IFBW |  [SYSTem:CALibrate:ALL:IFBW](GP-IB_Command_Finder/SystCalAll.md#ifbw) |  [IFBW](COM_Reference/Properties/IFBW_Property.md)  
Set the power level |  [SYSTem:CALibrate:ALL:PORT:SOURce:POWer](GP-IB_Command_Finder/SystCalAll.md#SourcePower) |  [PowerLevel](COM_Reference/Properties/PowerLevel-\(CalAll\)_Property.md)  
Set the power offset |  [SYSTem:CALibrate:ALL:PORT:SOURce:POWer:OFFSet](GP-IB_Command_Finder/SystCalAll.md#SourceOffset) |  [PowerOffset](COM_Reference/Properties/PowerOffset_\(CalAll\)_Property.md)  
Set the receiver atten |  [SYSTem:CALibrate:ALL:PORT:RECeiver:ATTen](GP-IB_Command_Finder/SystCalAll.md#RecAtten) |  [ReceiverAttenuator](COM_Reference/Properties/ReceiverAttenuator_Property.md)  
Set the source atten |  [SYSTem:CALibrate:ALL:PORT:SOURce:POWer:ATTen](GP-IB_Command_Finder/SystCalAll.md#SourceAtten) |  [SourceAttenuator](COM_Reference/Properties/SourceAttenuator_Property.md)  
Set the User Calset Prefix |  [SYSTem:CALibrate:ALL:CSET:PREFix](GP-IB_Command_Finder/SystCalAll.md#csetPrefix) |  [UserCalsetPrefix](COM_Reference/Properties/UserCalsetPrefix_Property.md)  
Set Path Configuration |  [SYSTem:CALibrate:ALL:PATH:CONFigure:ELEMent](GP-IB_Command_Finder/SystCalAll.md#ConfigElement) |  [PathConfigurationElement](COM_Reference/Properties/PathConfigurationElement_Property.md)  
Read unique Cal properties |  [SYSTem:CAL:ALL:MCLass:PROPerty:NAME:CATalog?](GP-IB_Command_Finder/SystCalAll.md#PropNameCat) |  [PropertyNames](COM_Reference/Properties/PropertyNames_Property.md)  
Read unique property values |  [SYSTem:CAL:ALL:MCLass:PROPerty:VALue:CATalog?](GP-IB_Command_Finder/SystCalAll.md#PropValueCat) |  [PropertyValues](COM_Reference/Properties/PropertyValues_Property.md)  
Set property name/value |  [SYSTem:CAL:ALL:MCLass:PROPerty:VALue](GP-IB_Command_Finder/SystCalAll.md#PropValueSelect) |  [PropertyValue](COM_Reference/Properties/PropertyValue_Property.md)  
Read primary Cal channel |  [SYSTem:CALibrate:ALL:GUIDed:CHANnel[:VALue]?](GP-IB_Command_Finder/SystCalAll.md#GuideChan) |  None  
Get GuidedCal handle |  None |  [GuidedCalibration](COM_Reference/Objects/GuidedCalibration_Object.md)  
For each channel, sets the ports to be calibrated. |  [SYSTem:CALibrate:ALL:CHANnel:PORTs](GP-IB_Command_Finder/SystCalAll.md#PortsSelect) |  [CalibrationPorts](COM_Reference/Properties/CalibrationPorts_Property.md)  
Returns a final list of ports to be calibrated. |  [SYSTem:CALibrate:ALL:GUIDed:PORTs?](GP-IB_Command_Finder/SystCalAll.md#GuidedPorts) |  [SParameterCalPorts](COM_Reference/Properties/SParameterCalPorts_Property.md)  
Read generated Cal Sets |  [SYSTem:CALibrate:ALL:CSET:CATalog?](GP-IB_Command_Finder/SystCalAll.md#csetCat) |  [GeneratedCalsets](COM_Reference/Properties/GeneratedCalsets_Property.md)  
Returns all cal all guided calibration channels |  [SYSTem:CALibrate:ALL:GUIDed:CHANnel:LIST?](GP-IB_Command_Finder/SystCalAll.md#SYSTem:CALibrate:ALL:GUIDed:CHANnel:CATalog) |  None  
Returns available ports for independent power calibration. |  [SYSTem:CALibrate:ALL:INDependent:SOURce:CALibrate:CATalog?](GP-IB_Command_Finder/SystCalAll.md#SYSTem:CALibrate:ALL:INDependent:SOURce:CALibrate:CATalog) |  [ValidPorts](COM_Reference/Properties/ValidPorts.md)  
Adds a power cal range for a specific port <n>. |  [SYSTem:CALibrate:ALL:INDependent:SOURce:CALibrate:RANGe:ADD](GP-IB_Command_Finder/SystCalAll.md#SYSTem:CALibrate:ALL:INDependent:SOURce:CALibrate:RANGe:ADD) |  [AddPowerCalRange](COM_Reference/Methods/AddPowerCalRange_Method.md)  
Resets all ranges for the given source port <n>. |  [SYSTem:CALibrate:ALL:INDependent:SOURce:CALibrate:RANGe:CLEar](GP-IB_Command_Finder/SystCalAll.md#SYSTem:CALibrate:ALL:INDependent:SOURce:CALibrate:RANGe:CLEar) |  [Reset](COM_Reference/Methods/Reset_\(Independent_CalAll\)_Method.md)  
Queries how many ranges are included in the calibration for source port <n>. |  [SYSTem:CALibrate:ALL:INDependent:SOURce:CALibrate:RANGe:COUNt?](GP-IB_Command_Finder/SystCalAll.md#SYSTem:CALibrate:ALL:INDependent:SOURce:CALibrate:RANGe:COUNt) |  [RangeCount](COM_Reference/Properties/RangeCount_\(Independent_Power_Cal\)_Property.md)  
Sets and gets the number of points for range <m> for source port<n>. |  [SYSTem:CALibrate:ALL:INDependent:SOURce:CALibrate:RANGe:POINts](GP-IB_Command_Finder/SystCalAll.md#SYSTem:CALibrate:ALL:INDependent:SOURce:CALibrate:RANGe:POINts) |  [NumberOfPoints](COM_Reference/Properties/NumberOfPoints_\(PowerCalRange\)_Property.md)  
Sets and gets the start frequency for range <m> for source port<n>. |  [SYSTem:CALibrate:ALL:INDependent:SOURce:CALibrate:RANGe:STARt](GP-IB_Command_Finder/SystCalAll.md#SYSTem:CALibrate:ALL:INDependent:SOURce:CALibrate:RANGe:STARt) |  [StartFrequency](COM_Reference/Properties/StartFrequency_\(PowerCalRange\)_Property.md)  
Sets and gets the stop frequency for range <m> for source port<n>. |  [SYSTem:CALibrate:ALL:INDependent:SOURce:CALibrate:RANGe:STOP](GP-IB_Command_Finder/SystCalAll.md#SYSTem:CALibrate:ALL:INDependent:SOURce:CALibrate:RANGe:STOP) |  [StopFrequency](COM_Reference/Properties/StopFrequency_\(PowerCalRange\)_Property.md)  
  
Recall / Save / Apply a Calibration or Error Term  
---  
Recall a Calibration |  [SENSe:CORRection:CSET](GP-IB_Command_Finder/Sense/CorrCset.md#sccse) |  [app.Recall](COM_Reference/Methods/Recall_Method.md)  
Apply a Calibration to a measurement |  [SENSe:CORRection:CSET](GP-IB_Command_Finder/Sense/CorrCset.md#sccse) |  [app.Recall](COM_Reference/Methods/Recall_Method.md)  
Save a Calibration |  [SENSe:CORR:CSET:SAVE](GP-IB_Command_Finder/Sense/CorrCset.md#sccsv) |  [app.Save](COM_Reference/Methods/Save_Method.md)  
Save or Recall an Error Term |  [CALCulate:DATA Scorr](GP-IB_Command_Finder/Calculate/Data.md) |  [Data Topic](DataTopic.md)  
Read/ Write Cal Set data |  [SENSe:CORRection:CSET:DATA](GP-IB_Command_Finder/Sense/CorrCset.md#data) |  None  
Apply an Error Term after Uploading |  [SENSe:CORRection:COLLect:APPLy](GP-IB_Command_Finder/Sense/Sense_Correction.md#apply) |  None  
Cal Sets  
Quickly test a prototype of automation software |  [SENSe:CORRection:CSET:CREate:DEFault](GP-IB_Command_Finder/Sense/CorrCset.md#create) |  None  
Create a Cal Set |  [SENSe:CORRection:CSET:CREate](GP-IB_Command_Finder/Sense/CorrCset.md#create) |  [calMgr.CreateCalSet](COM_Reference/Methods/CreateCalSet_Method.md)  
Delete a Cal Set |  [SENSe:CORRection:CSET:DELete](GP-IB_Command_Finder/Sense/CorrCset.md#delete) |  [calMgr.DeleteCalSet](COM_Reference/Methods/DeleteCalSet_Method.md)  
List Cal Sets |  [CSET:CATalog?](GP-IB_Command_Finder/CSET.md#CAT) |  [calMgr.GetCalSetCatalog](COM_Reference/Methods/Get_CalSetCatalog_Method.md)  
List Cal Sets in VNA |  None |  [EnumerateCalSets](COM_Reference/Methods/EnumerateCalSets_Method.md)  
Get Cal Set Information |  None |  [calMgr.GetCalSetUsageInfo](COM_Reference/Methods/Get_CalSetUsageInfo_Method.md)  
List Cal Set Error Terms |  [SENSe:CORRection:CSET:ETERM:CATalog?](GP-IB_Command_Finder/Sense/CorrCset.md#etermCAT) |  [Get ErrorTermList2](COM_Reference/Methods/Get_ErrorTermList2_Method.md)  
Return if a Cal Set exists |  [CSET:EXISts?](GP-IB_Command_Finder/CSET.md#Exists) |  [Exists](COM_Reference/Methods/Exists_Method.md)  
|  |  None  
Select a Cal Set by GUID |  [SENSe:CORRection:CSET:ACTivate](GP-IB_Command_Finder/Sense/CorrCset.md#activate) |  [calMgr.GetCalSetByGUID](COM_Reference/Methods/Get_CalSetByGUID_Method.md)  
Apply a Cal Set to a channel |  [SENSe:CORRection:CSET:ACTivate](GP-IB_Command_Finder/Sense/CorrCset.md#activate) |  [channel.SelectCalSet](COM_Reference/Methods/SelectCalSet_Method.md)  
Copy a Cal Set |  [SENSe:CORRection:CSET:COPY](GP-IB_Command_Finder/Sense/CorrCset.md#copy) |  [CalSet.Copy](COM_Reference/Methods/Copy_Method.md)  
Save a Cal Set |  [SENSe:CORRection:CSET:SAVE](GP-IB_Command_Finder/Sense/CorrCset.md#sccsv) |  [CalSet.Save](COM_Reference/Methods/Save_CalSet_Method.md)  
Save Cal Sets |  None |  [app.SaveCalSets](COM_Reference/Methods/Save_CalSets_Method.md)  
Automatically save to User Cal Set |  [SENSe:CORRection:PREFerence:CSET:SAVE](GP-IB_Command_Finder/Sense/Sense_Correction.md#CsetSave) |  None  
Change the Description of a Cal Set |  [SENSe:CORRection:CSET:DESCription](GP-IB_Command_Finder/Sense/CorrCset.md#desc) |  [CalSet.Description](COM_Reference/Properties/Description_Property.md)  
Change the Name of a Cal Set |  [SENSe:CORRection:CSET:NAME](GP-IB_Command_Finder/Sense/CorrCset.md#name) |  [calset.Name](COM_Reference/Properties/Name_Calset_Property.md)  
Recall a Cal File |  [MMEMory:LOAD](GP-IB_Command_Finder/Memory.md#recall) |  [app.Recall](COM_Reference/Methods/Recall_Method.md)  
Save 'in-memory' Cal Set to disk. |  [SENSe:CORRection:CSET:FLATten](GP-IB_Command_Finder/Sense/CorrCset.md#Flatten) |  None  
Create Cal Set with De-embeded fixture removed. |  [CSET:FIXTure:DEEMbed](GP-IB_Command_Finder/CSET.md#deembed) |  [Deembed](COM_Reference/Methods/Deembed_Method.md)  
Create Cal Set with Matching Network included. |  [CSET:FIXTure:EMBed](GP-IB_Command_Finder/CSET.md#embed) |  [Embed](COM_Reference/Methods/Embed_Method.md)  
Adds stimulus data to a specific buffer. |  None |  [PutErrorTermStimulus](COM_Reference/Methods/PutErrorTermStimulus_Method.md)  
Returns the stimulus values over which the specific error term was acquired. |  None |  [GetErrorTermStimulus](COM_Reference/Methods/GetErrorTermStimulus_Method.md)  
Returns FOM stimulus values from a Calset. |  [SENSe:CORRection:CSET:STIMulus?](GP-IB_Command_Finder/Sense/CorrCset.md#Stimulus) |  [StimulusValues](COM_Reference/Properties/StimulusValues_Property.md)  
Returns the Cal Types from the calset. |  None |  [ContentDescriptor](COM_Reference/Properties/ContentDescriptor_Property.md)  
Returns the properties of the calset. |  None |  [Properties](COM_Reference/Properties/Properties_Property.md)  
Returns the numbers of the channels using the calset. |  None |  [ChannelClients](COM_Reference/Properties/ChannelClients_Property.md)  
Unselect Cal Set |  [SENSe:CORRection:CSET:DEACtivate](GP-IB_Command_Finder/Sense/CorrCset.md#DEACtivate) |  [UnselectCalset](COM_Reference/Methods/UnselectCalset_Method.md)  
  
Cal Set Items  
---  
Returns names of the items in a cal set |  [SENSe:CORRection:CSET:ITEM:CAT?](GP-IB_Command_Finder/Sense/CorrCset.md#SENSe:CORRection:CSET:ITEM:CATalog) |  [Item](COM_Reference/Properties/Item_Property.md)  
Remove name-value pair from cal set |  None |  [RemoveItem](COM_Reference/Methods/RemoveItem_Method.md)  
Read the value of the Cal Set item. |  [SENSe:CORRection:CSET:ITEM[:DATA]?](GP-IB_Command_Finder/Sense/CorrCset.md#SENSe:CORRection:CSET:ITEM:DATA) |  None  
Enumerate name-value pair items in the cal set. |  None |  [EnumerateItems](COM_Reference/Methods/EnumerateItems_Method.md)  
  
Apply Cal Types  
---  
Catalog ALL Cal Types for the PNA |  [SENSe:CORRection:TYPE:CATalog?](GP-IB_Command_Finder/Sense/Sense_Correction.md#catalog) |  [calMgr.GetCalTypes](COM_Reference/Methods/Get_CalTypes_Method.md)  
Catalog Cal Types in the Cal Set |  [SENSe:CORRection:CSET:TYPE:CATalog?](GP-IB_Command_Finder/Sense/CorrCset.md#TypeCat) |  None  
Is a specific Cal Type contained in the Cal Set? |  None |  [calMgr.HasCalType](COM_Reference/Methods/Has_CalType_Method.md)  
Set and return the measurement Cal Type |  [CALCulate:MEASure:CORRection:TYPE](GP-IB_Command_Finder/Calculate/MeasureCorrection.md#CALCulate:MEASure:CORRection:TYPE) |  [meas.CalibrationTypeID](COM_Reference/Properties/CalibrationTypeID_property.md)  
Set port to measure QSOLT reflection standards. |  None |  None  
  
Correction Settings  
---  
Turn Correction ON|OFF for a channel |  [SENSe:CORRection](GP-IB_Command_Finder/Sense/Sense_Correction.md#scs) |  [chan.ErrorCorrection](COM_Reference/Properties/ErrorCorrection_Channel_Property.md)  
Turn Correction ON|OFF for a measurement |  [CALCulate:MEASure:CORRection[:STATe]](GP-IB_Command_Finder/Calculate/MeasureCorrection.md#CALCulate:MEASure:CORRection:STATe) |  [meas.ErrorCorrection](COM_Reference/Properties/Error_Correction_Property.md)  
Interpolation ON|OFF |  [SENSe:CORRection:INTerpolate](GP-IB_Command_Finder/Sense/Sense_Correction.md#scis) |  [meas.InterpolateCorrection](COM_Reference/Properties/Interpolate_Correction_Property.md)  
Returns the error correction state for the measurement |  [CALCulate:MEASure:CORRection:INDicator?](GP-IB_Command_Finder/Calculate/MeasureCorrection.md#CALCulate:MEASure:CORRection:STATe:INDicator) |  [ErrorCorrectionIndicator](COM_Reference/Properties/ErrorCorrectionIndicator_Property.md)  
  
Preferences  
---  
Set default Cal Set Save behavior |  [SENSe:CORRection:PREFerence:CSET:SAVE](GP-IB_Command_Finder/Sense/Sense_Correction.md#CsetSave) |  [RemoteCalStoragePreference](COM_Reference/Properties/RemoteCalStoragePreference_Property.md)  
Sets behavior for simulated cal |  [SENSe:CORRection:PREFerence:SIMCal](GP-IB_Command_Finder/Sense/Sense_Correction.md#Simcal) |  None  
External or internal trigger during cal |  [SENSe:CORRection:PREFerence:TRIG:FREE](GP-IB_Command_Finder/Sense/Sense_Correction.md#PrefTrig) |  [PreferInternalTriggerOnUnguidedCal](COM_Reference/Properties/PreferInternalTriggerOnChannelSingle_Property.md)  
Set ECal Auto-orient |  [SENSe:CORRection:PREFerence:ECAL:ORIentation](GP-IB_Command_Finder/Sense/Sense_Correction.md#Orie) |  [cal.OrientECALModule](COM_Reference/Properties/OrientECALModule_Property.md)  
Set ECal Port Map |  [SENSe:CORRection:PREFerence:ECAL:PMAP](GP-IB_Command_Finder/Sense/Sense_Correction.md#Pmap) |  [cal.ECALPortMapEx](COM_Reference/Properties/ECALPortMapEx_Property.md)  
Set default Cal Type |  None |  None  
  
Port Extensions  
---  
Extensions ON|OFF |  [SENSe:CORRection:EXTension](GP-IB_Command_Finder/Sense/CorrExtension.md#ExtState) |  [portExtension.State](COM_Reference/Properties/State_Property.md)  
Port 1 Extensions Value |  [SENSe:CORRection:EXTension:PORT](GP-IB_Command_Finder/Sense/CorrExtension.md#PortTime) |  [portExt.Port1](COM_Reference/Properties/Port_1_Property.md)  
Port 2 Extensions Value |  [SENSe:CORRection:EXTension:PORT](GP-IB_Command_Finder/Sense/CorrExtension.md#PortTime) |  [portExt.Port2](COM_Reference/Properties/Port_2_Property.md)  
Set Freq 1|2 |  [SENSe:CORRection:EXTension:PORT:FREQuency](GP-IB_Command_Finder/Sense/CorrExtension.md#PortExtFreqX) |  [Fix.PortFreq1](COM_Reference/Properties/PortFreq1_Property.md)  
Set Loss 1|2 |  [SENSe:CORRection:EXTension:PORT:LOSS](GP-IB_Command_Finder/Sense/CorrExtension.md#PortExtLoss) |  [fix.PortLoss1](COM_Reference/Properties/PortLoss1_Property.md)  
Use 1|2 |  [SENSe:CORRection:EXTension:PORT:INCLude](GP-IB_Command_Finder/Sense/CorrExtension.md#PortExtIncl) |  [fix.PortExtUse1](COM_Reference/Properties/PortExtUse1_Property.md)  
Set Loss at DC |  [SENSe:CORRection:EXTension:PORT:LDC](GP-IB_Command_Finder/Sense/CorrExtension.md#LossDC) |  [fix.PortLossDC](COM_Reference/Properties/PortLossDC_Property.md)  
Relative Velocity |  [SENSe:CORRection:RVELocity:COAX](GP-IB_Command_Finder/Sense/Sense_Correction.md#scrc) |  [app.VelocityFactor](COM_Reference/Properties/Velocity_Factor_Property.md)  
Port Ext in distance |  [SENSe:CORRection:EXTension:PORT:DISTance](GP-IB_Command_Finder/Sense/CorrExtension.md#portDist) |  [PortDistance](COM_Reference/Properties/PortDistance_Property.md)  
Set distance units |  [SENSe:CORRection:EXTension:PORT:UNIT](GP-IB_Command_Finder/Sense/CorrExtension.md#UNIT) |  [PortDistanceUnit](COM_Reference/Properties/PortDistanceUnit_Property.md)  
Set Media per port |  [SENSe:CORRection:EXTension:PORT:MEDium](GP-IB_Command_Finder/Sense/CorrExtension.md#portMedium) |  [PortMedium](COM_Reference/Properties/PortMedium_Property.md)  
Set waveguide cutoff freq per port |  [SENSe:CORRection:EXTension:PORT:WGCutoff](GP-IB_Command_Finder/Sense/CorrExtension.md#portWGC) |  [PortWGCutoffFreq](COM_Reference/Properties/PortWGCutoffFreq_Property.md)  
Set Velocity Factor per port |  [SENSe:CORRection:EXTension:PORT:VELFactor](GP-IB_Command_Finder/Sense/CorrExtension.md#portVF) |  [PortVelocityFactor](COM_Reference/Properties/PortVelocityFactor_Property.md)  
Couple to system Velocity Factor |  [SENSe:CORRection:EXTension:PORT:SYSVelocity](GP-IB_Command_Finder/Sense/CorrExtension.md#sysVelocity) |  [PortCoupleToSystemVelocity](COM_Reference/Properties/PortCoupleToSystemVelocity_Property.md)  
Couple to system Media type |  [SENSe:CORRection:EXTension:PORT:SYSMedia](GP-IB_Command_Finder/Sense/CorrExtension.md#sysMedia) |  [PortCoupleToSystemMedia](COM_Reference/Properties/PortCoupleToSystemMedia_Property.md)  
  
Auto Port Extensions  
---  
Measure OPEN or SHORT for Auto Port Ext. |  [SENSe:CORRection:EXTension:AUTO:MEASure](GP-IB_Command_Finder/Sense/CorrExtension.md#autoMeas) |  [AutoPortExtMeasure](COM_Reference/Methods/AutoPortExtMeasure_Method.md)  
Sets the frequencies used for Auto Port Ext. calculation. |  [SENSe:CORRection:EXTension:AUTO:CONFig](GP-IB_Command_Finder/Sense/CorrExtension.md#autoConfig) |  [AutoPortExtConfig](COM_Reference/Properties/AutoPortExtConfig_Property.md)  
Include loss correction in Auto Port Ext.? |  [SENSe:CORRection:EXTension:AUTO:LOSS](GP-IB_Command_Finder/Sense/CorrExtension.md#AutoLoss) |  [AutoPortExtLoss](COM_Reference/Properties/AutoPortExtLoss_Property.md)  
Include DC Offset in Auto Port Ext.? |  [SENSe:CORRection:EXTension:AUTO:DCOFfset](GP-IB_Command_Finder/Sense/CorrExtension.md#AutoDCOffset) |  [AutoPortExtDCOffset](COM_Reference/Properties/AutoPortExtDCOffset_Property.md)  
Enable specified port for Auto Port Ext.. |  [SENSe:CORRection:EXTension:AUTO:PORT<n>](GP-IB_Command_Finder/Sense/CorrExtension.md#autoPort) |  [AutoPortExtState](COM_Reference/Properties/AutoPortExtState_Property.md)  
Clears old port extension delay and loss data. |  [SENSe:CORRection:EXTension:AUTO:RESet](GP-IB_Command_Finder/Sense/CorrExtension.md#autoReset) |  [AutoPortExtReset](COM_Reference/Methods/AutoPortExtReset_Method.md)  
Set user span start frequency for Auto Port Ext. |  [SENSe:CORRection:EXTension:AUTO:STARt](GP-IB_Command_Finder/Sense/CorrExtension.md#autoStart) |  [AutoPortExtSearchStart](COM_Reference/Properties/AutoPortExtSearchStart_Property.md)  
Set user span stop frequency for Auto Port Ext. |  [SENSe:CORRection:EXTension:AUTO:STOP](GP-IB_Command_Finder/Sense/CorrExtension.md#autoStop) |  [AutoPortExtSearchStop](COM_Reference/Properties/AutoPortExtSearchStop_Property.md)  
  
Fixturing Commands See also [Ground Loop De-
embedding/Embedding](DataTopic.htm#Ground_Loop) commands  
---  
Turn fixturing ON and OFF |  [CALCulate:FSIMulator:STATe](GP-IB_Command_Finder/Calculate/FSimulator.md#FSimState) |  [FixturingState](COM_Reference/Properties/FixturingState_Property.md)  
Change order of operations |  [CALCulate:FSIMulator:SENDed:OORDer](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#oorder) |  None  
2and 4-port Extrapolate |  [CALCulate:FSIMulator:SNP:EXTRapolate](GP-IB_Command_Finder/Calculate/FSimulator.md#extrapolate) |  [EnableSnPDataExtrapolation](COM_Reference/Properties/EnableSnPDataExtrapolation_Property.md)  
2-Port Fixturing  
Port matching ON and OFF |  [CALCulate:FSIMulator:SENDed:PMCircuit:STATe](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#PMCState) |  [PortMatchingState](COM_Reference/Properties/PortMatchingState_Property.md)  
Reverse ports |  [CALCulate:FSIMulator:SENDed:DEEMbed:PORT<n>:SNP:REVerse](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#ReversePorts) |  [Reverse2PortAdapter](COM_Reference/Properties/Reverse2PortAdapter_Property.md)  
Sets Port Matching circuit model. |  [CALCulate:FSIMulator:SENDed:PMCircuit:PORT:TYPE](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#pmcType) |  [PortMatchingCktModel](COM_Reference/Properties/PortMatchingCktModel_Property.md)  
Sets Port Matching 'S2P' file name. |  [CALCulate:FSIMulator:SENDed:PMCircuit:PORT:USER:FILename](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#pmcFileName) |  [strPortMatch_S2PFile](COM_Reference/Properties/strPortMatch_S2PFile_Property.md)  
Sets Capacitance 'C' value. |  [CALCulate:FSIMulator:SENDed:PMCircuit:PORT:PARameters:C](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#pmcC) |  [PortMatching_C](COM_Reference/Properties/PortMatching_C_Property.md)  
Sets Conductance 'G' value. |  [CALCulate:FSIMulator:SENDed:PMCircuit:PORT:PARameters:G](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#pmcG) |  [PortMatching_G](COM_Reference/Properties/PortMatching_G_Property.md)  
Sets Inductance 'L' value. |  [CALCulate:FSIMulator:SENDed:PMCircuit:PORT:PARameters:L](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#pmcL) |  [PortMatching_L](COM_Reference/Properties/PortMatching_L_Property.md)  
Sets Resistance 'R' value. |  [CALCulate:FSIMulator:SENDed:PMCircuit:PORT:PARameters:R](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#pmcR) |  [PortMatching_R](COM_Reference/Properties/PortMatching_R_Property.md)  
De-embed ON and OFF |  [CALCulate:FSIMulator:SENDed:DEEMbed:STATe](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#DeemState) |  [Port2PdeembedState](COM_Reference/Properties/Port2PdeembedState_Property.md)  
Sets De-embedding circuit model. |  [CALCulate:FSIMulator:SENDed:DEEMbed:PORT](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#deembedType) |  [Port2PdeembedCktModel](COM_Reference/Properties/Port2PdeembedCktModel_Property.md)  
Sets De-embedding 'S2P' file name. |  [CALCulate:FSIMulator:SENDed:DEEMbed:PORT:USER:FILename](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#deembedFileName) |  [strPort2Pdeembed_S2PFile](COM_Reference/Properties/strPort2Pdeembed_S2PFile_Property.md)  
Port Impedance ON and OFF |  [CALCulate:FSIMulator:SENDed:ZCONversion:STATe](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#ZState) |  [PortArbzState](COM_Reference/Properties/PortArbzState_Property.md)  
Port Z Real |  [CALCulate:FSIMulator:SENDed:ZCONversion:PORT:REAL](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#ZReal) |  [PortArbzReal](COM_Reference/Properties/PortArbzReal_Property.md)  
Port Z Imag |  [CALCulate:FSIMulator:SENDed:ZCONversion:PORT:IMAG](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#ZImag) |  [PortArbzImag](COM_Reference/Properties/PortArbzImag_Property.md)  
Port Z Real and Imag |  [CALCulate:FSIMulator:SENDed:ZCONversion:PORT:Z0](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#ZValue) |  [PortArbzZ0](COM_Reference/Properties/PortArbzZ0_Property.md)  
4-Port Network Embed/De-embed commands  
Specifies the PNA / DUT topology |  [CALCulate:FSIMulator:EMBed:TYPE](GP-IB_Command_Finder/Calculate/FSimulatorEmbed.md#TopType) |  [Embed4PortTopology](COM_Reference/Properties/Embed4PortTopology_Property.md)  
Specifies the 4-port touchstone file |  [CALCulate:FSIMulator:EMBed:NETWork:FILename](GP-IB_Command_Finder/Calculate/FSimulatorEmbed.md#Filename) |  [Embed4PortNetworkFilename](COM_Reference/Properties/Embed4PortNetworkFilename_Property.md)  
Embed|De-embed? |  [CALCulate:FSIMulator:EMBed:NETWork:TYPE](GP-IB_Command_Finder/Calculate/FSimulatorEmbed.md#type) |  [Embed4PortNetworkMode](COM_Reference/Properties/Embed4PortNetworkMode_Property.md)  
Specify PNA port connections |  [CALCulate:FSIMulator:EMBed:TOPology:A:PORTs](GP-IB_Command_Finder/Calculate/FSimulatorEmbed.md#topA) [CALCulate:FSIMulator:EMBed:TOPology:B:PORTs](GP-IB_Command_Finder/Calculate/FSimulatorEmbed.md#topB) [CALCulate:FSIMulator:EMBed:TOPology:C:PORTs](GP-IB_Command_Finder/Calculate/FSimulatorEmbed.md#topC) [CALCulate:FSIMulator:EMBed:TOPology:D:PORTs](GP-IB_Command_Finder/Calculate/FSimulatorEmbed.md#topD) |  [Embed4PortList](COM_Reference/Properties/Embed4PortList_Property.md) [SetCustomDUTTopology](COM_Reference/Methods/SetCustomDUTTopology_Method.md)  
4-port remap |  [CALCulate:FSIMulator:EMBed:NETWork<n>:PMAP](GP-IB_Command_Finder/Calculate/FSimulatorEmbed.md#pmap) |  [NetworkPortMap](COM_Reference/Methods/NetworkPortMap_Method.md)  
Turn ON or OFF |  [CALCulate:FSIMulator:EMBed:STATe](GP-IB_Command_Finder/Calculate/FSimulatorEmbed.md#state) |  [Embed4PortState](COM_Reference/Properties/Embed4PortState_Property.md)  
Maps the physical VNA ports to a device of balanced and single-ended logical ports for multi-port systems with greater than 4 ports |  [CALCulate:DTOPology](GP-IB_Command_Finder/Calculate/Calculate_DTOPology_Command.md) |  [SetCustomDUTTopology](COM_Reference/Methods/SetCustomDUTTopology_Method.md)  
Differential Port Arbitrary Impedance  
Sets the impedance value |  [CALCulate:FSIMulator:BALun:DZConversion:BPORT:Z0](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#dzcR) |  [DiffZConvPortZ0](COM_Reference/Properties/DiffZConvPortZ0_Property.md)  
Sets real part of impedance |  [CALCulate:FSIMulator:BALun:DZConversion:BPORT:REAL](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#dzcReal) |  [DiffZConvPortReal](COM_Reference/Properties/DiffZConvPortReal_Property.md)  
Sets imaginary part of impedance |  [CALCulate:FSIMulator:BALun:DZConversion:BPORT:IMAG](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#dzcImag) |  [DiffZConvPortImag](COM_Reference/Properties/DiffZConvPortImag_Property.md)  
Turn ON or OFF |  [CALCulate:FSIMulator:BALun:DZConversion:STATe](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#dzcState) |  [DiffZConvState](COM_Reference/Properties/DiffZConvState_Property.md)  
Common Mode Port Arbitrary Impedance  
Sets the impedance value |  [CALCulate:FSIMulator:BALun:CZConversion:BPORT:Z0](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#CzcR) |  [CmnModeZConvPortZ0](COM_Reference/Properties/CmnModeZConvPortZ0_Property.md)  
Sets real part of impedance |  [CALCulate:FSIMulator:BALun:CZConversion:BPORT:REAL](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#czcReal) |  [CmnModeZConvPortReal](COM_Reference/Properties/CmnModeZConvPortReal_Property.md)  
Sets imaginary part of impedance |  [CALCulate:FSIMulator:BALun:CZConversion:BPORT:IMAG](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#CzcImag) |  [CmnModeZConvPortImag](COM_Reference/Properties/CmnModeZConvPortImag_Property.md)  
Turn ON or OFF |  [CALCulate:FSIMulator:BALun:CZConversion:STATe](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#czcState) |  [CmnModeZConvState](COM_Reference/Properties/CmnModeZConvState_Property.md)  
Differential Port Matching  
Sets type of circuit to embed. |  [CALCulate:FSIMulator:BALun:DMCircuit:BPORt](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#dmcType) |  [DiffPortMatchMode](COM_Reference/Properties/DiffPortMatchMode_Property.md)  
Specifies the 2-port touchstone file |  [CALCulate:FSIMulator:BALun:DMCircuit:BPORt:USER:FILename](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#dmcFilename) |  [DiffPortMatchUserFilename](COM_Reference/Properties/DiffPortMatchUserFilename_Property.md)  
Sets Capacitance value |  [CALCulate:FSIMulator:BALun:DMCircuit:BPORt:PARameters:C](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#dmcParC) |  [DiffPortMatch_C](COM_Reference/Properties/DiffPortMatch_C_Property.md)  
Sets Conductance value |  [CALCulate:FSIMulator:BALun:DMCircuit:BPORt:PARameters:G](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#dmcParG) |  [DiffPortMatch_G](COM_Reference/Properties/DiffPortMatch_G_Property.md)  
Sets Inductance value |  [CALCulate:FSIMulator:BALun:DMCircuit:BPORt:PARameters:L](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#dmcParL) |  [DiffPortMatch_L](COM_Reference/Properties/DiffPortMatch_L_Property.md)  
Sets Resistance value |  [CALCulate:FSIMulator:BALun:DMCircuit:BPORt:PARameters:R](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#dmcParR) |  [DiffPortMatch_R](COM_Reference/Properties/DiffPortMatch_R_Property.md)  
Turns ON/OFF |  [CALCulate:FSIMulator:BALun:DMCircuit:STATe](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#dmcState) |  [DiffPortMatchState](COM_Reference/Properties/DiffPortMatchState_Property.md)  
Power Compensation  
Compensate source power |  [CALCulate:FSIMulator:SENDed:POWer:PORT:COMPensation](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#PowerPortComp) |  [EnablePowerCompensation](COM_Reference/Properties/EnablePowerCompensation_Property.md)  
Remote ONLY  
Create Cal Set with De-embeded fixture removed. |  [CSET:FIXTure:DEEMbed](GP-IB_Command_Finder/CSET.md#deembed) |  [Deembed](COM_Reference/Methods/Deembed_Method.md)  
Create Cal Set with Matching network included. |  [CSET:FIXTure:EMBed](GP-IB_Command_Finder/CSET.md#embed) |  [Embed](COM_Reference/Methods/Embed_Method.md)  
  
Cal Plane Manager |  SCPI |  COM  
---|---|---  
Characterize a fixture |  [CSET:FIXTure:CHARacterize](GP-IB_Command_Finder/CSET.md#fixtureCharacter) |  [CharacterizeFixture](COM_Reference/Methods/CharacterizeFixture_Method.md)  
Creates a single S2P file from two existing files. |  [CSET:FIXTure:CASCade](GP-IB_Command_Finder/CSET.md#FIXTureCASCade) |  [CascadeS2PFiles](COM_Reference/Methods/CascadeS2PFiles_Method.md)  
  
Global Delta Match Cal  
---  
Initiate Cal |  [SENSe:CORRection:COLLect:GUIDed:DMATch](GP-IB_Command_Finder/Sense/CorrGuided.md#DmatchInit) |  [guid.GenerateGlobalDeltaMatchSequence](COM_Reference/Methods/GenerateGlobalDeltaMatchSequence_Method.md)  
Read ports that require Cal |  [SENSe:CORRection:COLLect:GUIDed:DMATch:APPLy:PORTs?](GP-IB_Command_Finder/Sense/CorrGuided.md#DmatchApplyPorts) |  [guid.PortsNeedingDeltaMatch](COM_Reference/Properties/PortsNeedingDeltaMatch_Property.md)  
Apply a Cal |  [SENSe:CORRection:COLLect:GUIDed:DMATch:APPLy](GP-IB_Command_Finder/Sense/CorrGuided.md#DmatchApply) |  [guid.ApplyDeltaMatchFromCalSet](COM_Reference/Methods/ApplyDeltaMatchFromCalSet_Method.md)  
  
Manage and Modify Cal Kits  
---  
Set a Cal Kit Active |  [SENSe:CORRection:COLLect:CKIT](GP-IB_Command_Finder/Sense/CorrCollCKIT.md#scccs) |  [app.CalKitType](COM_Reference/Properties/CalKitType_Property.md)  
Clear all Cal Kits from PNA |  [SENSe:CORRection:CKIT:CLEar](GP-IB_Command_Finder/Sense/CorrCKIT_SCPI.md#clear) |  None  
Get a Handle to the Active Cal Kit |  None |  [app.ActiveCalKit](COM_Reference/Properties/Active_Cal_Kit_Property.md)  
Save All Cal Kits after Modifying |  None |  [app.SaveKits](COM_Reference/Methods/Save_Kits_Method.md)  
Load collection of Kits |  [SENSe:CORRection:CKIT:LOAD](GP-IB_Command_Finder/Sense/CorrCKIT_SCPI.md#load) |  None  
Load (Recall) All Cal Kits |  None |  [app.RecallKits](COM_Reference/Methods/Recall_Kits_Method.md)  
Import a specified kit. |  [SENSe:CORRection:CKIT:IMPort](GP-IB_Command_Finder/Sense/CorrCKIT_SCPI.md#import) |  None  
Restore Cal Kit Default |  [SENSe:CORRection:COLLect:CKIT:RESet](GP-IB_Command_Finder/Sense/CorrCollCKIT.md#scccr) |  None  
Restore ALL Cal Kits Default |  [SENSe:CORRection:CKIT:INITialize](GP-IB_Command_Finder/Sense/CorrCKIT_SCPI.md#initialize) |  None  
Build a Hybrid Cal Kit |  None |  [app.BuildHybridKit](COM_Reference/Methods/Build_Hybrid_Kit_Method.md)  
Set the Name of a Cal Kit |  [SENSe:CORRection:COLLect:CKIT:NAME](GP-IB_Command_Finder/Sense/CorrCollCKIT.md#scccn) |  [calKit.Name](COM_Reference/Properties/Name_CalKit_Property.md)  
Set a description of a Cal Kit |  [SENSe:CORRection:COLLect:CKIT:DESCription](GP-IB_Command_Finder/Sense/CorrCollCKIT.md#desc) |  None  
Get the amount of installed kits |  [SENSe:CORRection:CKIT:COUNt?](GP-IB_Command_Finder/Sense/CorrCKIT_SCPI.md#count) |  None  
Set the Port Label of a Cal Kit |  None |  [calKit.Portlabel](COM_Reference/Properties/PortLabel_Property.md)  
Saves a Cal Kit to a file. |  [SENSe:CORRection:CKIT:EXPort](GP-IB_Command_Finder/Sense/CorrCKIT_SCPI.md#Export) |  None  
  
Modify TRL Cal Kit  
---  
Set reference plane |  [SENSe:CORRection:COLLect:CKIT:TRLoption:RPLane](GP-IB_Command_Finder/Sense/CorrCollCKIT.md#TRLRplane) |  None  
Set impedance standard |  [SENSe:CORRection:COLLect:CKIT:TRLoption:IMPedance](GP-IB_Command_Finder/Sense/CorrCollCKIT.md#TRLImpedance) |  None  
Set LRL auto-characterization |  [SENSe:CORRection:COLLect:CKIT:TRLoption:LRLChar](GP-IB_Command_Finder/Sense/CorrCollCKIT.md#TRLLRLChar) |  None  
  
Modify Cal Standards  
---  
Select a Cal Standard |  [SENSe:CORRection:COLLect:CKIT:STANdard](GP-IB_Command_Finder/Sense/CorrCollCKIT.md#ss) |  [calkit.GetCalStandard](COM_Reference/Methods/Get_Cal_Standard_Method.md)  
Delete a standard |  [SENSe:CORRection:COLLect:CKIT:STANdard:REMove](GP-IB_Command_Finder/Sense/CorrCollCKIT.md#delete) |  None  
Change description of a standard |  [SENSe:CORRection:COLLect:CKIT:STANdard:SDEScription](GP-IB_Command_Finder/Sense/CorrCollCKIT.md#sdes) |  None  
Assign a Class to a Standard |  [SENSe:CORRection:COLLect:CKIT:ORDer1](GP-IB_Command_Finder/Sense/CorrCollCKIT.md#sccco) |  [calKit.StandardForClass](COM_Reference/Properties/StandardForClass_Property.md)  
Set Standard Type |  [SENSe:CORRection:COLLect:CKIT:STANdard:TYPE](GP-IB_Command_Finder/Sense/CorrCollCKIT.md#st) |  [calstd.Type](COM_Reference/Properties/Type_calstd_Property.md)  
Add connector family name |  [SENSe:CORRection:COLLect:CKIT:CONNector:ADD](GP-IB_Command_Finder/Sense/CorrCollCKIT.md#add) |  None  
Delete connector family name |  [SENSe:CORRection:COLLect:CKIT:CONNector:DELete](GP-IB_Command_Finder/Sense/CorrCollCKIT.md#ConnDelete) |  None  
List connector family names used in a Cal Kit |  [SENSe:CORRection:COLLect:CKIT:CONNector:CATalog?](GP-IB_Command_Finder/Sense/CorrCollCKIT.md#cat) |  None  
Replace connector family name. |  [SENSe:CORRection:COLLect:CKIT:CONNector:FNAMe](GP-IB_Command_Finder/Sense/CorrCollCKIT.md#Fname) |  None  
Assign connector family name to a standard |  [SENSe:CORRection:COLLect:CKIT:CONNector:SNAMe](GP-IB_Command_Finder/Sense/CorrCollCKIT.md#sname) |  None  
Set Delay |  [SENSe:CORRection:COLLect:CKIT:STANard:DELay](GP-IB_Command_Finder/Sense/CorrCollCKIT.md#sd) |  [calstd.Delay](COM_Reference/Properties/Delay_Property.md)  
Set Loss |  [SENSe:CORRection:COLLect:CKIT:STANdard:LOSS](GP-IB_Command_Finder/Sense/CorrCollCKIT.md#sls) |  [calstd.loss](COM_Reference/Properties/Loss_Property.md)  
Set Impedance |  [SENSe:CORRection:COLLect:CKIT:STANdard:IMPedance](GP-IB_Command_Finder/Sense/CorrCollCKIT.md#si) |  [calstd.Z0](COM_Reference/Properties/Z0_Property.md)  
Set Max Frequency |  [SENSe:CORRection:COLLect:CKIT:STANdard:FMAXimum](GP-IB_Command_Finder/Sense/CorrCollCKIT.md#sfx) |  [calstd.MaximumFrequency](COM_Reference/Properties/MaximumFrequency_Property.md)  
Set Min Frequency |  [SENSe:CORRection:COLLect:CKIT:STANdard:FMINimum](GP-IB_Command_Finder/Sense/CorrCollCKIT.md#sfn) |  [calstd.MinimumFrequency](COM_Reference/Properties/MinimumFrequency_Property.md)  
Set Label |  [SENSe:CORRection:COLLect:CKIT:STANdard:LABel](GP-IB_Command_Finder/Sense/CorrCollCKIT.md#sl) |  [calstd.Label](COM_Reference/Properties/Label_Property.md)  
Set Medium (coax | waveguide) |  [SENSe:CORRection:COLLect:CKIT:STANdard:CHARacter](GP-IB_Command_Finder/Sense/CorrCollCKIT.md#sc) |  [calstd.Medium](COM_Reference/Properties/Medium_Property.md)  
Set Capacitance (C0 to C3) |  [SENSe:CORRection:COLLect:CKIT:STANdard:C0](GP-IB_Command_Finder/Sense/CorrCollCKIT.md#c0) |  [calstd.C0](COM_Reference/Properties/C0_Property.md)  
Set Inductance (L0 to L3) |  [SENSe:CORRection:COLLect:CKIT:STANdard:L0](GP-IB_Command_Finder/Sense/CorrCollCKIT.md#l0) |  [calstd.L0](COM_Reference/Properties/L0_Property.md)  
Set Arbitrary Impedance (TZReal, TZImag) |  [SENSe:CORRection:COLLect:CKIT:STANdard:TZReal](GP-IB_Command_Finder/Sense/CorrCollCKIT.md#TZReal) |  [calstd.TZReal](COM_Reference/Properties/TZReal_Property.md)  
  
Modify TRL Cal Kit  
---  
Set reference plane |  [SENSe:CORRection:COLLect:CKIT:TRLoption:RPLane](GP-IB_Command_Finder/Sense/CorrCollCKIT.md#TRLRplane) |  None  
Set impedance standard |  [SENSe:CORRection:COLLect:CKIT:TRLoption:IMPedance](GP-IB_Command_Finder/Sense/CorrCollCKIT.md#TRLImpedance) |  None  
Set LRL auto-characterization |  [SENSe:CORRection:COLLect:CKIT:TRLoption:LRLChar](GP-IB_Command_Finder/Sense/CorrCollCKIT.md#TRLLRLChar) |  None  
  
### Real-time Uncertainty

Setup Options  
---  
![](../assets/images/UncertOpts.gif) |  [SYSTem:UNCertainty:ETERm:NOIS:ENAB](GP-IB_Command_Finder/SystUncertainty.md#EtermNoiseEnable) |  [PortNoiseEnabled](COM_Reference/Properties/PortNoiseEnabled_Property.md)  
[SYSTem:UNCertainty:ETERm:CABLe:REPeat](GP-IB_Command_Finder/SystUncertainty.md#EtermCableRepeatEnab) |  [CableRepeatabilityEnabled](COM_Reference/Properties/CableRepeatabilityEnabled_Property.md)  
[SYSTem:UNCertainty:ETERm:SDEFinitions](GP-IB_Command_Finder/SystUncertainty.md#EtermSdef) |  [StandardDefinitionsEnabled](COM_Reference/Properties/StandardDefinitionsEnabled_Property.md)  
[SYSTem:UNCertainty:POINts:MAXimum](GP-IB_Command_Finder/SystUncertainty.md#PointsMAX) |  [MaximumUncertaintyPoints](COM_Reference/Properties/MaximumUncertaintyPoints_Property.md)  
  
Noise Characterization  
---  
Clear noise data on specified port |  [SYSTem:UNCertainty:PORT<p>:NOISe:RESet](GP-IB_Command_Finder/SystUncertainty.md#NOISeRESet) |  [ResetNoise](COM_Reference/Methods/ResetNoise_Method.md)  
Clear noise data on all ports |  [SYSTem:UNCertainty:PORT:NOISe:RESet](GP-IB_Command_Finder/SystUncertainty.md#NOISeRESet) |  [ResetNoiseForAllPorts](COM_Reference/Methods/ResetNoiseForAllPorts_Method.md)  
Copy noise from a port to all ports |  [SYSTem:UNCertainty:PORT:NOISe:ALL:COPY](GP-IB_Command_Finder/SystUncertainty.md#NoiseAllCopy) |  [CopyNoiseToAllPorts](COM_Reference/Methods/CopyNoiseToAllPorts_Method.md)  
Start Noise char |  [SENSe:CORRection:COLLect:GUIDed:UNCertainty:CHARacterize:NOISe](GP-IB_Command_Finder/Sense/CorrGuided.md#UncertNoiseInit) |  [InitiateNoiseCharacterization](COM_Reference/Methods/InitiateNoiseCharacterization_Method.md)  
  
Cables Characterization  
---  
List cables |  [SYSTem:UNCertainty:CABLe:CATalog?](GP-IB_Command_Finder/SystUncertainty.md#CABLeCAT) |  [Cables Collection](COM_Reference/Objects/Cables_Collection.md)  
Assign Cable to all ports |  [SYSTem:UNCertainty:PORT:CABLe:ALL](GP-IB_Command_Finder/SystUncertainty.md#CABLeSelALL) |  [SelectCableForAllPorts](COM_Reference/Methods/SelectCableForAllPorts_Method.md)  
Assign Cable to specified port |  [SYSTem:UNCertainty:PORT<p>:CABLe](GP-IB_Command_Finder/SystUncertainty.md#CABLeSELect) |  [Cable](COM_Reference/Properties/Cable_Property.md)  
Reset repeatability |  [SYSTem:UNCertainty:CABL:REP:RES](GP-IB_Command_Finder/SystUncertainty.md#CABLeRESet) |  [ResetRepeatability](COM_Reference/Methods/ResetRepeatability_Method.md)  
Start Cable char |  [SENS:CORR:COLL:GUID:UNCertainty:CHAR:CABLe](GP-IB_Command_Finder/Sense/CorrGuided.md#UncertCableINIT) |  [InitiateCableCharacterization](COM_Reference/Methods/InitiateCableCharacterization_Method.md)  
  
Uncertainty workspace  
---  
Load workspace |  [SYSTem:UNCertainty:LOAD](GP-IB_Command_Finder/SystUncertainty.md#LOAD) |  [Recall](COM_Reference/Methods/Recall_uncert_Method.md)  
Save workspace |  [SYSTem:UNCertainty:STORe](GP-IB_Command_Finder/SystUncertainty.md#STORe) |  [Save](COM_Reference/Methods/Save_uncert_Method.md)  
  
Enabling a Guided Calibration to include Uncertainties  
---  
Checkbox on [Guided Cal Select Ports](../S3_Cals/Calibration_Wizard.md#GuidedSelCalType) page |  [SENSe:CORRection:COLectL:GUIDed:UNCertainty](GP-IB_Command_Finder/Sense/CorrGuided.md#UncertEnab) |  [UncertaintyEnabled](COM_Reference/Properties/UncertaintyEnabled_Property.md)  
  
Trace Properties  
---  
![](../assets/images/UncertTracePropDiag.gif) |  [CALCulate:MEASure:UNCertainty:DISPlay:TYPE](GP-IB_Command_Finder/Calculate/MeasureUncertainty.md#CALCulate:MEASure:UNCertainty:DISPlay:TYPE) |  [DisplayType](COM_Reference/Properties/DisplayType_Property.md)  
[CALCulate:MEASure:UNCertainty:DISPlay:CFACtor](GP-IB_Command_Finder/Calculate/MeasureUncertainty.md#CALCulate:MEASure:UNCertainty:DISPlay:CFACtor) |  [CoverageFactor](COM_Reference/Properties/CoverageFactor_Property.md)  
[CALCulate:MEASure:UNCertainty:MODE:NOISe](GP-IB_Command_Finder/Calculate/MeasureUncertainty.md#CALCulate:MEASure:UNCertainty:MODE:NOISe) |  [MeasurementNoiseUncertainty](COM_Reference/Properties/MeasurementNoiseUncertainty_Property.md)  
[CALCulate:MEASure:UNCertainty:MODE:CABLe:REPeat](GP-IB_Command_Finder/Calculate/MeasureUncertainty.md#CALCulate:MEASure:UNCertainty:MODE:CABLe:REPeat) |  [CableRepeatabilityUncertainty](COM_Reference/Properties/CableRepeatabilityUncertainty_Property.md)  
[CALCulate:MEASure:UNCertainty:MODE:ETERm](GP-IB_Command_Finder/Calculate/MeasureUncertainty.md#CALCulate:MEASure:UNCertainty:MODE:ETERm) |  [ErrorTermUncertainty](COM_Reference/Properties/ErrorTermUncertainty_Property.md)  
Apply to all traces |  None |  None  
Add Trace |  None |  None  
Save uncertainty data |  [CALCulate:MEASure:UNCertainty:SAVE](GP-IB_Command_Finder/Calculate/MeasureUncertainty.md#CALCulate:MEASure:UNCertainty:SAVE) |  [WriteUncertaintyFile](COM_Reference/Methods/WriteUncertaintyFile_Method.md)  
  
Multiple Power Sensors [See commands to configure a Power Meter as Receiver
(PMAR)](XTraceChanTopic.htm#PMAR)  
---  
Enable multiple sensors |  [SENSe:CORRection:COLLect:GUIDed:PSENsor:MULTiple](GP-IB_Command_Finder/Sense/CorrCollGuidPSens.md#multState) |  [UseMultipleSensors](COM_Reference/Properties/UseMultipleSensors_Property.md)  
Add sensors |  [SENSe:CORRection:COLLect:GUIDed:PSENsor:MULTiple:ADD](GP-IB_Command_Finder/Sense/CorrCollGuidPSens.md#MultAdd) |  [Add](COM_Reference/Methods/Add_GuidedPowerSensors_Method.md)  
Assign power sensor name |  [SENSe:CORRection:COLLect:GUIDed:PSENsor:MULTiple:NAME](GP-IB_Command_Finder/Sense/CorrCollGuidPSens.md#multName) |  [Name](COM_Reference/Properties/Name_PowerSensor_Property.md)  
Remove sensors |  [SENSe:CORRection:COLLect:GUIDed:PSENsor:MULTiple:REMove](GP-IB_Command_Finder/Sense/CorrCollGuidPSens.md#multRemove) |  [Remove](COM_Reference/Methods/Remove_Method.md)  
Read the number of configured sensors |  [SENSe:CORRection:COLLect:GUIDed:PSENsor:MULTiple:COUNt?](GP-IB_Command_Finder/Sense/CorrCollGuidPSens.md#multCount) |  [Count](COM_Reference/Properties/Count_Property.md)  
Set start freq |  [SENSe:CORRection:COLLect:GUIDed:PSENsor:MULTiple:FREQuency:STARt](GP-IB_Command_Finder/Sense/CorrCollGuidPSens.md#multFreqStart) |  [StartFrequency](COM_Reference/Properties/Start_Frequency_Property.md)  
Set stop freq |  [SENSe:CORRection:COLLect:GUIDed:PSENsor:MULTiple:FREQuency:STOP](GP-IB_Command_Finder/Sense/CorrCollGuidPSens.md#multFreqStop) |  [StopFrequency](COM_Reference/Properties/Stop_Frequency_Property.md)  
Set connector type |  [SENSe:CORRection:COLLect:GUIDed:PSENsor:MULTiple:CONNector](GP-IB_Command_Finder/Sense/CorrCollGuidPSens.md#MultConn) |  [PowerSensorConnectorType](COM_Reference/Properties/PowerSensorConnectorType_Property.md)  
Set Cal Kit |  [SENSe:CORRection:COLLect:GUIDed:PSENsor:MULTiple:CKIT](GP-IB_Command_Finder/Sense/CorrCollGuidPSens.md#MultCKIT) |  [PowerSensorCalKitType](COM_Reference/Properties/PowerSensorCalKitType_Property.md)  
  
Source Power Calibration  
---  
Copy Source Power cal to another channel |  [SYSTem:MACRo:COPY:CHANnel:SOURce](GP-IB_Command_Finder/System.md#copySPC) |  [ApplySourcePowerCorrectionTo](COM_Reference/Methods/ApplySourcePowerCorrectionTo_Method.md)  
GPIB Power Meter Address |  [SYSTem:COMMunicate:GPIB:PMETer:ADDRess](GP-IB_Command_Finder/SystCommunicate.md#gpibadd) |  [pwrCal.PowerMeterGPIBAddress](COM_Reference/Properties/PowerMeterGPIBAddress_Property.md)  
Set source power cal method |  [SOURce:POWer:CORRection:COLLect:ACQ](GP-IB_Command_Finder/SourceCorrection.md#aquire) |  [SetCalInfoEx Method](COM_Reference/Methods/SetCalInfoEx_Method.md)  
Turn correction ON|OFF |  [SOURce:POWer:CORRection](GP-IB_Command_Finder/SourceCorrection.md#state) |  [SourcePowerCorrection](COM_Reference/Properties/SourcePowerCorrection_Property.md)  
Applies correction values after completing a source power cal acquisition sweep. Optionally do reference receiver cal. |  [SOURce:POWer:CORRection:COLLect:SAVE](GP-IB_Command_Finder/SourceCorrection.md#save) |  [ApplyPowerCorrectionValuesEx](COM_Reference/Methods/ApplyPowerCorrectionValuesEx_Method.md)  
Returns the currently-selected power sensor channel (A or B) for use at a specific frequency. |  None |  [PowerAcquisitionDevice](COM_Reference/Properties/PowerAcquisitionDevice_Property.md)  
Set power level |  [SOURce:POWer:CORRection:LEV](GP-IB_Command_Finder/SourceCorrection.md#level) |  [SetCalInfoEx Method](COM_Reference/Methods/SetCalInfoEx_Method.md)  
Set power offset |  [SOURce:POWer:CORRection:OFFSet](GP-IB_Command_Finder/SourceCorrection.md#offset) |  [SourcePowerCalPowerOffset](COM_Reference/Properties/SourcePowerCalPowerOffset_Property.md)  
Set settling tolerance |  [SOURce:POWer:CORRection:COLLect:AVERage:NTOLerance](GP-IB_Command_Finder/SourceCorrection.md#averTol) |  [ReadingsTolerance](COM_Reference/Properties/ReadingsTolerance_Property.md)  
Set max readings for settling |  [SOURce:POWer:CORRection:COLLect:AVERerage:COUNt](GP-IB_Command_Finder/SourceCorrection.md#average) |  [ReadingsPerPoint](COM_Reference/Properties/ReadingsPerPoint_Property.md)  
Set accuracy tolerance |  [SOURce:POWer:CORRection:COLLect:ITERation:NTOLerance](GP-IB_Command_Finder/SourceCorrection.md#iterTol) |  [IterationsTolerance](COM_Reference/Properties/IterationsTolerance_Property.md)  
Set max readings for accuracy |  [SOURce:POWer:CORRection:COLLect:ITERation:COUNt](GP-IB_Command_Finder/SourceCorrection.md#IterCount) |  [MaximumIterationsPerPoint](COM_Reference/Properties/MaximumIterationsPerPoint_Property.md)  
Turn ON|OFF display of readings |  [SOURce:POWer:CORRection:COLLect:DISPlay](GP-IB_Command_Finder/SourceCorrection.md#display) |  [AcquirePowerReadingsEx](COM_Reference/Methods/AcquirePowerReadingsEx_Method.md)  
Acquire receiver-only readings |  [SOURce:POWer:CORRection:COLLect:ACQuire:REC](GP-IB_Command_Finder/SourceCorrection.md#aquire) |  [AcquirePowerReadingsEx](COM_Reference/Methods/AcquirePowerReadingsEx_Method.md)  
Initiates a source power cal acquisition. |  [SOURce:POWer:CORRection:COLLect:ACQuire](GP-IB_Command_Finder/SourceCorrection.md#aquire) |  [AcquirePowerReadingsEx](COM_Reference/Methods/AcquirePowerReadingsEx_Method.md)  
Aborts a source power cal acquisition sweep that is currently in progress. |  [SOURce:POWer:CORRection:COLLect:ABORt](GP-IB_Command_Finder/SourceCorrection.md#abort) |  [AbortPowerAcquisition](COM_Reference/Methods/AbortPowerAcquisition_Method.md)  
Launches the Power Meter Settings dialog on the PNA. |  None |  [LaunchPowerMeterSettingsDialog](COM_Reference/Methods/LaunchPowerMeterSettingsDialog_Method.md)  
Frequency checking (ON|OFF) |  [SOURce:POWer:CORRection:COLLect:FCHeck](GP-IB_Command_Finder/SourceCorrection.md#fcheck) |  [UsePowerSensorFrequencyLimits](COM_Reference/Properties/UsePowerSensorFrequencyLimits_Property.md)  
Check test port power |  None |  [CheckPower](COM_Reference/Methods/CheckPower_Method.md)  
Calibrate the source at multiple power levels. |  None |  None  
Specifies if the source power cal in the calset linked to a measurement cal should be enabled or disabled with that cal |  None |  [PreferSourcePowerCalFromCalset](COM_Reference/Properties/PreferSourcePowerCalFromCalset_Property.md)  
Enable/disable use of error messages during a source calibration if calibration fails to achieve desired power level at the power sensor |  [SOURce:POWer:CORRection:COLLect:WARN](GP-IB_Command_Finder/SourceCorrection.md#SOURce:POWer:CORRection:COLLect:WARN) |  None  
  
Power Meter/Sensor settings [See commands to configure a Power Meter as
Receiver (PMAR)](XTraceChanTopic.htm#PMAR) [See commands to configure multiple
power sensors for guided Power Cal](CalTopic.htm#MultiplePsensors)  
---  
Specifies the type of power sensor to be used |  [SYSTem:COMMunicate:PSENsor](GP-IB_Command_Finder/SystCommunicate.md#PSensorType) |  [Path](COM_Reference/Properties/Path_Property.md)  
Specifies the location of the power sensor to be used. |  [SYSTem:COMMunicate:PSENsor](GP-IB_Command_Finder/SystCommunicate.md#PSensorType) |  [Locator](COM_Reference/Properties/Locator_Property.md)  
Returns the ID string of connected USB power meters / sensors. |  [SYSTem:COMMunicate:USB:PMETer:CATalog?](GP-IB_Command_Finder/SystCommunicate.md#USBList) |  [USBPowerMeterCatalog](COM_Reference/Properties/USBPowerMeterCatalog_Property.md)  
Pwr meter Max Readings for settling |  [SOURce:POWer:CORRection:COLLect:AVERerage:COUNt](GP-IB_Command_Finder/SourceCorrection.md#average) |  [ReadingsPerPoint](COM_Reference/Properties/ReadingsPerPoint_Property.md)  
Pwr meter settling tolerance |  [SOURce:POWer:CORRection:COLLect:AVERage:NTOLerance](GP-IB_Command_Finder/SourceCorrection.md#averTol) |  [ReadingsTolerance](COM_Reference/Properties/ReadingsTolerance_Property.md)  
Minimum Frequency |  [SOURce:POWer:CORRection:COLLect:<>SENsor](GP-IB_Command_Finder/SourceCorrection.md#frange) |  [MinimumFrequency](COM_Reference/Properties/MinimumFrequency_sourceCal_Property.md)  
Maximum Frequency |  [SOURce:POWer:CORRection:COLLect:<>SENsor](GP-IB_Command_Finder/SourceCorrection.md#frange) |  [MaximiumFrequency](COM_Reference/Properties/MaximiumFrequency_sourceCal_Property.md)  
Power meter channel |  None |  [PowerMeterChannel](COM_Reference/Properties/PowerMeterChannel_Property.md)  
Set sensor cal factor |  [SOURce:POWer:CORRection:COLLect:<>SENsor:RCFactor](GP-IB_Command_Finder/SourceCorrection.md#Rfactor) |  [ReferenceCalFactor](COM_Reference/Properties/ReferenceCalFactor_Property.md)  
Set table type |  [SOURce:POWer:CORRection:COLLect:TABLe <>SENsor](GP-IB_Command_Finder/SourceCorrection.md#tselect) |  None  
Read/Write cal data |  [SOURce:POWer:CORRection:DATA](GP-IB_Command_Finder/SourceCorrection.md#corrdata) |  [See Data](DataTopic.md)  
Use Loss table? |  [SOURce:POWer:CORRection:COLLect:TABLe:LOSS](GP-IB_Command_Finder/SourceCorrection.md#tloss) |  [UsePowerLossSegments](COM_Reference/Properties/UsePowerLossSegments_Property.md)  
Cal Factor Table |  [SOURce:POWer:CORRection:COLLect:TABLe:SELect](GP-IB_Command_Finder/SourceCorrection.md#tselect) |  [CalFactorSegments Collection](COM_Reference/Objects/CalFactorSegments_Collection.md)  
Read number of segments in table |  [SOURce:POWer:CORRection:COLLect:TABLe:POINts?](GP-IB_Command_Finder/SourceCorrection.md#points) |  [Count](COM_Reference/Properties/Count_Property.md)  
Segment number |  None |  [SegmentNumber](COM_Reference/Properties/Segment_Number_Property.md)  
Add segment |  None |  [Add](COM_Reference/Methods/Add_PowerSensorCalFactorSegment_Method.md)  
Cal factor of the segment |  [SOURce:POWer:CORRection:COLLect:TABLe:DATA](GP-IB_Command_Finder/SourceCorrection.md#tdata) |  [CalFactor](COM_Reference/Properties/CalFactor_Property.md)  
Frequency of the segment |  [SOURce:POWer:CORRection:COLLect:TABLe:FREQuency](GP-IB_Command_Finder/SourceCorrection.md#RWfreq) |  [Frequency](COM_Reference/Properties/Frequency_Property.md)  
Power Loss Table |  [SOURce:POWer:CORRection:COLLect:TABLe:SELect](GP-IB_Command_Finder/SourceCorrection.md#tselect) |  [PowerLossSegments Collection](COM_Reference/Objects/PowerLossSegments_Collection.md)  
Read number of segments in table |  [SOURce:POWer:CORRection:COLLect:TABLe:POINts?](GP-IB_Command_Finder/SourceCorrection.md#points) |  [Count](COM_Reference/Properties/Count_Property.md)  
Segment number |  None |  [SegmentNumber](COM_Reference/Properties/Segment_Number_Property.md)  
Add segment |  None |  [Add](COM_Reference/Methods/Add_PowerLossSegment_Method.md)  
Frequency |  [SOURce:POWer:CORRection:COLLect:TABLe:FREQuency](GP-IB_Command_Finder/SourceCorrection.md#RWfreq) |  [Frequency](COM_Reference/Properties/Frequency_Property.md)  
Loss value |  [SOURce:POWer:CORRection:COLLect:TABLe:DATA](GP-IB_Command_Finder/SourceCorrection.md#tdata) |  [Loss](COM_Reference/Properties/Loss_sourceCal_Property.md)  
Receiver Cal  
Set offset from test port power |  [SENSe:CORRection:RPOWer:OFFSet[:AMPLitude]](GP-IB_Command_Finder/Sense/Sense_Correction.md#RecPowerOffset) |  [DoReceiverPowerCal](COM_Reference/Methods/DoReceiverPowerCal_Method.md)  
Set cal method to receiver cal |  [SENSe:CORRection:COLLect:METHod RPOWer](GP-IB_Command_Finder/Sense/Sense_Correction.md#sccm) |  [DoReceiverPowerCal](COM_Reference/Methods/DoReceiverPowerCal_Method.md)  
Take measurement |  [SENSe:CORRection:COLLect[:ACQuire] POWer](GP-IB_Command_Finder/Sense/Sense_Correction.md#scca) |  None  
Turn receiver cal ON | OFF |  [SENSe:CORRection[:STATe] ON|OFF](GP-IB_Command_Finder/Sense/Sense_Correction.md#scs) |  [Error Correction](COM_Reference/Properties/Error_Correction_Property.md)  
Do interpolation |  [SENSe:CORRection:INTerpolate[:STATe] ON|OFF](GP-IB_Command_Finder/Sense/Sense_Correction.md#scis) |  [InterpolateCorrection](COM_Reference/Properties/Interpolate_Correction_Property.md)  
  
CalPod  
---  
Command used to send other commands as arguments |  [CONTrol:CALPod:COMMand](GP-IB_Command_Finder/Control.md#Calpod) |  None  
Start the CalPod software |  [Calpod:LAUNch](GP-IB_Command_Finder/Calpod.md#launch) |  None  
Assign Calpod serial number to a port. |  [Calpod:ENABle](GP-IB_Command_Finder/Calpod.md#enable) |  None  
Unassign Calpod serial number from a port. |  [Calpod:Disable](GP-IB_Command_Finder/Calpod.md#disable) |  None  
Initialize the selected channel |  [Calpod:INITialize:ACTive](GP-IB_Command_Finder/Calpod.md#InitActive) |  None  
Initialize ALL channels |  [Calpod:INITialize:ALL](GP-IB_Command_Finder/Calpod.md#InitAll) |  None  
Recorrect the selected channel |  [Calpod:Recorrect:ACTive](GP-IB_Command_Finder/Calpod.md#RecorrectActive) |  None  
Recorrect ALL channels |  [Calpod:Recorrect:ALL](GP-IB_Command_Finder/Calpod.md#recorrectAll) |  None  
Show refresh dialog |  [Calpod:SHOW](GP-IB_Command_Finder/Calpod.md#show) |  None  
Hide refresh dialog |  [Calpod:HIDE](GP-IB_Command_Finder/Calpod.md#hide) |  None  
Sets impedance state |  [Calpod:STATe](GP-IB_Command_Finder/Calpod.md#State) |  None  
Read Calpod temperature |  [Calpod:TEMP?](GP-IB_Command_Finder/Calpod.md#Temp) |  None  
  
Custom Cal Window  
---  
Turn ON | OFF Custom Cal window. |  [SENSe:CORRection:COLLect:DISPlay:WINDow](GP-IB_Command_Finder/Sense/Sense_Correction.md#CalWindowState) |  [DisplayNAWindowDuringCalAcquisition](COM_Reference/Methods/DisplayNAWindowDuringCalAcquisition_Method.md)  
Show NO Custom Cal windows. |  [SENSe:CORRection:COLLect:DISPlay:WINDow:AOFF](GP-IB_Command_Finder/Sense/Sense_Correction.md#CalWindowAoff) |  [DisplayOnlyCalWindowDuringCalAcquisition](COM_Reference/Methods/DisplayOnlyCalWindowDuringCalAcquisition_Method.md)  
Specify channel to sweep before Cal acquisition. |  [SENSe:CORRection:COLLect:SWEep:CHANnel](GP-IB_Command_Finder/Sense/Sense_Correction.md#CalWinSweepChan) |  [AllowChannelToSweepDuringCalAcquisition](COM_Reference/Methods/AllowChannelToSweepDuringCalAcquisition_Method.md)  
Sweep NO channel before Cal acquisition. |  [SENSe:CORRection:COLLect:SWEep:CHANnel:AOFF](GP-IB_Command_Finder/Sense/Sense_Correction.md#CalWindowSweepAoff) |  [SweepOnlyCalChannelDuringCalAcquisition](COM_Reference/Methods/SweepOnlyCalChannelDuringCalAcquisition_Method.md)  
Preview sweep before remote Cal acquisition. |  [SENSe:CORRection:COLLect:GUIDed:PACQuire](GP-IB_Command_Finder/Sense/CorrGuided.md#previewAcquire) |  [SetupMeasurementsForStep](COM_Reference/Methods/SetupMeasurementsForStep_Method.md)  
  
Retrieve and Put Calibration Data  
---  
Retrieve Cal Data from the PNA |  [SENSe:CORRection:CSET:DATA](GP-IB_Command_Finder/Sense/CorrCset.md#data) |  [see Data Topic](DataTopic.md)  
Put Cal Data in the PNA |  [SENSe:CORRection:CSET:DATA](GP-IB_Command_Finder/Sense/CorrCset.md#data) |  [see Data Topic](DataTopic.md)  
  
Automatic Fixture Removal (AFR)  
---  
Turns on or off the option "Automatically iterate when Impedance Method Auto is checked." | [AFR:ADVanced:AUTO:ITERate:METHod:CHECk[:STATe]](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AdvAutoIterMethChecStat) | None  
Turns on or off the option "Automatically iterate when Calibration Reference Z0 is set to System Z0 or custom value. | [AFR:ADVanced:AUTO:ITERate:REFZ:SET[:STATe]](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AdvAutoIterRefzSetStat) | None  
Gets or sets the DUT gate coefficient. | [AFR:ADVanced:DUTGate:COEFficient](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AdvDutgCoef) | None  
Sets or gets the description of the AFR DUT Gate Domain (single-ended or differential). | [AFR:ADVanced:DUTGate:DOMain](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AFRAdvDutgDom) | None  
Turns ON or OFF the Fitting Thru after AFR DUT Gate. | [AFR:ADVanced:DUTGate:ILFitting:MANual[:STATe]](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AdvDutgIlfManStat) | None  
Turns ON or OFF AFR DUTGate | [AFR:ADVanced:DUTGate:MANual[:STATe]](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AdvDutgManStat) | None  
Turns ON or OFF AFR DUTGate Only Reflection Option | [AFR:ADVanced:DUTGate:REFLection:MANual[:STATe]](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AdvDutgReflManStat) | None  
Applies advanced algorithm to fixture impedance mismatching cases for better results. | [AFR:ADVanced:FIXTure:IMPedance:FTUNe[:STATe]](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AdvFixtImpFtunStat) | None  
Turns ON of OFF AFR mode conversion. |  [AFR:ADVanced:MCONversion[:STATe]](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AFR:ADVanced:MCONversion:STATe) |  None  
Sets or reads the gating mode in 1-port characterization. | [AFR:ADVanced:REFLection:GATing:MODE](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AdvReflGatMode) | None  
Gets or sets the position parameter in 1-port characterization. | [AFR:ADVanced:REFLection:GATing:MODE::CUSTom:POSition](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AdvReflGatModeCustPos) | None  
Gets or sets the N parameter in 1-port characterization. | [AFR:ADVanced:REFLection:GATing:MODE:MINimum:NVALue](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AdvReflGatModeMinNval) | None  
Gets or sets the spike tolerance parameter in 1-port characterization. | [AFR:ADVanced:REFLection:GATing:SPIKe:TOLerance](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AdvReflGatSpikTol) | None  
Gets or sets the ratio of the merge center for IL fitting at high frequency range 1-port characterization. | [AFR:ADVanced:REFLection:ILFitting:HIGH:MCENter](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AdvReflIlfHighMcen) | None  
Gets or sets the ratio of the merge span for IL fitting at high frequency range 1-port characterization. | [AFR:ADVanced:REFLection:ILFitting:HIGH:MSPan](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AdvReflIlfHighMsp) | None  
Gets or sets the start ratio for IL fitting at high frequency range 1-port characterization. | [AFR:ADVanced:REFLection:ILFitting:HIGH:STARt](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AdvReflIlfHighStar) | None  
Gets or sets the stop ratio for IL fitting at high frequency range 1-port characterization. | [AFR:ADVanced:REFLection:ILFitting:HIGH:STOP](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AdvReflIlfHighStop) | None  
Gets or sets the ratio of the merge center for IL fitting at low frequency range 1-port characterization. | [AFR:ADVanced:REFLection:ILFitting:LOW:MCENter](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AdvReflIlfLowMcen) | None  
Gets or sets the ratio of the merge span for IL fitting at low frequency range 1-port characterization. | [AFR:ADVanced:REFLection:ILFitting:LOW:MSPan](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AdvReflIlfLowMsp) | None  
Gets or sets the start ratio for IL fitting at low frequency range 1-port characterization. | [AFR:ADVanced:REFLection:ILFitting:LOW:STARt](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AdvReflIlfLowStar) | None  
Gets or sets the stop ratio for IL fitting at low frequency range 1-port characterization. | [AFR:ADVanced:REFLection:ILFitting:LOW:STOP](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AdvReflIlfLowStop) | None  
Resets the AFR configuration. |  [AFR:ADVanced:RESet](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AFR:ADVanced:RESet) |  None  
Gets or sets the manual start time in AFR configuration. |  [AFR:ADVanced:TIME:STARt](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AFR:ADVanced:TIME:STARt) |  None  
Gets or sets the manual stop time in AFR configuration. |  [AFR:ADVanced:TIME:STOP](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AFR:ADVanced:TIME:STOP) |  None  
Gets the AFR Version. | [AFR:ADVanced:VERSion?](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AdvVers) | None  
Gets or sets the manual window type in AFR configuration. |  [AFR:ADVanced:WINDow:COEFficient](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AFR:ADVanced:WINDow:COEFficient) |  None  
Turns ON of OFF the manual window coefficient of the AFR. |  [AFR:ADVanced:WINDow:MANual[:STATe]](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AFR:ADVanced:WINDow:MANual:STATe) |  None  
Selects whether the fixture is band limited or not. |  [AFR:FIXTure:BLIMited[:STATe]](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AFR:FIXTure:BLIMited_:STATe) |  None  
Selects whether to use DUT correction or not when the characterization fixture is not equal to the DUT measurement fixture. |  [AFR:FIXTure:CDUT[:STATe]](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AFR:FIXTure:CDUT_:STATe) |  None  
Selects Fixture Length A not equal to B correction. |  [AFR:FIXTure:CLENgth[:STATe]](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AFR:FIXTure:CLENgth_:STATe) |  None  
Selects Fixture Match A not equal to B correction. |  [AFR:FIXTure:CMATch[:STATe]](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AFR:FIXTure:CMATch_:STATe) |  None  
Describes the fixture inputs (single ended or differential). |  [AFR:FIXTure:INPuts](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AFR:FIXTure:INPuts) |  None  
Selects the number of fixtures to be characterized. |  [AFR:FIXTure:MEASurement](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AFR:FIXTure:MEASurement) |  None  
Refreshes preview data. |  [AFR:FIXTure:PREView](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AFR:FIXTure:PREView) |  None  
Reads the impedance profile of the calculated fixture model. |  [AFR:FIXTure:PREView:DATA[:IMPedance]?](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AFR:FIXTure:PREView:DATA:IMPedance) |  None  
Reads the impedance profile of the calculated fixture model at a specified position. |  [AFR:FIXTure:PREView:DATA[:IMPedance]:MARKer:Y?](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AFR:FIXTure:PREView:DATA:IMPedance:MARKer:Y) |  None  
Chooses the calibration reference Z0 after fixture removal. |  [AFR:FIXTure:REFZ](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AFR:FIXTure:REFZ) |  None  
Sets "System Z0" to Calibration Reference Z0. |  [AFR:FIXTure:SET:SYSZ[:STATe]](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AFR:FIXTure:SET:SYSZ) |  None  
Specifies whether thrus are used in case of multi-port fixtures. |  [AFR:FIXTure:USE:THRUs[:STATe]](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AFR:FIXTure:USE:THRUs) |  None  
Restores the default AFR settings. |  [AFR:INITialize](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AFR:INITialize) |  None  
Specifies the file paths of saved fixture data. |  [AFR:SAVE:FILename](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AFR:SAVE:FILename) |  None  
Specifies whether the port impedances are normalized in saving the AFR fixture files. |  [AFR:SAVE:IMPedance:NORMalize[:STATe]](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AFR:SAVE:IMPedance:NORMalize) |  None  
Assigns the ports for saved fixture data in several formats. |  [AFR:SAVE:PORTs](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AFR:SAVE:PORTs) |  None  
Sets the file type to save fixture data. |  [AFR:SAVE:TYPE](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AFR:SAVE:TYPE) |  None  
Selects all OPEN standards. |  [AFR:STANdard:ALLOpen[:STATe]](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AFR:STANdard:ALLOpen:STATe) |  None  
Selects all SHORT standards. |  [AFR:STANdard:ALLShort[:STATe]](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AFR:STANdard:ALLShort:STATe) |  None  
Reads the impedance profile of the measured standard. |  [AFR:STANdard:DATA[:IMPedance]?](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AFR:STANdard:DATA:IMPedance) |  None  
Reads the impedance of the measured standard at a specified position. |  [AFR:STANdard:DATA[:IMPedance]:MARKer:Y?](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AFR:STANdard:DATA:IMPedance:MARKer:Y) |  None  
Sets the fixture length for the selected fixture (for 1X AFR only). |  [AFR:STANdard:EDIT:FLENgth](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AFR:STANdard:EDIT:FLENgth) |  None  
Sets the gate position for the selected fixture. |  [AFR:STANdard:EDIT:GATE](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AFR:STANdard:EDIT:GATE) |  None  
Sets the impedance for the selected term. |  [AFR:STANdard:EDIT:IMPedance](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AFR:STANdard:EDIT:IMPedance) |  None  
Sets the impedance method. |  [AFR:STANdard:EDIT:IMPedance:METHod](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AFR:STANdard:EDIT:IMPedance:METHod) |  None  
Loads the calibration standards data from a file. |  [AFR:STANdard:LOAD](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AFR:STANdard:LOAD) |  None  
Measures calibration standard. |  [AFR:STANdard:MEASure](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AFR:STANdard:MEASure) |  None  
Specifies fixture thru settings. |  [AFR:STANdard:THRU](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AFR:STANdard:THRU) |  None  
Chooses the calibration standards. |  [AFR:STANdard:USE](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AFR:STANdard:USE) |  None  
  
Cal Update  
---  
Sets and returns the averaging used to improve noise errors. |  [SYSTem:CALibrate:CALupdate:AVERage:COUNt](GP-IB_Command_Finder/SystCalDrift.md#SYSTem:CALibrate:DRIFt:AVERage:COUNt) |  None  
Sets and returns the IF bandwidth used by the measurement channel. |  [SYSTem:CALibrate:CALupdate:BWIDth[:RESolution]](GP-IB_Command_Finder/SystCalDrift.md#SYSTem:CALibrate:DRIFt:BWIDth:RESolution) |  None  
Selects the channel(s) to calibrate. |  [SYSTem:CALibrate:CALupdate:CHANnel[:SELect]](GP-IB_Command_Finder/SystCalDrift.md#SYSTem:CALibrate:DRIFt:CHANnel:ALL:STATe) |  None  
Sets and returns the gate start value for time domain gating. |  [SYSTem:CALibrate:CALupdate:GATE:STARt](GP-IB_Command_Finder/SystCalDrift.md#SYSTem:CALibrate:DRIFt:GATE:STARt) |  None  
Sets and returns the state of gate coupling for gate start value. |  [SYSTem:CALibrate:CALupdate:GATE:STARt:COUPle[:STATe]](GP-IB_Command_Finder/SystCalDrift.md#SYSTem:CALibrate:DRIFt:GATE:STARt:COUPle:STATe) |  None  
Sets and returns the gate stop value for time domain gating. |  [SYSTem:CALibrate:CALupdate:GATE:STOP](GP-IB_Command_Finder/SystCalDrift.md#SYSTem:CALibrate:DRIFt:GATE:STOP) |  None  
Sets and returns the state of gate coupling for gate stop value. |  [SYSTem:CALibrate:CALupdate:GATE:STOP:COUPle[:STATe]](GP-IB_Command_Finder/SystCalDrift.md#SYSTem:CALibrate:DRIFt:GATE:STOP:COUPle:STATe) |  None  
Initializes the selected ports. |  [SYSTem:CALibrate:CALupdate:INITialize](GP-IB_Command_Finder/SystCalDrift.md#SYSTem:CALibrate:DRIFt:INITialize) |  None  
Recorrects the list of previously initialized ports. |  [SYSTem:CALibrate:CALupdate:RECorrect](GP-IB_Command_Finder/SystCalDrift.md#SYSTem:CALibrate:DRIFt:RECorrect) |  None  
Sets and returns the reference cal set name. |  [SYSTem:CALibrate:CALupdate:REFerence](GP-IB_Command_Finder/SystCalDrift.md#SYSTem:CALibrate:DRIFt:REFerence) |  None  
Selects the port numbers to initialize. |  [SYSTem:CALibrate:CALupdate:PORTs[:SELect]](GP-IB_Command_Finder/SystCalDrift.md#SYSTem:CALibrate:DRIFt:PORTs:SELect) |  None  
Use a channel's existing IF BW, Averaging, and Power value settings or enter the values manually. |  [SYSTem:CALibrate:CALupdate:SETTings:AUTO](GP-IB_Command_Finder/SystCalDrift.md#SYSTem:CALibrate:DRIFt:SETTings:AUTO) |  None  
Manually sets and returns the source power for the active measurement channel. |  [SYSTem:CALibrate:CALupdate:SOURce:POWer](GP-IB_Command_Finder/SystCalDrift.md#SYSTem:CALibrate:DRIFt:SOURce:POWer) |  None  
  
* * *

