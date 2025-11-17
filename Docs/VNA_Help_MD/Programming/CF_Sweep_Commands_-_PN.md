# Sweep Commands - Phase Noise Measurement Class

Click [here](CF_Sweep_Commands.md) to view links to Sweep commands for all
Measurement Classes.

Main | Sweep Timing | Source Control  
---|---|---  
Main Tab Commands  
---  
Softkey | Sub-item | SCPI | COM  
Number of Points |  | [SENSe:SWEep:POINts](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssp) | [NumberOfPoints](COM_Reference/Properties/Number_of__Points_Property.md)  
Start |  | [SENSe:FREQuency:STARt](GP-IB_Command_Finder/Sense/Frequency.md#start) | [StartFrequency](COM_Reference/Properties/Start_Frequency_Property.md)  
Stop |  | [SENSe:FREQuency:STOP](GP-IB_Command_Finder/Sense/Frequency.md#stop) | [StopFrequency](COM_Reference/Properties/Stop_Frequency_Property.md)  
[Phase Noise Setup...](CF_Setup_Commands_-_PN.md) |  |  |   
Sweep Timing Tab Commands  
Softkey | Sub-item | SCPI | COM  
Sweep Time | Auto | [SENSe:SWEep:TIME:AUTO](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssta) | [chan.SweepTime](COM_Reference/Properties/Sweep_Time_Property.md)  
Manual | [SENSe:SWEep:TIME[:STOP]](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#sst) | [chan.SweepTime](COM_Reference/Properties/Sweep_Time_Property.md)  
Dwell Time |  | [SENSe:SWEep:DWELl](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssd) | [DwellTime](COM_Reference/Properties/Dwell_Time_Property.md)  
Sweep Delay |  | [SENSe:SWEep:DWELl:SDELay](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#SweepDelay) | [SweepDelay](COM_Reference/Properties/Sweep_Delay_Property.md)  
Sweep Mode | AUTO | [SENSe:SWEep:GENeration](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssg) | [SweepGenerationMode](COM_Reference/Properties/Sweep_Generation_Mode_Property.md)  
STEPPED | [SENSe:SWEep:GENeration](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssg) | [SweepGenerationMode](COM_Reference/Properties/Sweep_Generation_Mode_Property.md)  
Sweep Sequence | STD | [SENSe:SWEep:GENeration:POINtsweep](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#GenPoint) | [PointSweepState](COM_Reference/Properties/PointSweepState_Property.md)  
POINT | [SENSe:SWEep:GENeration:POINtsweep](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#GenPoint) | [PointSweepState](COM_Reference/Properties/PointSweepState_Property.md)  
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
Properties  
Autoselect Pulse Detection Method | [SENSe:SWEep:PULSe:DETectmode[:AUTO]](GP-IB_Command_Finder/Sense/SweepPulse.md#detectmode) | [AutoDetection](COM_Reference/Properties/AutoDetection_Property.md)  
Narrowband | [SENSe:SWEep:PULSe:WIDeband[:STATe]](GP-IB_Command_Finder/Sense/SweepPulse.md#wideband) | [WideBandDectionState](COM_Reference/Properties/WideBandDectionState_Property.md)  
Wideband | [SENSe:SWEep:PULSe:WIDeband[:STATe]](GP-IB_Command_Finder/Sense/SweepPulse.md#wideband) | [WideBandDectionState](COM_Reference/Properties/WideBandDectionState_Property.md)  
SW Gating | [SENSe:SWEep:PULSe:SWGate](GP-IB_Command_Finder/Sense/SweepPulse.md#swgate) | [SoftwareGateState](COM_Reference/Properties/SoftwareGateState_Property.md)  
Autoselect IF Path Gain and Loss | [SENSe:SWEep:PULSe:IFGain[:AUTO]](GP-IB_Command_Finder/Sense/SweepPulse.md#IFGain) | None  
IF Path... | [SENSe:PATH:CONFig:ELEMent[:STATe]](GP-IB_Command_Finder/Sense/Path.md#state) | [Element](COM_Reference/Properties/Element_Property.md)  
Optimize Pulse Frequency | [SENSe:SWEep:PULSe:PRF[:AUTO]](GP-IB_Command_Finder/Sense/SweepPulse.md#prf) | [AutoOptimizePRF](COM_Reference/Properties/AutoOptimizePRF_Property.md)  
Autoselect Profile Sweep Time | [SENSe:SWEep:PULSe:MODE](GP-IB_Command_Finder/Sense/SweepPulse.md#mode) | [PulseMeasMode](COM_Reference/Properties/PulseMeasMode_Property.md)  
IFBW | [SENSe:SWEep:PULSe:CWTime[:AUTO]](GP-IB_Command_Finder/Sense/SweepPulse.md#CWSweepAuto) | [AutoIFBandWidth](COM_Reference/Properties/AutoIFBandWidth_Property.md)  
Sweep Time | [SENSe:SWEep:TIME](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#sst) | [chan.SweepTime](COM_Reference/Properties/Sweep_Time_Property.md)  
Number of Points | [SENSe:SWEep:POINts](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssp) | [NumberOfPoints](COM_Reference/Properties/Number_of__Points_Property.md)  
|  | PulseOffAlcMode  
Measurement Timing  
Width | [SENSe:SWEep:PULSe:TIMing](GP-IB_Command_Finder/Sense/SweepPulse.md#timing) | [AutoPulseTiming](COM_Reference/Properties/AutoPulseTiming_Property.md)  
Delay | [SENSe:SWEep:PULSe:TIMing](GP-IB_Command_Finder/Sense/SweepPulse.md#timing) | [AutoPulseTiming](COM_Reference/Properties/AutoPulseTiming_Property.md)  
Pulse Gen | [SENSe:SWEep:PULSe:MODE](GP-IB_Command_Finder/Sense/SweepPulse.md#mode) | [PulseMeasMode](COM_Reference/Properties/PulseMeasMode_Property.md)  
Master Pulse Trigger | [SENSe:PATH:CONFig:ELEMent[:STATe]](GP-IB_Command_Finder/Sense/Path.md#state) | [Element](COM_Reference/Properties/Element_Property.md)  
Autoselect Width & Delay | [SENSe:SWEep:PULSe:TIMing](GP-IB_Command_Finder/Sense/SweepPulse.md#timing) | [AutoPulseTiming](COM_Reference/Properties/AutoPulseTiming_Property.md)  
Autoselect Pulse Generators | [SENSe:SWEep:PULSe:DRIVe[:AUTO]](GP-IB_Command_Finder/Sense/SweepPulse.md#drive) | [AutoSelectPulseGen](COM_Reference/Properties/AutoSelectPulseGen_Property.md)  
Pulse Generators...  
Width | [SENSe:PULSe:WIDTh](GP-IB_Command_Finder/Sense/Pulse.md#width) | [Width](COM_Reference/Properties/Width_Property.md)  
Delay | [SENSe:PULSe:DELay](GP-IB_Command_Finder/Sense/Pulse.md#delay) | [Delay](COM_Reference/Properties/Delay_pulse_Property.md)  
Invert | [SENSe:PULSe:INVert](GP-IB_Command_Finder/Sense/Pulse.md#invert) | [Invert](COM_Reference/Properties/Invert_Property.md)  
Enable | [SENSe:PULSe[:STATe]](GP-IB_Command_Finder/Sense/Pulse.md#state) | [State](COM_Reference/Properties/State_pulse_Property.md)  
Trigger | [SENSe:PATH:CONFig:ELEMent[:STATe]](GP-IB_Command_Finder/Sense/Path.md#state) | [Element](COM_Reference/Properties/Element_Property.md)  
Frequency | [SENSe:SWEep:PULSe:PRIMary:FREQuency](GP-IB_Command_Finder/Sense/SweepPulse.md#MasterFreq) | [PrimaryFrequency](COM_Reference/Properties/MasterFrequency_Property.md)  
Period | [SENSe:SWEep:PULSe:PRIMary:PERiod](GP-IB_Command_Finder/Sense/SweepPulse.md#MasterPeriod) | [PrimaryPeriod](COM_Reference/Properties/MasterPeriod_Property.md)  
Enable Source x Modulator | [SENSe:PATH:CONFig:ELEMent[:STATe]](GP-IB_Command_Finder/Sense/Path.md#state) | [Element](COM_Reference/Properties/Element_Property.md)  
Modulator Drive | [SENSe:PATH:CONFig:ELEMent[:STATe]](GP-IB_Command_Finder/Sense/Path.md#state) | [Element](COM_Reference/Properties/Element_Property.md)  
Offset Pulse using Modulator and ADC Delays | [SENSe:PULSe:HWDelay[:STATe]](GP-IB_Command_Finder/Sense/Pulse.md#SENSe:PULSe:HWDelay:STATe) | [EnableOffsetDelays](COM_Reference/Properties/EnableOffsetDelays_Property.md)  
Modulator Delay | [SENSe:PULSe:HWDelay:MODulator](GP-IB_Command_Finder/Sense/Pulse.md#SENSe:PULSe:HWDelay:MODulator) | [ModulatorDelay](COM_Reference/Properties/ModulatorDelay_Property.md)  
Fixed ADC Delay | [SENSe:PULSe:HWDelay:ADC?](GP-IB_Command_Finder/Sense/Pulse.md#SENSe:PULSe:HWDelay:ADC) | [FixedADCDelay](COM_Reference/Properties/FixedADCDelay_Property.md)  
Synchronize ADCs using pulse trigger | [SENSe:PATH:CONFig:ELEMent[:STATe]](GP-IB_Command_Finder/Sense/Path.md#state) | [Element](COM_Reference/Properties/Element_Property.md)  
Pulse4 Output Indicates | [SENSe:PULSe4:OPTion](GP-IB_Command_Finder/Sense/Pulse.md#SENSe:PULSe4:OPTion) | [Pulse4OutAsADCActivity](COM_Reference/Properties/Pulse4OutAsADCActivity_Property.md)  
All ADC Activity | [SENSe:PULSe4:OPTion:MODE ALL](GP-IB_Command_Finder/Sense/Pulse.md#SENSe:PULSe4:OPTion:MODE) | None  
Trace ADC Activity | [SENSe:PULSe4:OPTion:MODE TRACe](GP-IB_Command_Finder/Sense/Pulse.md#SENSe:PULSe4:OPTion:MODE) | None  
Pulse Trigger... |  |   
Trigger Source | [SENSe:PATH:CONFig:ELEMent[:STATe]](GP-IB_Command_Finder/Sense/Path.md#state) | [Element](COM_Reference/Properties/Element_Property.md)  
Trigger Level/Edge | [SENSe:PULSe:TTYPe](GP-IB_Command_Finder/Sense/Pulse.md#TType) | [TriggerInType](COM_Reference/Properties/TriggerInType_Property.md)  
Synchronize ADCs using pulse trigger | [SENSe:PULSe[:STATe]](GP-IB_Command_Finder/Sense/Pulse.md#state) | [State](COM_Reference/Properties/State_pulse_Property.md)  
[Trigger...](CF_Trigger_Commands.md) |  |   
DC Source... | Enable DC Outputs | [SOURce:DC:ENABle](GP-IB_Command_Finder/SourceDC.md#Enable) | [EnableAllOutput](COM_Reference/Properties/EnableAllOutput_Property.md)  
State | [SOURce:DC:STATe](GP-IB_Command_Finder/SourceDC.md#state) | [State](COM_Reference/Properties/State_DC_Property.md)  
Start DC | [SOURce:DC:STARt](GP-IB_Command_Finder/SourceDC.md#start) | [Start](COM_Reference/Properties/Start_DC_Property.md)  
Stop DC | [SOURce:DC:STOP](GP-IB_Command_Finder/SourceDC.md#stop) | [Stop](COM_Reference/Properties/Stop_DC_Property.md)  
Limits...  
State | [SOURce:DC:STATe](GP-IB_Command_Finder/SourceDC.md#state) | [State](COM_Reference/Properties/State_DC_Property.md)  
Min | [SOURce:DC:LIMIt:MINimum](GP-IB_Command_Finder/SourceDC.md#SOURce:DC:LIMit:MINimum) | [LimitMin](COM_Reference/Properties/LimitMin_Property.md)  
Max | [SOURce:DC:LIMIt:MAXimum](GP-IB_Command_Finder/SourceDC.md#SOURce:DC:LIMit:MAXimum) | [LimitMax](COM_Reference/Properties/LimitMax_Property.md)

