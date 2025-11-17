# Sweep Commands - Swept IMD Measurement Class

Only the Main, Sweep Timing, and Source Control Sweep commands corresponding
to the Swept IMD measurement class are documented here. The Segment Table
commands are identical to the Sweep commands for the Standard measurement
class and can be accessed by clicking [here](CF_Sweep_Commands_-
_Standard.htm#Segment_Table_Tab_Commands) or by clicking on the softtab on the
graphic below.

Click [here](CF_Sweep_Commands.md) to view links to Sweep commands for all
Measurement Classes.

Main | Sweep Timing | Source Control | [Segment Table](CF_Sweep_Commands_-_Standard.md#Segment_Table_Tab_Commands)  
---|---|---|---  
Main Tab Commands  
---  
Softkey | Sub-item | SCPI | COM  
Number of Points |  | [SENSe:SWEep:POINts](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssp) | [NumberOfPoints](COM_Reference/Properties/Number_of__Points_Property.md)  
Sweep Type | Sweep fc | [SENSe:IMD:SWEep:TYPE](GP-IB_Command_Finder/Sense/IMD.md#SweepType) | [SweepType](COM_Reference/Properties/SweepType_imd_Property.md)  
Sweep DeltaF | [SENSe:IMD:SWEep:TYPE](GP-IB_Command_Finder/Sense/IMD.md#SweepType) | [SweepType](COM_Reference/Properties/SweepType_imd_Property.md)  
Power Sweep | [SENSe:IMD:SWEep:TYPE](GP-IB_Command_Finder/Sense/IMD.md#SweepType) | [SweepType](COM_Reference/Properties/SweepType_imd_Property.md)  
CW Time | [SENSe:IMD:SWEep:TYPE](GP-IB_Command_Finder/Sense/IMD.md#SweepType) | [SweepType](COM_Reference/Properties/SweepType_imd_Property.md)  
Segment Sweep | [SENSe:IMD:SWEep:TYPE](GP-IB_Command_Finder/Sense/IMD.md#SweepType) | [SweepType](COM_Reference/Properties/SweepType_imd_Property.md)  
Start | Set DeltaF | [SENS:IMD:FREQ:DFR](GP-IB_Command_Finder/Sense/IMD.md#DFRCW) | [DeltaFrequency](COM_Reference/Properties/DeltaFrequency_Property.md)  
Set Center Freq | [SENS:IMD:FREQ:FCEN](GP-IB_Command_Finder/Sense/IMD.md#FCentCW) | [FrequencyCenter](COM_Reference/Properties/FrequencyCenter_Property.md)  
Start for Center Freq Sweep | [SENS:IMD:FREQ:FCEN:STAR](GP-IB_Command_Finder/Sense/IMD.md#FCentStart) | [FrequencyCenterStart](COM_Reference/Properties/FrequencyCenterStart_Property.md)  
Center for Center Freq Sweep | [SENS:IMD:FREQ:FCEN:CENT](GP-IB_Command_Finder/Sense/IMD.md#FcentCenter) | [FrequencyCenterCenter](COM_Reference/Properties/FrequencyCenterCenter_Property.md)  
Span for Center Freq Sweep | [SENS:IMD:FREQ:FCEN:SPAN](GP-IB_Command_Finder/Sense/IMD.md#FCentSpan) | [FrequencyCenterSpan](COM_Reference/Properties/FrequencyCenterspan_Property.md)  
Start for DeltaF Sweep | [SENS:IMD:FREQ:DFR:STAR](GP-IB_Command_Finder/Sense/IMD.md#DFRStart) | [DeltaFrequencyStart](COM_Reference/Properties/DeltaFrequencyStart_Property.md)  
Set F1 for CW and Power Sweep | [SENS:IMD:FREQ:F1](GP-IB_Command_Finder/Sense/IMD.md#FreqF1) | [F1Frequency](COM_Reference/Properties/F1Frequency_Property.md)  
Set F2 for CW and Power Sweep | [SENS:IMD:FREQ:F2](GP-IB_Command_Finder/Sense/IMD.md#FreqF2) | [F2Frequency](COM_Reference/Properties/F2Frequency_Property.md)  
Stop | Stop for Center Freq Sweep | [SENS:IMD:FREQ:FCEN:STOP](GP-IB_Command_Finder/Sense/IMD.md#FCentStop) | [FrequencyCenterStop](COM_Reference/Properties/FrequencyCenterStop_Property.md)  
Stop for DeltaF Sweep | [SENS:IMD:FREQ:DFR:STOP](GP-IB_Command_Finder/Sense/IMD.md#DFRStop) | [DeltaFrequencyStop](COM_Reference/Properties/DeltaFrequencyStop_Property.md)  
X-axis Type |  | [SENSe:FOM:DISPlay:SELect](GP-IB_Command_Finder/Sense/FOM.md#select) | [DisplayRange](COM_Reference/Properties/DisplayRange_Property.md)  
[IMD Setup...](CF_Setup_Commands_-_IMD.md#Swept_IMD_Setup_Commands) |  |  |   
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
[DC Source...](CF_Sweep_Commands_-_Standard.md#DC_Source) |  |  |   
[Global Source](CF_Sweep_Commands_-_Standard.md#Global_Source) |  |  | 

