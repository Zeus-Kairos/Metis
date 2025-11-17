# Cal Commands - Standard Measurement Class

Click [here](CF_Cal_Commands.md) to view links to Cal commands for all
Measurement Classes.

Main | Port  
Extension | Cal Sets  
& Cal Kits | Fixtures  
---|---|---|---  
Main Tab Commands  
---  
Softkey | Sub-item | SCPI | COM  
Basic Cal... | Connector | [SENSe:CORRection:COLLect:CKIT:CONNector:ADD](GP-IB_Command_Finder/Sense/CorrGuided.md#gConSelect) | None  
Cal Kit | [SENSe:CORRection:COLLect:CKIT[:SELect]](GP-IB_Command_Finder/Sense/CorrCollCKIT.md#scccs) | [CalKitType](COM_Reference/Properties/CalKitTypeCalibrator_Property.md)  
Show all cal kits | [SENSe:CORRection:COLLect:CKIT:CATalog?](GP-IB_Command_Finder/Sense/CorrCollCKIT.md#cat) | [GetCompatibleCalKits](COM_Reference/Methods/GetCompatibleCalKits_Method.md)  
Cal Type | [SENSe:CORRection:COLLect:METHod](GP-IB_Command_Finder/Sense/Sense_Correction.md#sccm) | [SetCalInfo](COM_Reference/Methods/SetCalInfo_Method.md)  
Other Cals | Cal All...  
Select the channels to be calibrated | [SYSTem:CALibrate:ALL:SELect](GP-IB_Command_Finder/SystCalAll.md#ChanSelect) | [Channels](COM_Reference/Properties/Channels_Property.md)  
Use Smart Cal Order | [SYSTem:CALibrate:ALL:MCLass:PROPerty:VALue[:STATe]](GP-IB_Command_Finder/SystCalAll.md#PropValueSelect) | [PropertyValue](COM_Reference/Properties/PropertyValue_Property.md)  
Enable Extra Power Cals | [SYSTem:CALibrate:ALL:MCLass:PROPerty:VALue[:STATe]](GP-IB_Command_Finder/SystCalAll.md#PropValueSelect) | [PropertyValue](COM_Reference/Properties/PropertyValue_Property.md)  
Independent Calibration Channels | [SYSTem:CALibrate:ALL:MCLass:PROPerty:VALue[:STATe]](GP-IB_Command_Finder/SystCalAll.md#PropValueSelect) | [PropertyValue](COM_Reference/Properties/PropertyValue_Property.md)  
Include Power Calibration | [SYSTem:CALibrate:ALL:MCLass:PROPerty:VALue[:STATe]](GP-IB_Command_Finder/SystCalAll.md#PropValueSelect) | [PropertyValue](COM_Reference/Properties/PropertyValue_Property.md)  
Set the IFBW | [SYSTem:CALibrate:ALL:IFBW](GP-IB_Command_Finder/SystCalAll.md#ifbw) | [IFBW](COM_Reference/Properties/IFBW_Property.md)  
Set the power level | [SYSTem:CALibrate:ALL:PORT:SOURce:POWer](GP-IB_Command_Finder/SystCalAll.md#SourcePower) | [PowerLevel](COM_Reference/Properties/PowerLevel-\(CalAll\)_Property.md)  
Set the power offset | [SYSTem:CALibrate:ALL:PORT:SOURce:POWer:OFFSet](GP-IB_Command_Finder/SystCalAll.md#SourceOffset) | [PowerOffset](COM_Reference/Properties/PowerOffset_\(CalAll\)_Property.md)  
Set the receiver atten | [SYSTem:CALibrate:ALL:PORT:SOURce:POWer:ATTen](GP-IB_Command_Finder/SystCalAll.md#SourceAtten) | [SourceAttenuator](COM_Reference/Properties/SourceAttenuator_Property.md)  
Set the User Calset Prefix | [SYSTem:CALibrate:ALL:CSET:PREFix](GP-IB_Command_Finder/SystCalAll.md#csetPrefix) | [UserCalsetPrefix](COM_Reference/Properties/UserCalsetPrefix_Property.md)  
Set Path Configuration | [SYSTem:CALibrate:ALL:PATH:CONFigure:ELEMent](GP-IB_Command_Finder/SystCalAll.md#ConfigElement) | [PathConfigurationElement](COM_Reference/Properties/PathConfigurationElement_Property.md)  
Read unique Cal properties | [SYSTem:CALibrate:ALL:MCLass:PROPerty:NAME:CATalog?](GP-IB_Command_Finder/SystCalAll.md#PropNameCat) | [PropertyNames](COM_Reference/Properties/PropertyNames_Property.md)  
Read unique property values | [SYSTem:CALibrate:ALL:MCLass:PROPerty:VALue:CATalog?](GP-IB_Command_Finder/SystCalAll.md#PropValueCat) | [PropertyValues](COM_Reference/Properties/PropertyValues_Property.md)  
Set property name/value | [SYSTem:CALibrate:ALL:MCLass:PROPerty:VALue](GP-IB_Command_Finder/SystCalAll.md#PropValueSelect) | [PropertyValue](COM_Reference/Properties/PropertyValue_Property.md)  
Read primary Cal channel | [SYSTem:CALibrate:ALL:GUIDed:CHANnel[:VALue]?](GP-IB_Command_Finder/SystCalAll.md#GuideChan) | None  
Returns all cal all guided calibration channels | [SYSTem:CALibrate:ALL:GUIDed:CHANnel:LIST?](GP-IB_Command_Finder/SystCalAll.md#SYSTem:CALibrate:ALL:GUIDed:CHANnel:CATalog) | None  
Get Guided Cal handle | None | [GuidedCalibration](COM_Reference/Objects/GuidedCalibration_Object.md)  
For each channel, sets the ports to be calibrated | [SYSTem:CALibrate:ALL:CHANnel:PORTs](GP-IB_Command_Finder/SystCalAll.md#PortsSelect) | [CalibrationPorts](COM_Reference/Properties/CalibrationPorts_Property.md)  
Returns a final list of ports to be calibrated | [SYSTem:CALibrate:ALL:GUIDed:PORTs?](GP-IB_Command_Finder/SystCalAll.md#GuidedPorts) | [SParameterCalPorts](COM_Reference/Properties/SParameterCalPorts_Property.md)  
Read generated Cal Sets | [SYSTem:CALibrate:ALL:CSET:CATalog?](GP-IB_Command_Finder/SystCalAll.md#csetCat) | [GeneratedCalsets](COM_Reference/Properties/GeneratedCalsets_Property.md)  
[Independent Power Calibration](../S3_Cals/Calibrate_All_Channels.md#Setting_Up_an_Independent_Power_Calibration) |  |   
Return available ports | [SYSTem:CALibrate:ALL:INDependent:SOURce:CALibrate:CATalog?](GP-IB_Command_Finder/SystCalAll.md#SYSTem:CALibrate:ALL:INDependent:SOURce:CALibrate:CATalog) | [ValidPorts](COM_Reference/Properties/ValidPorts.md)  
Add a power cal range  | [SYSTem:CALibrate:ALL:INDependent:SOURce:CALibrate:RANGe:ADD](GP-IB_Command_Finder/SystCalAll.md#SYSTem:CALibrate:ALL:INDependent:SOURce:CALibrate:RANGe:ADD) | [AddPowerCalRange](COM_Reference/Methods/AddPowerCalRange_Method.md)  
Reset all ranges | [SYSTem:CALibrate:ALL:INDependent:SOURce:CALibrate:RANGe:CLEar](GP-IB_Command_Finder/SystCalAll.md#SYSTem:CALibrate:ALL:INDependent:SOURce:CALibrate:RANGe:CLEar) | [Reset](COM_Reference/Methods/Reset_\(Independent_CalAll\)_Method.md)  
Query how many ranges are included  | [SYSTem:CALibrate:ALL:INDependent:SOURce:CALibrate:RANGe:COUNt?](GP-IB_Command_Finder/SystCalAll.md#SYSTem:CALibrate:ALL:INDependent:SOURce:CALibrate:RANGe:COUNt) | [RangeCount](COM_Reference/Properties/RangeCount_\(Independent_Power_Cal\)_Property.md)  
Set number of points | [SYSTem:CALibrate:ALL:INDependent:SOURce:CALibrate:RANGe:POINts](GP-IB_Command_Finder/SystCalAll.md#SYSTem:CALibrate:ALL:INDependent:SOURce:CALibrate:RANGe:POINts) | [NumberOfPoints](COM_Reference/Properties/NumberOfPoints_\(PowerCalRange\)_Property.md)  
Set start frequency  | [SYSTem:CALibrate:ALL:INDependent:SOURce:CALibrate:RANGe:STARt](GP-IB_Command_Finder/SystCalAll.md#SYSTem:CALibrate:ALL:INDependent:SOURce:CALibrate:RANGe:STARt) | [StartFrequency](COM_Reference/Properties/StartFrequency_\(PowerCalRange\)_Property.md)  
Set stop frequency | [SYSTem:CALibrate:ALL:INDependent:SOURce:CALibrate:RANGe:STOP](GP-IB_Command_Finder/SystCalAll.md#SYSTem:CALibrate:ALL:INDependent:SOURce:CALibrate:RANGe:STOP) | [StopFrequency](COM_Reference/Properties/StopFrequency_\(PowerCalRange\)_Property.md)  
Smart Cal...  
Initiate a Guided Cal | [SENSe:CORRection:COLLect:GUIDed:INITiate](GP-IB_Command_Finder/Sense/CorrGuided.md#gInit) | [Initialize](COM_Reference/Methods/Initialize_Method.md)  
Returns a text description (string) of the current calibration settings. | [SENSe<ch>:CORRection:COLLect:GUIDed:CONFig:DESCription?](GP-IB_Command_Finder/Sense/CorrGuided.md#CONFig_DESC) | None  
Loads the calibration configurations from file and commits all settings. | [SENSe<ch>:CORRection:COLLect:GUIDed:CONFig:LOAD[:IMMediate] <string>](GP-IB_Command_Finder/Sense/CorrGuided.md#CONFig_LOAD) | None  
Returns a text description (string) of the calibration settings contained in the specified filename. | [SENSe<ch>:CORRection:COLLect:GUIDed:CONFig:LOAD:DESCription? <string>](GP-IB_Command_Finder/Sense/CorrGuided.md#CONFig_LOAD_DESC) | None  
Save the current guided calibration settings to file. | [SENSe<ch>:CORRection:COLLect:GUIDed:CONFig:SAVE <string>](GP-IB_Command_Finder/Sense/CorrGuided.md#CONFig_SAVE) | None  
List valid Connector Types for a Port | [SENSe:CORRection:COLLect:GUIDed:CONNector:CATalog?](GP-IB_Command_Finder/Sense/CorrGuided.md#gConnCat) | [ValidConnectorTypes](COM_Reference/Properties/ValidConnectorType_Property.md)  
List valid Cal Kits for a Connector type | [SENSe:CORRection:COLLect:GUIDed:CKIT:CATalog?](GP-IB_Command_Finder/Sense/CorrGuided.md#ckitCatConn) | [GetCompatibleCalKits](COM_Reference/Methods/GetCompatibleCalKits_Method.md)  
Select a Connector Type | [SENSe:CORRection:COLLect:GUIDed:CONNector:PORT](GP-IB_Command_Finder/Sense/CorrGuided.md#gConSelect) | [ConnectorType](COM_Reference/Properties/ConnectorType_Property.md)  
Select a Cal Kit | [SENSe:CORRection:COLLect:GUIDed:CKIT:PORT](GP-IB_Command_Finder/Sense/CorrGuided.md#gKit) | [CalKitType](COM_Reference/Properties/CalKitType_Property.md)  
Set cal method for each port pair | [SENSe:CORRection:COLLect:GUIDed:PATH:CMEThod](GP-IB_Command_Finder/Sense/CorrGuided.md#PathCmethod) | [PathCalMethod](COM_Reference/Properties/PathCalMethod_Property.md)  
Set Thru Method for each port pair | [SENSe:CORRection:COLLect:GUIDed:PATH:TMEThod](GP-IB_Command_Finder/Sense/CorrGuided.md#PathTMethod) | [PathThruMethod](COM_Reference/Properties/PathThruMethod_Property.md)  
Set Thru Port Pairs | [SENSe:CORRection:COLLect:GUIDed:THRU:PORTs](GP-IB_Command_Finder/Sense/CorrGuided.md#pairs) | [ThruPortList](COM_Reference/Properties/ThruPortList_Property.md)  
Return Number of Steps in a Cal | [SENSe:CORRection:COLLect:GUIDed:STEPs?](GP-IB_Command_Finder/Sense/CorrGuided.md#gSteps) | [GenerateSteps](COM_Reference/Methods/GenerateSteps_Method.md)  
Return a Description of a Cal Step | [SENSe:CORRection:COLLect:GUIDed:DESCription?](GP-IB_Command_Finder/Sense/CorrGuided.md#gDesc) | [GetStepDescription](COM_Reference/Methods/Get_StepDescription_Method.md)  
Measure a Cal Standard in a Guided Cal | [SENSe:CORRection:COLLect:GUIDed:ACQuire](GP-IB_Command_Finder/Sense/CorrGuided.md#gAcquire) | [AcquireStep](COM_Reference/Methods/AcquireStep_Method.md)  
Save Cal | [SENSe:CORRection:COLLect:GUIDed:SAVE](GP-IB_Command_Finder/Sense/CorrGuided.md#gSave) | [GenerateErrorTerms](COM_Reference/Methods/GenerateErrorTerms_Method.md)  
E Cal...  
Specify Module and Characterization | [SENSe:CORRection:COLLect:ACQuire](GP-IB_Command_Finder/Sense/Sense_Correction.md#scca) | [cal.ECALCharacterizationEx](COM_Reference/Properties/ECALCharacterizationEx_Property.md)  
Do ECAL 1-Port | [SENSe:CORRection:COLLect:CKIT 99](GP-IB_Command_Finder/Sense/CorrCollCKIT.md#scccs) | [cal.DoECAL1PortEx](COM_Reference/Methods/DoECAL1PortEx_Method.md)  
Do ECAL 2-Port | [SENSe:CORRection:COLLect:CKIT 99](GP-IB_Command_Finder/Sense/CorrCollCKIT.md#scccs) | [cal.DoECAL2PortEx](COM_Reference/Methods/DoECAL2PortEx_Method.md)  
Get ECAL Module Info | [SENSe:CORRection:COLLect:CKIT:INFormation?](GP-IB_Command_Finder/Sense/CorrCollCKIT.md#Inf) [SENSe:CORRection:CKIT:ECAL:INFormation?](GP-IB_Command_Finder/Sense/CorrCKIT_SCPI.md#ECALInf) | [cal.GetCalKitTypeString](COM_Reference/Methods/GetCalKitTypeString_Method.md) [cal.GetECALModuleInfoEx](COM_Reference/Methods/Get_ECALModuleInfoEx_Method.md)  
Get list of ECal Modules attached to PNA | [SENSe:CORRection:CKIT:ECAL:LIST?](GP-IB_Command_Finder/Sense/CorrCKIT_SCPI.md#List) | [cal.ECALModuleNumberList](COM_Reference/Properties/ECALModuleNumberList_Property.md)  
Get list of characterizations in ECal module | [SENSe:CORRection:CKIT:ECAL:CLISt?](GP-IB_Command_Finder/Sense/CorrCKIT_SCPI.md#Clist) | [cal.ECALCharacterizationIndexList](COM_Reference/Properties/ECALCharacterizationIndexList_Property.md)  
Perform Module Orientation during calibration | [SENSe:CORRection:PREFerence:ECAL:ORIentation](GP-IB_Command_Finder/Sense/Sense_Correction.md#Orie) | [cal.OrientECALModule](COM_Reference/Properties/OrientECALModule_Property.md)  
Maps ECAL Module to PNA Ports | [SENSe:CORRection:PREFerence:ECAL:PMAP](GP-IB_Command_Finder/Sense/Sense_Correction.md#Pmap) | [cal.ECALPortMapEx](COM_Reference/Properties/ECALPortMapEx_Property.md)  
Reads ECal orientation | [SENSe:CORRection:CKIT:ECAL:ORIent?](GP-IB_Command_Finder/Sense/CorrCKIT_SCPI.md#Orient) | [ECalModules](COM_Reference/Objects/ECalModules_Collection.md)  
Perform ECal Isolation | [SENSe:CORRection:COLLect:ISOLation:ECAL](GP-IB_Command_Finder/Sense/Sense_Correction.md#IsoEcal) | [ECALIsolation](COM_Reference/Properties/ECALIsolation_Property.md)  
Increment Avg for ECal Isolation | [SENSe:CORRection:COLLect:ISOLation:AVERage:INCRement](GP-IB_Command_Finder/Sense/Sense_Correction.md#IsolAvg) | [IsolationAveragingIncrement](COM_Reference/Properties/IsolationAveragingIncrement_Property.md)  
Response Cal...  
Launch Cal Wizard | [SYSTem:CORRection:WIZard](GP-IB_Command_Finder/System.md#wiz) | [app.LaunchCalWizard](COM_Reference/Methods/LaunchCalWizard_Method.md)  
Set Cal Type | [SENSe:CORRection:COLLect:METHod](GP-IB_Command_Finder/Sense/Sense_Correction.md#sccm) | [cal.SetCalInfo](COM_Reference/Methods/SetCalInfo_Method.md)  
Select a Cal Kit | [SENSe:CORRection:COLLect:CKIT](GP-IB_Command_Finder/Sense/CorrCollCKIT.md#scccs) | [app.CalKitType](COM_Reference/Properties/CalKitType_Property.md)  
Get a Handle to the Active Cal Kit | None | [app.ActiveCalKit](COM_Reference/Properties/Active_Cal_Kit_Property.md)  
Simultaneous 2-Port Calibration | [SENSe:CORRection:TSTandards](GP-IB_Command_Finder/Sense/Sense_Correction.md#2STDS1) | [cal.Simultaneous2PortAcquisition](COM_Reference/Properties/Simultaneous2PortAcquisition_Property.md)  
Acquisition Direction | [SENSe:CORRection:SFORward](GP-IB_Command_Finder/Sense/Sense_Correction.md#sforward) | [cal.AcquisitionDirection](COM_Reference/Properties/AcquisitionDirection_Property.md)  
Measure a Standard | [SENSe:CORRection:COLLect](GP-IB_Command_Finder/Sense/Sense_Correction.md#scca) | [cal.AcquireCalStandard](COM_Reference/Methods/Acquire_Cal_Standard_Method.md)  
Calculate Errors | [SENSe:CORRection:COLLect:SAVE](GP-IB_Command_Finder/Sense/Sense_Correction.md#sccs) | [cal.CalculateErrorCoeffecients](COM_Reference/Methods/Calculate_Error_Coefficients_Method.md)  
Do Isolation | [SENSe:CORRection:COLLect](GP-IB_Command_Finder/Sense/Sense_Correction.md#scca) | [cal.AcquireCalStandard](COM_Reference/Methods/Acquire_Cal_Standard_Method.md)  
Perform and apply Response (Normalization) cal | [SENSe:CORRection:COLLect:METHod](GP-IB_Command_Finder/Sense/Sense_Correction.md#sccm) | [DoResponseCal](COM_Reference/Methods/DoResponseCal_Method.md)  
Source Power Cal...  
Copy Source Power cal to another channel | [SYSTem:MACRo:COPY:CHANnel:SOURce](GP-IB_Command_Finder/System.md#copySPC) | [ApplySourcePowerCorrectionTo](COM_Reference/Methods/ApplySourcePowerCorrectionTo_Method.md)  
GPIB Power Meter Address | [SYSTem:COMMunicate:PSENsor](GP-IB_Command_Finder/SystCommunicate.md#PSensorType) | [pwrCal.PowerMeterGPIBAddress](COM_Reference/Properties/PowerMeterGPIBAddress_Property.md)  
Set source power cal method | [SOURce:POWer:CORRection:COLLect:ACQuire](GP-IB_Command_Finder/SourceCorrection.md#aquire) | [SetCalInfoEx Method](COM_Reference/Methods/SetCalInfoEx_Method.md)  
Turn correction ON|OFF | [SOURce:POWer:CORRection](GP-IB_Command_Finder/SourceCorrection.md#state) | [SourcePowerCorrection](COM_Reference/Properties/SourcePowerCorrection_Property.md)  
Applies correction values after completing a source power cal acquisition sweep Optionally do reference receiver cal | [SOURce:POWer:CORRection:COLLect:SAVE](GP-IB_Command_Finder/SourceCorrection.md#save) | [ApplyPowerCorrectionValuesEx](COM_Reference/Methods/ApplyPowerCorrectionValuesEx_Method.md)  
Returns the currently-selected power sensor channel (A or B) for use at a specific frequency | None | [PowerAcquisitionDevice](COM_Reference/Properties/PowerAcquisitionDevice_Property.md)  
Set power level | [SOURce:POWer:CORRection:LEVel](GP-IB_Command_Finder/SourceCorrection.md#level) | [SetCalInfoEx Method](COM_Reference/Methods/SetCalInfoEx_Method.md)  
Set power offset | [SOURce:POWer:CORRection:OFFSet](GP-IB_Command_Finder/SourceCorrection.md#offset) | [SourcePowerCalPowerOffset](COM_Reference/Properties/SourcePowerCalPowerOffset_Property.md)  
Set settling tolerance | [SOURce:POWer:CORRection:COLLect:AVERage:NTOLerance](GP-IB_Command_Finder/SourceCorrection.md#averTol) | [ReadingsTolerance](COM_Reference/Properties/ReadingsTolerance_Property.md)  
Set max readings for settling | [SOURce:POWer:CORRection:COLLect:AVERage:COUNt](GP-IB_Command_Finder/SourceCorrection.md#average) | [ReadingsPerPoint](COM_Reference/Properties/ReadingsPerPoint_Property.md)  
Set accuracy tolerance | [SOURce:POWer:CORRection:COLLect:ITERation:NTOLerance](GP-IB_Command_Finder/SourceCorrection.md#iterTol) | [IterationsTolerance](COM_Reference/Properties/IterationsTolerance_Property.md)  
Set max readings for accuracy | [SOURce:POWer:CORRection:COLLect:ITERation:COUNt](GP-IB_Command_Finder/SourceCorrection.md#IterCount) | [MaximumIterationsPerPoint](COM_Reference/Properties/MaximumIterationsPerPoint_Property.md)  
Turn ON|OFF display of readings | [SOURce:POWer:CORRection:COLLect:DISPlay](GP-IB_Command_Finder/SourceCorrection.md#display) | [AcquirePowerReadingsEx](COM_Reference/Methods/AcquirePowerReadingsEx_Method.md)  
Acquire receiver-only readings | [SOURce:POWer:CORRection:COLLect:ACQuire](GP-IB_Command_Finder/SourceCorrection.md#aquire) | [AcquirePowerReadingsEx](COM_Reference/Methods/AcquirePowerReadingsEx_Method.md)  
Initiates a source power cal acquisition | [SOURce:POWer:CORRection:COLLect:ACQuire](GP-IB_Command_Finder/SourceCorrection.md#aquire) | [AcquirePowerReadingsEx](COM_Reference/Methods/AcquirePowerReadingsEx_Method.md)  
Aborts a source power cal acquisition sweep that is currently in progress | [SOURce:POWer:CORRection:COLLect:ABORt](GP-IB_Command_Finder/SourceCorrection.md#abort) | [AbortPowerAcquisition](COM_Reference/Methods/AbortPowerAcquisition_Method.md)  
Launches the Power Meter Settings dialog on the PNA | None | [LaunchPowerMeterSettingsDialog](COM_Reference/Methods/LaunchPowerMeterSettingsDialog_Method.md)  
Frequency checking (ON|OFF) | [SOURce:POWer:CORRection:COLLect:FCHeck](GP-IB_Command_Finder/SourceCorrection.md#fcheck) | [UsePowerSensorFrequencyLimits](COM_Reference/Properties/UsePowerSensorFrequencyLimits_Property.md)  
Check test port power | None | [CheckPower](COM_Reference/Methods/CheckPower_Method.md)  
Calibrate the source at multiple power levels | None | None  
Cal Update...  
Select Channel | [SYSTem:CALibrate:CALupdate:CHANnels[:SELect]](GP-IB_Command_Finder/SystCalDrift.md#SYSTem:CALibrate:DRIFt:CHANnel:ALL:STATe) | None  
Reference Cal Set | [SYSTem:CALibrate:CALupdate:REFerence](GP-IB_Command_Finder/SystCalDrift.md#SYSTem:CALibrate:DRIFt:REFerence) | None  
IF Bandwidth | [SYSTem:CALibrate:CALupdate:BWIDth[:RESolution]](GP-IB_Command_Finder/SystCalDrift.md#SYSTem:CALibrate:DRIFt:BWIDth:RESolution) | None  
Averaging | [SYSTem:CALibrate:CALupdate:AVERage:COUNt](GP-IB_Command_Finder/SystCalDrift.md#SYSTem:CALibrate:DRIFt:AVERage:COUNt) | None  
Power | [SYSTem:CALibrate:CALupdate:SOURce:POWer](GP-IB_Command_Finder/SystCalDrift.md#SYSTem:CALibrate:DRIFt:SOURce:POWer) | None  
Auto | [SYSTem:CALibrate:CALupdate:SETTings:AUTO](GP-IB_Command_Finder/SystCalDrift.md#SYSTem:CALibrate:DRIFt:SETTings:AUTO) | None  
Auto-Calculate Gates | None | None  
Select | [SYSTem:CALibrate:CALupdate:PORTs[:SELect]](GP-IB_Command_Finder/SystCalDrift.md#SYSTem:CALibrate:DRIFt:PORTs:SELect) | None  
Gate Start | [SYSTem:CALibrate:CALupdate:GATE:STARt](GP-IB_Command_Finder/SystCalDrift.md#SYSTem:CALibrate:DRIFt:GATE:STARt) | None  
Gate Start Couple | [SYSTem:CALibrate:CALupdate:GATE:STARt:COUPle[:STATe]](GP-IB_Command_Finder/SystCalDrift.md#SYSTem:CALibrate:DRIFt:GATE:STARt:COUPle:STATe) | None  
Gate Stop | [SYSTem:CALibrate:CALupdate:GATE:STOP](GP-IB_Command_Finder/SystCalDrift.md#SYSTem:CALibrate:DRIFt:GATE:STOP) | None  
Gate Stop Couple | [SYSTem:CALibrate:CALupdate:GATE:STOP:COUPle[:STATe]](GP-IB_Command_Finder/SystCalDrift.md#SYSTem:CALibrate:DRIFt:GATE:STOP:COUPle:STATe) | None  
Initialize | [SYSTem:CALibrate:CALupdate:INITialize](GP-IB_Command_Finder/SystCalDrift.md#SYSTem:CALibrate:DRIFt:INITialize) | None  
Recorrect | [SYSTem:CALibrate:CALupdate:RECorrect](GP-IB_Command_Finder/SystCalDrift.md#SYSTem:CALibrate:DRIFt:RECorrect) | None  
Advanced |  |   
Enable All Cal Updates | None | None  
Disable All Cal Updates | None | None  
Delete All Cal Update Cal Sets | None | None  
Set Dialog to Defaults | None | None  
Correction | Channel Correction On | [SENSe:CORRection:STATe](GP-IB_Command_Finder/Sense/Sense_Correction.md#scs) | [chan.ErrorCorrection](COM_Reference/Properties/ErrorCorrection_Channel_Property.md)  
Channel Correction Off | [SENSe:CORRection:STATe](GP-IB_Command_Finder/Sense/Sense_Correction.md#scs) | [chan.ErrorCorrection](COM_Reference/Properties/ErrorCorrection_Channel_Property.md)  
Cal Set...  
Create a Cal Set | [SENSe:CORRection:CSET:CREate](GP-IB_Command_Finder/Sense/CorrCset.md#create) | [calMgr.CreateCalSet](COM_Reference/Methods/CreateCalSet_Method.md)  
Delete a Cal Set | [CSET:DEL](GP-IB_Command_Finder/CSET.md#delete) | [calMgr.DeleteCalSet](COM_Reference/Methods/DeleteCalSet_Method.md)  
List Cal Sets | [CSET:CATalog?](GP-IB_Command_Finder/CSET.md#CAT) | [calMgr.GetCalSetCatalog](COM_Reference/Methods/Get_CalSetCatalog_Method.md)  
List Cal Sets in PNA | None | [EnumerateCalSets](COM_Reference/Methods/EnumerateCalSets_Method.md)  
Get Cal Set Information | None | [calMgr.GetCalSetUsageInfo](COM_Reference/Methods/Get_CalSetUsageInfo_Method.md)  
List Cal Set Error Terms | [SENSe:CORRection:CSET:ETERm:CATalog?](GP-IB_Command_Finder/Sense/CorrCset.md#etermCAT) | [Get ErrorTermList2](COM_Reference/Methods/Get_ErrorTermList2_Method.md)  
Return if a Cal Set exists | [CSET:EXISts?](GP-IB_Command_Finder/CSET.md#Exists) | [Exists](COM_Reference/Methods/Exists_Method.md)  
Select a Cal Set by GUID | [SENSe:CORRection:CSET:ACTivate](GP-IB_Command_Finder/Sense/CorrCset.md#activate) | [calMgr.GetCalSetByGUID](COM_Reference/Methods/Get_CalSetByGUID_Method.md)  
Apply a Cal Set to a channel | [SENSe:CORRection:CSET:ACTivate](GP-IB_Command_Finder/Sense/CorrCset.md#activate) | [channel.SelectCalSet](COM_Reference/Methods/SelectCalSet_Method.md)  
Copy a Cal Set | [SENSe:CORRection:CSET:COPY](GP-IB_Command_Finder/Sense/CorrCset.md#copy) | [CalSet.Copy](COM_Reference/Methods/Copy_Method.md)  
Save a Cal Set | [SENSe:CORRection:CSET:SAVE](GP-IB_Command_Finder/Sense/CorrCset.md#sccsv) | [CalSet.Save](COM_Reference/Methods/Save_CalSet_Method.md)  
Save Cal Sets | None | [app.SaveCalSets](COM_Reference/Methods/Save_CalSets_Method.md)  
Automatically save to User Cal Set | [SENSe:CORRection:PREFerence:CSET:SAVE](GP-IB_Command_Finder/Sense/Sense_Correction.md#CsetSave) | None  
Change the Description of a Cal Set | [SENSe:CORRection:CSET:DESCription](GP-IB_Command_Finder/Sense/CorrCset.md#desc) | [CalSet.Description](COM_Reference/Properties/Description_Property.md)  
Change the Name of a Cal Set | [SENSe:CORRection:CSET:NAME](GP-IB_Command_Finder/Sense/CorrCset.md#name) | [calset.Name](COM_Reference/Properties/Name_Calset_Property.md)  
Recall a Cal File | [MMEMory:LOAD](GP-IB_Command_Finder/Memory.md#recall) | [app.Recall](COM_Reference/Methods/Recall_Method.md)  
Save 'in-memory' Cal Set to disk. | [SENSe:CORRection:CSET:FLATten](GP-IB_Command_Finder/Sense/CorrCset.md#Flatten) | None  
Create Cal Set with De-embeded fixture removed | [CSET:FIXTure:DEEMbed](GP-IB_Command_Finder/CSET.md#deembed) | [Deembed](COM_Reference/Methods/Deembed_Method.md)  
Create Cal Set with Matching Network included | [CSET:FIXTure:EMBed](GP-IB_Command_Finder/CSET.md#embed) | [Embed](COM_Reference/Methods/Embed_Method.md)  
Adds stimulus data to a specific buffer | None | [PutErrorTermStimulus](COM_Reference/Methods/PutErrorTermStimulus_Method.md)  
Returns the stimulus values over which the specific error term was acquired | None | [GetErrorTermStimulus](COM_Reference/Methods/GetErrorTermStimulus_Method.md)  
Returns FOM stimulus values from a Calset | [SENSe:CORRection:CSET:STIMulus?](GP-IB_Command_Finder/Sense/CorrCset.md#Stimulus) | [StimulusValues](COM_Reference/Properties/StimulusValues_Property.md)  
Returns the Cal Types from the calset | None | [ContentDescriptor](COM_Reference/Properties/ContentDescriptor_Property.md)  
Returns the properties of the calset | None | [Properties](COM_Reference/Properties/Properties_Property.md)  
Returns the numbers of the channels using the calset | None | [ChannelClients](COM_Reference/Properties/ChannelClients_Property.md)  
Unselect Cal Set | [SENSe:CORRection:CSET:DEACtivate](GP-IB_Command_Finder/Sense/CorrCset.md#DEACtivate) | [UnselectCalset](COM_Reference/Methods/UnselectCalset_Method.md)  
Factory Cal | ON/OFF | [SYSTem:FCORrection:CHANnel:COUPler[:STATe]](GP-IB_Command_Finder/System.md#chanCouple) | None  
Src Power Correct | ON/OFF | [SOURce:POWer:CORRection[:STATe]](GP-IB_Command_Finder/SourceCorrection.md#state) | [SourcePowerCorrection](COM_Reference/Properties/SourcePowerCorrection_Property.md)  
Interpolation | ON/OFF | [SENSe:CORRection:INTerpolate[:STATe]](GP-IB_Command_Finder/Sense/Sense_Correction.md#scis) | [InterpolateCorrection](COM_Reference/Properties/Interpolate_Correction_Property.md)  
Correction Methods... | Power Correction Type | [SENSe:CORRection:WAVE[:METHod]](GP-IB_Command_Finder/Sense/Sense_Correction.md#methodsMatch) | None  
| Enable Port Subset Correction | [SENSe:CORRection:METHods:PORT:SUBSet:[:STATe]](GP-IB_Command_Finder/Sense/Sense_Correction.md#SENSe:CORRection:METHods:PORT:SUBSet:STATe) | [CorrectionSubsettingState](COM_Reference/Properties/CorrectionSubsettingState_Property.md)  
| Select Ports in Subset | [SENSe:CORRection:METHods:PORT:SUBSet:FULL[:VALue]](GP-IB_Command_Finder/Sense/Sense_Correction.md#SENSe:CORRection:METHods:PORT:SUBSet:FULL:VALue) | [FullyCorrectedPorts](COM_Reference/Properties/FullyCorrectedPorts_Property.md)  
| Clear All | [SENSe:CORRection:METHods:PORT:SUBSet:RESet](GP-IB_Command_Finder/Sense/Sense_Correction.md#SENSe:CORRection:METHods:PORT:SUBSet:RESet) | [ResetPortValues](COM_Reference/Methods/ResetPortValues_Method.md)  
| (SA Class) Select Ports Will Correct Power Using Actual Waves | [SENSe:CORRection:METHods:SA:PORT](GP-IB_Command_Finder/Sense/Sense_Correction.md#MethSAPort) | None  
Correction Properties... |  | None | [Properties](COM_Reference/Properties/Properties_Property.md)  
Port Extension Tab Commands  
Softkey | Sub-item | SCPI | COM  
Select | Port N | [SENSe:CORRection:EXTension:PORT](GP-IB_Command_Finder/Sense/CorrExtension.md#PortTime) | [portExt.Port1](COM_Reference/Properties/Port_1_Property.md) [portExt.Port2](COM_Reference/Properties/Port_2_Property.md)  
Port Extension | ON/OFF | [SENSe:CORRection:EXTension](GP-IB_Command_Finder/Sense/CorrExtension.md#ExtState) | [portExtension.State](COM_Reference/Properties/State_Property.md)  
Time |  | [SENSe:CORRection:EXTension:PORT:TIME](GP-IB_Command_Finder/Sense/CorrExtension.md#PortTime) | [PortDelay](COM_Reference/Properties/PortDelay_Property.md)  
Distance |  | [SENSe:CORRection:EXTension:PORT:DISTance](GP-IB_Command_Finder/Sense/CorrExtension.md#portDist) | [PortDistance](COM_Reference/Properties/PortDistance_Property.md)  
Velocity Factor |  | [SENSe:CORRection:RVELocity:COAX](GP-IB_Command_Finder/Sense/Sense_Correction.md#scrc) | [app.VelocityFactor](COM_Reference/Properties/Velocity_Factor_Property.md)  
DC Loss |  | [SENSe:CORRection:EXTension:PORT:LDC](GP-IB_Command_Finder/Sense/CorrExtension.md#LossDC) | [fix.PortLossDC](COM_Reference/Properties/PortLossDC_Property.md)  
Port Extensions... | Extensions ON|OFF | [SENSe:CORRection:EXTension](GP-IB_Command_Finder/Sense/CorrExtension.md#ExtState) | [portExtension.State](COM_Reference/Properties/State_Property.md)  
Port 1 Extensions Value | [SENSe:CORRection:EXTension:PORT](GP-IB_Command_Finder/Sense/CorrExtension.md#PortTime) | [portExt.Port1](COM_Reference/Properties/Port_1_Property.md)  
Port 2 Extensions Value | [SENSe:CORRection:EXTension:PORT](GP-IB_Command_Finder/Sense/CorrExtension.md#PortTime) | [portExt.Port2](COM_Reference/Properties/Port_2_Property.md)  
Set Freq 1|2 | [SENSe:CORRection:EXTension:PORT:FREQuency](GP-IB_Command_Finder/Sense/CorrExtension.md#PortExtFreqX) | [Fix.PortFreq1](COM_Reference/Properties/PortFreq1_Property.md)  
Set Loss 1|2 | [SENSe:CORRection:EXTension:PORT:LOSS](GP-IB_Command_Finder/Sense/CorrExtension.md#PortExtLoss) | [fix.PortLoss1](COM_Reference/Properties/PortLoss1_Property.md)  
Use 1|2 | [SENSe:CORRection:EXTension:PORT:INCLude](GP-IB_Command_Finder/Sense/CorrExtension.md#PortExtIncl) | [fix.PortExtUse1](COM_Reference/Properties/PortExtUse1_Property.md)  
Set Loss at DC | [SENSe:CORRection:EXTension:PORT:LDC](GP-IB_Command_Finder/Sense/CorrExtension.md#LossDC) | [fix.PortLossDC](COM_Reference/Properties/PortLossDC_Property.md)  
Relative Velocity | [SENSe:CORRection:RVELocity:COAX](GP-IB_Command_Finder/Sense/Sense_Correction.md#scrc) | [app.VelocityFactor](COM_Reference/Properties/Velocity_Factor_Property.md)  
Port Ext in distance | [SENSe:CORRection:EXTension:PORT:DISTance](GP-IB_Command_Finder/Sense/CorrExtension.md#portDist) | [PortDistance](COM_Reference/Properties/PortDistance_Property.md)  
Set distance units | [SENSe:CORRection:EXTension:PORT:UNIT](GP-IB_Command_Finder/Sense/CorrExtension.md#UNIT) | [PortDistanceUnit](COM_Reference/Properties/PortDistanceUnit_Property.md)  
Set Media per port | [SENSe:CORRection:EXTension:PORT:MEDium](GP-IB_Command_Finder/Sense/CorrExtension.md#portMedium) | [PortMedium](COM_Reference/Properties/PortMedium_Property.md)  
Set waveguide cutoff freq per port | [SENSe:CORRection:EXTension:PORT:WGCutoff](GP-IB_Command_Finder/Sense/CorrExtension.md#portWGC) | [PortWGCutoffFreq](COM_Reference/Properties/PortWGCutoffFreq_Property.md)  
Set Velocity Factor per port | [SENSe:CORRection:EXTension:PORT:VELFactor](GP-IB_Command_Finder/Sense/CorrExtension.md#portVF) | [PortVelocityFactor](COM_Reference/Properties/PortVelocityFactor_Property.md)  
Couple to system Velocity Factor | [SENSe:CORRection:EXTension:PORT:SYSVelocity](GP-IB_Command_Finder/Sense/CorrExtension.md#sysVelocity) | [PortCoupleToSystemVelocity](COM_Reference/Properties/PortCoupleToSystemVelocity_Property.md)  
Couple to system Media type | [SENSe:CORRection:EXTension:PORT:SYSMedia](GP-IB_Command_Finder/Sense/CorrExtension.md#sysMedia) | [PortCoupleToSystemMedia](COM_Reference/Properties/PortCoupleToSystemMedia_Property.md)  
Auto Port Extension... | Measure OPEN or SHORT for Auto Port Ext | [SENSe:CORRection:EXTtension:AUTO:MEASure](GP-IB_Command_Finder/Sense/CorrExtension.md#autoMeas) | [AutoPortExtMeasure](COM_Reference/Methods/AutoPortExtMeasure_Method.md)  
Sets the frequencies used for Auto Port Ext. calculation | [SENSe:CORRection:EXTension:AUTO:CONFig](GP-IB_Command_Finder/Sense/CorrExtension.md#autoConfig) | [AutoPortExtConfig](COM_Reference/Properties/AutoPortExtConfig_Property.md)  
Include loss correction in Auto Port Ext | [SENSe:CORRection:EXTension:AUTO:LOSS](GP-IB_Command_Finder/Sense/CorrExtension.md#AutoLoss) | [AutoPortExtLoss](COM_Reference/Properties/AutoPortExtLoss_Property.md)  
Include DC Offset in Auto Port Ext | [SENSe:CORRection:EXTension:AUTO:DCOFfset](GP-IB_Command_Finder/Sense/CorrExtension.md#AutoDCOffset) | [AutoPortExtDCOffset](COM_Reference/Properties/AutoPortExtDCOffset_Property.md)  
Enable specified port for Auto Port Ext | [SENSe:CORRection:EXTension:AUTO:PORT<n>](GP-IB_Command_Finder/Sense/CorrExtension.md#autoPort) | [AutoPortExtState](COM_Reference/Properties/AutoPortExtState_Property.md)  
Clears old port extension delay and loss data | [SENSe:CORRection:EXTension:AUTO:RESet](GP-IB_Command_Finder/Sense/CorrExtension.md#autoReset) | [AutoPortExtReset](COM_Reference/Methods/AutoPortExtReset_Method.md)  
Set user span start frequency for Auto Port Ext | [SENSe:CORRection:EXTension:AUTO:STARt](GP-IB_Command_Finder/Sense/CorrExtension.md#autoStart) | [AutoPortExtSearchStart](COM_Reference/Properties/AutoPortExtSearchStart_Property.md)  
Set user span stop frequency for Auto Port Ext | [SENSe:CORRection:EXTension:AUTO:STOP](GP-IB_Command_Finder/Sense/CorrExtension.md#autoStop) | [AutoPortExtSearchStop](COM_Reference/Properties/AutoPortExtSearchStop_Property.md)  
Cal Sets & Cal Kits Tab Commands  
Softkey | Sub-item | SCPI | COM  
Cal Set... |  | [CSET](GP-IB_Command_Finder/CSET.md) |   
Cal Set Viewer | ON/OFF | [DISPlay:TOOL:CSET[:STATe]](GP-IB_Command_Finder/Display.md#DISPlay:TOOLbar:CSET:STATe) | None  
Cal Kit... | Set a Cal Kit Active | [SENSe:CORRection:COLLect:CKIT](GP-IB_Command_Finder/Sense/CorrCollCKIT.md#scccs) | [app.CalKitType](COM_Reference/Properties/CalKitType_Property.md)  
Clear all Cal Kits from PNA | [SENSe:CORRection:CKIT:CLEar](GP-IB_Command_Finder/Sense/CorrCKIT_SCPI.md#clear) | None  
Get a Handle to the Active Cal Kit | None | [app.ActiveCalKit](COM_Reference/Properties/Active_Cal_Kit_Property.md)  
Save All Cal Kits after Modifying | None | [app.SaveKits](COM_Reference/Methods/Save_Kits_Method.md)  
Load collection of Kits | [SENSe:CORRection:CKIT:LOAD](GP-IB_Command_Finder/Sense/CorrCKIT_SCPI.md#load) | None  
Load (Recall) All Cal Kits | None | [app.RecallKits](COM_Reference/Methods/Recall_Kits_Method.md)  
Import a specified kit | [SENSe:CORRection:CKIT:IMPort](GP-IB_Command_Finder/Sense/CorrCKIT_SCPI.md#import) | None  
Restore Cal Kit Default | [SENSe:CORRection:CKIT:INITialize](GP-IB_Command_Finder/Sense/CorrCKIT_SCPI.md#initialize) | None  
Restore ALL Cal Kits Default | [SENSe:CORRection:CKIT:INITialize](GP-IB_Command_Finder/Sense/CorrCKIT_SCPI.md#initialize) | None  
Build a Hybrid Cal Kit | None | [app.BuildHybridKit](COM_Reference/Methods/Build_Hybrid_Kit_Method.md)  
Set the Name of a Cal Kit | [SENSe:CORRection:COLLect:CKIT:NAME](GP-IB_Command_Finder/Sense/CorrCollCKIT.md#scccn) | [calKit.Name](COM_Reference/Properties/Name_CalKit_Property.md)  
Set a description of a Cal Kit | [SENSe:CORRection:COLLect:CKIT:DESCription](GP-IB_Command_Finder/Sense/CorrCollCKIT.md#desc) | None  
Get the amount of installed kits | [SENSe:CORRection:CKIT:COUNt?](GP-IB_Command_Finder/Sense/CorrCKIT_SCPI.md#count) | None  
Set the Port Label of a Cal Kit | None | [calKit.Portlabel](COM_Reference/Properties/PortLabel_Property.md)  
Saves a Cal Kit to a file | [SENSe:CORRection:CKIT:EXPort](GP-IB_Command_Finder/Sense/CorrCKIT_SCPI.md#Export) | None  
ECal... |   
Cal Pod... | Command used to send other commands as arguments | [CONTrol:CALPod:COMMand](GP-IB_Command_Finder/Control.md#Calpod) | None  
Start the CalPod software | [Calpod:LAUNch](GP-IB_Command_Finder/Calpod.md#launch) | None  
Assign Calpod serial number to a port. | [Calpod:ENABle](GP-IB_Command_Finder/Calpod.md#enable) | None  
Unassign Calpod serial number from a port. | [Calpod:Disable](GP-IB_Command_Finder/Calpod.md#disable) | None  
Initialize the selected channel | [Calpod:INITialize:ACTive](GP-IB_Command_Finder/Calpod.md#InitActive) | None  
Initialize ALL channels | [Calpod:INITialize:ALL](GP-IB_Command_Finder/Calpod.md#InitAll) | None  
Recorrect the selected channel | [Calpod:Recorrect:ACTive](GP-IB_Command_Finder/Calpod.md#RecorrectActive) | None  
Recorrect ALL channels | [Calpod:Recorrect:ALL](GP-IB_Command_Finder/Calpod.md#recorrectAll) | None  
Show refresh dialog | [Calpod:SHOW](GP-IB_Command_Finder/Calpod.md#show) | None  
Hide refresh dialog | [Calpod:HIDE](GP-IB_Command_Finder/Calpod.md#hide) | None  
Sets impedance state | [Calpod:STATe](GP-IB_Command_Finder/Calpod.md#State) | None  
Read Calpod temperature | [Calpod:TEMP?](GP-IB_Command_Finder/Calpod.md#Temp) | None  
Uncertainty Setup... | Trace Type | [CALCulate:UNCertainty:DISPlay:TYPE](GP-IB_Command_Finder/Calculate/Uncertainty.md#UNCertDISPlayTYPE) | [DisplayType](COM_Reference/Properties/DisplayType_Property.md)  
Coverage factor value | [CALCulate:UNCertainty:DISPlay:CFACtor](GP-IB_Command_Finder/Calculate/Uncertainty.md#UncertDispFactor) | [CoverageFactor](COM_Reference/Properties/CoverageFactor_Property.md)  
Noise contribution | [CALCulate:UNCertainty:MODE:NOISe](GP-IB_Command_Finder/Calculate/Uncertainty.md#UncertNoise) | [MeasurementNoiseUncertainty](COM_Reference/Properties/MeasurementNoiseUncertainty_Property.md)  
Cable/connection repeatability contribution | [CALCulate:UNCertainty:MODE:CABLe:REPeat](GP-IB_Command_Finder/Calculate/Uncertainty.md#UncertCableRepeat) | [CableRepeatabilityUncertainty](COM_Reference/Properties/CableRepeatabilityUncertainty_Property.md)  
Error term uncertainties | [CALCulate:UNCertainty:MODE:ETERm](GP-IB_Command_Finder/Calculate/Uncertainty.md#MODE:ETERm) | [ErrorTermUncertainty](COM_Reference/Properties/ErrorTermUncertainty_Property.md)  
Save uncertainty data | [CALCulate:UNCertainty:SAVE](GP-IB_Command_Finder/Calculate/Uncertainty.md#save) | [WriteUncertaintyFile](COM_Reference/Methods/WriteUncertaintyFile_Method.md)  
Add Trace | None | None  
Apply to all traces | None | None  
Fixtures Tab Commands  
Softkey | Sub-item | SCPI | COM  
[Fixture Simulator Draft](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md) and [Fixture Simulator Active](GP-IB_Command_Finder/Calculate/FSimulatorActive.md) | Copy draft fixture to active fixture | [CALCulate:FSIMulator:DRAFt:APPLy](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#Apply) [CALCulate:FSIMulator:APPLy](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#APPLy) | None  
Discards changes on scratch/draft fixture | [CALCulate:FSIMulator:DRAFt:DISCard](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#Discard) | None  
Saves SNP file corresponding to the entire scratch fixture | [CALCulate:FSIMulator:DRAFt:SAVE](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#Save) | None  
Saves SNP file corresponding to the entire active fixture | [CALCulate:FSIMulator:SAVE](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#SAVE) | None  
|  |   
Loads an active fixture topology file | [CALCulate:FSIMulator:TOPology:LOAD](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#CALCulate:FSIMulator:TOPology:LOAD) | None  
|  |   
Saves an active fixture topology file | [CALCulate:FSIMulator:TOPology:SAVE](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#CALCulate:FSIMulator:TOPology:SAVE) | None  
Sets and returns on power compensation for the active fixture | [CALCulate:FSIMulator:POWer:PORT:COMPensate[:STATe]](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#PowPortComp) | None  
Section State Switches  
Turns port extensions ON and OFF for all ports | [CALCulate:FSIMulator:DRAFt:SECTion:EXTension:ENABle](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#SectExtEnab) [CALCulate:FSIMulator:SECTion:EXTension:ENABle?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#SectExtEnab) | None  
Turns all circuits ON and OFF for all ports | [CALCulate:FSIMulator:DRAFt:SECTion:CIRCuit:ENABle](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#SectCircEnab) [CALCulate:FSIMulator:SECTion:CIRCuit:ENABle?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#SectCircEnab) | None  
Turns all ZConversions ON and OFF (both SE and BAL) | [CALCulate:FSIMulator:DRAFt:SECTion:ZCONversion:ENABle](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#SecZconEnab) [CALCulate:FSIMulator:SECTion:ZCONversion:ENABle?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#SectZconEnab) | None  
Circuit Section  
Returns a comma-separated list of circuit numbers created in the draft circuit | [CALCulate:FSIMulator:DRAFt:CIRCuit:CATalog?](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#CircCat) [CALCulate:FSIMulator:CIRCuit:CATalog?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#CircCat) | None  
Returns the next free circuit number than be used to create a new circuit block | [CALCulate:FSIMulator:DRAFt:CIRCuit:NEXT?](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#CircNext) | None  
Create a block of the specified block type with the specified fixture port count | [CALCulate::FSIMulator:DRAFt:CIRCuit:ADD](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#CircAdd) | None  
Deletes the specified circuit | [CALCulate:FSIMulator:DRAFt:CIRCuit:DELete](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#CircDel) | None  
Sets the VNA ports for the specified circuit | [CALCulate:FSIMulator:DRAFt:CIRCuit:VNA:PORTs](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#CircVnaPort) [CALCulate:FSIMulator:CIRCuit:VNA:PORTs?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#CircVnaPort) | None  
Sets the Device ports for the specified circuit  | [CALCulate:FSIMulator:DRAFt:CIRCuit:DEVice:PORTs](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#CircDevPort) [CALCulate:FSIMulator:CIRCuit:DEVice:PORTs?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#CircDevPort) | None  
Sets the resistance circuit element | [CALCulate:FSIMulator:DRAFt:CIRCuit:PARameter:R](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#CircParR) [CALCulate:FSIMulator:DRAFt:CIRCuit:PARameter:R2](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#CircParR2) [CALCulate:FSIMulator:CIRCuit:PARameter:R?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#CircParR) [CALCulate:FSIMulator:CIRCuit:PARameter:R2?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#CircParR2) | None  
Sets the inductance circuit element | [CALCulate:FSIMulator:DRAFt:CIRCuit:PARameter:L](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#CircParL) [CALCulate:FSIMulator:DRAFt:CIRCuit:PARameter:L2](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#CircParL2) [CALCulate:FSIMulator:CIRCuit:PARameter:L?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#CircParL) [CALCulate:FSIMulator:CIRCuit:PARameter:L2?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#CircParL2) | None  
Sets the capacitance circuit element | [CALCulate:FSIMulator:DRAFt:CIRCuit:PARameter:C](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#CircParC) [CALCulate:FSIMulator:DRAFt:CIRCuit:PARameter:C2](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#CircParC2) [CALCulate:FSIMulator:CIRCuit:PARameter:C?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#CircParC) [CALCulate:FSIMulator:CIRCuit:PARameter:C2?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#CircParC2) | None  
Sets the conductance circuit element | [CALCulate:FSIMulator:DRAFt:CIRCuit:PARameter:G](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#CircParG) [CALCulate:FSIMulator:DRAFt:CIRCuit:PARameter:G2](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#CircParG2) [CALCulate:FSIMulator:CIRCuit:PARameter:G?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#CircParG) [CALCulate:FSIMulator:CIRCuit:PARameter:G2?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#CircParG2) | None  
Sets the impedance (Z0) for the ideal block (scalar value). | [CALCulate:FSIMulator:DRAFt:CIRCuit:PARameter:Z0](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#CircParZ0) [CALCulate:FSIMulator:CIRCuit:PARameter:Z0?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#CircParZ0) | None  
Sets the R value at output of transformer (real only) | [CALCulate:FSIMulator:DRAFt:CIRCuit:PARameter:ROUT](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#CircParRout) [CALCulate:FSIMulator:CIRCuit:PARameter:ROUT?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#CircParRou) | None  
Sets the R value at input of transformer (real only) | [CALCulate:FSIMulator:DRAFt:CIRCuit:PARameter:RIN](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#CircParRin) [CALCulate:FSIMulator:CIRCuit:PARameter:RIN?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#CirParRin) | None  
Sets port extension delay in time | [CALCulate:FSIMulator:DRAFt:CIRCuit:PARameter:DELay](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#CircParDel) [CALCulate:FSIMulator:CIRCuit:PARameter:DELay?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#CircParDel) | None  
Sets the loss at DC | [CALCulate:FSIMulator:DRAFt:CIRCuit:PARameter:LOSS:VALue](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#CircParLossVal) [CALCulate:FSIMulator:CIRCuit:PARameter:LOSS:VALue?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#CircParLossVal) | None  
Sets the filename | [CALCulate:FSIMulator:DRAFt:CIRCuit:FILE](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#CircFile) [CALCulate:FSIMulator:CIRCuit:FILE?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#CircFile) | None  
Sets whether or not extrapolation is allowed | [CALCulate:FSIMulator:DRAFt:CIRCuit:FILE:EXTRapolate](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#CircFileExtr) [CALCulate:FSIMulator:CIRCuit:FILE:EXTRapolate?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#CircFileExtr) | None  
embedded or de-embedded? | [CALCulate:FSIMulator:DRAFt:CIRCuit:EMBED:TYPE](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#CircEmbedType) [CALCulate:FSIMulator:CIRCuit:EMBED:TYPE?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#CircEmbedType) | None  
Turns the circuit ON and OFF | [CALCulate:FSIMulator:DRAFt:CIRCuit:STATe](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#CircStat) [CALCulate:FSIMulator:CIRCuit:STATe?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#CircStat) | None  
Impedance Conversion  
Sets the differential port impedance conversion function ON/OFF | [CALCulate:FSIMulator:DRAFt:ZCONversion:DIFFerential:STATe](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#ZconDiffStat) [CALCulate:FSIMulator:ZCONversion:DIFFerential:STATe?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#ZconDiffStat) | None  
Sets the complex impedance value for differential port impedance | [CALCulate:FSIMulator:DRAFt:ZCONversion:DIFFerential:BPORt:COMPLe](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#ZconDiffBportComp)x [CALCulate:FSIMulator:ZCONversion:DIFFerential:BPORt:COMPLex?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#ZconDiffBportComp) [CALCulate:FSIMulator:ZCONversion:DIFFerential:LPORt:COMPLex?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#ZconDiffLportComp) | None  
Sets the real impedance value for differential port impedance | [CALCulate:FSIMulator:DRAFt:ZCONversion:DIFFerential:BPORt:SCALar](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#ZconDiffBportScal) [CALCulate:FSIMulator:DRAFt:ZCONversion:DIFFerential:LPORt:SCALar](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#ZconDiffLportScal) [CALCulate:FSIMulator:ZCONversion:DIFFerential:BPORt:SCALar?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#ZconDiffBportScal) [CALCulate:FSIMulator:ZCONversion:DIFFerential:LPORt:SCALar?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#ZconDiffLportScal) | None  
Sets the common mode port impedance conversion function ON/OFF | [CALCulate:FSIMulator:DRAFt:ZCONversion:COMMonmode:STATe](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#ZcomCommStat) [CALCulate:FSIMulator:ZCONversion:COMMonmode:STATe?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#ZconCommStat) | None  
Sets the complex impedance value for common mode port impedance | [CALCulate:FSIMulator:DRAFt:ZCONversion:COMMonmode:BPORt:COMPLex](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#ZconCommBportComp) [CALCulate:FSIMulator:DRAFt:ZCONversion:COMMonmode:LPORt:COMPLex](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#ZconCommLportComp) [CALCulate:FSIMulator:ZCONversion:COMMonmode:BPORt:COMPLex?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#ZconCommBportComp) [CALCulate:FSIMulator:ZCONversion:COMMonmode:LPORt:COMPLex?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#ZconCommportComp) | None  
Sets the real impedance value for common mode port impedance | [CALCulate:FSIMulator:DRAFt:ZCONversion:COMMonmode:BPORt:SCALar](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#ZconCommBportScal) [CALCulate:FSIMulator:DRAFt:ZCONversion:COMMonmode:LPORt:SCALar](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#ZconCommLportScal) [CALCulate:FSIMulator:ZCONversion:COMMonmode:BPORt:SCALar?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#ZconCommBportScal) [CALCulate:FSIMulator:ZCONversion:COMMonmode:LPORt:SCALar?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#ZconCommLportScal) | None  
Sets the single-ended ZCONV ON/OFF | [CALCulate:FSIMulator:DRAFt:ZCONversion:SENDed:PORT:STATe](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#ZconSendPortStat) | None  
Sets the complex impedance value for SE port impedance | [CALCulate:FSIMulator:DRAFt:ZCONversion:SENDed:PORT:COMPLex](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#ZconSendPortComp) [CALCulate:FSIMulator:ZCONversion:SENDed:PORT:COMPLex?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#ZconSendPortComp) | None  
Sets the real impedance value for SE port impedance | [CALCulate:FSIMulator:DRAFt:ZCONversion:SENDed:PORT:SCALar](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#ZconSendPotScal) [CALCulate:FSIMulator:ZCONversion:SENDed:PORT:SCALar?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#ZconSendPortScal) | None  
Port Extension  
Sets delay in time | [CALCulate:FSIMulator:DRAFt:EXTension:PORT:DELay](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#ExtPortDel) [CALCulate:FSIMulator:EXTension:PORT:DELay?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#ExtPortDel) | None  
Sets delay in physical distance | [CALCulate:FSIMulator:DRAFt:EXTension:PORT:DISTance:VALue](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#ExtPortDistVal) [CALCulate:FSIMulator:EXTension:PORT:DISTance:VALue?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#ExtPortDistVal) | None  
Sets unit for port extension distance | [CALCulate:FSIMulator:DRAFt:EXTension:PORT:DISTance:UNIT](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#ExtPortDistUnit) [CALCulate:FSIMulator:EXTension:PORT:DISTance:UNIT?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#ExtPortDistUnit) | None  
Sets frequency value for "loss1" or "loss2" | [CALCulate:FSIMulator:DRAFt:EXTension:PORT:LOSS:FREQuency](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#ExtPortLossFreq) [CALCulate:FSIMulator:EXTension:PORT:LOSS:FREQuency?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#ExtPortLossFreq) | None  
Sets loss value for "loss1" or "loss2" | [CALCulate:FSIMulator:DRAFt:EXTension:PORT:LOSS:VALue](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#ExtPortLossVal) [CALCulate:FSIMulator:EXTension:PORT:LOSS:VALue?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#ExtPortLossVal) | None  
Turns "loss1" or "loss2" ON/OFF | [CALCulate:FSIMulator:DRAFt:EXTension:PORT:LOSS:STATe](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#ExtPortEnd) [CALCulate:FSIMulator:EXTension:PORT:LOSS:STATe?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#ExtPortLoss) | None  
Sets media type | [CALCulate:FSIMulator:DRAFt:EXTension:PORT:MEDium](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#ExtPortMed) [CALCulate:FSIMulator:EXTension:PORT:MEDium?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#ExtPortMed) | None  
Sets waveguide cutoff frequency | [CALCulate:FSIMulator:DRAFt:EXTension:PORT:WAVEguide:FCUToff](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#ExtPortWaveFcut) [CALCulate:FSIMulator:EXTension:PORT:WAVEguide:FCUToff?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#ExtPortWaveFcut) | None  
Sets couple to system media | [CALCulate:FSIMulator:DRAFt:EXTension:PORT:WAVEguide:COUPle](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#ExtPortWaveCoup) [CALCulate:FSIMulator:EXTension:PORT:WAVEguide:COUPle?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#ExtPortWaveCoup) | None  
Sets velocity factor | [CALCulate:FSIMulator:DRAFt:EXTension:PORT:VELocity:FACtor](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#ExtPortVelFac) [CALCulate:FSIMulator:EXTension:PORT:VELocity:FACtor?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#ExtPortVelFac) | None  
Sets coupling to system velocity factor | [CALCulate:FSIMulator:DRAFt:EXTension:PORT:VELocity:COUPle](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#ExtPortVelCoup) [CALCulate:FSIMulator:EXTension:PORT:VELocity:COUPle?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#ExtPortVelCoup) | None  
Sets the port loss at DC | [CALCulate:FSIMulator:DRAFt:EXTension:PORT:DCLoss:VALue](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#ExtPortDclVAL) [CALCulate:FSIMulator:EXTension:PORT:DCLoss:VALue?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#ExtPortDclVAL) | None  
Turns port extension ON/OFF | [CALCulate:FSIMulator:DRAFt:EXTension:PORT[:STATe]](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#ExtPortStat) [CALCulate:FSIMulator:EXTension:PORT[:STATe]?](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#ExtPortStat) | None  
Moves the port extension block to the right-most side of the circuit sections | [CALCulate:FSIMulator:DRAFt:EXTension:PORT:END](GP-IB_Command_Finder/Calculate/FSimulatorDraft.md#ExtPortEnd) | None  
Apply Fixtures | ON/OFF | [CALCulate:FSIMulator:STATe](GP-IB_Command_Finder/Calculate/FSimulator.md#FSimState) | [FixturingState](COM_Reference/Properties/FixturingState_Property.md)  
Power Comp... | Port N | [CALCulate:FSIMulator:POWer:PORT:COMPensate:STATe](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#PowPortComp) | [EnablePowerCompensation](COM_Reference/Properties/EnablePowerCompensation_Property.md)  
Compensate Only For De-Embeds | [CALCulate:FSIMulator:POWer:COMPensate:MODE](GP-IB_Command_Finder/Calculate/FSimulatorActive.md#CALCulate:FSIMulator:POWer:COMPensate:MODE) | None  
Fixture Setup | Change order of operations | [CALCulate:FSIMulator:SENDed:OORDer](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#oorder) | None  
2 and 4-port Extrapolate | [CALCulate:FSIMulator:SNP:EXTRapolate](GP-IB_Command_Finder/Calculate/FSimulator.md#extrapolate) | [EnableSnPDataExtrapolation](COM_Reference/Properties/EnableSnPDataExtrapolation_Property.md)  
2-Port Fixturing  
Port matching ON and OFF | [CALCulate:FSIMulator:SENDed:PMCircuit:STATe](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#PMCState) | [PortMatchingState](COM_Reference/Properties/PortMatchingState_Property.md)  
Reverse ports | [CALCulate:FSIMulator:SENDed:DEEM:PORT<n>:SNP:REVerse](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#ReversePorts) | [Reverse2PortAdapter](COM_Reference/Properties/Reverse2PortAdapter_Property.md)  
Sets Port Matching circuit model | [CALCulate:FSIMulator:SENDed:PMCircuit:PORT:TYPE](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#pmcType) | [PortMatchingCktModel](COM_Reference/Properties/PortMatchingCktModel_Property.md)  
Sets Port Matching 'S2P' file name | [CALCulate:FSIMulator:SENDed:PMCircuit:PORT:USER:FILename](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#pmcFileName) | [strPortMatch_S2PFile](COM_Reference/Properties/strPortMatch_S2PFile_Property.md)  
Sets Capacitance 'C' value | [CALCulate:FSIMulator:SENDed:PMCircuit:PORT:PARameters:C](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#pmcC) | [PortMatching_C](COM_Reference/Properties/PortMatching_C_Property.md)  
Sets Conductance 'G' value | [CALCulate:FSIMulator:SENDed:PMCircuit:PORT:PARameters:G](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#pmcG) | [PortMatching_G](COM_Reference/Properties/PortMatching_G_Property.md)  
Sets Inductance 'L' value | [CALCulate:FSIMulator:SENDed:PMCircuit:PORT:PARameters:L](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#pmcL) | [PortMatching_L](COM_Reference/Properties/PortMatching_L_Property.md)  
Sets Resistance 'R' value | [CALCulate:FSIMulator:SENDed:PMCircuit:PORT:PARameters:R](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#pmcR) | [PortMatching_R](COM_Reference/Properties/PortMatching_R_Property.md)  
De-embed ON and OFF | [CALCulate:FSIMulator:SENDed:DEEMbed:STATe](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#DeemState) | [Port2PdeembedState](COM_Reference/Properties/Port2PdeembedState_Property.md)  
Sets De-embedding circuit model | [CALCulate:FSIMulator:SENDed:DEEMbed:PORT](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#deembedType) | [Port2PdeembedCktModel](COM_Reference/Properties/Port2PdeembedCktModel_Property.md)  
Sets De-embedding 'S2P' file name | [CALCulate:FSIMulator:SENDed:DEEM:PORT:USER:FILename](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#deembedFileName) | [strPort2Pdeembed_S2PFile](COM_Reference/Properties/strPort2Pdeembed_S2PFile_Property.md)  
Port Impedance ON and OFF | [CALCulate:FSIMulator:SENDed:ZCONversion:STATe](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#ZState) | [PortArbzState](COM_Reference/Properties/PortArbzState_Property.md)  
Port Z Real | [CALCulate:FSIMulator:SENDed:ZCONversion:PORT:REAL](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#ZReal) | [PortArbzReal](COM_Reference/Properties/PortArbzReal_Property.md)  
Port Z Imag | [CALCulate:FSIMulator:SENDed:ZCONversion:PORT:IMAG](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#ZImag) | [PortArbzImag](COM_Reference/Properties/PortArbzImag_Property.md)  
Port Z Real and Imag | [CALCulate:FSIMulator:SENDed:ZCONversion:PORT:Z0](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#ZValue) | [PortArbzZ0](COM_Reference/Properties/PortArbzZ0_Property.md)  
4-Port Network Embed/De-embed commands  
Specifies the PNA / DUT topology | [CALCulate:FSIMulator:EMBed:TYPE](GP-IB_Command_Finder/Calculate/FSimulatorEmbed.md#TopType) | [Embed4PortTopology](COM_Reference/Properties/Embed4PortTopology_Property.md)  
Specifies the 4-port touchstone file | [CALCulate:FSIMulator:EMBed:NETWork:FILename](GP-IB_Command_Finder/Calculate/FSimulatorEmbed.md#Filename) | [Embed4PortNetworkFilename](COM_Reference/Properties/Embed4PortNetworkFilename_Property.md)  
Embed|De-embed? | [CALCulate:FSIMulator:EMBed:NETWork:TYPE](GP-IB_Command_Finder/Calculate/FSimulatorEmbed.md#type) | [Embed4PortNetworkMode](COM_Reference/Properties/Embed4PortNetworkMode_Property.md)  
Specify PNA port connections | [CALCulate:FSIMulator:EMBed:TOPology:A:PORTs](GP-IB_Command_Finder/Calculate/FSimulatorEmbed.md#topA) [CALCulate:FSIMulator:EMBed:TOPology:B:PORTs](GP-IB_Command_Finder/Calculate/FSimulatorEmbed.md#topB) [CALCulate:FSIMulator:EMBed:TOPology:C:PORTs](GP-IB_Command_Finder/Calculate/FSimulatorEmbed.md#topC) [CALCulate:FSIMulator:EMBed:TOPology:D:PORTs](GP-IB_Command_Finder/Calculate/FSimulatorEmbed.md#topD) | [Embed4PortList](COM_Reference/Properties/Embed4PortList_Property.md) [SetCustomDUTTopology](COM_Reference/Methods/SetCustomDUTTopology_Method.md)  
4-port remap | [CALCulate:FSIMulator:EMBed:NETWork<n>:PMAP](GP-IB_Command_Finder/Calculate/FSimulatorEmbed.md#pmap) | [NetworkPortMap](COM_Reference/Methods/NetworkPortMap_Method.md)  
Turn ON or OFF | [CALCulate:FSIMulator:EMBed:STATe](GP-IB_Command_Finder/Calculate/FSimulatorEmbed.md#state) | [Embed4PortState](COM_Reference/Properties/Embed4PortState_Property.md)  
Differential Port Arbitrary Impedance  
Sets the impedance value | [CALCulate:FSIMulator:BAunL:DZConversion:BPORt:Z0](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#dzcR) | [DiffZConvPortZ0](COM_Reference/Properties/DiffZConvPortZ0_Property.md)  
Sets real part of impedance | [CALCulate:FSIMulator:BALun:DZConversion:BPORt:REAL](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#dzcReal) | [DiffZConvPortReal](COM_Reference/Properties/DiffZConvPortReal_Property.md)  
Sets imaginary part of impedance | [CALCulate:FSIMulator:BALun:DZConversion:BPORt:IMAG](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#dzcImag) | [DiffZConvPortImag](COM_Reference/Properties/DiffZConvPortImag_Property.md)  
Turn ON or OFF | [CALCulate:FSIMulator:BALun:DZConversion:STATe](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#dzcState) | [DiffZConvState](COM_Reference/Properties/DiffZConvState_Property.md)  
Common Mode Port Arbitrary Impedance  
Sets the impedance value | [CALCulate:FSIMulator:BALun:CZConversion:BPORt:Z0](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#CzcR) | [CmnModeZConvPortZ0](COM_Reference/Properties/CmnModeZConvPortZ0_Property.md)  
Sets real part of impedance | [CALCulate:FSIMulator:BALun:CZConversion:BPORt:REAL](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#czcReal) | [CmnModeZConvPortReal](COM_Reference/Properties/CmnModeZConvPortReal_Property.md)  
Sets imaginary part of impedance | [CALCulate:FSIMulator:BALun:CZConversion:BPORt:IMAG](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#CzcImag) | [CmnModeZConvPortImag](COM_Reference/Properties/CmnModeZConvPortImag_Property.md)  
Turn ON or OFF | [CALCulate:FSIMulator:BALun:CZConversion:STATe](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#czcState) | [CmnModeZConvState](COM_Reference/Properties/CmnModeZConvState_Property.md)  
Differential Port Matching  
Sets type of circuit to embed | [CALCulate:FSIMulator:BALun:DMCircuit:BPORt](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#dmcType) | [DiffPortMatchMode](COM_Reference/Properties/DiffPortMatchMode_Property.md)  
Specifies the 2-port touchstone file | [CALCulate:FSIMulator:BALun:DMCircuit:BPORt:USER:FILename](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#dmcFilename) | [DiffPortMatchUserFilename](COM_Reference/Properties/DiffPortMatchUserFilename_Property.md)  
Sets Capacitance value | [CALCulate:FSIMulator:BALun:DMCircuit:BPORt:PARameters:C](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#dmcParC) | [DiffPortMatch_C](COM_Reference/Properties/DiffPortMatch_C_Property.md)  
Sets Conductance value | [CALCulate:FSIMulator:BALun:DMCircuit:BPORt:PARameters:G](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#dmcParG) | [DiffPortMatch_G](COM_Reference/Properties/DiffPortMatch_G_Property.md)  
Sets Inductance value | [CALCulate:FSIMulator:BALun:DMCircuit:BPORt:PARameters:L](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#dmcParL) | [DiffPortMatch_L](COM_Reference/Properties/DiffPortMatch_L_Property.md)  
Sets Resistance value | [CALCulate:FSIMulator:BALun:DMCircuit:BPORt:PARameters:R](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#dmcParR) | [DiffPortMatch_R](COM_Reference/Properties/DiffPortMatch_R_Property.md)  
Turns ON/OFF | [CALCulate:FSIMulator:BALun:DMCircuit:STATe](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#dmcState) | [DiffPortMatchState](COM_Reference/Properties/DiffPortMatchState_Property.md)  
Remote ONLY  
Create Cal Set with De-embeded fixture removed | [CSET:FIXTure:DEEMbed](GP-IB_Command_Finder/CSET.md#deembed) | [Deembed](COM_Reference/Methods/Deembed_Method.md)  
Create Cal Set with Matching network included | [CSET:FIXTure:EMBed](GP-IB_Command_Finder/CSET.md#embed) | [Embed](COM_Reference/Methods/Embed_Method.md)  
Cal Plane Manager...  | Characterize a fixture | [CSET:FIXTure:CHARacterize](GP-IB_Command_Finder/CSET.md#fixtureCharacter) | [CharacterizeFixture](COM_Reference/Methods/CharacterizeFixture_Method.md)  
Creates a single S2P file from two existing files | [CSET:FIXTure:CASCade](GP-IB_Command_Finder/CSET.md#FIXTureCASCade) | [CascadeS2PFiles](COM_Reference/Methods/CascadeS2PFiles_Method.md)  
[Auto Fixture Removal...](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md) |  | [CSET:FIXTure:DEEMbed](GP-IB_Command_Finder/CSET.md#deembed) | [Deembed](COM_Reference/Methods/Deembed_Method.md)

