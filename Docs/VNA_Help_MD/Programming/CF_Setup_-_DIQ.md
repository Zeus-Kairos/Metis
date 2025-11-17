# Setup Commands - Differential I/Q Measurement Class

Only the Main Setup commands corresponding to the Differential I/Q measurement
class are documented here. All other commands are identical to the Setup
commands for the Standard measurement class and can be accessed by clicking
[here](CF_Setup_Commands_-_Standard.md) or by clicking on the softtabs on the
graphic below.

Click [here](CF_Setup_Commands.md) to view links to Setup commands for all
Measurement Classes.

Main | [Layout](CF_Setup_Commands_-_Standard.md#Customize_Meas_Commands) | [System  
Setup](CF_System_Commands.htm#System_Setup_Tab_Commands) | [Internal  
Hardware](CF_Setup_Commands_-_Standard.htm#Internal_Hardware_Commands) | [External  
Hardware](CF_Setup_Commands_-_Standard.htm#External_Hardware_Commands)  
---|---|---|---|---  
Main Tab Commands  
---  
Softkey | Sub-item | SCPI | COM  
DIQ Setup... | Frequency Range Settings | [SENSe:DIQ:FREQuency:RANGe:ADD](GP-IB_Command_Finder/Sense/DIQ.md#FrRangeAdd) | [AddRange](COM_Reference/Methods/AddRange_Method.md)  
Frequency | [SENSe:DIQ:FREQuency:RANGe:Start](GP-IB_Command_Finder/Sense/DIQ.md#FrRangeStart) | [RangeStartFrequency](COM_Reference/Properties/RangeStartFrequency_Property.md)  
[SENSe:DIQ:FREQuency:RANGe:STOP](GP-IB_Command_Finder/Sense/DIQ.md#FrRangeStop) | [RangeStopFrequency](COM_Reference/Properties/RangeStopFrequency_Property.md)  
[SENSe:DIQ:FREQuency:RANGe:IFBW](GP-IB_Command_Finder/Sense/DIQ.md#FrRangeIFBW) | [RangeIFBW](COM_Reference/Properties/RangeIFBW_Property.md)  
Coupling | [SENSe:DIQ:FREQuency:RANGe:COUPle:STATe](GP-IB_Command_Finder/Sense/DIQ.md#FrRangeCplState) | [RangeCoupleState](COM_Reference/Properties/RangeCoupleState_Property.md)  
[SENSe:DIQ:FREQuency:RANGe:COUPle:ID](GP-IB_Command_Finder/Sense/DIQ.md#FrRangeCplID) | [RangeCoupled](COM_Reference/Properties/RangeCoupleId_Property.md)  
[SENSe:DIQ:FREQuency:RANGe:COUPle:OFFSet](GP-IB_Command_Finder/Sense/DIQ.md#FrRangeCplOffset) | [RangeOffset](COM_Reference/Properties/RangeOffset_Property.md)  
[SENSe:DIQ:FREQuency:RANGe:COUPle:UCONvert](GP-IB_Command_Finder/Sense/DIQ.md#FrRangeCplUconv) | [RangeOffsetUp](COM_Reference/Properties/RangeOffsetUp_Property.md)  
[SENSe:DIQ:FREQuency:RANGe:COUPle:MULTiplier](GP-IB_Command_Finder/Sense/DIQ.md#FrRangeCplMult) | [RangeMultiplier](COM_Reference/Properties/RangeMultiplier_Property.md)  
[SENSe:DIQ:FREQuency:RANGe:COUPle:DIVisor](GP-IB_Command_Finder/Sense/DIQ.md#FrRangeCplDivisor) | [RangeDivisor](COM_Reference/Properties/RangeDivisor_Property.md)  
Remove | [SENSe:DIQ:FREQuency:RANGe:DELete](GP-IB_Command_Finder/Sense/DIQ.md#FrRangeDelete) | [DeleteRange](COM_Reference/Methods/DeleteRange_Method.md)  
Source Configuration |  |   
Source State | [SENSe:DIQ:PORT:STATe](GP-IB_Command_Finder/Sense/DIQ.md#PortState) | [SourceState](COM_Reference/Properties/SourceState_Property.md)  
Frequency Range | [SENSe:DIQ:PORT:RANGe](GP-IB_Command_Finder/Sense/DIQ.md#PortRange) | [SourceRange](COM_Reference/Properties/SourceRange_Property.md)  
Ext Source Port | [SOURce:PHASe:EXTernal:CATalog?](GP-IB_Command_Finder/SourcePhase.md#SOURce:PHASe:EXTernal:CATalog) [SOURce:PHASe:EXTernal:PORT](GP-IB_Command_Finder/SourcePhase.md#SOURce:PHASe:EXTernal:PORT) | None None  
Power | [SENSe:DIQ:PORT:POWer:SWEep](GP-IB_Command_Finder/Sense/DIQ.md#PortPowerSwp) | [PowerSweepState](COM_Reference/Properties/PowerSweepState_Property.md)  
[SENSe:DIQ:PORT:POWer:STARt](GP-IB_Command_Finder/Sense/DIQ.md#PortPowerStart) | [PortStartPower](COM_Reference/Properties/PortStartPower_Property.md)  
[SENSe:DIQ:PORT:POWer:STOP](GP-IB_Command_Finder/Sense/DIQ.md#PortPowerStop) | [PortStopPower](COM_Reference/Properties/PortStopPower_Property.md)  
[SENSe:DIQ:PORT:POWer:ALC:MODE](GP-IB_Command_Finder/Sense/DIQ.md#PortPowerALC) | [PortLevelingMode](COM_Reference/Properties/PortLevelingMode_Property.md)  
[SENSe:DIQ:PORT:POWer:ATTenuation](GP-IB_Command_Finder/Sense/DIQ.md#PortPowerAtten) | [PortAttenuator](COM_Reference/Properties/PortAttenuator_Property.md)  
[SENSe:DIQ:PORT:POWer:ATTenuation:AUTO](GP-IB_Command_Finder/Sense/DIQ.md#PortPowerSwp) | [AutoRangeState](COM_Reference/Properties/AutoRangeState_Property.md)  
Phase | [SENSe:DIQ:PORT:PHASe:STATe](GP-IB_Command_Finder/Sense/DIQ.md#PortPhaseState) | [PortPhaseState](COM_Reference/Properties/PortPhaseState_Property.md)  
[SENSe:DIQ:PORT:PHASe:SWEep](GP-IB_Command_Finder/Sense/DIQ.md#PortPhaseSweep) | [PhaseSweepState](COM_Reference/Properties/PhaseSweepState_Property.md)  
[SENSe:DIQ:PORT:PHASe:STARt](GP-IB_Command_Finder/Sense/DIQ.md#PortPhaseStart) | [PortPhaseStart](COM_Reference/Properties/PortPhaseStart_Property.md)  
[SENSe:DIQ:PORT:PHASe:STOP](GP-IB_Command_Finder/Sense/DIQ.md#PortPhaseStop) | [PortPhaseStop](COM_Reference/Properties/PortPhaseStop_Property.md)  
[SENSe:DIQ:PORT:PHASe:REFerence](GP-IB_Command_Finder/Sense/DIQ.md#PortPhaseRef) | [PortReference](COM_Reference/Properties/PortReference_Property.md)  
[SENSe:DIQ:PORT:PHASe:PARameter](GP-IB_Command_Finder/Sense/DIQ.md#PortPhasePar) | [PortPhaseParameter](COM_Reference/Properties/PortPhaseParameter_Property.md)  
[SOURce:PHASe:CONTrol:TOLerance](GP-IB_Command_Finder/SourcePhase.md#tolerance) | [PhaseTolerance](COM_Reference/Properties/PhaseTolerance_Property.md)  
[SOURce:PHASe:CONTrol:ITERation](GP-IB_Command_Finder/SourcePhase.md#iteration) | [PhaseIterationNumber](COM_Reference/Properties/PhaseIterationNumber_Property.md)  
Match Correction | [SENSe:DIQ:PORT:MATCh:STATe](GP-IB_Command_Finder/Sense/DIQ.md#PortMatchState) | [MatchState](COM_Reference/Properties/MatchState_Property.md)  
[SENSe:DIQ:PORT:MATCh:TRECeiver](GP-IB_Command_Finder/Sense/DIQ.md#PortMatchTrec) | [MatchTestReceiver](COM_Reference/Properties/MatchTestReceiver_Property.md)  
[SENSe:DIQ:PORT:MATCh:RRECeiver](GP-IB_Command_Finder/Sense/DIQ.md#PortMatchRRec) | [MatchRefReceiver](COM_Reference/Properties/MatchRefReceiver_Property.md)  
[SENSe:DIQ:PORT:MATCh:RANGe](GP-IB_Command_Finder/Sense/DIQ.md#PortMatchRange) | [MatchFrequencyRange](COM_Reference/Properties/MatchFrequencyRange_Property.md)  
Meas Class... |  | [CALCulate:MEASure:DEFine](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:DEFine) | [CreateCustomMeasurementEx](COM_Reference/Methods/CreateCustomMeasurementEx_Method.md)  
Quick Start... | S-Param | [CALCulate:MEASure:PARameter](GP-IB_Command_Finder/Calculate/MeasurePARameter.md#CALCulate:MEASure:PARameter) | [CreateSParameterEx](COM_Reference/Methods/Create_SParameterEX_Method.md)  
Balanced | [CALCulate:MEASure:PARameter](GP-IB_Command_Finder/Calculate/MeasurePARameter.md#CALCulate:MEASure:PARameter) | [BalSMeasurement](COM_Reference/Properties/BalSMeasurement_Property.md) [BBalMeasurement](COM_Reference/Properties/BBalMeasurement_Property.md) [SBalMeasurement](COM_Reference/Properties/SBalMeasurement_Property.md) [SSBMeasurement](COM_Reference/Properties/SSBMeasurement_Property.md)  
Other | [CALCulate:MEASure:PARameter](GP-IB_Command_Finder/Calculate/MeasurePARameter.md#CALCulate:MEASure:PARameter) | [CreateSParameterEx](COM_Reference/Methods/Create_SParameterEX_Method.md)

