# Sweep Commands - Modulation Distortion and Modulation Distortion Converters
Measurement Class

Click [here](CF_Sweep_Commands.md) to view links to Sweep commands for all
Measurement Classes.

Main | Sweep Timing | Source Control  
---|---|---  
Main Tab Commands  
---  
Softkey | Sub-item | SCPI | COM  
Number of Points |  | [SENSe:SWEep:POINts](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssp) | [NumberOfPoints](COM_Reference/Properties/Number_of__Points_Property.md)  
Sweep Type | Fixed | [SENSe:SWEep:TYPE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssty) | [SweepType](COM_Reference/Properties/Sweep_Type_Property.md)  
Power | [SENSe:SWEep:TYPE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssty) | [SweepType](COM_Reference/Properties/Sweep_Type_Property.md)  
Start |  | [SENSe:FREQuency:STARt](GP-IB_Command_Finder/Sense/Frequency.md#start) | [StartFrequency](COM_Reference/Properties/Start_Frequency_Property.md)  
Stop |  | [SENSe:FREQuency:STOP](GP-IB_Command_Finder/Sense/Frequency.md#stop) | [StopFrequency](COM_Reference/Properties/Stop_Frequency_Property.md)  
X-axis Type... | Select | [DISPlay:WINDow:TRACe[:STATe]](GP-IB_Command_Finder/Display.md#tstat) | [View](COM_Reference/Properties/View_Property.md)  
Sweep Type | [SENSe:DISTortion:SWEep:TYPE](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:TYPE) | None  
X-axis Type | [CALCulate:MEASure:DATA:X:AXIS](GP-IB_Command_Finder/Calculate/MeasureDATA.md#CALCulate:MEASure:DATA:X:AXiS) | None  
Fixed Parameters (Power Sweep only) Parameter Value |  [CALCulate:MEASure:DATA:X:AXIS:FIXed:PARameter](GP-IB_Command_Finder/Calculate/MeasureDATA.md#CALCulate:MEASure:DATA:X:AXIS:FIXed:PARameter) [CALCulate:MEASure:DATA:X:AXIS:FIXed:PARameter:VALue](GP-IB_Command_Finder/Calculate/MeasureDATA.md#CALCulate:MEASure:DATA:X:AXIS:FIXed:PARameter:VALue) |  None None  
[MOD Setup...](CF_Setup_Commands_-_MOD.md) |  |  |   
[MODX Setup...](CF_Setup_Commands_-_MOD.md) |  |  |   
Sweep Timing Tab Commands  
Softkey | Sub-item | SCPI | COM  
Sweep Delay |  | [SENSe:SWEep:DWELl:SDELay](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#SweepDelay) | [SweepDelay](COM_Reference/Properties/Sweep_Delay_Property.md)  
Dist Meas Delay |  | [SENSe:DISTortion:SWEep:DWELl](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:DWELl) | None  
Re-use S-Param |  | [SENSe:DISTortion:SWEep:SPARam:REUSe](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:SPARam:REUSe) | None  
Source Control Tab Commands  
Softkey | Sub-item | SCPI | COM  
[Source Modulation...](CF_Setup_Commands_-_MOD.md#Modulate_Tab) |  |  |   
Pulse Setup... | Pulse Measurement  
Off | [SENSe:SWEep:PULSe:MODE](GP-IB_Command_Finder/Sense/SweepPulse.md#mode) | [PulseMeasMode](COM_Reference/Properties/PulseMeasMode_Property.md)  
Standard Pulse | [SENSe:SWEep:PULSe:MODE](GP-IB_Command_Finder/Sense/SweepPulse.md#mode) | [PulseMeasMode](COM_Reference/Properties/PulseMeasMode_Property.md)  
Pulse Timing  
RF Pulse Width | [SENSe:SWEep:PULSe:PRIMary:WIDth](GP-IB_Command_Finder/Sense/SweepPulse.md#MasterWidth) | [PrimaryWidth](COM_Reference/Properties/MasterWidth_Property.md)  
Pulse Period | [SENSe:SWEep:PULSe:PRIMaryPERiod](GP-IB_Command_Finder/Sense/SweepPulse.md#MasterPeriod) | [PrimaryPeriod](COM_Reference/Properties/MasterPeriod_Property.md)  
|  |   
|  |   
Measurement Timing  
Device | [SENSe:PULSe:MTIMing:DEVice](GP-IB_Command_Finder/Sense/Pulse.md#SENSe:PULSe:MTIMing:DEVice) | [PulseTimingDevice](COM_Reference/Properties/PulseTimingDevice_Property.md)  
Width | [SENSe:SWEep:PULSe:PRIMary:WIDth](GP-IB_Command_Finder/Sense/SweepPulse.md#MasterWidth) | [PrimaryWidth](COM_Reference/Properties/MasterWidth_Property.md)  
Delay | None | None  
Invert | [SENSe:PULSe:INVert](GP-IB_Command_Finder/Sense/Pulse.md#invert) | [Invert](COM_Reference/Properties/Invert_Property.md)  
Enable | [SENSe:PULSe[:STATe]](GP-IB_Command_Finder/Sense/Pulse.md#state) | [State](COM_Reference/Properties/State_pulse_Property.md)  
Autoselect Receiver Timing | [SENse:DISTortion:PULSe:RECeiver:AUTO](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:PULSe:RECeiver:AUTO) | None  
Offset Pulses using ADC Delay | [SENSe:PULSe:HWDelay[:STATe]](GP-IB_Command_Finder/Sense/Pulse.md#SENSe:PULSe:HWDelay:STATe) | [EnableOffsetDelays](COM_Reference/Properties/EnableOffsetDelays_Property.md)  
Plot Pulse Timing... | None | None  
Pulse Generators...  
Width | [SENSe:PULSe:WIDTh](GP-IB_Command_Finder/Sense/Pulse.md#width) | [Width](COM_Reference/Properties/Width_Property.md)  
Delay | [SENSe:PULSe:DELay](GP-IB_Command_Finder/Sense/Pulse.md#delay) | [Delay](COM_Reference/Properties/Delay_pulse_Property.md)  
Invert | [SENSe:PULSe:INVert](GP-IB_Command_Finder/Sense/Pulse.md#invert) | [Invert](COM_Reference/Properties/Invert_Property.md)  
Enable | [SENSe:PULSe[:STATe]](GP-IB_Command_Finder/Sense/Pulse.md#state) | [State](COM_Reference/Properties/State_pulse_Property.md)  
Trigger | [SENSe:PATH:CONFig:ELEMent[:STATe]](GP-IB_Command_Finder/Sense/Path.md#state) | [Element](COM_Reference/Properties/Element_Property.md)  
Frequency | [SENSe:SWEep:PULSe:PRIMary:FREQuency](GP-IB_Command_Finder/Sense/SweepPulse.md#MasterFreq) | [PrimaryFrequency](COM_Reference/Properties/MasterFrequency_Property.md)  
Period | [SENSe:SWEep:PULSe:PRIMary:PERiod](GP-IB_Command_Finder/Sense/SweepPulse.md#MasterPeriod) | [PrimaryPeriod](COM_Reference/Properties/MasterPeriod_Property.md)  
Enable Source x Modulator | [SENSe:PATH:CONFig:ELEMent[:STATe]](GP-IB_Command_Finder/Sense/Path.md#state) | [Element](COM_Reference/Properties/Element_Property.md)  
ALC Open Loop | [SOURce:POWer:ALC[:MODE]](GP-IB_Command_Finder/source.md#ALCMode) | [ALCLevelingMode](COM_Reference/Properties/ALCLevelingMode_Property.md)  
Modulator Drive | [SENSe:PATH:CONFig:ELEMent[:STATe]](GP-IB_Command_Finder/Sense/Path.md#state) | [Element](COM_Reference/Properties/Element_Property.md)  
Offset Pulse using ADC Delay and RF Modulator Delay | [SENSe:PULSe:HWDelay[:STATe]](GP-IB_Command_Finder/Sense/Pulse.md#SENSe:PULSe:HWDelay:STATe) | [EnableOffsetDelays](COM_Reference/Properties/EnableOffsetDelays_Property.md)  
Modulator Delay | [SENSe:PULSe:HWDelay:MODulator](GP-IB_Command_Finder/Sense/Pulse.md#SENSe:PULSe:HWDelay:MODulator) | [ModulatorDelay](COM_Reference/Properties/ModulatorDelay_Property.md)  
Synchronize ADCs using Pulse Trigger | [SENSe:PATH:CONFig:ELEMent[:STATe]](GP-IB_Command_Finder/Sense/Path.md#state) | [Element](COM_Reference/Properties/Element_Property.md)  
Pulse4 Output Indicates ADC Activity | [SENSe:PULSe4:OPTion](GP-IB_Command_Finder/Sense/Pulse.md#SENSe:PULSe4:OPTion) | [Pulse4OutAsADCActivity](COM_Reference/Properties/Pulse4OutAsADCActivity_Property.md)  
Pulse Trigger... |  |   
Trigger Source | [SENSe:PATH:CONFig:ELEMent[:STATe]](GP-IB_Command_Finder/Sense/Path.md#state) | [Element](COM_Reference/Properties/Element_Property.md)  
Trigger Level/Edge | [SENSe:PULSe:TTYPe](GP-IB_Command_Finder/Sense/Pulse.md#TType) | [TriggerInType](COM_Reference/Properties/TriggerInType_Property.md)  
Synchronize ADCs using pulse trigger | [SENSe:PULSe[:STATe]](GP-IB_Command_Finder/Sense/Pulse.md#state) | [State](COM_Reference/Properties/State_pulse_Property.md)  
[Trigger...](CF_Trigger_Commands.md) |  |   
DC Source... | On/Off | [SOURce:DC:STATe](GP-IB_Command_Finder/SourceDC.md#state) | [State](COM_Reference/Properties/State_DC_Property.md)

