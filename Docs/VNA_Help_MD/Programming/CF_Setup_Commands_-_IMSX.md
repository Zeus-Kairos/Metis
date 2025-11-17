# Setup Commands - IM Spectrum Converters Measurement Class

Only the Main and Layout Setup commands corresponding to the IM Spectrum
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
IMSX Setup... | Frequency  
Sweep Type  
Linear | [SENSe:IMS:SWEep:TYPE](GP-IB_Command_Finder/Sense/IMS.md#SweepType) |  [SweepType](COM_Reference/Properties/Sweep_Type_Property.md)  
2nd Order Spectrum | [SENSe:IMS:SWEep:TYPE](GP-IB_Command_Finder/Sense/IMS.md#SweepType) |  [SweepType](COM_Reference/Properties/Sweep_Type_Property.md)  
3rd Order Spectrum | [SENSe:IMS:SWEep:TYPE](GP-IB_Command_Finder/Sense/IMS.md#SweepType) |  [SweepType](COM_Reference/Properties/Sweep_Type_Property.md)  
Nth Order Spectrum | [SENSe:IMS:SWEep:TYPE](GP-IB_Command_Finder/Sense/IMS.md#SweepType) |  [SweepType](COM_Reference/Properties/Sweep_Type_Property.md)  
Order N | [SENSe:IMS:SWEep:ORDer](GP-IB_Command_Finder/Sense/IMS.md#SweepOrder) |  [SweepOrder](COM_Reference/Properties/SweepOrder_Property.md)  
Resolution BW | [SENSe:IMS:RBW](GP-IB_Command_Finder/Sense/IMS.md#RBW) |  [ResolutionBW](COM_Reference/Properties/ResolutionBW_Property.md)  
Stimulus Settings  
fc (Tone Center) | [SENSe:IMS:STIMulus:FCENter](GP-IB_Command_Finder/Sense/IMS.md#StimFCenter) |  [FrequencyCenter](COM_Reference/Properties/FrequencyCenter_Property.md)  
Delta F | [SENSe:IMS:STIMulus:DFRequency](GP-IB_Command_Finder/Sense/IMS.md#StimDFR) |  [DeltaFrequency](COM_Reference/Properties/DeltaFrequency_Property.md)  
f1 | [SENSe:IMS:STIMulus:F1FRequency](GP-IB_Command_Finder/Sense/IMS.md#Stimf1) |  [F1Frequency](COM_Reference/Properties/F1Frequency_Property.md)  
f2 | [SENSe:IMS:STIMulus:F2FRequency](GP-IB_Command_Finder/Sense/IMS.md#StimF2) |  [F2Frequency](COM_Reference/Properties/F2Frequency_Property.md)  
Response Settings  
Start Spectrum | [SENSe:IMS:RESPonse:STARt](GP-IB_Command_Finder/Sense/IMS.md#RecStart) |  [SpectrumStartFrequency](COM_Reference/Properties/SpectrumStartFrequency_Property.md)  
Stop Spectrum | [SENSe:IMS:RESPonse:STOP](GP-IB_Command_Finder/Sense/IMS.md#RecStop) |  [SpectrumStopFrequency](COM_Reference/Properties/SpectrumStopFrequency_Property.md)  
Center Spectrum | [SENSe:IMS:RESPonse:CENTer](GP-IB_Command_Finder/Sense/IMS.md#RecCenter) |  [SpectrumCenterFrequency](COM_Reference/Properties/SpectrumCenterFrequency_Property.md)  
Span Spectrum | [SENSe:IMS:RESPonse:SPAN](GP-IB_Command_Finder/Sense/IMS.md#RecSpan) |  [SpectrumSpanFrequency](COM_Reference/Properties/SpectrumSpanFrequency_Property.md)  
Tone Power  
Power On (All Channels) | [OUTPut[:STATe]](GP-IB_Command_Finder/Output.md#RFOUt) |  [SourcePowerState](COM_Reference/Properties/Source_Power_State_Property.md)  
DUT Input  
Input Port | [SENSe:IMS:PMAP](GP-IB_Command_Finder/Sense/IMS.md#pmap) |  [SetPortMap](COM_Reference/Methods/SetPortMap_Method.md)  
Source Attenuator | [SOURce:POWer:ATTenuation](GP-IB_Command_Finder/source.md#attval) |  [Attenuator](COM_Reference/Properties/Attenuator_Property.md)  
Receiver Attenuator | [SENSe:POWer:ATTenuator](GP-IB_Command_Finder/Sense/Power.md) |  [ReceiverAttenuator](COM_Reference/Properties/Receiver_Attenuator_Property.md)  
DUT Output  
Output Port | [SENSe:IMS:PMAP](GP-IB_Command_Finder/Sense/IMS.md#pmap) |  [SetPortMap](COM_Reference/Methods/SetPortMap_Method.md)  
Source Attenuator | [SOURce:POWer:ATTenuation](GP-IB_Command_Finder/source.md#attval) |  [Attenuator](COM_Reference/Properties/Attenuator_Property.md)  
Receiver Attenuator | [SENSe:POWer:ATTenuator](GP-IB_Command_Finder/Sense/Power.md) |  [ReceiverAttenuator](COM_Reference/Properties/Receiver_Attenuator_Property.md)  
Tone Powers  
Coupled Tone Powers | [SENSe:IMS:TPOWer:COUPle[:STATe]](GP-IB_Command_Finder/Sense/IMS.md#TPowerCouple) |  [CoupleTonePower](COM_Reference/Properties/CoupleTonePower_Property.md)  
ALC On | [SENSe:IMS:TPOWer:LEVel](GP-IB_Command_Finder/Sense/IMS.md#tPowerLevel) |  [LevelingMethod](COM_Reference/Properties/LevelingMethod_Property.md)  
Power Leveling |  |   
Set Input Power | [SENSe:IMS:TPOWer:LEVel](GP-IB_Command_Finder/Sense/IMS.md#tPowerLevel) |  [LevelingMethod](COM_Reference/Properties/LevelingMethod_Property.md)  
Set Input Power, receiver leveling | [SENSe:IMS:TPOWer:LEVel](GP-IB_Command_Finder/Sense/IMS.md#tPowerLevel) |  [LevelingMethod](COM_Reference/Properties/LevelingMethod_Property.md)  
Set Input Power, equal tones at output | [SENSe:IMS:TPOWer:LEVel](GP-IB_Command_Finder/Sense/IMS.md#tPowerLevel) |  [LevelingMethod](COM_Reference/Properties/LevelingMethod_Property.md)  
Set Output Power, receiver leveling | [SENSe:IMS:TPOWer:LEVel](GP-IB_Command_Finder/Sense/IMS.md#tPowerLevel) |  [LevelingMethod](COM_Reference/Properties/LevelingMethod_Property.md)  
Fixed | [SENSe:IMS:STIMulus:TPOWer:F1](GP-IB_Command_Finder/Sense/IMS.md#TPowrF1) [SENSe:IMS:STIMulus:TPOWer:F2](GP-IB_Command_Finder/Sense/IMS.md#tPowerF2) |  [TonePower](COM_Reference/Properties/TonePower_Property.md)  
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

