# Setup Commands - Standard Measurement Class

Click [here](CF_Setup_Commands.md) to view links to Setup commands for all
Measurement Classes.

Main |  Layout |  [System  
Setup](CF_System_Commands.htm#System_Setup_Tab_Commands) |  Internal  
Hardware |  External  
Hardware  
---|---|---|---|---  
  
Main Tab Commands  
---  
Softkey | Sub-item | SCPI |  COM  
Sweep Setup...  | Sweep Type  
Linear Frequency | [SENSe:SWEep:TYPE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssty) |  [SweepType](COM_Reference/Properties/Sweep_Type_Property.md)  
Log Frequency | [SENSe:SWEep:TYPE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssty) |  [SweepType](COM_Reference/Properties/Sweep_Type_Property.md)  
Power Sweep | [SENSe:SWEep:TYPE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssty) |  [SweepType](COM_Reference/Properties/Sweep_Type_Property.md)  
CW Time | [SENSe:SWEep:TYPE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssty) |  [SweepType](COM_Reference/Properties/Sweep_Type_Property.md)  
Segment Sweep | [SENSe:SWEep:TYPE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssty) |  [SweepType](COM_Reference/Properties/Sweep_Type_Property.md)  
Phase Sweep | [SENSe:SWEep:TYPE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssty) |  [SweepType](COM_Reference/Properties/Sweep_Type_Property.md)  
Sweep Properties  
Start | [SENSe:FREQuency:STARt](GP-IB_Command_Finder/Sense/Frequency.md#start) |  [StartFrequency](COM_Reference/Properties/Start_Frequency_Property.md)  
Stop | [SENSe:FREQuency:STOP](GP-IB_Command_Finder/Sense/Frequency.md#stop) |  [StopFrequency](COM_Reference/Properties/Stop_Frequency_Property.md)  
Power | [SOURce:POWer[:LEVel][:IMMediate][:AMPLitude]](GP-IB_Command_Finder/source.md#pwrval) |  [TestPortPower](COM_Reference/Properties/Test_Port_Power_Property.md)  
Points | [SENSe:SWEep:POINts](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssp) |  [NumberOfPoints](COM_Reference/Properties/Number_of__Points_Property.md)  
IF Bandwidth | [SENSe:BWIDth[:RESolution]](GP-IB_Command_Finder/Sense/Sense_Bandwidth.md#res) |  [IFBandwidth](COM_Reference/Properties/IF_Bandwidth_Property.md)  
Start Power | [SOURce:POWer:STARt](GP-IB_Command_Finder/source.md#start) |  [chan.StartPower](COM_Reference/Properties/Start_Power_Property.md)  
Stop Power | [SOURce:POWer:STOP](GP-IB_Command_Finder/source.md#stop) |  [chan.StopPower](COM_Reference/Properties/Stop_Power_Property.md)  
CW Freq | [SENSe:FREQuency[:CW]](GP-IB_Command_Finder/Sense/Frequency.md#cw) |  [CWFrequency](COM_Reference/Properties/CW_Frequency_Property.md)  
Segment Table  
X-axis Point Spacing | [SENSe:SEGMent:X:SPACing](GP-IB_Command_Finder/Sense/Segment.md#X AXIS) |  [chan.XAxisPointSpacing](COM_Reference/Properties/XAxisPointSpacing_Property.md)  
Allow arbitrary Segments | [SENSe:SEGMent:ARBitrary](GP-IB_Command_Finder/Sense/Segment.md#arb) |  [segs.AllowArbitrarySegments](COM_Reference/Properties/AllowArbitrarySegments_Property.md)  
Display Center/Span Freq | [SENSe:SEGMent:FREQuency:CENTer](GP-IB_Command_Finder/Sense/Segment.md#cent) [SENSe:SEGMent:FREQuency:SPAN](GP-IB_Command_Finder/Sense/Segment.md#span) |  [chan.centerFrequency](COM_Reference/Properties/CenterFreq_Property.md) [chan.FrequencySpan](COM_Reference/Properties/Frequency_Span_Property.md)  
Timing  
Sweep Time | [SENSe:SWEep:TIME](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#sst) |  [SweepTime](COM_Reference/Properties/Sweep_Time_Property.md)  
Dwell Time | [SENSe:SWEep:DWELl](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssd) |  [DwellTime](COM_Reference/Properties/Dwell_Time_Property.md)  
Sweep Delay | [SENSe:SWEep:DWELl:SDELay](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#SweepDelay) |  [SweepDelay](COM_Reference/Properties/Sweep_Delay_Property.md)  
Auto Sweep Time | [SENSe:SWEep:TIME:AUTO](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssta) |  [SweepTime](COM_Reference/Properties/Sweep_Time_Property.md)  
Fast Sweep - Reduce settling time | [SENSe:SWEep:SPEed](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#SweepSpeed) |  [SweepSpeedMode](COM_Reference/Properties/SweepSpeedMode_Property.md)  
Sweep Mode | [SENSe:SWEep:GENeration](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssg) |  [SweepGenerationMode](COM_Reference/Properties/Sweep_Generation_Mode_Property.md)  
Sweep Sequence | [SENSe:SWEep:GENeration:POINtsweep](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#GenPoint) |  [PointSweepState](COM_Reference/Properties/PointSweepState_Property.md)  
Meas Class... |  | [CALCulate:MEASure:DEFine](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:DEFine) |  [CreateCustomMeasurementEx](COM_Reference/Methods/CreateCustomMeasurementEx_Method.md)  
Quick Start... | S-Param | [CALCulate:MEASure:PARameter](GP-IB_Command_Finder/Calculate/MeasurePARameter.md#CALCulate:MEASure:PARameter) |  [CreateSParameterEx](COM_Reference/Methods/Create_SParameterEX_Method.md)  
Balanced | [CALCulate:MEASure:PARameter](GP-IB_Command_Finder/Calculate/MeasurePARameter.md#CALCulate:MEASure:PARameter) |  [BalSMeasurement](COM_Reference/Properties/BalSMeasurement_Property.md) [BBalMeasurement](COM_Reference/Properties/BBalMeasurement_Property.md) [SBalMeasurement](COM_Reference/Properties/SBalMeasurement_Property.md) [SSBMeasurement](COM_Reference/Properties/SSBMeasurement_Property.md)  
Other | [CALCulate:MEASure:PARameter](GP-IB_Command_Finder/Calculate/MeasurePARameter.md#CALCulate:MEASure:PARameter) |  [CreateSParameterEx](COM_Reference/Methods/Create_SParameterEX_Method.md)  
Layout Tab Commands  
Softkey | Sub-item | SCPI |  COM  
New Trace |  | [DISPlay:WINDow:TRACe[:STATe]](GP-IB_Command_Finder/Display.md#tstat) |  [View](COM_Reference/Properties/View_Property.md)  
New Channel |  | None |  [chans.Add](COM_Reference/Methods/Add_channels_Method.md)  
New Window |  | [DISPlay:WINDow[:STATe]](GP-IB_Command_Finder/Display.md#dwstat) |  [Add](COM_Reference/Methods/Add_NAWindows_Method.md)  
New Sheet |  | [DISPlay:SHEet:STATe](GP-IB_Command_Finder/Display.md#SheetState) |  None  
Delete | TrN | [DISPlay:WINDow:TRACe:DELete](GP-IB_Command_Finder/Display.md#tdel) |  None  
ChN | [SYSTem:CHANnels:DELete](GP-IB_Command_Finder/System.md#ChanDelete) |  [RemoveChannelNumber](COM_Reference/Methods/RemoveChannelNumber_Method.md)  
WinN | [DISPlay:WINDow[:STATe]](GP-IB_Command_Finder/Display.md#dwstat) |  [Add](COM_Reference/Methods/Add_NAWindows_Method.md)  
Select | TrN | [DISPlay:WINDow:TRACe:SELect](GP-IB_Command_Finder/Display.md#tselect) |  None  
ChN | None |  None  
WinN | [DISPlay:WINDow:TRACe:SELect](GP-IB_Command_Finder/Display.md#tselect) |  None  
Measure... | S-Parameter | [CALCulate:MEASure:PARameter](GP-IB_Command_Finder/Calculate/MeasurePARameter.md#CALCulate:MEASure:PARameter) |  [CreateSParameterEx](COM_Reference/Methods/Create_SParameterEX_Method.md)  
Balanced | [CALCulate:MEASure:PARameter](GP-IB_Command_Finder/Calculate/MeasurePARameter.md#CALCulate:MEASure:PARameter) |  [BalSMeasurement](COM_Reference/Properties/BalSMeasurement_Property.md) [BBalMeasurement](COM_Reference/Properties/BBalMeasurement_Property.md) [SBalMeasurement](COM_Reference/Properties/SBalMeasurement_Property.md) [SSBMeasurement](COM_Reference/Properties/SSBMeasurement_Property.md)  
Receivers | [CALCulate:MEASure:PARameter](GP-IB_Command_Finder/Calculate/MeasurePARameter.md#CALCulate:MEASure:PARameter) |  [CreateSParameterEx](COM_Reference/Methods/Create_SParameterEX_Method.md)  
Meas Class... |  | [CALCulate:MEASure:DEFine](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:DEFine) |  [CreateCustomMeasurementEx](COM_Reference/Methods/CreateCustomMeasurementEx_Method.md)  
Internal Hardware Tab Commands  
Softkey | Sub-item | SCPI |  COM  
RF Path Config... |  | [SENSe:PATH:CONFig:ELEMent[:STATe]](GP-IB_Command_Finder/Sense/Path.md#state) |  [Element](COM_Reference/Properties/Element_Property.md)  
IF Path Config... |  | [SENSe:PATH:CONFig:ELEMent[:STATe]](GP-IB_Command_Finder/Sense/Path.md#state) |  [Element](COM_Reference/Properties/Element_Property.md)  
Mechanical Devices... | [Trigger...](CF_Trigger_Commands.md#Trigger) |  |   
Interface Control... |  Enable Interface Control |  [CONTrol:CHANnel:INTerface:CONTrol[:STATe]](GP-IB_Command_Finder/Control.md#InterfaceState) |  [IC.State](COM_Reference/Properties/State_Property.md)  
Channel |  None |  None  
Channel Control Label |  None |  None  
Before Sweep Start  
Enable Control |  None |  None  
Handler I/O Control |  [CONTrol:HANDler[:DATA]](GP-IB_Command_Finder/ControlHandler.md#handdata) |  None  
Test Set I/O Control (addr. data) |  [CONTrol:EXTernal:TESTset:DATa](GP-IB_Command_Finder/ControlExt.md#data) |  None  
Dwell After Command |  None |  None  
Aux I/O Output Voltage |  [CONTrol:AUXiliary:OUTPut:VOLTage](GP-IB_Command_Finder/ControlAux.md#output) |  [put_OutputVoltage](COM_Reference/Methods/put_OutputVoltageMode_Method.md)  
After Sweep End  
Enable Control |  None |  None  
Handler I/O Control |  [CONTrol:HANDler[:DATA]](GP-IB_Command_Finder/ControlHandler.md#handdata) |  None  
Test Set I/O Control (addr. data) |  [CONTrol:EXTernal:TESTset:DATa](GP-IB_Command_Finder/ControlExt.md#data) |  None  
Dwell After Command |  None |  None  
Aux I/O Output Voltage |  [CONTrol:AUXiliary:OUTPut:VOLTage](GP-IB_Command_Finder/ControlAux.md#output) |  [put_OutputVoltage](COM_Reference/Methods/put_OutputVoltageMode_Method.md)  
Reset All |  [CALCulate:MEASure:DELete:ALL](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:DELete:ALL) |  None  
Save |  None |  None  
Recall |  [CONTrol:CHANnel:INTerface:CONTrol:CONFig:RECall[:STATe]](GP-IB_Command_Finder/Control.md#InterfaceRecall) |  [IC.ConfigurationFile](COM_Reference/Properties/ConfigurationFile_Property.md)  
Reference... |  Auto-select Reference |  [SENSe:ROSCillator:CONT:AUTO](GP-IB_Command_Finder/Sense/Roscillator.md#SENSe:ROSCillator:CONT:AUTO) |  None  
Reference In |  [SENSe:ROSCillator:EXTernal:FREQuency](GP-IB_Command_Finder/Sense/Roscillator.md#SENSe:ROSCillator:EXTernal:FREQuency) |  None  
Internal/External |  [SENSe:ROSCillator:SOURce](GP-IB_Command_Finder/Sense/Roscillator.md#SENSe:ROSCillator:SOURce) [SENSe:ROSCilator:SOURce:CATalog](GP-IB_Command_Finder/Sense/Roscillator.md#catalog) |  None  
Reference Out |  [SENSe:ROSCillator:OUTPut:FREQuency](GP-IB_Command_Finder/Sense/Roscillator.md#SENSe:ROSCillator:EXTernal:FREQuency) |  None  
LF Extension |  | [SENSe:SWEep:LFEXtension:STATe](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#SENSe:SWEep:LFEXtension:STATe) | [LowFrequencyExtension](COM_Reference/Properties/LowFrequencyExtension_Property.md)  
External Hardware Tab Commands  
Softkey |  Sub-item |  SCPI |  COM  
External Device... |  New |  [SYSTem:CONFigure:EDEVice:ADD](GP-IB_Command_Finder/SystConfigExternalDevice.md#Add) |  [Add (External Device)](COM_Reference/Methods/Add_External_Device_Method.md)  
Remove |  [SYSTem:CONFigure:EDEVice:REMove](GP-IB_Command_Finder/SystConfigExternalDevice.md#Remove) |  [Remove](COM_Reference/Methods/Remove_Method.md)  
Name |  [SYSTem:CONFigure:EDEVice:ADD](GP-IB_Command_Finder/SystConfigExternalDevice.md#Add) |  [Add (External Device)](COM_Reference/Methods/Add_External_Device_Method.md)  
Device Type |  [SYSTem:CONFigure:EDEVice:DTYPe](GP-IB_Command_Finder/SystConfigExternalDevice.md#DTYPe) |  [DeviceType](COM_Reference/Properties/DeviceType_Property.md)  
Driver |  [SYSTem:CONFigure:EDEVice:DRIVer](GP-IB_Command_Finder/SystConfigExternalDevice.md#Driver) |  [Driver](COM_Reference/Properties/Driver_Property.md)  
Active - Show in UI |  [SYSTem:CONFigure:EDEVice:STATe](GP-IB_Command_Finder/SystConfigExternalDevice.md#State) |  [Active](COM_Reference/Properties/Active_ExtDev_Property.md)  
Device Properties...  
DC Meter  
Timeout |  None |  None  
Dwell Before Sweep |  [SYSTem:CONFigure:EDEVice:DC:DSWeep](GP-IB_Command_Finder/SystConfigExtDC.md#DwellSweep) |  [SweepDwell](COM_Reference/Properties/SweepDwell_Property.md)  
Dwell After Point Set |  [SYSTem:CONFigure:EDEVice:DC:DPOint](GP-IB_Command_Finder/SystConfigExtDC.md#DwellPoint) |  [PointDwell](COM_Reference/Properties/PointDwell_Property.md)  
Type |  [SYSTem:CONFigure:EDEVice:DC:TYPE](GP-IB_Command_Finder/SystConfigExtDC.md#TYPE) |  [DCType](COM_Reference/Properties/DCType_Property.md)  
Receiver Correction On |  [SYSTem:CONFigure:EDEVice:DC:CORRection](GP-IB_Command_Finder/SystConfigExtDC.md#CorrectionState) |  [DCCorrection](COM_Reference/Properties/DCCorrection_Property.md)  
Offset |  [SYSTem:CONFigure:EDEVice:DC:OFFSet](GP-IB_Command_Finder/SystConfigExtDC.md#offset) |  [DCOffset](COM_Reference/Properties/DCOffset_Property.md)  
Scaling |  [SYSTem:CONFigure:EDEVice:DC:SCALe](GP-IB_Command_Finder/SystConfigExtDC.md#scale) |  [DCScale](COM_Reference/Properties/DCScale_Property.md)  
Edit Commands... |  |   
ID Query |  [SYSTem:CONFigure:EDEVice:DC:QUERy:ID](GP-IB_Command_Finder/SystConfigExtDC.md#SYSTem:CONFigure:EDEVice:DC:QUERy:ID) |  [IDQuery](COM_Reference/Properties/IDQuery_Property.md)  
Error Query |  [SYSTem:CONFigure:EDEVice:DC:QUERy:ERRor](GP-IB_Command_Finder/SystConfigExtDC.md#SYSTem:CONFigure:EDEVice:DC:QUERy:ERRor) |  [ErrorQuery](COM_Reference/Properties/ErrorQuery_Property.md)  
Enable I/O |  [SYSTem:CONFigure:EDEVice:DC:COMMand:INIT](GP-IB_Command_Finder/SystConfigExtDC.md#SYSTem:CONFigure:EDEVice:DC:COMMand:INIT) |  [InitCmd](COM_Reference/Properties/InitCmd_Property.md)  
Disable I/O |  [SYSTem:CONFigure:EDEVice:DC:COMMand:EXIT](GP-IB_Command_Finder/SystConfigExtDC.md#SYSTem:CONFigure:EDEVice:DC:COMMand:EXIT) |  [ExitCmd](COM_Reference/Properties/ExitCmd_Property.md)  
Before Sweep |  [SYSTem:CONFigure:EDEVice:DC:COMMand:SWEep:BEFore](GP-IB_Command_Finder/SystConfigExtDC.md#SYSTem:CONFigure:EDEVice:DC:COMMand:SWEep:BEFore) |  [BeforeSweepCmd](COM_Reference/Properties/BeforeSweepCmd_Property.md)  
After Sweep |  [SYSTem:CONFigure:EDEVice:DC:COMMand:SWEep:AFTer](GP-IB_Command_Finder/SystConfigExtDC.md#SYSTem:CONFigure:EDEVice:DC:COMMand:SWEep:AFTer) |  [AfterSweepCmd](COM_Reference/Properties/AfterSweepCmd_Property.md)  
Abort Sweep |  [SYSTem:CONFigure:EDEVice:DC:COMMand:SWEep:ABORt](GP-IB_Command_Finder/SystConfigExtDC.md#SYSTem:CONFigure:EDEVice:DC:COMMand:SWEep:ABORt) |  [AbortSweepCmd](COM_Reference/Properties/AbortSweepCmd_Property.md)  
Point Set Commands |  [SYSTem:CONFigure:EDEVice:DC:COMMand:POINt:SET](GP-IB_Command_Finder/SystConfigExtDC.md#SYSTem:CONFigure:EDEVice:DC:COMMand:POINt:SET) |  [PointCmd](COM_Reference/Properties/PointCmd_Property.md)  
DC Source  
Timeout |  None |  None  
Dwell Before Sweep |  [SYSTem:CONFigure:EDEVice:DC:DSWeep](GP-IB_Command_Finder/SystConfigExtDC.md#DwellSweep) |  [SweepDwell](COM_Reference/Properties/SweepDwell_Property.md)  
Dwell After Point Set |  [SYSTem:CONFigure:EDEVice:DC:DPOint](GP-IB_Command_Finder/SystConfigExtDC.md#DwellPoint) |  [PointDwell](COM_Reference/Properties/PointDwell_Property.md)  
Type |  [SYSTem:CONFigure:EDEVice:DC:TYPE](GP-IB_Command_Finder/SystConfigExtDC.md#TYPE) |  [DCType](COM_Reference/Properties/DCType_Property.md)  
|  [SYSTem:CONFigure:EDEVice:DC:LIMit:CURRent](GP-IB_Command_Finder/SystConfigExtDC.md#SYSTem:CONFigure:EDEVice:DC:LIMit:CURRent) |  [CurrentLimit](COM_Reference/Properties/CurrentLimit.md)  
|  [SYSTem:CONFigure:EDEVice:DC:LIMit:VOLTage](GP-IB_Command_Finder/SystConfigExtDC.md#SYSTem:CONFigure:EDEVice:DC:LIMit:VOLTage) |  [VoltageLimit](COM_Reference/Properties/VoltageLimit.md)  
Edit Commands... |  |   
ID Query |  [SYSTem:CONFigure:EDEVice:DC:QUERy:ID](GP-IB_Command_Finder/SystConfigExtDC.md#SYSTem:CONFigure:EDEVice:DC:QUERy:ID) |  [IDQuery](COM_Reference/Properties/IDQuery_Property.md)  
Error Query |  [SYSTem:CONFigure:EDEVice:DC:QUERy:ERRor](GP-IB_Command_Finder/SystConfigExtDC.md#SYSTem:CONFigure:EDEVice:DC:QUERy:ERRor) |  [ErrorQuery](COM_Reference/Properties/ErrorQuery_Property.md)  
Enable I/O |  [SYSTem:CONFigure:EDEVice:DC:COMMand:INIT](GP-IB_Command_Finder/SystConfigExtDC.md#SYSTem:CONFigure:EDEVice:DC:COMMand:INIT) |  [InitCmd](COM_Reference/Properties/InitCmd_Property.md)  
Disable I/O |  [SYSTem:CONFigure:EDEVice:DC:COMMand:EXIT](GP-IB_Command_Finder/SystConfigExtDC.md#SYSTem:CONFigure:EDEVice:DC:COMMand:EXIT) |  [ExitCmd](COM_Reference/Properties/ExitCmd_Property.md)  
Read Max Using |  [SYSTem:CONFigure:EDEVice:DC:MAX:VALue](GP-IB_Command_Finder/SystConfigExtDC.md#SYSTem:CONFigure:EDEVice:DC:MAX:VALue) |  [MaxOutput](COM_Reference/Properties/MaxOutput_Property.md)  
Define Max As |  [SYSTem:CONFigure:EDEVice:DC:MAX[:STATe]](GP-IB_Command_Finder/SystConfigExtDC.md#SYSTem:CONFigure:EDEVice:DC:MAX_:STATe) [SYSTem:CONFigure:EDEVice:DC:MAX:VALue](GP-IB_Command_Finder/SystConfigExtDC.md#SYSTem:CONFigure:EDEVice:DC:MAX:VALue) |  [MaxOutputState](COM_Reference/Properties/MaxOutputState_Property.md) [MaxOutput](COM_Reference/Properties/MaxOutput_Property.md)  
Read Min Using |  [SYSTem:CONFigure:EDEVice:DC:MIN:VALue](GP-IB_Command_Finder/SystConfigExtDC.md#SYSTem:CONFigure:EDEVice:DC:MIN:VALue) |  [MinOutput](COM_Reference/Properties/MinOutput_Property.md)  
Define Min As |  [SYSTem:CONFigure:EDEVice:DC:MIN[:STATe]](GP-IB_Command_Finder/SystConfigExtDC.md#SYSTem:CONFigure:EDEVice:DC:MIN_:STATe) [SYSTem:CONFigure:EDEVice:DC:MIN:VALue](GP-IB_Command_Finder/SystConfigExtDC.md#SYSTem:CONFigure:EDEVice:DC:MIN:VALue) |  [MinOutputState](COM_Reference/Properties/MinOutputState_Property.md) [MinOutput](COM_Reference/Properties/MinOutput_Property.md)  
Before Sweep |  [SYSTem:CONFigure:EDEVice:DC:COMMand:SWEep:BEFore](GP-IB_Command_Finder/SystConfigExtDC.md#SYSTem:CONFigure:EDEVice:DC:COMMand:SWEep:BEFore) |  [BeforeSweepCmd](COM_Reference/Properties/BeforeSweepCmd_Property.md)  
After Sweep |  [SYSTem:CONFigure:EDEVice:DC:COMMand:SWEep:AFTer](GP-IB_Command_Finder/SystConfigExtDC.md#SYSTem:CONFigure:EDEVice:DC:COMMand:SWEep:AFTer) |  [AfterSweepCmd](COM_Reference/Properties/AfterSweepCmd_Property.md)  
Abort Sweep |  [SYSTem:CONFigure:EDEVice:DC:COMMand:SWEep:ABORt](GP-IB_Command_Finder/SystConfigExtDC.md#SYSTem:CONFigure:EDEVice:DC:COMMand:SWEep:ABORt) |  [AbortSweepCmd](COM_Reference/Properties/AbortSweepCmd_Property.md)  
Point Set Commands |  [SYSTem:CONFigure:EDEVice:DC:COMMand:POINt:SET](GP-IB_Command_Finder/SystConfigExtDC.md#SYSTem:CONFigure:EDEVice:DC:COMMand:POINt:SET) |  [PointCmd](COM_Reference/Properties/PointCmd_Property.md)  
Hybrid Source  
Input Source Carrier Frequency |  [SYSTem:CONFigure:EDEVice:SOURce:HYBRid:INPut:FREQuency:CARRier](GP-IB_Command_Finder/SystConfigExternalDevice.md#HYBR:INP:FREQ:CARR) |  None  
Input Multiplier |  [SYSTem:CONFigure:EDEVice:SOURce:HYBRid:INPut:FREQuency:MULTiplier](GP-IB_Command_Finder/SystConfigExternalDevice.md#HYBR:INP:FREQ:MULT) |  None  
Input Source Name |  [SYSTem:CONFigure:EDEVice:SOURce:HYBRid:INPut:NAME](GP-IB_Command_Finder/SystConfigExternalDevice.md#HYBR:INP:NAME) |  None  
Input Source Power Limit |  [SYSTem:CONFigure:EDEVice:SOURce:HYBRid:INPut:POWer:LIMit](GP-IB_Command_Finder/SystConfigExternalDevice.md#HYBR:INP:POW:LIM) |  None  
Enable Pulse (Input) |  [SYSTem:CONFigure:EDEVice:SOURce:HYBRid:INPut:PULSe:ENABle](GP-IB_Command_Finder/SystConfigExternalDevice.md#HYBR:INP:PULS:ENAB) |  None  
LO Multiplier |  [SYSTem:CONFigure:EDEVice:SOURce:HYBRid:LO:FREQuency:MULTiplier](GP-IB_Command_Finder/SystConfigExternalDevice.md#HYBR:LO:FREQ:MULT) |  None  
LO Source Name |  [SYSTem:CONFigure:EDEVice:SOURce:HYBRid:LO:NAME](GP-IB_Command_Finder/SystConfigExternalDevice.md#HYBR:LO:NAME) |  None  
LO Power |  [SYSTem:CONFigure:EDEVice:SOURce:HYBRid:LO:POWer](GP-IB_Command_Finder/SystConfigExternalDevice.md#HYBR:LO:POWer) |  None  
Enable Pulse (LO) |  [SYSTem:CONFigure:EDEVice:SOURce:HYBRid:LO:PULSe:ENABle](GP-IB_Command_Finder/SystConfigExternalDevice.md#HYBR:LO:PULS:ENAB) |  None  
Lock Dependent Sources |  [SYSTem:CONFigure:EDEVice:SOURce:HYBRid:LOCK:STATe](GP-IB_Command_Finder/SystConfigExternalDevice.md#HYBR:LOCK:STAT) |  None  
Freq Max (SSB Mixer) |  [SYSTem:CONFigure:EDEVice:SOURce:HYBRid:OUTPut:FREQuency:MAX](GP-IB_Command_Finder/SystConfigExternalDevice.md#HYBR:OUTP:FREQ:MAX) |  None  
Freq Min (SSB Mixer) |  [SYSTem:CONFigure:EDEVice:SOURce:HYBRid:OUTPut:FREQuency:MIN](GP-IB_Command_Finder/SystConfigExternalDevice.md#HYBR:OUTP:FREQ:MIN) |  None  
Gain (SSB Mixer) |  [SYSTem:CONFigure:EDEVice:SOURce:HYBRid:OUTPut:GAIN](GP-IB_Command_Finder/SystConfigExternalDevice.md#HYBR:OUTP:GAIN) |  None  
Equation (SSB Mixer) |  [SYSTem:CONFigure:EDEVice:SOURce:HYBRid:OUTPut:MIXer:SIDeband](GP-IB_Command_Finder/SystConfigExternalDevice.md#HYBR:OUTP:MIX:SID) |  None  
Hybrid Type |  [SYSTem:CONFigure:EDEVice:SOURce:HYBRid:TYPE](GP-IB_Command_Finder/SystConfigExternalDevice.md#HYBR:TYPE) |  None  
Power Meter  
Sensor A/B |  None |  [PowerMeterChannel](COM_Reference/Properties/PowerMeterChannel_Property.md)  
Tolerance |  [SOURce:POWer:CORRection:COLLect:AVERage:NTOLerance](GP-IB_Command_Finder/SourceCorrection.md#averTol) |  [ReadingsTolerance](COM_Reference/Properties/ReadingsTolerance_Property.md)  
Max Number of Readings |  [SOURce:POWer:CORRection:COLLect:AVERerage:COUNt](GP-IB_Command_Finder/SourceCorrection.md#average) |  [ReadingsPerPoint](COM_Reference/Properties/ReadingsPerPoint_Property.md)  
Use Loss Table |  [SOURce:POWer:CORRection:COLLect:TABLe:LOSS](GP-IB_Command_Finder/SourceCorrection.md#tloss) [SOURce:POWer:CORRection:COLLect:TABLe:SELect](GP-IB_Command_Finder/SourceCorrection.md#tselect) |  [UsePowerLossSegments](COM_Reference/Properties/UsePowerLossSegments_Property.md) [CalFactorSegments Collection](COM_Reference/Objects/CalFactorSegments_Collection.md)  
Edit Table |  [SOURce:POWer:CORRection:COLLect:TABLe:POINts?](GP-IB_Command_Finder/SourceCorrection.md#points) [SOURce:POWer:CORRection:COLLect:TABLe:FREQuency](GP-IB_Command_Finder/SourceCorrection.md#RWfreq) [SOURce:POWer:CORRection:COLLect:TABLe:DATA](GP-IB_Command_Finder/SourceCorrection.md#tdata) |  [Count](COM_Reference/Properties/Count_Property.md) [Frequency](COM_Reference/Properties/Frequency_Property.md) [Loss](COM_Reference/Properties/Loss_sourceCal_Property.md) [SegmentNumber](COM_Reference/Properties/Segment_Number_Property.md) [Add](COM_Reference/Methods/Add_PowerLossSegment_Method.md)  
Uncertainty... |  [SYSTem:CONFigure:EDEVice:PMAR:UNCertainty:CATalog?](GP-IB_Command_Finder/SystConfigExtPMAR.md#SYSTem:CONFigure:EDEVice:PMAR:UNC:CAT) [SYSTem:CONFigure:EDEVice:PMAR:UNCertainty:FILE](GP-IB_Command_Finder/SystConfigExtPMAR.md#SYSTem:CONFigure:EDEVice:PMAR:UNC:FILE) [SYSTem:CONFigure:EDEVice:PMAR:UNCertainty:MODel](GP-IB_Command_Finder/SystConfigExtPMAR.md#SYSTem:CONFigure:EDEVice:PMAR:UNC:MOD) [SYSTem:CONFigure:EDEVice:PMAR:UNCertainty:PLEVel?](GP-IB_Command_Finder/SystConfigExtPMAR.md#SYSTem:CONFigure:EDEVice:PMAR:UNCertainty:PLEVel) [SYSTem:CONFigure:EDEVice:PMAR:UNCertainty:READ?](GP-IB_Command_Finder/SystConfigExtPMAR.md#SYSTem:CONFigure:EDEVice:PMAR:UNCertainty:READ) |  [UncertaintyModelCatalog](COM_Reference/Properties/UncertaintyModelCatalog_Property.md) [UncertaintyFile](COM_Reference/Properties/UncertaintyFile_Property.md) [UncertaintyModel](COM_Reference/Properties/UncertaintyModel_Property.md) [PowerForBestAccuracy](COM_Reference/Properties/PowerForBestAccuracy_Property.md) [PowerMtrReadingUncertainty](COM_Reference/Properties/PowerMtrReadingUncertainty_Property.md)  
Pulse Generator  
Time out |  [SYSTem:CONFigure:EDEVice:TOUT](GP-IB_Command_Finder/SystConfigExternalDevice.md#Tout) |  [TimeOut](COM_Reference/Properties/TimeOut_Property.md)  
Primary Mode |  [SYSTem:CONFigure:EDEVice:PULSe:PMODe](GP-IB_Command_Finder/SystConfigExtPulseGen.md#Mmode) |  [PrimaryMode](COM_Reference/Properties/MasterMode_Property.md)  
Output |  [SYSTem:CONFigure:EDEVice:PULSe:CHAN](GP-IB_Command_Finder/SystConfigExtPulseGen.md#chan) |  [OutputChannel](COM_Reference/Properties/OutputChannel_Property.md)  
High |  [SYSTem:CONFigure:EDEVice:PULSe:HAMP](GP-IB_Command_Finder/SystConfigExtPulseGen.md#hamp) |  [HighAmplitude](COM_Reference/Properties/HighAmplitude_Property.md)  
Low |  [SYSTem:CONFigure:EDEVice:PULSe:LAMP](GP-IB_Command_Finder/SystConfigExtPulseGen.md#lamp) |  [LowAmplitude](COM_Reference/Properties/LowAmplitude_Property.md)  
Source Imp |  [SYSTem:CONFigure:EDEVice:PULSe:SIMP](GP-IB_Command_Finder/SystConfigExtPulseGen.md#simp) |  [SourceImpedance](COM_Reference/Properties/SourceImpedance_Property.md)  
Load Imp |  [SYSTem:CONFigure:EDEVice:PULSe:LIMP](GP-IB_Command_Finder/SystConfigExtPulseGen.md#limp) |  [LoadImpedance](COM_Reference/Properties/LoadImpedance_Property.md)  
SMU  
Setup |  |   
Chan N |  [SYSTem:CONFigure:EDEVice:ADD](GP-IB_Command_Finder/SystConfigExternalDevice.md#Add) |  [Add (External Device)](COM_Reference/Methods/Add_External_Device_Method.md)  
Trigger Mode |  [SYSTem:CONFigure:EDEVice:SOURce:TMODe](GP-IB_Command_Finder/SystConfigExternalDevice.md#ESourceTMODE) |  [TriggerMode](COM_Reference/Properties/TriggerMode_ExtDev_Property.md)  
SMU Trigger In |  |  [TriggerInPin](COM_Reference/Properties/TriggerInPin_Property.md)  
SMU Trigger Out |  |  [TriggerPort](COM_Reference/Properties/TriggerPort_Property.md)  
Source/Voltage Meter/Current Meter |  |   
SMU Chan |  [SYSTem:CONFigure:EDEVice:IOENable](GP-IB_Command_Finder/SystConfigExternalDevice.md#IOEnable) [SYSTem:CONFigure:EDEVice:SMU:CHANnel[1-4]:STATe](GP-IB_Command_Finder/SystConfigExternalDevice.md#SYSTem:CONFigure:EDEVice:SMU:CHANnel:STATe) |  [IOEnable](COM_Reference/Properties/IOEnable_Property.md) [ChanActive](COM_Reference/Properties/ChanActive_Property.md)  
Source type |  [SYSTem:CONFigure:EDEVice:DC:TYPE](GP-IB_Command_Finder/SystConfigExtDC.md#TYPE) |  [DCType](COM_Reference/Properties/DCType_Property.md)  
Timeout |  [SYSTem:CONFigure:EDEVice:TOUT](GP-IB_Command_Finder/SystConfigExternalDevice.md#Tout) |  [TimeOut](COM_Reference/Properties/TimeOut_Property.md)  
Dwell Before Sweep |  [SYSTem:CONFigure:EDEVice:DC:DSWeep](GP-IB_Command_Finder/SystConfigExtDC.md#DwellSweep) |  [SweepDwell](COM_Reference/Properties/SweepDwell_Property.md)  
Dwell After Point Set |  [SYSTem:CONFigure:EDEVice:DC:DPOint](GP-IB_Command_Finder/SystConfigExtDC.md#DwellPoint) |  [PointDwell](COM_Reference/Properties/PointDwell_Property.md)  
Current Limit |  [SYSTem:CONFigure:EDEVice:DC:LIMit:CURRent](GP-IB_Command_Finder/SystConfigExtDC.md#SYSTem:CONFigure:EDEVice:DC:LIMit:CURRent) |  [CurrentLimit](COM_Reference/Properties/CurrentLimit.md)  
Voltage Limit |  [SYSTem:CONFigure:EDEVice:DC:LIMit:VOLTage](GP-IB_Command_Finder/SystConfigExtDC.md#SYSTem:CONFigure:EDEVice:DC:LIMit:VOLTage) |  [VoltageLimit](COM_Reference/Properties/VoltageLimit.md)  
Source Correction On |  [SYSTem:CONFigure:EDEVice:DC:CORRection](GP-IB_Command_Finder/SystConfigExtDC.md#CorrectionState) |  [DCCorrection](COM_Reference/Properties/DCCorrection_Property.md)  
Offset |  [SYSTem:CONFigure:EDEVice:DC:OFFSet](GP-IB_Command_Finder/SystConfigExtDC.md#offset) |  [DCOffset](COM_Reference/Properties/DCOffset_Property.md)  
Scaling |  [SYSTem:CONFigure:EDEVice:DC:SCALe](GP-IB_Command_Finder/SystConfigExtDC.md#scale) |  [DCScale](COM_Reference/Properties/DCScale_Property.md)  
Receiver Correction On |  [SYSTem:CONFigure:EDEVice:DC:CORRection](GP-IB_Command_Finder/SystConfigExtDC.md#CorrectionState) |  [DCCorrection](COM_Reference/Properties/DCCorrection_Property.md)  
Edit Commands - DC Source |  |   
Edit Commands - DC Meter |  |   
Source  
Enable Output  
(multi-channel sources) |  [SYSTem:CONFigure:EDEVice:CHANnel<cnum>:BASE](GP-IB_Command_Finder/SystConfigExternalDevice.md#CHANnel_BASE) [SYSTem:CONFigure:EDEVice:CHANnel<cnum>:COUNt](GP-IB_Command_Finder/SystConfigExternalDevice.md#CHANnel_COUNt) [SYSTem:CONFigure:EDEVice:CHANnel<cnum>:NAME](GP-IB_Command_Finder/SystConfigExternalDevice.md#CHANnel_NAME) [SYSTem:CONFigure:EDEVice:CHANnel<cnum>:NUMBer](GP-IB_Command_Finder/SystConfigExternalDevice.md#CHANnel_NUMBer) [SYSTem:CONFigure:EDEVice:CHANnel<cnum>[:STATe]](GP-IB_Command_Finder/SystConfigExternalDevice.md#CHANnel_STATe) [SYSTem:CONFigure:EDEVice:CHANnel:SYNC](GP-IB_Command_Finder/SystConfigExternalDevice.md#CHANnel_SYNC) |  None  
Timeout |  [SYSTem:CONFigure:EDEVice:TOUT](GP-IB_Command_Finder/SystConfigExternalDevice.md#Tout) |  [TimeOut](COM_Reference/Properties/TimeOut_Property.md)  
Dwell Per Point |  [SYSTem:CONFigure:EDEVice:SOURce:DPP](GP-IB_Command_Finder/SystConfigExternalDevice.md#ESourceDPP) |  [DwellPerPoint](COM_Reference/Properties/DwellPerPoint_Property.md)  
Enable Modulation Control |  [SYSTem:CONFigure:EDEVice:SOURce:MODulation:CONTrol[:STATe]](GP-IB_Command_Finder/SystConfigExternalDevice.md#SYSTem:CONFigure:EDEVice:SOURce:MODulation:CONTrol:STATe) |  [EnableModulationControl](COM_Reference/Properties/EnableModulationControl_Property.md)  
Trigger Mode |  [SYSTem:CONFigure:EDEVice:SOURce:TMODe](GP-IB_Command_Finder/SystConfigExternalDevice.md#ESourceTMODE) |  [TriggerMode](COM_Reference/Properties/TriggerMode_ExtDev_Property.md)  
Trigger Port |  [SYSTem:CONFigure:EDEVice:SOURce:TPORt](GP-IB_Command_Finder/SystConfigExternalDevice.md#ESourceTport) |  [TriggerPort](COM_Reference/Properties/TriggerPort_Property.md)  
Edit Commands... |  |   
Operation complete (*OPC) |  None |  None  
Preset |  None |  None  
Set CW Frequency |  None |  None  
Set CW Sweep Mode |  None |  None  
Set Power |  None |  None  
Set Power State |  None |  None  
Power Meter Setup... |  Interface |  [SYSTem:COMMunicate:GPIB:PMETer:CATalog?](GP-IB_Command_Finder/SystCommunicate.md#SYSTem:COMMunicate:GPIB:PMETer:CATalog) [SYSTem:COMMunicate:USB:PMETer:CATalog?](GP-IB_Command_Finder/SystCommunicate.md#USBList) |  None  
Sensors |  [SYSTem:CONFigure:EDEVice:PMAR:SENSor](GP-IB_Command_Finder/SystConfigExtPMAR.md#pmarSens) |  [SensorIndex](COM_Reference/Properties/SensorIndex_Property.md)  
Tolerance |  [SYSTem:CONFigure:EDEVice:PMAR:READing:NTOLerance](GP-IB_Command_Finder/SystConfigExtPMAR.md#pmarReadNtol) |  [ReadingsTolerance](COM_Reference/Properties/ReadingsTolerance_Property.md)  
Max Number of Readings |  [SYSTem:CONFigure:EDEVice:PMAR:READing:COUNt](GP-IB_Command_Finder/SystConfigExtPMAR.md#pmarReadCount) |  [ReadingsPerPoint](COM_Reference/Properties/ReadingsPerPoint_Property.md)  
Use Loss Table |  [SYSTem:CONFigure:EDEVice:PMAR:TABle:LOSS:DATA](GP-IB_Command_Finder/SystConfigExtPMAR.md#pmarLossData) |  [Loss](COM_Reference/Properties/Loss_sourceCal_Property.md)  
Edit Table |  [SYSTem:CONFigure:EDEVice:PMAR:TABle:LOSS:DATA](GP-IB_Command_Finder/SystConfigExtPMAR.md#pmarLossData) |  [Loss](COM_Reference/Properties/Loss_sourceCal_Property.md)  
External Testset... |  Select ID |  [SENSe:MULTiplexer:OUTPut[:DATa]](GP-IB_Command_Finder/Sense/Multiplexer.md#TSOutputData) |  [ControlLines](COM_Reference/Properties/ControlLines_Property.md)  
Test Set |  [SENSe:MULTiplexer:TYPe](GP-IB_Command_Finder/Sense/Multiplexer.md#type) [SENSe:MULTiplexer:ADDRess](GP-IB_Command_Finder/Sense/Multiplexer.md#address) |  [ts.Add](COM_Reference/Methods/Add_Testset_Method.md)  
Enable Test Set Control |  None |  None  
Show Test Set Properties |  None |  None  
Port Control |  [SENSe:MULTiplexer:PORT:SELect](GP-IB_Command_Finder/Sense/Multiplexer.md#PortSelect) |  [ts.SelectPort](COM_Reference/Properties/SelectPort_Property.md)  
Control Lines |  [SENSe:MULTiplexer:OUTPut[:DATa]](GP-IB_Command_Finder/Sense/Multiplexer.md#TSOutputData) |  [ControlLines](COM_Reference/Properties/ControlLines_Property.md)  
Line X |  None |  None  
DC Source |  [SCPI Commands](GP-IB_Command_Finder/SystConfigExtDC.md) |  [COM Commands](COM_Reference/Objects/ExternalDCDevice_Object.md)  
(E5092A only) |  [CONTrol:MULTiplexer Commands](GP-IB_Command_Finder/Control_Multiplexer.md) |  None  
Multiport | Testset | [SENSe:MULTiplexer:TYPe](GP-IB_Command_Finder/Sense/Multiplexer.md#type) |  [ts.Add](COM_Reference/Methods/Add_Testset_Method.md)  
Address/ID | [SENSe:MULTiplexer:ADDRess](GP-IB_Command_Finder/Sense/Multiplexer.md#address) |  None  
Restart as a standalone PNA | [SYSTem:CONFigure](GP-IB_Command_Finder/System.md#config) |  [app.Configure](COM_Reference/Methods/Configure_Method.md)  
Restart as a multiport PNA with this testset | [SYSTem:CONFigure](GP-IB_Command_Finder/System.md#config) |  [app.Configure](COM_Reference/Methods/Configure_Method.md)  
port count = | [SENSe:MULTiplexer:COUNt?](GP-IB_Command_Finder/Sense/Multiplexer.md#count) |  None  
Millimeter Config... (See Supported Applications) | Select Configuration | [SYSTem:CONFigure:MWAVe:CONFigure:ACTive](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:CONFiguration:ADD) [SYSTem:CONFigure:MWAVe:CONFigure:CATalog?](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:CONFiguration:CATalog) | None  
New | [SYSTem:CONFigure:MWAVe:CONFigure:ADD](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:CONFiguration:ADD) | None  
Remove | [SYSTem:CONFigure:MWAVe:CONFigure:REMove](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:CONFiguration:REMove) | None  
Multiplier RF IN | [SYSTem:CONFigure:MWAVe:FREQuency:RF:MULTiplier](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:FREQuency:RF:MULTiplier) | None  
Multiplier LO IN | [SYSTem:CONFigure:MWAVe:FREQuency:LO:MULTiplier](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:FREQuency:LO:MULTiplier) | None  
Test Port Frequency | [SYSTem:CONFigure:MWAVe:FREQuency:STARt](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:FREQuency:STARt) [SYSTem:CONFigure:MWAVe:FREQuency:STOP](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:FREQuency:STOP) | None  
Name | [SYSTem:CONFigure:MWAVe:CONFigure:ACTive](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:CONFiguration:ADD) | None  
Test Set | [SYSTem:CONFigure:MWAVe:TSET:NAME](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:TSET:NAME) [SYSTem:CONFigure:MWAVe:TSET:CATalog?](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:TSET:CATalog) | None  
Enable Modules | [SYSTem:CONFigure:MWAVe:TSET:PORT](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:TSET:PORT) [SYSTem:CONFigure:MWAVe:TSET:PORT:COUNt?](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:TSET:PORT:COUNt) | None  
Mixer Mode | [SYSTem:CONFigure:MWAVe:TSET:MIXer](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:TSET:MIXer) | None  
Module IF Gain | None | None  
Test Set IF Switch settings for Channel N | [SYSTem:CONFigure:MWAVe:TSET:RPANel](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:TSET:RPANel) | None  
Enable Test Set RF ALC | [SYSTem:CONFigure:MWAVe:TSET:ALC](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:TSET:ALC) | None  
Max Power limit at Module RF IN | [SYSTem:CONFigure:MWAVe:TSET:POWer:LIMit](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:TSET:POWer:LIMit) | None  
Offset | [SYSTem:CONFigure:MWAVe:TSET:POWer:OFFSet](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:TSET:POWer:OFFSet) | None  
Slope | [SYSTem:CONFigure:MWAVe:TSET:POWer:SLOPe](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:TSET:POWer:SLOPe) | None  
PNA RF Source... | [SYSTem:CONFigure:MWAVe:FREQuency:RF:SOURce](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:FREQuency:RF:SOURce) | None  
RF Start | [SYSTem:CONFigure:MWAVe:FREQuency:RF:STARt?](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:FREQuency:RF:STARt) | None  
RF Stop | [SYSTem:CONFigure:MWAVe:FREQuency:RF:STOP?](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:FREQuency:RF:STOP) | None  
PNA LO Source... | [SYSTem:CONFigure:MWAVe:FREQuency:LO:SOURce](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:FREQuency:LO:SOURce) | None  
LO Start | [SYSTem:CONFigure:MWAVe:FREQuency:LO:STARt?](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:FREQuency:LO:STARt) | None  
LO Stop | [SYSTem:CONFigure:MWAVe:FREQuency:LO:STOP?](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:FREQuency:LO:STOP) | None  
Return the model number of the active test set. | [SYSTem:CONFigure:MWAVe:CONF:ACTive:MODel?](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:CONF:ACTive:MODel) | None  
Return the option number of the active test set. | [SYSTem:CONFigure:MWAVe:CONF:ACTive:OPTion?](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:CONF:ACTive:OPTion) | None  
Return the model number of the frequency extender module connected to the specified port number. | [SYSTem:CONFigure:MWAVe:CONF:ACTive:PORT{1:4}:MODel?](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:CONF:ACTive:PORT:MODel) | None  
Return the option number of the frequency extender module connected to the specified port number. | [SYSTem:CONFigure:MWAVe:CONF:ACTive:PORT{1:4}:OPTion?](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:CONF:ACTive:PORT:OPTion) | None  
Read serial number of frequency extender module connected to specified port. | [SYSTem:CONFigure:MWAVe:CONF:ACTive:PORT{1:4}:SERial?](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:CONF:ACTive:PORT:SERial) | None  
Read serial number of active test set. | [SYSTem:CONFigure:MWAVe:CONF:ACTive:SERial?](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:CONF:ACTive:SERial) | None

