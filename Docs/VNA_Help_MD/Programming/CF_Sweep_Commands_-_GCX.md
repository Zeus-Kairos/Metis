# Sweep Commands - Gain Compression Converters Measurement Class

Click [here](CF_Sweep_Commands.md) to view links to Sweep commands for all
Measurement Classes.

Main | Sweep Timing | Source Control  
---|---|---  
Main Tab Commands  
---  
Softkey | Sub-item | SCPI | COM  
Number of Points |  | [SENSe:SWEep:POINts](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssp) | [NumberOfPoints](COM_Reference/Properties/Number_of__Points_Property.md)  
X-Axis Type |  | [CALCulate:MEASure:MIXer:XAXis](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:MIXer:XAXis) | [ActiveXAxisRange](COM_Reference/Properties/ActiveXAxisRange_Conv_Property.md)  
[Sweep Type](CF_Setup_Commands_-_GCX.md#GCX_Setup...) |  |  |   
[GCX Setup...](CF_Setup_Commands_-_GCX.md#GCX_Setup...) |  |  |   
Sweep Timing Tab Commands  
Softkey | Sub-item | SCPI | COM  
Sweep Time | Auto | [SENSe:SWEep:TIME:AUTO](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssta) | [chan.SweepTime](COM_Reference/Properties/Sweep_Time_Property.md)  
Manual | [SENSe:SWEep:TIME[:STOP]](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#sst) | [chan.SweepTime](COM_Reference/Properties/Sweep_Time_Property.md)  
Dwell Time |  | [SENSe:SWEep:DWELl](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssd) | [DwellTime](COM_Reference/Properties/Dwell_Time_Property.md)  
Sweep Delay |  | [SENSe:SWEep:DWELl:SDELay](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#SweepDelay) | [SweepDelay](COM_Reference/Properties/Sweep_Delay_Property.md)  
Fast Sweep | ON | [SENSe:SWEep:SPEed](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#SweepSpeed) | [SweepSpeedMode](COM_Reference/Properties/SweepSpeedMode_Property.md)  
OFF | [SENSe:SWEep:SPEed](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#SweepSpeed) | [SweepSpeedMode](COM_Reference/Properties/SweepSpeedMode_Property.md)  
Source Control Tab Commands  
Softkey | Sub-item | SCPI | COM  
Pulse Setup... | Pulse Measurement  
Off | [SENSe:SWEep:PULSe:MODE](GP-IB_Command_Finder/Sense/SweepPulse.md#mode) | [PulseMeasMode](COM_Reference/Properties/PulseMeasMode_Property.md)  
Standard Pulse | [SENSe:SWEep:PULSe:MODE](GP-IB_Command_Finder/Sense/SweepPulse.md#mode) | [PulseMeasMode](COM_Reference/Properties/PulseMeasMode_Property.md)  
Pulse Profile | [SENSe:SWEep:PULSe:MODE](GP-IB_Command_Finder/Sense/SweepPulse.md#mode) | [PulseMeasMode](COM_Reference/Properties/PulseMeasMode_Property.md)  
Pulse Timing  
Pulse Width | [SENSe:SWEep:PULSe:PRIMary:WIDth](GP-IB_Command_Finder/Sense/SweepPulse.md#MasterWidth) | [PrimaryWidth](COM_Reference/Properties/MasterWidth_Property.md)  
Pulse Period | [SENSe:SWEep:PULSe:PRIMary:PERiod](GP-IB_Command_Finder/Sense/SweepPulse.md#MasterPeriod) | [PrimaryPeriod](COM_Reference/Properties/MasterPeriod_Property.md)  
Pulse Frequency | [SENSe:SWEep:PULSe:PRIMary:FREQuency](GP-IB_Command_Finder/Sense/SweepPulse.md#MasterFreq) | [PrimaryFrequency](COM_Reference/Properties/MasterFrequency_Property.md)  
Embedded LO... | Embedded LO Mode On | [SENSe:MIXer:LO:FREQuency:MODE](GP-IB_Command_Finder/Sense/MIXerSCPI.md#LoMode) | [LORangeMode](COM_Reference/Properties/LORangeMode_cv_Property.md)  
Tuning Point | [SENSe:MIXer:ELO:NORMalize:POINT](GP-IB_Command_Finder/Sense/MixrEmbedLO.md#point) | [NormalizePoint](COM_Reference/Properties/NormalizePoint_Property.md)  
LO Frequency Delta | [SENSe:MIXer:ELO:LO:DELTA](GP-IB_Command_Finder/Sense/MixrEmbedLO.md#delta) | [LOFrequencyDelta](COM_Reference/Properties/LOFrequencyDelta_Property.md)  
Tuning Settings |  |   
Broadband and precise | [SENSe:MIXer:ELO:TUNing:MODE](GP-IB_Command_Finder/Sense/MixrEmbedLO.md#mode) | [TuningMode](COM_Reference/Properties/TuningMode_Property.md)  
Precise only | None | None  
Disable tuning | None | None  
Sweep Span | [SENSe:MIXer:ELO:TUNing:SPAN](GP-IB_Command_Finder/Sense/MixrEmbedLO.md#span) | [BroadbandTuningSpan](COM_Reference/Properties/BroadbandTuningSpan_Property.md)  
Max Iterations | [SENSe:MIXer:ELO:TUNing:ITERations](GP-IB_Command_Finder/Sense/MixrEmbedLO.md#iteration) | [MaxPreciseTuningIterations](COM_Reference/Properties/MaxPreciseTuningIterations_Property.md)  
Tolerance | [SENSe:MIXer:ELO:TUNing:TOLerance](GP-IB_Command_Finder/Sense/MixrEmbedLO.md#tolerance) | [PreciseTuningTolerance](COM_Reference/Properties/PreciseTuningTolerance_Property.md)  
Tuning IFBW | [SENSe:MIXer:ELO:TUNing:IFBW](GP-IB_Command_Finder/Sense/MixrEmbedLO.md#ifbw) | [TuningIFBW](COM_Reference/Properties/TuningIFBW_Property.md)  
Tune every | [SENSe:MIXer:ELO:TUNing:INTerval](GP-IB_Command_Finder/Sense/MixrEmbedLO.md#interval) | [TuningSweepInterval](COM_Reference/Properties/TuningSweepInterval_Property.md)

