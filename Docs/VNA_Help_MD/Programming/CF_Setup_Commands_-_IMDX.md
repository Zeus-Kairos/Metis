# Setup Commands - Swept IMD Converters Measurement Class

Only the Main and Layout Setup commands corresponding to the Swept IMD
Converters measurement class are documented here. All other commands are
identical to the Setup commands for the Standard measurement class and can be
accessed by clicking [here](CF_Setup_Commands_-_Standard.md) or by clicking
on the softtabs on the graphic below.

Click [here](CF_Setup_Commands.md) to view links to Setup commands for all
Measurement Classes.

Main |  Layout |  [System  
Setup](CF_System_Commands.htm#System_Setup_Tab_Commands) |  [Internal  
Hardware](CF_Setup_Commands_-_Standard.htm#Internal_Hardware_Commands) |  [External  
Hardware](CF_Setup_Commands_-_Standard.htm#External_Hardware_Commands)  
---|---|---|---|---  
Main Tab Commands  
---  
Softkey | Sub-item | SCPI |  COM  
IMDX Setup... | Tone Frequency  
Sweep Type  
Sweep fc | [SENSe:IMD:SWEep:TYPE](GP-IB_Command_Finder/Sense/IMD.md#SweepType) |  [SweepType](COM_Reference/Properties/SweepType_imd_Property.md)  
Sweep DeltaF | [SENSe:IMD:SWEep:TYPE](GP-IB_Command_Finder/Sense/IMD.md#SweepType) |  [SweepType](COM_Reference/Properties/SweepType_imd_Property.md)  
Power Sweep | [SENSe:IMD:SWEep:TYPE](GP-IB_Command_Finder/Sense/IMD.md#SweepType) |  [SweepType](COM_Reference/Properties/SweepType_imd_Property.md)  
CW | [SENSe:IMD:SWEep:TYPE](GP-IB_Command_Finder/Sense/IMD.md#SweepType) |  [SweepType](COM_Reference/Properties/SweepType_imd_Property.md)  
LO Power Sweep | [SENSe:IMD:SWEep:TYPE](GP-IB_Command_Finder/Sense/IMD.md#SweepType) |  [SweepType](COM_Reference/Properties/SweepType_imd_Property.md)  
X-Axis Display  
Annotation | [CALCulate:MEASure:MIXer:XAXis](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:MIXer:XAXis) |  [ActiveXAxisRange](COM_Reference/Properties/ActiveXAxisRange_Conv_Property.md)  
Sweep Settings  
Start fc | [SENSe:IMD:FREQuency:FCENter:STARt](GP-IB_Command_Finder/Sense/IMD.md#FCentStart) |  [FrequencyCenterStart](COM_Reference/Properties/FrequencyCenterStart_Property.md)  
Stop fc | [SENSe:IMD:FREQuency:FCENter:STOP](GP-IB_Command_Finder/Sense/IMD.md#FCentStop) |  [FrequencyCenterStop](COM_Reference/Properties/FrequencyCenterStop_Property.md)  
Center fc | [SENSe:IMD:FREQuency:FCENter:CENTer](GP-IB_Command_Finder/Sense/IMD.md#FcentCenter) |  [FrequencyCenter](COM_Reference/Properties/FrequencyCenter_Property.md)  
Span fc | [SENSe:IMD:FREQuency:FCENter:SPAN](GP-IB_Command_Finder/Sense/IMD.md#FCentSpan) |  [FrequencyCenterSpan](COM_Reference/Properties/FrequencyCenterspan_Property.md)  
Fixed DeltaF | [SENSe:IMD:FREQuency:DFRequency[:CW]](GP-IB_Command_Finder/Sense/IMD.md#DFRCW) |  [DeltaFrequency](COM_Reference/Properties/DeltaFrequency_Property.md)  
Number Of Points | [SENSe:SWEep:POINt](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssp) |  [NumberOfPoints](COM_Reference/Properties/Number_of__Points_Property.md)  
Main Tone IFBW | [SENSe:IMD:IFBWidth:MAIN](GP-IB_Command_Finder/Sense/IMD.md#ifbwMain) |  [MainToneIFBandwidth](COM_Reference/Properties/MainToneIFBandwidth_Property.md)  
IM Tone IFBW | [SENSe:IMD:IFBWidth:IMTone](GP-IB_Command_Finder/Sense/IMD.md#ifbwTone) |  [IMToneIFBandwidth](COM_Reference/Properties/IMToneIFBandwidth_Property.md)  
Reduce IF BW at Low Frequencies | None |  None  
Tone Power  
Power On (All Channels) | [OUTPut[:STATe]](GP-IB_Command_Finder/Output.md#RFOUt) |  [SourcePowerState](COM_Reference/Properties/Source_Power_State_Property.md)  
DUT Input Port  
Input Port | [SENSe:IMD:PMAP](GP-IB_Command_Finder/Sense/IMD.md#PMap) |  [SetPortMap](COM_Reference/Methods/SetPortMap_Method.md)  
Source Attenuator | [SOURce:POWer:ATTenuation](GP-IB_Command_Finder/source.md#attval) |  [Attenuator](COM_Reference/Properties/Attenuator_Property.md)  
Receiver Attenuator | [SENSe:POWer:ATTenuator](GP-IB_Command_Finder/Sense/Power.md) |  [ReceiverAttenuator](COM_Reference/Properties/Receiver_Attenuator_Property.md)  
DUT Output Port  
Output Port | [SENSe:IMD:PMAP](GP-IB_Command_Finder/Sense/IMD.md#PMap) |  [SetPortMap](COM_Reference/Methods/SetPortMap_Method.md)  
Source Attenuator | [SOURce:POWer:ATTenuation](GP-IB_Command_Finder/source.md#attval) |  [Attenuator](COM_Reference/Properties/Attenuator_Property.md)  
Receiver Attenuator | [SOURce:POWer:ATTenuation](GP-IB_Command_Finder/source.md#attval) |  [ReceiverAttenuator](COM_Reference/Properties/Receiver_Attenuator_Property.md)  
Tone Powers  
Coupled Tone Powers | [SENSe:IMD:TPOWer:COUPle[:STATe]](GP-IB_Command_Finder/Sense/IMD.md#PMap) |  [CoupleTonePower](COM_Reference/Properties/CoupleTonePower_Property.md)  
ALC On | [SENSe:IMD:TPOWer:LEV](GP-IB_Command_Finder/Sense/IMD.md#tpowLev) |  [LevelingMethod](COM_Reference/Properties/LevelingMethod_Property.md)  
Power Leveling |  |   
Set Input Power | [SENSe:IMD:TPOWer:LEV](GP-IB_Command_Finder/Sense/IMD.md#tpowLev) |  [LevelingMethod](COM_Reference/Properties/LevelingMethod_Property.md)  
Set Input Power, receiver leveling | [SENSe:IMD:TPOWer:LEV](GP-IB_Command_Finder/Sense/IMD.md#tpowLev) |  [LevelingMethod](COM_Reference/Properties/LevelingMethod_Property.md)  
Set Input Power, equal tones at output | [SENSe:IMD:TPOWer:LEV](GP-IB_Command_Finder/Sense/IMD.md#tpowLev) |  [LevelingMethod](COM_Reference/Properties/LevelingMethod_Property.md)  
Set Output Power, receiver leveling | [SENSe:IMD:TPOWer:LEV](GP-IB_Command_Finder/Sense/IMD.md#tpowLev) |  [LevelingMethod](COM_Reference/Properties/LevelingMethod_Property.md)  
Fixed | [SENSe:IMD:TPOWer:F1](GP-IB_Command_Finder/Sense/IMD.md#TPowf1) [SENSe:IMD:TPOWer:F2](GP-IB_Command_Finder/Sense/IMD.md#TPowF2) |  [TonePower](COM_Reference/Properties/TonePower_Property.md)  
Start | [SENSe:IMD:TPOWer:F1:STARt](GP-IB_Command_Finder/Sense/IMD.md#TpowF1Start) [SENSe:IMD:TPOWer:F2:STARt](GP-IB_Command_Finder/Sense/IMD.md#TpowF2Start) |  [TonePowerStart](COM_Reference/Properties/TonePowerStart_Property.md)  
Stop | [SENSe:IMD:TPOWer:F1:STOP](GP-IB_Command_Finder/Sense/IMD.md#TpowF1Stop) [SENSe:IMD:TPOWer:F2:STOP](GP-IB_Command_Finder/Sense/IMD.md#TpowF2Stop) |  [TonePowerStop](COM_Reference/Properties/TonePowerStop_Property.md)  
Step | None |  None  
Path Configuration... | [SENSe:PATH:CONFig:ELEMent[:STATe]](GP-IB_Command_Finder/Sense/Path.md#state) |  [Element](COM_Reference/Properties/Element_Property.md)  
Mixer Frequency  
Input | [SENSe:MIXer:CALCulate](GP-IB_Command_Finder/Sense/MIXerSCPI.md#calc) |  [Calculate](COM_Reference/Methods/Calculate_Method.md)  
LO1 | [SENSe:MIXer:LO:FREQuency:FIXed](GP-IB_Command_Finder/Sense/MIXerSCPI.md#LO_FIX) |  [LOFixedFrequency](COM_Reference/Properties/LOFixedFrequency_Property.md)  
Input > LO | [SENSe:MIXer:LO:FREQuency:ILTI](GP-IB_Command_Finder/Sense/MIXerSCPI.md#ilti) |  [IsInputGreaterThanLO](COM_Reference/Properties/InputIsGreaterThanLO_Property.md)  
Output | [SENSe:MIXer:CALCulate](GP-IB_Command_Finder/Sense/MIXerSCPI.md#calc) |  [Calculate](COM_Reference/Methods/Calculate_Method.md)  
Mixer Power  
Power On (All Channels) | [OUTPut[:STATe]](GP-IB_Command_Finder/Output.md#RFOUt) |  [SourcePowerState](COM_Reference/Properties/Source_Power_State_Property.md)  
LO1 Power | [SENSe:MIXer:LO:POWer](GP-IB_Command_Finder/Sense/MIXerSCPI.md#LO_POWer) |  [LOPower](COM_Reference/Properties/LOPower_Property.md)  
LO2 Power | [SENSe:MIXer:LO:POWer](GP-IB_Command_Finder/Sense/MIXerSCPI.md#LO_POWer) |  [LOPower](COM_Reference/Properties/LOPower_Property.md)  
LO Start Power | [SENSe:MIXer:LO:FREQuency:STARt](GP-IB_Command_Finder/Sense/MIXerSCPI.md#LO_Start) |  [LOStartFrequency](COM_Reference/Properties/LOStartFrequency_Property.md)  
LO Stop Power | [SENSe:MIXer:LO:FREQuency:STOP](GP-IB_Command_Finder/Sense/MIXerSCPI.md#LO_stop) |  [LOStopFrequency](COM_Reference/Properties/LOStopFrequency_Property.md)  
Source Attenuator | [SOURce:POWer:ATTenuation](GP-IB_Command_Finder/source.md#attval) |  [Attenuator](COM_Reference/Properties/Attenuator_Property.md)  
Receiver Attenuator | [SENSe:POWer:ATTenuator](GP-IB_Command_Finder/Sense/Power.md) |  [ReceiverAttenuator](COM_Reference/Properties/Receiver_Attenuator_Property.md)  
Path Configuration... | [SENSe:PATH:CONFig:ELEMent[:STATe]](GP-IB_Command_Finder/Sense/Path.md#state) |  [Element](COM_Reference/Properties/Element_Property.md)  
Mixer Setup  
Converter Stages | [SENSe:MIXer:STAGe](GP-IB_Command_Finder/Sense/MIXerSCPI.md#Stage) |  [LOStage](COM_Reference/Properties/LOStage_Property.md)  
Recall a previously-configured external source | [SENSe:MIXer:LO:NAME](GP-IB_Command_Finder/Sense/MIXerSCPI.md#name) |  [LOName](COM_Reference/Properties/LOName_Property.md)  
Assign a source to mixer input or LO | [SENSe:MIXer:ROLE:DEVice](GP-IB_Command_Finder/Sense/MIXerSCPI.md#RoleDevice) |  [AssignSourceToRole](COM_Reference/Methods/AssignSourceToRole_Method.md)  
Read all assigned roles | [SENSe:MIXer:ROLE:CATalog?](GP-IB_Command_Finder/Sense/MIXerSCPI.md#RoleCat) |  [GetSourceByRole](COM_Reference/Methods/GetSourceByRole_Method.md)  
Read the source assigned to a role | [SENSe:MIXer:ROLE:DEVice](GP-IB_Command_Finder/Sense/MIXerSCPI.md#RoleDevice) |  [GetSourceRoles](COM_Reference/Methods/GetSourceRoles_Method.md)  
Input Numerator Frac.Mult | [SENSe:MIXer:INPut:FREQuency:NUMerator](GP-IB_Command_Finder/Sense/MIXerSCPI.md#INPut_NUM) |  [InputNumerator](COM_Reference/Properties/InputNumerator_Property.md)  
Input Denominator Frac.Mult | [SENSe:MIXer:INPut:FREQuency:DENominator](GP-IB_Command_Finder/Sense/MIXerSCPI.md#INPut_DEN) |  [InputDenominator](COM_Reference/Properties/InputDenominator_Property.md)  
LO Numerator Frac. Mult. | [SENSe:MIXer:LO:FREQuency:NUMerator](GP-IB_Command_Finder/Sense/MIXerSCPI.md#LO_NUM) |  [LONumerator](COM_Reference/Properties/LONumerator_Property.md)  
LO Denominator Frac.Mult | [SENSe:MIXer:LO:FREQuency:DENominator](GP-IB_Command_Finder/Sense/MIXerSCPI.md#LO_DEN) |  [LODenominator](COM_Reference/Properties/LODenominator_Property.md)  
Path Configuration... | [SENSe:PATH:CONFig:ELEMent[:STATe]](GP-IB_Command_Finder/Sense/Path.md#state) |  [Element](COM_Reference/Properties/Element_Property.md)  
Save... | [SENSe:MIXer:SAVE](GP-IB_Command_Finder/Sense/MIXerSCPI.md#Save) |  [SaveFile](COM_Reference/Methods/SaveFile_Method.md)  
Load... | [SENSe:MIXer:LOAD](GP-IB_Command_Finder/Sense/MIXerSCPI.md#Load) |  [LoadFile](COM_Reference/Methods/LoadFile_Method.md)  
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
Measure... |  | [CALCulate:MEASure:PARameter](GP-IB_Command_Finder/Calculate/MeasurePARameter.md#CALCulate:MEASure:PARameter) |  [CreateSParameterEx](COM_Reference/Methods/Create_SParameterEX_Method.md)  
Meas Class... |  | [CALCulate:MEASure:DEFine](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:DEFine) |  [CreateCustomMeasurementEx](COM_Reference/Methods/CreateCustomMeasurementEx_Method.md)

