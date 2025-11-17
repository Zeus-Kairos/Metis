# Setup Commands - Swept IMD Measurement Class

Only the Main and Layout Setup commands corresponding to the Swept IMD
measurement class are documented here. All other commands are identical to the
Setup commands for the Standard measurement class and can be accessed by
clicking [here](CF_Setup_Commands_-_Standard.md) or by clicking on the
softtabs on the graphic below.

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
IMD Setup... | Frequency  
Sweep Type  
Sweep fc | [SENSe:IMD:SWEep:TYPE](GP-IB_Command_Finder/Sense/IMD.md#SweepType) | [SweepType](COM_Reference/Properties/SweepType_imd_Property.md)  
Sweep DeltaF | [SENSe:IMD:SWEep:TYPE](GP-IB_Command_Finder/Sense/IMD.md#SweepType) | [SweepType](COM_Reference/Properties/SweepType_imd_Property.md)  
Power Sweep | [SENSe:IMD:SWEep:TYPE](GP-IB_Command_Finder/Sense/IMD.md#SweepType) | [SweepType](COM_Reference/Properties/SweepType_imd_Property.md)  
CW | [SENSe:IMD:SWEep:TYPE](GP-IB_Command_Finder/Sense/IMD.md#SweepType) | [SweepType](COM_Reference/Properties/SweepType_imd_Property.md)  
Segment Sweep fc | [SENSe:IMD:SWEep:TYPE](GP-IB_Command_Finder/Sense/IMD.md#SweepType) | [SweepType](COM_Reference/Properties/SweepType_imd_Property.md)  
Sweep Settings  
Start fc | [SENSe:IMD:FREQuency:FCENter:STARt](GP-IB_Command_Finder/Sense/IMD.md#FCentStart) | [FrequencyCenterStart](COM_Reference/Properties/FrequencyCenterStart_Property.md)  
Center fc | [SENSe:IMD:FREQuency:FCENter:CENTer](GP-IB_Command_Finder/Sense/IMD.md#FcentCenter) | [FrequencyCenter](COM_Reference/Properties/FrequencyCenter_Property.md)  
Fixed DeltaF | [SENSe:IMD:FREQuency:DFRequency[:CW]](GP-IB_Command_Finder/Sense/IMD.md#DFRCW) | [DeltaFrequency](COM_Reference/Properties/DeltaFrequency_Property.md)  
Number Of Points | [SENSe:SWEep:POINt](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssp) | [NumberOfPoints](COM_Reference/Properties/Number_of__Points_Property.md)  
Stop fc | [SENSe:IMD:FREQuency:FCENter:STOP](GP-IB_Command_Finder/Sense/IMD.md#FCentStop) | [FrequencyCenterStop](COM_Reference/Properties/FrequencyCenterStop_Property.md)  
Span fc | [SENSe:IMD:FREQuency:FCENter:SPAN](GP-IB_Command_Finder/Sense/IMD.md#FCentSpan) | [FrequencyCenterSpan](COM_Reference/Properties/FrequencyCenterspan_Property.md)  
Main Tone IFBW | [SENSe:IMD:IFBWidth:MAIN](GP-IB_Command_Finder/Sense/IMD.md#ifbwMain) | [MainToneIFBandwidth](COM_Reference/Properties/MainToneIFBandwidth_Property.md)  
IM Tone IFBW | [SENSe:IMD:IFBWidth:IMTone](GP-IB_Command_Finder/Sense/IMD.md#ifbwTone) | [IMToneIFBandwidth](COM_Reference/Properties/IMToneIFBandwidth_Property.md)  
Reduce IF BW at Low Frequencies | None | None  
Power  
Power On (All Channels) | [OUTPut[:STATe]](GP-IB_Command_Finder/Output.md#RFOUt) | [SourcePowerState](COM_Reference/Properties/Source_Power_State_Property.md)  
DUT Input  
Input Port | [SENSe:IMD:PMAP](GP-IB_Command_Finder/Sense/IMD.md#PMap) | [SetPortMap](COM_Reference/Methods/SetPortMap_Method.md)  
Source Attenuator | [SOURce:POWer:ATTenuation](GP-IB_Command_Finder/source.md#attval) | [Attenuator](COM_Reference/Properties/Attenuator_Property.md)  
Receiver Attenuator | [SENSe:POWer:ATTenuator](GP-IB_Command_Finder/Sense/Power.md) | [ReceiverAttenuator](COM_Reference/Properties/Receiver_Attenuator_Property.md)  
DUT Output  
Output Port | [SENSe:IMD:PMAP](GP-IB_Command_Finder/Sense/IMD.md#PMap) | [SetPortMap](COM_Reference/Methods/SetPortMap_Method.md)  
Source Attenuator | [SOURce:POWer:ATTenuation](GP-IB_Command_Finder/source.md#attval) | [Attenuator](COM_Reference/Properties/Attenuator_Property.md)  
Receiver Attenuator | [SENSe:POWer:ATTenuator](GP-IB_Command_Finder/Sense/Power.md) | [ReceiverAttenuator](COM_Reference/Properties/Receiver_Attenuator_Property.md)  
Tone Powers  
Coupled Tone Powers | [SENSe:IMD:TPOWer:COUPle[:STATe]](GP-IB_Command_Finder/Sense/IMD.md#PMap) | [CoupleTonePower](COM_Reference/Properties/CoupleTonePower_Property.md)  
ALC On | [SENSe:IMD:TPOWer:LEV](GP-IB_Command_Finder/Sense/IMD.md#tpowLev) | [LevelingMethod](COM_Reference/Properties/LevelingMethod_Property.md)  
Power Leveling |  |   
Set Input Power | [SENSe:IMD:TPOWer:LEV](GP-IB_Command_Finder/Sense/IMD.md#tpowLev) | [LevelingMethod](COM_Reference/Properties/LevelingMethod_Property.md)  
Set Input Power, receiver leveling | [SENSe:IMD:TPOWer:LEV](GP-IB_Command_Finder/Sense/IMD.md#tpowLev) | [LevelingMethod](COM_Reference/Properties/LevelingMethod_Property.md)  
Set Input Power, equal tones at output | [SENSe:IMD:TPOWer:LEV](GP-IB_Command_Finder/Sense/IMD.md#tpowLev) | [LevelingMethod](COM_Reference/Properties/LevelingMethod_Property.md)  
Set Output Power, receiver leveling | [SENSe:IMD:TPOWer:LEV](GP-IB_Command_Finder/Sense/IMD.md#tpowLev) | [LevelingMethod](COM_Reference/Properties/LevelingMethod_Property.md)  
Fixed | [SENSe:IMD:TPOWer:F1](GP-IB_Command_Finder/Sense/IMD.md#TPowf1) [SENSe:IMD:TPOWer:F2](GP-IB_Command_Finder/Sense/IMD.md#TPowF2) | [TonePower](COM_Reference/Properties/TonePower_Property.md)  
Start | [SENSe:IMD:TPOWer:F1:STARt](GP-IB_Command_Finder/Sense/IMD.md#TpowF1Start) [SENSe:IMD:TPOWer:F2:STARt](GP-IB_Command_Finder/Sense/IMD.md#TpowF2Start) | [TonePowerStart](COM_Reference/Properties/TonePowerStart_Property.md)  
Stop | [SENSe:IMD:TPOWer:F1:STOP](GP-IB_Command_Finder/Sense/IMD.md#TpowF1Stop) [SENSe:IMD:TPOWer:F2:STOP](GP-IB_Command_Finder/Sense/IMD.md#TpowF2Stop) | [TonePowerStop](COM_Reference/Properties/TonePowerStop_Property.md)  
Step | None | None  
Path Configuration... | [SENSe:PATH:CONFig:ELEMent[:STATe]](GP-IB_Command_Finder/Sense/Path.md#state) | [Element](COM_Reference/Properties/Element_Property.md)  
Configure  
Receiver Configuration | [SENSe:IMD:RECeiver:CONFig:COMBiner:PATH](GP-IB_Command_Finder/Sense/IMD.md#SENSe:IMD:RECeiver:CONFig:COMBiner:PATH) [SENSe:IMD:RECeiver:CONFig:REFerence COUNt](GP-IB_Command_Finder/Sense/IMD.md#SENSe:IMD:RECeiver:CONFig:REFerence:COUNt) | None  None  
Add Source... | [SENSe:ROLE:DEVice](GP-IB_Command_Finder/Sense/Role.md#Device) | [AssignSourceToRole](COM_Reference/Methods/AssignSourceToRole_Method.md)  
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

