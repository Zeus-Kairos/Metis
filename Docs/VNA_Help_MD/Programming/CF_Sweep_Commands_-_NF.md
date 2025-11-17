# Sweep Commands - Noise Figure Cold Source Measurement Class

Only the Main, Sweep Timing, and Source Control Sweep commands corresponding
to the Noise Figure Cold Source measurement class are documented here. The
Segment Table commands are identical to the Sweep commands for the Standard
measurement class and can be accessed by clicking [here](CF_Sweep_Commands_-
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
Sweep Type | Linear Frequency | [SENSe:SWEep:TYPE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssty) | [SweepType](COM_Reference/Properties/Sweep_Type_Property.md)  
Log Frequency | [SENSe:SWEep:TYPE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssty) | [SweepType](COM_Reference/Properties/Sweep_Type_Property.md)  
CW Time | [SENSe:SWEep:TYPE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssty) | [SweepType](COM_Reference/Properties/Sweep_Type_Property.md)  
Segment Sweep | [SENSe:SWEep:TYPE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssty) | [SweepType](COM_Reference/Properties/Sweep_Type_Property.md)  
Start |  | [SENSe:FREQuency:STARt](GP-IB_Command_Finder/Sense/Frequency.md#start) | [StartFrequency](COM_Reference/Properties/Start_Frequency_Property.md)  
Stop |  | [SENSe:FREQuency:STOP](GP-IB_Command_Finder/Sense/Frequency.md#stop) | [StopFrequency](COM_Reference/Properties/Stop_Frequency_Property.md)  
X-axis Type |  | [SENSe:FOM:DISPlay:SELect](GP-IB_Command_Finder/Sense/FOM.md#select) | [DisplayRange](COM_Reference/Properties/DisplayRange_Property.md)  
[NF Setup...](CF_Setup_Commands_-_NF.md#NF_Setup...) |  |  |   
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
Frequency Offset... | Frequency Offset (ON/OFF) | [SENSe:FOM[:STATe]](GP-IB_Command_Finder/Sense/FOM.md#state) | [State](COM_Reference/Properties/State_Property.md)  
Mode - Coupled and Un-coupled | [SENSe:FOM:RANGe:COUPled](GP-IB_Command_Finder/Sense/FOM.md#coupled) | [Coupled](COM_Reference/Properties/Coupled_Property.md)  
Sweep Type | [SENSe:FOM:RANGe:SWEep:TYPE](GP-IB_Command_Finder/Sense/FOM.md#SwpType) | [SweepType](COM_Reference/Properties/Sweep_Type_Property.md)  
Settings |  |   
Start | [SENSe:FOM:RANGe:FREQuency:STARt](GP-IB_Command_Finder/Sense/FOM.md#FStart) | [StartFrequency](COM_Reference/Properties/Start_Frequency_Property.md)  
Stop | [SENSe:FOM:RANGe:FREQuency:STOP](GP-IB_Command_Finder/Sense/FOM.md#FStart) | [StopFrequency](COM_Reference/Properties/Stop_Frequency_Property.md)  
Annotation - Primary, Source, and Receivers | [SENSe:FOM:RANGe:NAME?](GP-IB_Command_Finder/Sense/FOM.md#FStart) | [Name](COM_Reference/Properties/Name_FOMRange_Property.md)  
X-Axis Point Spacing | [SENSe:FOM:RANGe:SEGMent:SWEep:POINts](GP-IB_Command_Finder/Sense/FOMSegm.md#Points) | [NumberOfPoints](COM_Reference/Properties/Number_of__Points_Property.md)  
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

