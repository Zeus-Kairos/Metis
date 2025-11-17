[File](FileTopic.md) | [Instrument](XTraceChanTopic.md) | [Response](XResponseTopic.md) | [Stimulus](XStimulusTopic.md) | [Utility](XUtilityTopic.md) | [Cal](CalTopic.md) | [Apps](MixerTopic.md) | [Remote ONLY](DataTopic.md)

* * *

Get and Put Data: [Measurement](DataTopic.md#meas) | [Cal](DataTopic.md#getCalData) | [Power Cal](DataTopic.md#Power) | [Custom](DataTopic.md#custom) | Power Range  
Other: [GPIB Pass-through](XUtilityTopic.md#passthru) | [VISA Pass-through](XUtilityTopic.md#VISA_Pass_Through) | [Capabilities](DataTopic.md#Capabilities) | [Status](DataTopic.md#Status)/[Events](DataTopic.md#Events) | [Rear-panel](DataTopic.md#rear) | [FIFO and FastCW](DataTopic.md#FIFO) | [Speed up Measurements!](XResponseTopic.md) | Ground Loop

Description | SCPI | COM  
---|---|---  
Get X-Axis values (variant) | [CALCulate:MEASure:X:VALues?](GP-IB_Command_Finder/Calculate/MeasureX.md#CALCulate:MEASure:X:VALues) | [Get X-axis Values](COM_Reference/Methods/Get_X-axis_Values_Method.md)  
Get X-Axis values (typed) | None | [Get X-Axis Values 2](COM_Reference/Methods/Get_X-Axis_Values_2.md)  
Set/get X-axis for trace | [CALCulate:MEASure:X:AXIS](GP-IB_Command_Finder/Calculate/MeasureX.md#CALCulate:MEASure:X:AXiS) | None  
Set/get the X-Axis domain | [CALCulate:MEASure:X:AXIS:DOMain](GP-IB_Command_Finder/Calculate/MeasureX.md#CALCulate:MEASure:X:AXIS:DOMain) | None  
Get X-Axis values (Meas object) | None | [Get XAxisValues](COM_Reference/Methods/Get_XAxisValues_Method.md)  
Get Measurement Data FROM the Analyzer  
Get typed complex data from the specified location. Returned in two arrays. | None | [IArrayTrans.getComplex](COM_Reference/Methods/Get_Complex_Method.md)  
Get typed NAComplex data from the specified location. Returned in one array. | None | [IArrayTrans.getNAComplex](COM_Reference/Methods/Get_NAComplex_Method.HTM)  
Get typed data pairs from the specified location. Returned in two arrays. | None | [IArrayTrans.getPairedData](COM_Reference/Methods/Get_Paired_Data_Method.md)  
Get typed scalar data from the specified location. Returned in one array. | None | [IArrayTrans.getScalar](COM_Reference/Methods/Get_Scalar_Method.md)  
Get variant data from the specified location in a SPECIFIED FORMAT. Returned in one array. | None | [meas.GetDataByString](COM_Reference/Methods/Get_DataByString_Method.md)  
Get receiver data | [CALCulate:MEASure:RDATA?](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:RDATA) | All of the above  
Specifies ASCII or REAL type for data transfers | [Format:Data](GP-IB_Command_Finder/Format_SCPI.md#fd) | None  
Get complex or formatted data from the measurement or memory result buffer | [CALCulate:MEASure:DATA](GP-IB_Command_Finder/Calculate/MeasureDATA.md#CALC:MEAS:DATA) | All of the above  
Get the formatted data array of multiple traces of the selected channel. | [CALCulate:DATA:MFData](GP-IB_Command_Finder/Calculate/Data.md#DataMfdata) | None  
Get the corrected data array of multiple traces of the selected channel. | [CALCulate:DATA:MSData](GP-IB_Command_Finder/Calculate/Data.md#DataMsdata) | None  
Gets SnP data for the specified ports. | [CALCulate:DATA:SNP:PORTs?](GP-IB_Command_Finder/Calculate/Data.md#snpReadByPort) | [GetSnpDataWithSpecifiedPorts](COM_Reference/Methods/Get_SnpDataWithSpecifiedPorts_Method.md)  
Get ALL SnP data | [CALCulate:DATA:SNP:PORTs?](GP-IB_Command_Finder/Calculate/Data.md#snpReadByPort) | [meas.GetSnPData](COM_Reference/Methods/Get_SnPData_Method.md)  
Put Measurement Data INTO the Analyzer  
Put complex data into the specified location. | None | [IArrayTrans.putComplex](COM_Reference/Methods/Put_Complex_Method.md)  
Put typed NAComplex data into the specified location. | None | [IArrayTrans.putNAComplex](COM_Reference/Methods/Put_NAComplex_Method.md)  
Put scalar data into the measurement result location. | None | [IArrayTrans.putScalar](COM_Reference/Methods/Put_Scalar_Method.md)  
Put complex Variant data into the specified location. | None | [IArrayTrans.putDataComplex](COM_Reference/Methods/Put_Data_Complex_Method.md)  
Put complex or formatted data into the measurement or memory result buffer | [CALCulate:MEASure:DATA](GP-IB_Command_Finder/Calculate/MeasureDATA.md#CALC:MEAS:DATA) | None  
Get Calibration Data FROM the Analyzer  
Get complex Error Term data | None | [Get ErrorTermComplexByString](COM_Reference/Methods/Get_ErrorTermComplexByString_Method.md)  
Get variant Error Term data | [SENSe:CORRection:CSET:DATA](GP-IB_Command_Finder/Sense/CorrCset.md#data) [CSET:ETERm[:DATA]?](GP-IB_Command_Finder/CSET.md#CSET:ETERm_:DATA) | [GetErrorTermByString](COM_Reference/Methods/Get_ErrorTermByString_Method.md)  
Get variant Error Term data by text filter | [CSET:ETERm:CATalog?](GP-IB_Command_Finder/CSET.md#CSET:ETERm:CATalog) | [Get ErrorTermList2](COM_Reference/Methods/Get_ErrorTermList2_Method.md)  
Get complex Standard data | None | [GetStandardComplexByString](COM_Reference/Methods/Get_StandardComplexByString_Method.md)  
Get variant Standard data | None | [GetStandardByString](COM_Reference/Methods/Get_StandardByString_Method.md)  
Get variant Standard data by text filter | None | [Get StandardList2](COM_Reference/Methods/Get_StandardList2_Method.md)  
Put Calibration Data INTO the Analyzer  
Put complex Error Term data | None | [PutErrorTermComplexByString](COM_Reference/Methods/Put_ErrorTermComplexByString_Method.md)  
Put variant Error Term data | [SENSe:CORRection:CSET:DATA](GP-IB_Command_Finder/Sense/CorrCset.md#data) [CSET:ETERm[:DATA]](GP-IB_Command_Finder/CSET.md#CSET:ETERm_:DATA) | [PutErrorTermByString](COM_Reference/Methods/Put_ErrorTermByString_Method.md)  
Put complex Standard data | None | [PutStandardComplexByString](COM_Reference/Methods/Put_StandardComplexByString_Method.md)  
Put variant Standard data | None | [PutStandardByString](COM_Reference/Methods/Put_StandardByString_Method.md)  
Power Calibration Data  
Get variant cal data | [SOURce:POWer:CORRection:DATA](GP-IB_Command_Finder/SourceCorrection.md#corrdata) | [Get SourcePowerCalDataEx](COM_Reference/Methods/Get_SourcePowerCalDataEx_Method.md)  
Get typed cal data | [SOURce:POWer:CORRection:DATA](GP-IB_Command_Finder/SourceCorrection.md#corrdata) | [Get SourcePowerCalDataScalarEx](COM_Reference/Methods/Get_SourcePowerCalDataScalarEx_Method.md)  
Put variant cal data | [SOURce:POWer:CORRection:DATA](GP-IB_Command_Finder/SourceCorrection.md#corrdata) | [Put SourcePowerCalDataEx](COM_Reference/Methods/Put_SourcePowerCalDataEx_Method.md)  
Put typed cal data | [SOURce:POWer:CORRection:DATA](GP-IB_Command_Finder/SourceCorrection.md#corrdata) | [Put SourcePowerCalDataScalarEx](COM_Reference/Methods/Put_SourcePowerCalDataScalarEx_Method.md)  
Get and Put Custom Measurement Data  
Get and Put Custom data | [CALCulate:MEASure:DATA](GP-IB_Command_Finder/Calculate/MeasureDATA.md#CALC:MEAS:DATA) | [IArrayTransfer2 Interface](COM_Reference/Objects/Measurement_Object.md#IArrayTransfer)  
  
Capabilities  
---  
Many queries regarding the capability of a specific PNA | [SYSTem:CAPabilities](GP-IB_Command_Finder/SystCapability.md) | [Capabilities Object](COM_Reference/Objects/Capabilities_Object.md)  
PXIe module queries | [SYSTem:CAPability:HARDware:MODule](GP-IB_Command_Finder/SystCapHardModule.md) |   
Read installed options | [*Opt?](GP-IB_Command_Finder/Common_Commands.md#opt) | [Options](COM_Reference/Properties/Options_Property.md)  
  
Power Range  
---  
Set/get list of discrete frequencies corresponding to powers | [SYSTem:CAPability:HARDware:POWer:DISCrete:FREQuency:LIST](GP-IB_Command_Finder/SystCapability.md#POWer:DISCrete:FREQuency:LIST) | [DiscreteFrequencies](COM_Reference/Properties/DiscreteFrequencies_Property.md)  
Get a single max leveled power value | [SYSTem:CAPability:HARDware:POWer:DISCrete:MAXimum?](GP-IB_Command_Finder/SystCapability.md#POWer:DISCrete:MAXimum) | [DiscreteGetMaxPower](COM_Reference/Methods/DiscreteGetMaxPower_Method.md)  
Get an array of max leveled power values | [SYSTem:CAPability:HARDware:POWer:DISCrete:MAXimum:LIST?](GP-IB_Command_Finder/SystCapability.md#POWer:DISCrete:MAXimum:LIST) | [DiscreteGetMaxPowerArray](COM_Reference/Methods/DiscreteGetMaxPowerArray_Method.md)  
Get a single minimum leveled power value | [SYSTem:CAPability:HARDware:POWer:DISCrete:MINimum?](GP-IB_Command_Finder/SystCapability.md#POWer:DISCrete:MINimum) | [DiscreteGetMinPower](COM_Reference/Methods/DiscreteGetMinPower_Method.md)  
Get an array of minimum leveled power values | [SYSTem:CAPability:HARDware:POWer:DISCrete:MINimum:LIST?](GP-IB_Command_Finder/SystCapability.md#POWer:DISCrete:MINimum:LIST) | [DiscreteGetMinPowerArray](COM_Reference/Methods/DiscreteGetMinPowerArray_Method.md)  
Set/get name of the value for the given path element name | [SYSTem:CAPability:HARDware:POWer:PATH:CONFig:ELEMent[:STATe]](GP-IB_Command_Finder/SystCapability.md#POWer:PATH:CONFig:ELEMent:STATe) | [PathElement](COM_Reference/Properties/PathElement_Property.md)  
Get all RF path element names | [SYSTem:CAPability:HARDware:POWer:PATH:CONFig:ELEMent:CATalog?](GP-IB_Command_Finder/SystCapability.md#POWer:PATH:CONFig:ELEMent:CATalog) | [PathElements](COM_Reference/Properties/PathElements_Property.md)  
Set/get port number for power data | [SYSTem:CAPability:HARDware:POWer:PORT](GP-IB_Command_Finder/SystCapability.md#HARDware:POWer:PORT) | [PortNumber](COM_Reference/Properties/PortNumber_Property.md)  
Set/get type of power range data to be returned | [SYSTem:CAPability:HARDware:POWer:TYPE](GP-IB_Command_Finder/SystCapability.md#POWer:TYPE) | [PowerRangeType](COM_Reference/Properties/PowerRangeType_Property.md)  
Get minimum of all max leveled power values | [SYSTem:CAPability:HARDware:POWer:RANGe:MAXimum?](GP-IB_Command_Finder/SystCapability.md#POWer:RANGe:MAXimum) | [RangeGetMaxPower](COM_Reference/Methods/RangeGetMaxPower_Method.md)  
Get maximum of all minimum power values | [SYSTem:CAPability:HARDware:POWer:RANGe:MINimum?](GP-IB_Command_Finder/SystCapability.md#POWer:RANGe:MINimum) | [RangeGetMinPower](COM_Reference/Methods/RangeGetMinPower_Method.md)  
Set/get lower bound of the frequency range | [SYSTem:CAPability:HARDware:POWer:RANGe:FREQuency:STARt](GP-IB_Command_Finder/SystCapability.md#POWer:RANGe:FREQuency:STARt) | [RangeStartFrequency](COM_Reference/Properties/RangeStartFrequency_\(PowerRange\)_Property.md)  
Set/get upper bound of the frequency range | [SYSTem:CAPability:HARDware:POWer:RANGe:FREQuency:STOP](GP-IB_Command_Finder/SystCapability.md#POWer:RANGe:FREQuency:STOP) | [RangeStopFrequency](COM_Reference/Properties/RangeStopFrequency_\(PowerRange\)_Property.md)  
Reset all Power Range properties to default values | [SYSTem:CAPability:HARDware:POWer:RESet](GP-IB_Command_Finder/SystCapability.md#POWer:RESet) | [Reset (Power Range)](COM_Reference/Methods/Reset_\(Power_Range\)_Method.md)  
  
Status Commands  
---  
Status Registers | [GP-IB/Status](GP-IB_Command_Finder/Status.md) | None  
*OPC;*WAI | [GP-IB/Common_Commands](GP-IB_Command_Finder/Common_Commands.md) | None  
  
Events  
---  
AllowAllEvents Method | None | [app.AllowAllEvents](COM_Reference/Methods/AllowAllEvents_Method.md)  
AllowEventCategory Method | None | [app.AllowEventCategory](COM_Reference/Methods/AllowEventCategory_Method.md)  
AllowEventMessage Method | None | [app.AllowEventMessage](COM_Reference/Methods/AllowEventMessage_Method.md)  
AllowEventSeverity Method | None | [app.AllowEventSeverity](COM_Reference/Methods/AllowEventSeverity_Method.md)  
DisallowAllEvents Method | None | [app.DisallowAllEvents](COM_Reference/Methods/DisallowAllEvents_Method.md)  
MessageText Method | None | [app.MessageText](COM_Reference/Properties/Message_Text_Method.md)  
OnCalEvent | None | [app.OnCalEvent](COM_Reference/Events/OnCalEvent.md)  
OnChannelEvent | None | [app.OnChannelEvent](COM_Reference/Events/OnChannelEvent.md)  
OnDisplayEvent | None | [app.OnDisplayEvent](COM_Reference/Events/OnDisplayEvent.md)  
OnHardwareEvent | None | [app.OnHardwareEvent](COM_Reference/Events/OnHardwareEvent.md)  
OnMeasurementEvent | None | [app.OnMeasurementEvent](COM_Reference/Events/OnMeasurementEvent.md)  
OnSCPIEvent | None | [app.OnSCPIEvent](COM_Reference/Events/OnSCPIEvent.md)  
OnSystemEvent | None | [app.OnSystemEvent](COM_Reference/Events/OnSystemEvent.md)  
OnUserEvent | None | [app.OnUserEvent](COM_Reference/Events/OnUserEvent.md)  
SetFailOnOverRange | None | [app.SetFailOnOverRange](COM_Reference/Methods/SetFailOnOverRange_Method.md)  
  
Rear Panel Connector Controls  
---  
Material Handler I/O Connector | [GP-IB/Control](GP-IB_Command_Finder/ControlHandler.md) | [MaterialHandler IO](COM_Reference/Objects/HWMaterialHandlerIO_Object.md)  
Auxiliary IO Connector | [GP-IB/Control](GP-IB_Command_Finder/ControlAux.md) | [Aux IO](COM_Reference/Objects/HWauxIO_Object.md)  
External Test Set Connector | [GP-IB/Control](GP-IB_Command_Finder/ControlExt.md) | [External Test Set](COM_Reference/Objects/HWExternalTestSetIO_Object.md)  
  
![](../assets/images/Tp.gif)

FIFO Data Buffer (N5264A Only)  
---  
FIFO ON|OFF | [SYSTem:FIFO[:STATe]](GP-IB_Command_Finder/SystFIFO.md#state) | [State](COM_Reference/Properties/State_Property.md)  
Read number of data points | [SYSTem:FIFO:DATA:COUNt?](GP-IB_Command_Finder/SystFIFO.md#DataCount) | [DataCount](COM_Reference/Properties/DataCount_Property.md)  
Read data | [SYSTem:FIFO:DATA?](GP-IB_Command_Finder/SystFIFO.md#data) | [Data](COM_Reference/Properties/Data_Property.md)  
Read data compact form | None | [DataInCompactForm](COM_Reference/Properties/DataInCompactForm_Property.md)  
Clear data | [SYSTem:FIFO:DATA:CLEar](GP-IB_Command_Finder/SystFIFO.md#clear) | [Clear](COM_Reference/Methods/Clear_fifo_Method.md)  
Returns a specific number of bytes to read | [SYST:FIFO:DATA:BYTe?](GP-IB_Command_Finder/SystFIFO.md#SYSTem:FIFO:DATA:BYTe) | [DataAsBytes](COM_Reference/Properties/DataInBytes_Property.md)  
Reads the FIFO buffer data as a Variant of a specified array size (SafeArray) of bytes. | [SYST:FIFO:DATA:BYTe:COUNt?](GP-IB_Command_Finder/SystFIFO.md#SYSTem:FIFO:DATA:BYTe:COUNt) | [DataByteCount](COM_Reference/Properties/DataByteCount_Property.md)  
Reads the FIFO buffer data as a Variant of a specified array size (SafeArray) of 32-bit floating point (Float32) numbers. |  | [DataAsFloat32](COM_Reference/Properties/DataInFloat32_Property.md)  
Reads the FIFO buffer data as a Variant of a specified array size (SafeArray) of 16-bit integers. |  | [DataAsInt16](COM_Reference/Properties/DataInInt16_Property.md)  
Reads the FIFO buffer data as a Variant of a specified array size (SafeArray) of 32-bit integers. |  | [DataAsInt32](COM_Reference/Properties/DataInInt32_Property.md)  
  
Other N5264A Commands  
---  
FastCW | [SENSe:SWEep:TYPE:FACW](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#swpTypeFASTCW) | [FastCWPointCount](COM_Reference/Properties/FastCWPointCount_Property.md)  
Enable Point Averaging | [SENSe:AVERage:MODE](GP-IB_Command_Finder/Sense/Average_SCPI.md#mode) | [AverageMode](COM_Reference/Properties/AverageMode_Property.md)  
Enable Point Sweep | [SENSe:SWEep:GENeration:POINtsweep](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#GenPoint) | [PointSweepState](COM_Reference/Properties/PointSweepState_Property.md)  
Set Trace Sweep | [SENSe:SWEep:TRIGger:MODE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#Mode) | [Trigger Mode](COM_Reference/Properties/Trigger_Mode_Property.md)  
  
Ground Loop De-embedding/Embedding commands  
---  
De-embedding |   
Sets and returns the Capacitance value | [CALCulate:FSIMulator:GLOop:DEEMbed:PARameters:C](GP-IB_Command_Finder/Calculate/FSimulatorGLoop.md#CALCulate:FSIMulator:GLOop:DEEMbed:C)  
Sets and returns the Inductance value | [CALCulate:FSIMulator:GLOop:DEEMbed:](GP-IB_Command_Finder/Calculate/FSimulatorGLoop.md#CALCulate:FSIMulator:GLOop:DEEMbed:C)[PARameters:L](GP-IB_Command_Finder/Calculate/FSimulatorGLoop.md#CALCulate:FSIMulator:GLOop:DEEMbed:C)  
Sets and returns the Resistance value | [CALCulate:FSIMulator:GLOop:DEEMbed:](GP-IB_Command_Finder/Calculate/FSimulatorGLoop.md#CALCulate:FSIMulator:GLOop:DEEMbed:R)[PARameters:R](GP-IB_Command_Finder/Calculate/FSimulatorGLoop.md#CALCulate:FSIMulator:GLOop:DEEMbed:C)  
Turns ON or OFF De-embedding | [CALCulate:FSIMulator:GLOop:DEEMbed:STATe](GP-IB_Command_Finder/Calculate/FSimulatorGLoop.md#CALCulate:FSIMulator:GLOop:DEEMbed:STATe)  
Specifies the circuit model type | [CALCulate:FSIMulator:GLOop:DEEMbed:TYPE](GP-IB_Command_Finder/Calculate/FSimulatorGLoop.md#CALCulate:FSIMulator:GLOop:DEEMbed:TYPE)  
Specifies the filename of the s1p file to load | [CALCulate:FSIMulator:GLOop:DEEMbed:USER:FILename](GP-IB_Command_Finder/Calculate/FSimulatorGLoop.md#CALCulate:FSIMulator:GLOop:DEEMbed:USER)  
Embedding |   
Sets and returns the Capacitance value | [CALCulate:FSIMulator:GLOop:EMBed:](GP-IB_Command_Finder/Calculate/FSimulatorGLoop.md#CALCulate:FSIMulator:GLOop:EMBed:C)[PARameters:C](GP-IB_Command_Finder/Calculate/FSimulatorGLoop.md#CALCulate:FSIMulator:GLOop:DEEMbed:C)  
Sets and returns the Inductance value | [CALCulate:FSIMulator:GLOop:EMBed:](GP-IB_Command_Finder/Calculate/FSimulatorGLoop.md#CALCulate:FSIMulator:GLOop:EMBed:L)[PARameters:L](GP-IB_Command_Finder/Calculate/FSimulatorGLoop.md#CALCulate:FSIMulator:GLOop:DEEMbed:C)  
Sets and returns the Resistance value | [CALCulate:FSIMulator:GLOop:EMBed:](GP-IB_Command_Finder/Calculate/FSimulatorGLoop.md#CALCulate:FSIMulator:GLOop:EMBed:R)[PARameters:R](GP-IB_Command_Finder/Calculate/FSimulatorGLoop.md#CALCulate:FSIMulator:GLOop:DEEMbed:C)  
Turns ON or OFF Embedding | [CALCulate:FSIMulator:GLOop:EMBed:STATe](GP-IB_Command_Finder/Calculate/FSimulatorGLoop.md#CALCulate:FSIMulator:GLOop:EMBed:STATe)  
Specifies the circuit model type | [CALCulate:FSIMulator:GLOop:EMBed:TYPE](GP-IB_Command_Finder/Calculate/FSimulatorGLoop.md#CALCulate:FSIMulator:GLOop:EMBed:TYPE)  
Specifies the filename of the s1p file to load | [CALCulate:FSIMulator:GLOop:EMBed:USER:FILename](GP-IB_Command_Finder/Calculate/FSimulatorGLoop.md#CALCulate:FSIMulator:GLOop:EMBed:USER)  
  
* * *

