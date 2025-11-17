# Setup Commands - Scalar Mixer/Converter \+ Phase Measurement Class

Only the Main and Layout Setup commands corresponding to the Scalar
Mixer/Converter \+ Phase measurement class are documented here. All other
commands are identical to the Setup commands for the Standard measurement
class and can be accessed by clicking [here](CF_Setup_Commands_-_Standard.md)
or by clicking on the softtabs on the graphic below.

Click [here](CF_Setup_Commands.md) to view links to Setup commands for all
Measurement Classes.

Main | Layout | [System  
Setup](CF_System_Commands.htm#System_Setup_Tab_Commands) | [Internal  
Hardware](CF_Setup_Commands_-_Standard.htm#Internal_Hardware_Commands) | [External  
Hardware](CF_Setup_Commands_-_Standard.htm#External_Hardware_Commands)  
---|---|---|---|---  
Main Tab Commands  
---  
Softkey | Sub-item | SCPI | COM  
SMC Setup... | Sweep  
Sweep Type  
Linear Frequency | [SENSe:SWEep:TYPE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssty) | [SweepType](COM_Reference/Properties/Sweep_Type_Property.md)  
CW Time | [SENSe:SWEep:TYPE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssty) | [SweepType](COM_Reference/Properties/Sweep_Type_Property.md)  
Segment Sweep | [SENSe:SWEep:TYPE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssty) | [SweepType](COM_Reference/Properties/Sweep_Type_Property.md)  
Power | [SENSe:SWEep:TYPE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssty) | [SweepType](COM_Reference/Properties/Sweep_Type_Property.md)  
X-Axis Point Spacing | [SENSe:SEGMent:X:SPACing](GP-IB_Command_Finder/Sense/Segment.md#X AXIS) | [XAxisPointSpacing](COM_Reference/Properties/XAxisPointSpacing_Property.md)  
Reversed Port 2 Coupler | [SENSe:MIXer:REVerse](GP-IB_Command_Finder/Sense/MIXerSCPI.md#Reverse) | [IncludeReverseSweep](COM_Reference/Properties/IncludeReverseSweep_Property.md)  
Number of Points | [SENSe:SWEep:POINts](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssp) | [NumberOfPoints](COM_Reference/Properties/Number_of__Points_Property.md)  
IF Bandwidth | [SENSe:BWIDth[:RESolution]](GP-IB_Command_Finder/Sense/Sense_Bandwidth.md#res) | [IFBandwidth](COM_Reference/Properties/IF_Bandwidth_Property.md)  
Phase Reference Point  
Enable Phase | [SENSe:MIXer:PHASe](GP-IB_Command_Finder/Sense/MIXerSCPI.md#Phase) | [EnablePhase](COM_Reference/Properties/EnablePhase_Property.md)  
Normalize First Point | [SENSe:MIXer:NORMalize](GP-IB_Command_Finder/Sense/MIXerSCPI.md#Normalize) | [NormalizePoint](COM_Reference/Properties/NormalizePoint_Property.md)  
Normalize Middle Point | [SENSe:MIXer:NORMalize](GP-IB_Command_Finder/Sense/MIXerSCPI.md#Normalize) | [NormalizePoint](COM_Reference/Properties/NormalizePoint_Property.md)  
Normalize Last Point | [SENSe:MIXer:NORMalize](GP-IB_Command_Finder/Sense/MIXerSCPI.md#Normalize) | [NormalizePoint](COM_Reference/Properties/NormalizePoint_Property.md)  
Specify Normalized Point | [SENSe:MIXer:NORMalize](GP-IB_Command_Finder/Sense/MIXerSCPI.md#Normalize) | [NormalizePoint](COM_Reference/Properties/NormalizePoint_Property.md)  
Use Absolute Phase (requires internal source as LO) | [SENSe:MIXer:PHASe:ABSolute[:STATe]](GP-IB_Command_Finder/Sense/MIXerSCPI.md#SENSe:MIXer:PHASe:ABSolute:STATe) | None  
Power  
Power On (All Channels) | [OUTPut[:STATe]](GP-IB_Command_Finder/Output.md#RFOUt) | [SourcePowerState](COM_Reference/Properties/Source_Power_State_Property.md)  
Port Powers Coupled | [SOURce:POWer:COUPle](GP-IB_Command_Finder/source.md#cplON) | [CouplePorts](COM_Reference/Properties/Couple_Ports_Property.md)  
DUT Input Port  
Input Port | [SENSe:MIXer:PMAP](GP-IB_Command_Finder/Sense/MIXerSCPI.md#pmap) | [SetDutPorts](COM_Reference/Methods/SetDutPorts_Method.md)  
Power Level | [SOURce:POWer[:LEVel][:IMMediate][:AMPLitude]](GP-IB_Command_Finder/source.md#pwrval) | [InputLinearPowerLevel](COM_Reference/Properties/InputLinearPowerLevel_Property.md)  
Source Leveling Mode | [SOURce:POWer:ALC[:MODE]](GP-IB_Command_Finder/source.md#ALCMode) | [ALCLevelingMode](COM_Reference/Properties/ALCLevelingMode_Property.md)  
DUT Output Port  
Output Port | [SENSe:MIXer:PMAP](GP-IB_Command_Finder/Sense/MIXerSCPI.md#pmap) | [SetDutPorts](COM_Reference/Methods/SetDutPorts_Method.md)  
Power Level | [SOURce:POWer[:LEVel][:IMMediate][:AMPLitude]](GP-IB_Command_Finder/source.md#pwrval) | [InputLinearPowerLevel](COM_Reference/Properties/InputLinearPowerLevel_Property.md)  
Source Leveling Mode | [SOURce:POWer:ALC[:MODE]](GP-IB_Command_Finder/source.md#ALCMode) | [ALCLevelingMode](COM_Reference/Properties/ALCLevelingMode_Property.md)  
DUT Input Port Power Sweep  
Start Power | [SOURce:POWer:PORT:STARt](GP-IB_Command_Finder/source.md#PortStart) | [StartPowerEx](COM_Reference/Properties/StartPowerEx_Property.md)  
Stop Power | [SOURce:POWer:PORT:STOP](GP-IB_Command_Finder/source.md#PortStop) | [StopPowerEx](COM_Reference/Properties/StopPowerEx_Property.md)  
Points | None | None  
Power Step | None | None  
DUT Output Port Power Sweep  
Start Power | [SOURce:POWer:PORT:STARt](GP-IB_Command_Finder/source.md#PortStart) | [StartPowerEx](COM_Reference/Properties/StartPowerEx_Property.md)  
Stop Power | [SOURce:POWer:PORT:STOP](GP-IB_Command_Finder/source.md#PortStop) | [StopPowerEx](COM_Reference/Properties/StopPowerEx_Property.md)  
|  | [Element](COM_Reference/Properties/Element_Property.md)  
Mixer Frequency  
Input | [SENSe:MIXer:CALCulate](GP-IB_Command_Finder/Sense/MIXerSCPI.md#calc) | [Calculate](COM_Reference/Methods/Calculate_Method.md)  
LO1 | [SENSe:MIXer:LO:FREQuency:FIXed](GP-IB_Command_Finder/Sense/MIXerSCPI.md#LO_FIX) | [LOFixedFrequency](COM_Reference/Properties/LOFixedFrequency_Property.md)  
Input > LO | [SENSe:MIXer:LO:FREQuency:ILTI](GP-IB_Command_Finder/Sense/MIXerSCPI.md#ilti) | [IsInputGreaterThanLO](COM_Reference/Properties/InputIsGreaterThanLO_Property.md)  
IF Start | [SENSe:MIXer:IF:FREQuency:STARt](GP-IB_Command_Finder/Sense/MIXerSCPI.md#IF_START) | [IFStartFrequency](COM_Reference/Properties/IFStartFrequency_Property.md)  
IF Stop | [SENSe:MIXer:IF:FREQuency:STOP](GP-IB_Command_Finder/Sense/MIXerSCPI.md#IF_STOP) | [IFStopFrequency_Property](COM_Reference/Properties/IFStopFrequency_Property.md)  
Output | [SENSe:MIXer:CALCulate](GP-IB_Command_Finder/Sense/MIXerSCPI.md#calc) | [Calculate](COM_Reference/Methods/Calculate_Method.md)  
Mixer Power  
Power On (All Channels) | [OUTPut[:STATe]](GP-IB_Command_Finder/Output.md#RFOUt) | [SourcePowerState](COM_Reference/Properties/Source_Power_State_Property.md)  
LO1 Power | [SENSe:MIXer:LO:POWer](GP-IB_Command_Finder/Sense/MIXerSCPI.md#LO_POWer) | [LOPower](COM_Reference/Properties/LOPower_Property.md)  
LO2 Power | [SENSe:MIXer:LO:POWer](GP-IB_Command_Finder/Sense/MIXerSCPI.md#LO_POWer) | [LOPower](COM_Reference/Properties/LOPower_Property.md)  
Source Attenuator | [SOURce:POWer:ATTenuation](GP-IB_Command_Finder/source.md#attval) | [chan.Attenuator](COM_Reference/Properties/Attenuator_Property.md)  
Receiver Attenuator | [SENSe:POWer:ATTenuator](GP-IB_Command_Finder/Sense/Power.md) | [chan.ReceiverAttenuator](COM_Reference/Properties/Receiver_Attenuator_Property.md)  
LO1 Swept Power  
Start | [SENSe:MIXer:LO:FREQuency:STARt](GP-IB_Command_Finder/Sense/MIXerSCPI.md#LO_Start) | [LOStartFrequency](COM_Reference/Properties/LOStartFrequency_Property.md)  
Stop | [SENSe:MIXer:LO:FREQuency:STOP](GP-IB_Command_Finder/Sense/MIXerSCPI.md#LO_stop) | [LOStopFrequency](COM_Reference/Properties/LOStopFrequency_Property.md)  
Step | None | None  
LO2 Swept Power  
Start | [SENSe:MIXer:LO:FREQuency:STARt](GP-IB_Command_Finder/Sense/MIXerSCPI.md#LO_Start) | [LOStartFrequency](COM_Reference/Properties/LOStartFrequency_Property.md)  
Stop | [SENSe:MIXer:LO:FREQuency:STOP](GP-IB_Command_Finder/Sense/MIXerSCPI.md#LO_stop) | [LOStopFrequency](COM_Reference/Properties/LOStopFrequency_Property.md)  
Step | None | None  
Path Configuration... | [SENSe:PATH:CONFig:ELEMent[:STATe]](GP-IB_Command_Finder/Sense/Path.md#state) | [Element](COM_Reference/Properties/Element_Property.md)  
Mixer Setup  
Converter Stages | [SENSe:MIXer:STAGe](GP-IB_Command_Finder/Sense/MIXerSCPI.md#Stage) | [LOStage](COM_Reference/Properties/LOStage_Property.md)  
Add Source... | [SENSe:ROLE:DEVice](GP-IB_Command_Finder/Sense/Role.md#Device) | [AssignSourceToRole](COM_Reference/Methods/AssignSourceToRole_Method.md)  
Path Configuration... | [SENSe:PATH:CONFig:ELEMent[:STATe]](GP-IB_Command_Finder/Sense/Path.md#state) | [Element](COM_Reference/Properties/Element_Property.md)  
Enable Embedded LO See[ Embedded LO Setup commands](CF_Sweep_Commands_-_SMC.md#Embedded_LO) | [SENSe:MIXer:LO:FREQuency:MODE](GP-IB_Command_Finder/Sense/MIXerSCPI.md#LoMode) | [LORangeMode](COM_Reference/Properties/LORangeMode_cv_Property.md)  
Port Input/Output | [SENSe:MIXer:PMAP](GP-IB_Command_Finder/Sense/MIXerSCPI.md#pmap) | [SetDutPorts](COM_Reference/Methods/SetDutPorts_Method.md)  
Input Numerator Frac.Mult  | [SENSe:MIXer:INPut:FREQuency:NUMerator](GP-IB_Command_Finder/Sense/MIXerSCPI.md#INPut_NUM) | [InputNumerator](COM_Reference/Properties/InputNumerator_Property.md)  
Input Denominator Frac.Mult  | [SENSe:MIXer:INPut:FREQuency:DENominator](GP-IB_Command_Finder/Sense/MIXerSCPI.md#INPut_DEN) | [InputDenominator](COM_Reference/Properties/InputDenominator_Property.md)  
LOx | [SENSe:MIXer:LO:NAME](GP-IB_Command_Finder/Sense/MIXerSCPI.md#name) | [LOName](COM_Reference/Properties/LOName_Property.md)  
LO Numerator Frac. Mult.  | [SENSe:MIXer:LO:FREQuency:NUMerator](GP-IB_Command_Finder/Sense/MIXerSCPI.md#LO_NUM) | [LONumerator](COM_Reference/Properties/LONumerator_Property.md)  
LO Denominator Frac.Mult  | [SENSe:MIXer:LO:FREQuency:DENominator](GP-IB_Command_Finder/Sense/MIXerSCPI.md#LO_DEN) | [LODenominator](COM_Reference/Properties/LODenominator_Property.md)  
Save... | [SENSe:MIXer:SAVE](GP-IB_Command_Finder/Sense/MIXerSCPI.md#Save) | [SaveFile](COM_Reference/Methods/SaveFile_Method.md)  
Load... | [SENSe:MIXer:LOAD](GP-IB_Command_Finder/Sense/MIXerSCPI.md#Load) | [LoadFile](COM_Reference/Methods/LoadFile_Method.md)  
Meas Class... |  | [CALCulate:MEASure:DEFine](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:DEFine) | [CreateCustomMeasurementEx](COM_Reference/Methods/CreateCustomMeasurementEx_Method.md)  
Quick Start... | S-Param | [CALCulate:MEASure:PARameter](GP-IB_Command_Finder/Calculate/MeasurePARameter.md#CALCulate:MEASure:PARameter) | [CreateSParameterEx](COM_Reference/Methods/Create_SParameterEX_Method.md)  
Balanced | [CALCulate:MEASure:PARameter](GP-IB_Command_Finder/Calculate/MeasurePARameter.md#CALCulate:MEASure:PARameter) | [BalSMeasurement](COM_Reference/Properties/BalSMeasurement_Property.md) [BBalMeasurement](COM_Reference/Properties/BBalMeasurement_Property.md) [SBalMeasurement](COM_Reference/Properties/SBalMeasurement_Property.md) [SSBMeasurement](COM_Reference/Properties/SSBMeasurement_Property.md)  
Other | [CALCulate:MEASure:PARameter](GP-IB_Command_Finder/Calculate/MeasurePARameter.md#CALCulate:MEASure:PARameter) | [CreateSParameterEx](COM_Reference/Methods/Create_SParameterEX_Method.md)  
Layout Tab Commands  
Softkey | Sub-item | SCPI | COM  
New Trace |  | [DISPlay:WINDow:TRACe[:STATe]](GP-IB_Command_Finder/Display.md#tstat) | [View](COM_Reference/Properties/View_Property.md)  
New Channel |  | None | [chans.Add](COM_Reference/Methods/Add_channels_Method.md)  
New Window |  | [DISPlay:WINDow[:STATe]](GP-IB_Command_Finder/Display.md#dwstat) | [Add](COM_Reference/Methods/Add_NAWindows_Method.md)  
New Sheet |  | [DISPlay:SHEet:STATe](GP-IB_Command_Finder/Display.md#SheetState) | None  
Delete | TrN | [DISPlay:WINDow:TRACe:DELete](GP-IB_Command_Finder/Display.md#tdel) | None  
ChN | [SYSTem:CHANnels:DELete](GP-IB_Command_Finder/System.md#ChanDelete) | [RemoveChannelNumber](COM_Reference/Methods/RemoveChannelNumber_Method.md)  
WinN | [DISPlay:WINDow[:STATe]](GP-IB_Command_Finder/Display.md#dwstat) | [Add](COM_Reference/Methods/Add_NAWindows_Method.md)  
Select | TrN | [DISPlay:WINDow:TRACe:SELect](GP-IB_Command_Finder/Display.md#tselect) | None  
ChN | None | None  
WinN | [DISPlay:WINDow:TRACe:SELect](GP-IB_Command_Finder/Display.md#tselect) | None  
Measure... |  | [CALCulate:MEASure:PARameter](GP-IB_Command_Finder/Calculate/MeasurePARameter.md#CALCulate:MEASure:PARameter) | [CreateSParameterEx](COM_Reference/Methods/Create_SParameterEX_Method.md)  
Meas Class... |  | [CALCulate:MEASure:DEFine](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:DEFine) | [CreateCustomMeasurementEx](COM_Reference/Methods/CreateCustomMeasurementEx_Method.md)

