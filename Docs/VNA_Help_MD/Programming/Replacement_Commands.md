# Superseded / Replacement Commands

* * *

As we expand the capability of the VNA, we will continue to develop new
commands. Sometimes, a command is replaced with a new command that delivers
more capability. The old (superseded) command will continue to work as usual,
but we recommend using the new (replacement) command in new code that you
develop.

In very few cases, commands become obsolete and no longer work as before.
Obsolete commands will likely NOT have a replacement.

  * [COM Obsolete Commands](Replacement_Commands.md#ComObsolete)

  * [SCPI Replacement Commands.](Replacement_Commands.md#SCPI)

  * [SCPI Obsolete Commands](Replacement_Commands.md#SCPIObsolete)

## COM Replacement Commands

Superseded Command | Replacement Command  
---|---  
[Acquire Cal Standard Method](COM_Reference/Methods/Acquire_Cal_Standard_Method.md) | [Acquire Cal Standard2 Method](COM_Reference/Methods/AcquireCalStandard2_Method.md)  
[Create SParameterEX Method](COM_Reference/Methods/Create_SParameterEX_Method.md) | [Create SParameter Method](COM_Reference/Methods/Create_SParameter_Method.md)  
[CreateCustomMeasurement Method](COM_Reference/Methods/CreateCustomMeasurement_Method.md) | [CreateCustomMeasurementEx Method](COM_Reference/Methods/CreateCustomMeasurementEx_Method.md)  
[Calibrator.getErrorTerm](COM_Reference/Methods/Get_Error_Term_Method.md) | [GetErrorTermByString_Method](COM_Reference/Methods/Get_ErrorTermByString_Method.md)  
[Calibrator.getStandard](COM_Reference/Methods/Get_Standard_Method.md) | [GetStandardByString_Method](COM_Reference/Methods/Get_StandardByString_Method.md)  
[Calibrator.putErrorTerm](COM_Reference/Methods/Put_Error_Term_Method.md) | [PutErrorTermByString_Method](COM_Reference/Methods/Put_ErrorTermByString_Method.md)  
[Calibrator.putStandard](COM_Reference/Methods/Put_Standard_Method.md) | [PutStandardByString_Method](COM_Reference/Methods/Put_StandardByString_Method.md)  
[AcquireCalConfidenceCheckECAL](COM_Reference/Methods/AcquireCalConfidenceCheckECAL.md) | [AcquireCalConfidenceCheckECALEx](COM_Reference/Methods/AcquireCalConfidenceCheckECALex_Method.md)  
[DoECAL1Port Method](COM_Reference/Methods/DoECAL1Port_Method.md) | [DoECAL1PortEx Method](COM_Reference/Methods/DoECAL1PortEx_Method.md)  
[DoECAL2Port Method](COM_Reference/Methods/DoECAL2Port_Method.md) | [DoECAL2PortEx Method](COM_Reference/Methods/DoECAL2PortEx_Method.md)  
[ECALCharacterization Property](COM_Reference/Properties/ECALCharacterization_Property.md) | [ECALCharacterizationEx Property](COM_Reference/Properties/ECALCharacterizationEx_Property.md)  
[ECALPortMap_Property](COM_Reference/Properties/ECALPortMap_Property.md) | [ECALPortMapEx_Property](COM_Reference/Properties/ECALPortMapEx_Property.md)  
[Get ECAL Module Info Method](COM_Reference/Methods/Get_ECAL_Module_Info_Method.md) | [Get ECALModuleInfoEx Method](COM_Reference/Methods/Get_ECALModuleInfoEx_Method.md)  
[IsECALModuleFound Property](COM_Reference/Properties/IsECALModuleFound_Property.md) | [IsECALModuleFoundEx Property](COM_Reference/Properties/IsECALModuleFoundEx_Property.md)  
[Trigger Signal Property](COM_Reference/Properties/Trigger_Signal_Property.md) | [Source Property](COM_Reference/Properties/Source_Property.md)  
[Trigger Type Property](COM_Reference/Properties/Trigger_Type_Property.md) | [Scope Property](COM_Reference/Properties/Scope_Property.md)  
[get SourcePowerCalData Method](COM_Reference/Methods/get_SourcePowerCalData_Method.md) | [Get SourcePowerCalDataEx Method](COM_Reference/Methods/Get_SourcePowerCalDataEx_Method.md)  
[get SourcePowerCalDataScalar Method](COM_Reference/Methods/get_SourcePowerCalDataScalar_Method.md) | [Get SourcePowerCalDataScalarEx Method](COM_Reference/Methods/Get_SourcePowerCalDataScalarEx_Method.md)  
[put SourcePowerCalData Method](COM_Reference/Methods/put_SourcePowerCalData_Method.md) | [Put SourcePowerCalDataEx Method](COM_Reference/Methods/Put_SourcePowerCalDataEx_Method.md)  
[put SourcePowerCalDataScalar Method](COM_Reference/Methods/put_SourcePowerCalDataScalar_Method.md) | [Put SourcePowerCalDataScalarEx Method](COM_Reference/Methods/Put_SourcePowerCalDataScalarEx_Method.md)  
ConfigNarrowBand Method | ConfigNarrowBand2 Method  
ConfigNarrowBand2 Method | [ConfigNarrowBand3 Method](COM_Reference/Methods/ConfigNarrowBand3_Method.md)  
[StandardForClass Property](COM_Reference/Properties/StandardForClass_Property.md) | [GetStandardForClass_Method](COM_Reference/Methods/Get_StandardForClass_Method.md) [SetStandardForClass_Method](COM_Reference/Methods/Set_StandardForClass_Method.md)  
[Port 1 Property](COM_Reference/Properties/Port_1_Property.md) | [PortDelay Property](COM_Reference/Properties/PortDelay_Property.md)  
[Port 2 Property](COM_Reference/Properties/Port_2_Property.md) | [PortDelay Property](COM_Reference/Properties/PortDelay_Property.md)  
[Port_3_Property](COM_Reference/Properties/Port_3_Property.md) | [PortDelay Property](COM_Reference/Properties/PortDelay_Property.md)  
[Normalization Property](COM_Reference/Properties/Normalization_Property.md) | [DoReceiverPowerCal Method](COM_Reference/Methods/DoReceiverPowerCal_Method.md)  
[InterpolateNormalization Property](COM_Reference/Properties/InterpolateNormalization_Property.md) | [Interpolate Correction Property](COM_Reference/Properties/Interpolate_Correction_Property.md)  
[Get ErrorTermComplex2 Method](COM_Reference/Methods/Get_ErrorTermComplex2_Method.md) | [GetErrorTermComplexByString_Method](COM_Reference/Methods/Get_ErrorTermComplexByString_Method.md)  
[Get ErrorTermList Method](COM_Reference/Methods/Get_ErrorTermList_Method.md) | [GetErrorTermList2_Method](COM_Reference/Methods/Get_ErrorTermList2_Method.md)  
[Get Standard Complex Method](COM_Reference/Methods/Get_Standard_Complex_Method.md) | [GetStandardComplexByString_Method](COM_Reference/Methods/Get_StandardComplexByString_Method.md)  
[Put ErrorTermComplex2 Method](COM_Reference/Methods/Put_ErrorTermComplex2_Method.md) | [PutErrorTermComplexByString_Method](COM_Reference/Methods/Put_ErrorTermComplexByString_Method.md)  
[Put Standard Complex Method](COM_Reference/Methods/Put_Standard_Complex_Method.md) | [PutStandardComplexByString_Method](COM_Reference/Methods/Put_StandardComplexByString_Method.md)  
[Get ErrorTerm2 Method](COM_Reference/Methods/Get_ErrorTerm2_Method.md) | [GetErrorTermByString_Method](COM_Reference/Methods/Get_ErrorTermByString_Method.md)  
[Get Standard2 Method](COM_Reference/Methods/Get_Standard2_Method.md) | [Get StandardByString_Method](COM_Reference/Methods/Get_StandardByString_Method.md)  
[Get StandardsList Method](COM_Reference/Methods/Get_StandardsList_Method.md) | [Get StandardList2_Method](COM_Reference/Methods/Get_StandardList2_Method.md)  
[Put ErrorTerm2 Method](COM_Reference/Methods/Put_ErrorTerm2_Method.md) | [PutErrorTermByString_Method](COM_Reference/Methods/Put_ErrorTermByString_Method.md)  
[Put Standard2 Method](COM_Reference/Methods/Put_Standard2_Method.md) | [PutStandardByString_Method](COM_Reference/Methods/Put_StandardByString_Method.md)  
[DataToDivisor](COM_Reference/Methods/DataToDivisor_Method.md) [LogMagnitudeOffset](COM_Reference/Properties/LogMagnitudeOffset_Property.md) [Normalization](COM_Reference/Properties/Normalization_Property.md) [InterpolateNormalization](COM_Reference/Properties/InterpolateNormalization_Property.md) | [DoReceiverPowerCal Method](COM_Reference/Methods/DoReceiverPowerCal_Method.md)  
[Save Cal Sets Method](COM_Reference/Methods/Save_CalSets_Method.md) | [Save (CalSet) Method](COM_Reference/Methods/Save_CalSet_Method.md)  
[app.Save .SNP](COM_Reference/Methods/Save_Method.md) | [WriteSnpFileWithSpecifiedPorts Method](COM_Reference/Methods/WriteSnpFileWithSpecifiedPorts_Method.md)  
[Get SnPData Method](COM_Reference/Methods/Get_SnPData_Method.md) | [Get SnpDataWithSpecifiedPorts Method](COM_Reference/Methods/Get_SnpDataWithSpecifiedPorts_Method.md)  
[AcquirePowerReadings Method](COM_Reference/Methods/AcquirePowerReadings_Method.md) | [AcquirePowerReadingsEx Method](COM_Reference/Methods/AcquirePowerReadingsEx_Method.md)  
[SetCalInfo2 (power meter) Method](COM_Reference/Methods/SetCalInfo2_\(power\)_Method.md) | [SetCalInfoEx (power meter) Method](COM_Reference/Methods/SetCalInfoEx_Method.md)  
[ThruCalMethod Property](COM_Reference/Properties/ThruCalMethod_Property.md) | [PathCalMethod Property](COM_Reference/Properties/PathCalMethod_Property.md)  
[PathThruMethod
Property](COM_Reference/Properties/PathThruMethod_Property.htm)  
[ApplyPowerCorrectionValues Method](COM_Reference/Methods/ApplyPowerCorrectionValues_Method.md) | [ApplyPowerCorrectionValuesEx Method](COM_Reference/Methods/ApplyPowerCorrectionValuesEx_Method.md)  
[PowerMeterGPIBAddress Property](COM_Reference/Properties/PowerMeterGPIBAddress_Property.md) | [PowerMeterInterface Object](COM_Reference/Objects/PowerMeterInterface_Object.md)  
[get InputVoltage Method](COM_Reference/Methods/get_InputVoltage_Method.md) | [get InputVoltageEX Method](COM_Reference/Properties/InputVoltageEX_Property.md)  
[Initialize (ECal)](COM_Reference/Methods/Initialize_ECal.md) | [InitializeEx Method](COM_Reference/Methods/InitializeEx_Method.md)  
[guided.CompatibleCalKits Property](COM_Reference/Properties/CompatibleCalKits_Property.md) | [guided.GetCompatibleCalKits Method](COM_Reference/Methods/GetCompatibleCalKits_Method.md)  
[AssignSourceToRole Method](COM_Reference/Methods/AssignSourceToRole_Method.md) | [RoleDevice Property](COM_Reference/Properties/RoleDevice_Property.md)  
[GetSourceByRole Method](COM_Reference/Methods/GetSourceByRole_Method.md) | [DefinedRoles Property](COM_Reference/Properties/DefinedRoles_Property.md)  
[GetSourceRoles Method](COM_Reference/Methods/GetSourceRoles_Method.md) | [DefinedRoles Property](COM_Reference/Properties/DefinedRoles_Property.md)  
  
## COM Obsolete Commands

|  
[Input A Property](COM_Reference/Properties/Input_A_Property.md) | No replacement  
[Input B Property](COM_Reference/Properties/Input_B_Property.md) | No replacement  
[Input_C_Property](COM_Reference/Properties/Input_C_Property.md) | No replacement  
[ECALIsolation Property](COM_Reference/Properties/ECALIsolation_Property.md) | No replacement  
[CalibrationPort Property](COM_Reference/Properties/CalibrationPort_Property.md) | No replacement  
|  
  
##

## SCPI Replacement Commands

Superseded Command | Replacement Command  
---|---  
[TRIGger[:SEQuence]:LEVel](GP-IB_Command_Finder/Trigger_SCPI.md#tssl) | [CONTrol:SIGNal](GP-IB_Command_Finder/Control.md#signal)  
[DISPlay:TILE](GP-IB_Command_Finder/Display.md#tile) | [DISP:ARRange](GP-IB_Command_Finder/Display.md#arrange)  
[CALC:CORR:OFFS:MAGN](GP-IB_Command_Finder/Calculate/Correction.md#OffsMagn) | [SENS:CORR:RPOW:OFFS](GP-IB_Command_Finder/Sense/Sense_Correction.md#RecPowerOffset)  
[CALC:NORM](GP-IB_Command_Finder/Calculate/Normalize.md#immediate) | [SENS:CORR:COLL:METH](GP-IB_Command_Finder/Sense/Sense_Correction.md#sccm) [SENS:CORR:COLL](GP-IB_Command_Finder/Sense/Sense_Correction.md#scca)  
[CALC:NORM:STAT](GP-IB_Command_Finder/Calculate/Normalize.md#state) | [SENS:CORR](GP-IB_Command_Finder/Sense/Sense_Correction.md#scs)  
[CALC:NORM:INT](GP-IB_Command_Finder/Calculate/Normalize.md#interpol) | [SENS:CORR:INT](GP-IB_Command_Finder/Sense/Sense_Correction.md#scis)  
[SENS:CORR:COLL:CKIT:RES](GP-IB_Command_Finder/Sense/CorrCollCKIT.md#scccr) | [SENS:CORR:CKIT:INITialize](GP-IB_Command_Finder/Sense/CorrCKIT_SCPI.md#initialize)  
[SENSe<ch>:MULTiplexer<id>:TSET:OUTPut[:DATA] <data>](GP-IB_Command_Finder/Sense/Multiplexer.md#outputData) | [SENSe<cnum>:MULTiplexer<id>:OUTPut[:DATa] <num>](GP-IB_Command_Finder/Sense/Multiplexer.md#outputData)  
[SENSe<ch>:MULTiplexer<id>:TSET9:PORT1 <char>](GP-IB_Command_Finder/Sense/Multiplexer.md#port1) [SENSe<ch>:MULTiplexer<id>:TSET9:PORT2 <char>](GP-IB_Command_Finder/Sense/Multiplexer.md#port2) [SENSe<ch>:MULTiplexer<id>:TSET9:PORT3 <char>](GP-IB_Command_Finder/Sense/Multiplexer.md#port3) [SENSe<ch>:MULTiplexer<id>:TSET9:PORT4 <char>](GP-IB_Command_Finder/Sense/Multiplexer.md#port4) | [SENSe<cnum>:MULTiplexer<id>:ALLPorts <char>](GP-IB_Command_Finder/Sense/Multiplexer.md#AllPorts)  
[CALC:PAR:DEF](GP-IB_Command_Finder/Calculate/Parameter.md#cpd) | [CALC:PAR:DEF:EXT](GP-IB_Command_Finder/Calculate/Parameter.md#DefineExtend)  
[CALC:PAR:MOD](GP-IB_Command_Finder/Calculate/Parameter.md#ModExtend) | [CALC:PAR:MOD:EXT](GP-IB_Command_Finder/Calculate/Parameter.md#ModExtend)  
[CALC:DATA:SNP?](GP-IB_Command_Finder/Calculate/Data.md#snp) | [CALC:DATA:SNP:PORTs](GP-IB_Command_Finder/Calculate/Data.md#snpReadByPort)  
[MMEM:STORe (snp)](GP-IB_Command_Finder/Memory.md#save) | [CALC:DATA:SNP:PORTs:SAVE](GP-IB_Command_Finder/Calculate/Data.md#snpSave)  
[SENS:SWEep:SRCPort](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#sss) | [CALC:PAR:DEF:EXT](GP-IB_Command_Finder/Calculate/Parameter.md#DefineExtend)  
[SOUR:POW:CORR:COLL:METH](GP-IB_Command_Finder/SourceCorrection.md#method) | [SOUR:POW:CORR:COLL:ACQ](GP-IB_Command_Finder/SourceCorrection.md#aquire)  
[SENSe<ch>:OFFSet:CW](GP-IB_Command_Finder/Sense/Offset_SCPI.md#Override) [SENSe<ch>:OFFSet:DIVisor](GP-IB_Command_Finder/Sense/Offset_SCPI.md#divisor) [SENSe<ch>:OFFSet:MULTiplier](GP-IB_Command_Finder/Sense/Offset_SCPI.md#mult) [SENSe<ch>:OFFSet:OFFSet](GP-IB_Command_Finder/Sense/Offset_SCPI.md#freqOffset) [SENSe<ch>:OFFSet:STARt?](GP-IB_Command_Finder/Sense/Offset_SCPI.md#start) [SENSe<ch>:OFFSet:[STATe]](GP-IB_Command_Finder/Sense/Offset_SCPI.md#state) [SENSe<ch>:OFFSet:STOP?](GP-IB_Command_Finder/Sense/Offset_SCPI.md#stop) | [SENS:FOM](GP-IB_Command_Finder/Sense/FOM.md)  
[SENSe<cnum>:POWer:ATTenuator](GP-IB_Command_Finder/Sense/Power.md) | [SOURce:POWer:ATTenuation:RECeiver:TEST](GP-IB_Command_Finder/source.md#SOURce:POWer:ATTenuation:RECeiver:TEST)  
[SENS:CORR:COLL:GUID:METH](GP-IB_Command_Finder/Sense/CorrGuided.md#gMETHod) | [SENS:CORR:COLL:GUID:PATH:CMEThod](GP-IB_Command_Finder/Sense/CorrGuided.md#PathCmethod)  
[SENS:CORR:COLL:GUID:PATH:TMEThod](GP-
IB_Command_Finder/Sense/CorrGuided.htm#PathTMethod)  
[SYST:COMM:GPIB:PMET:ADDR](GP-IB_Command_Finder/SystCommunicate.md#gpibadd) | [SYST:COMM:PSEN](GP-IB_Command_Finder/SystCommunicate.md#PSensorType)  
[SENS:SWE:TRIG:POIN](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#sstp) | [SENS:SWE:TRIG:MODE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#Mode)  
[SENS:CORR:CKIT:ECAL:INF?](GP-IB_Command_Finder/Sense/CorrCKIT_SCPI.md#ECALInf) | [SENS:CORR:CKIT:ECAL:KNAM:INF?](GP-IB_Command_Finder/Sense/CorrCKIT_SCPI.md#knameInf)  
[SENS:CORR:COLL:GUID:CKIT:PORT:CAT?](GP-IB_Command_Finder/Sense/CorrGuided.md#gKitCat) | [SENSe:CORR:COLL:GUID:CKIT:CAT?](GP-IB_Command_Finder/Sense/CorrGuided.md#ckitCatConn)  
[MMEMory:STORe:CITifile:DATA](GP-IB_Command_Finder/Memory.md#CitiData) [MMEMory:STORe:CITifile:FORMat](GP-IB_Command_Finder/Memory.md#citiFormat) [MMEMory:STORe:TRACe:FORMat:CITifile](GP-IB_Command_Finder/Memory.md#FORMATciti) [MMEMory:STORe:TRACe:CONTent:CITifile](GP-IB_Command_Finder/Memory.md#contents) | [MMEM:STOR:DATA](GP-IB_Command_Finder/Memory.md#StoreData)  
[DISP:WIND:ANN:MARK:SING](GP-IB_Command_Finder/Display.md#single) | [DISP:WIND:ANN:MARK:NUMB](GP-IB_Command_Finder/Display.md#MarkerNumber)  
[Sense:Correction:Collect:Guided:SMC](GP-IB_Command_Finder/Sense/CorrCollGuidSMC.md) | [Sense:Correction:Collect:Session:SMC](GP-IB_Command_Finder/Sense/CorrCollSessSMC.md)  
[Sense:Correction:Collect:Guided:VMC](GP-IB_Command_Finder/Sense/CorrCollGuidVMC.md) | [Sense:Correction:Collect:Session:VMC](GP-IB_Command_Finder/Sense/CorrCollSessVMC.md)  
[CALC:PAR:CAT:EXT?](GP-IB_Command_Finder/Calculate/Parameter.md#ParCatExtended) | [CALC:PAR:CATalog?](GP-IB_Command_Finder/Calculate/Parameter.md#cpc)  
[SENS:CORR:CSET:DELete](GP-IB_Command_Finder/Sense/CorrCset.md#delete) | [CSET:DEL](GP-IB_Command_Finder/CSET.md#delete)  
[SENS:CORR:CSET:CAT?](GP-IB_Command_Finder/Sense/CorrCset.md#catalog) | [CSET:CAT?](GP-IB_Command_Finder/CSET.md#CAT)  
|  
  
## SCPI Obsolete Commands  
  
[SENS:COUP](GP-IB_Command_Finder/Sense/Couple.md#alternateChop) | No replacement  
[SENS:CORR:EXT:REC](GP-IB_Command_Finder/Sense/CorrExtension.md#RecTime) | No replacement  
[SENS:CORR:ISOLation](GP-IB_Command_Finder/Sense/Sense_Correction.md#sciss) | No replacement  
[SENS:CORR:COLL:SESS:SMC:PWRC:SRCP](GP-IB_Command_Finder/Sense/CorrCollSessSMC.md#SRCPort) | No replacement  
[Calc:Data SCORR](GP-IB_Command_Finder/Calculate/Data.md#data) | [SENS:CORR:CSET:DATA](GP-IB_Command_Finder/Sense/CorrCset.md#data)  
[HCOP:ITEM:SEGData:STATe](GP-IB_Command_Finder/Hardcopy.md#segData) | No replacement  
[DISP:TOOL:MEAS](GP-IB_Command_Finder/Display.md#toolMeas) | No replacement  
[DISP:TOOL:STIM](GP-IB_Command_Finder/Display.md#toolStim) | No replacement  
[DISP:TOOL:SWEep](GP-IB_Command_Finder/Display.md#toolSweep) | No replacement  
[SENSe:SA:LO:FREQuency:VALue](GP-IB_Command_Finder/Sense/SA.md#FFT_FREQ_VALue) | [SENSe:SA:LO:FORCe:FREQuency](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:LO:FORCe:FREQuency)  
[SENSe:SA:LO:FREQuency:FORCe](GP-IB_Command_Finder/Sense/SA.md#FFTFreqMode) | [SENSe:SA:LO:FORCe[:STATe]](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:LO:FORCe:STATe)  
[SOURce:DPD:CORRection:COLLection:POWer[:FIXed]](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:CORRection:COLLection:POWer:FIXed) | [SENSe:DISTortion:SWEep:POWer:CARRier:LEVel](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:POWer:CARRier:LEVel)  
[SOURce:DPD:CORRection:COLLection:POWer:RECeiver](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:CORRection:COLLection:POWer:RECeiver) | [SENSe:DISTortion:SWEep:POWer:CARRier:LEVel:PORT](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:POWer:CARRier:LEVel:PORT)  
  
* * *

