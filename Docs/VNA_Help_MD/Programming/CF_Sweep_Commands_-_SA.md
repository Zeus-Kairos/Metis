# Sweep Commands - Spectrum Analyzer Measurement Class

Click [here](CF_Sweep_Commands.md) to view links to Sweep commands for all
Measurement Classes.

Main | Sweep Timing | Source Control | Segment Table | SA Coherence  
---|---|---|---|---  
Main Tab Commands  
---  
Softkey | Sub-item | SCPI | COM  
Number of Points |  | [SENSe:SWEep:POINts](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssp) | [NumberOfPoints](COM_Reference/Properties/Number_of__Points_Property.md)  
Sweep Type | Linear Frequency | [SENSe:SWEep:TYPE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssty) | [SweepType](COM_Reference/Properties/Sweep_Type_Property.md)  
Segment Sweep | [SENSe:SWEep:TYPE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssty) | [SweepType](COM_Reference/Properties/Sweep_Type_Property.md)  
Start |  | [SENSe:FREQuency:STARt](GP-IB_Command_Finder/Sense/Frequency.md#start) | [StartFrequency](COM_Reference/Properties/Start_Frequency_Property.md)  
Stop |  | [SENSe:FREQuency:STOP](GP-IB_Command_Finder/Sense/Frequency.md#stop) | [StopFrequency](COM_Reference/Properties/Stop_Frequency_Property.md)  
X-axis Type |  | [SENSe:FOM:DISPlay:SELect](GP-IB_Command_Finder/Sense/FOM.md#select) | [DisplayRange](COM_Reference/Properties/DisplayRange_Property.md)  
[SA Setup...](CF_Setup_Commands_-_SA.md) |  |  |   
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
Properties  
Autoselect Pulse Detection Method | [SENSe:SWEep:PULSe:DETectmode[:AUTO]](GP-IB_Command_Finder/Sense/SweepPulse.md#detectmode) | [AutoDetection](COM_Reference/Properties/AutoDetection_Property.md)  
Autoselect IF Path Gain and Loss | [SENSe:SWEep:PULSe:IFGain[:AUTO]](GP-IB_Command_Finder/Sense/SweepPulse.md#IFGain) | None  
IF Path... | [SENSe:PATH:CONFig:ELEMent[:STATe]](GP-IB_Command_Finder/Sense/Path.md#state) | [Element](COM_Reference/Properties/Element_Property.md)  
Optimize Pulse Frequency | [SENSe:SWEep:PULSe:PRF[:AUTO]](GP-IB_Command_Finder/Sense/SweepPulse.md#prf) | [AutoOptimizePRF](COM_Reference/Properties/AutoOptimizePRF_Property.md)  
Autoselect Profile Sweep Time | [SENSe:SWEep:PULSe:MODE](GP-IB_Command_Finder/Sense/SweepPulse.md#mode) | [PulseMeasMode](COM_Reference/Properties/PulseMeasMode_Property.md)  
IFBW | [SENSe:SWEep:PULSe:CWTime[:AUTO]](GP-IB_Command_Finder/Sense/SweepPulse.md#CWSweepAuto) | [AutoCWSweepTime](COM_Reference/Properties/AutoCWSweepTime_Property.md)  
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
Frequency | [SENSe:SWEep:PULSe:MASTer:FREQuency](GP-IB_Command_Finder/Sense/SweepPulse.md#MasterFreq) | [MasterFrequency](COM_Reference/Properties/MasterFrequency_Property.md)  
Period | [SENSe:SWEep:PULSe:MASTer:PERiod](GP-IB_Command_Finder/Sense/SweepPulse.md#MasterPeriod) | [MasterPeriod](COM_Reference/Properties/MasterPeriod_Property.md)  
Enable Source x Modulator | [SENSe:PATH:CONFig:ELEMent[:STATe]](GP-IB_Command_Finder/Sense/Path.md#state) | [Element](COM_Reference/Properties/Element_Property.md)  
Modulator Drive | [SENSe:PATH:CONFig:ELEMent[:STATe]](GP-IB_Command_Finder/Sense/Path.md#state) | [Element](COM_Reference/Properties/Element_Property.md)  
Offset Pulse using Modulator and ADC Delays | [SENSe:PULSe:HWDelay[:STATe]](GP-IB_Command_Finder/Sense/Pulse.md#SENSe:PULSe:HWDelay:STATe) | [EnableOffsetDelays](COM_Reference/Properties/EnableOffsetDelays_Property.md)  
Modulator Delay | [SENSe:PULSe:HWDelay:MODulator](GP-IB_Command_Finder/Sense/Pulse.md#SENSe:PULSe:HWDelay:MODulator) | [ModulatorDelay](COM_Reference/Properties/ModulatorDelay_Property.md)  
Fixed ADC Delay | [SENSe:PULSe:HWDelay:ADC?](GP-IB_Command_Finder/Sense/Pulse.md#SENSe:PULSe:HWDelay:ADC) | [FixedADCDelay](COM_Reference/Properties/FixedADCDelay_Property.md)  
Synchronize ADCs using pulse trigger | [SENSe:PATH:CONFig:ELEMent[:STATe]](GP-IB_Command_Finder/Sense/Path.md#state) | [Element](COM_Reference/Properties/Element_Property.md)  
Pulse4 Output Indicates ADC Activity | [SENSe:PULSe4:OPTion](GP-IB_Command_Finder/Sense/Pulse.md#SENSe:PULSe4:OPTion) | [Pulse4OutAsADCActivity](COM_Reference/Properties/Pulse4OutAsADCActivity_Property.md)  
Pulse Trigger... |  |   
Trigger Source | [SENSe:PATH:CONFig:ELEMent[:STATe]](GP-IB_Command_Finder/Sense/Path.md#state) | [Element](COM_Reference/Properties/Element_Property.md)  
Trigger Level/Edge | [SENSe:PULSe:TTYPe](GP-IB_Command_Finder/Sense/Pulse.md#TType) | [TriggerInType](COM_Reference/Properties/TriggerInType_Property.md)  
Synchronize ADCs using pulse trigger | [SENSe:PULSe[:STATe]](GP-IB_Command_Finder/Sense/Pulse.md#state) | [State](COM_Reference/Properties/State_pulse_Property.md)  
[Trigger...](CF_Trigger_Commands.md) |  |   
[DC Source...](CF_Sweep_Commands_-_Standard.md#DC_Source) |  |  |   
[Global Source](CF_Sweep_Commands_-_Standard.md#Global_Source) |  |  |   
Segment Table Tab Commands  
Softkey | Sub-item | SCPI | COM  
Add Segment |  | [SENSe:SEGMent:ADD](GP-IB_Command_Finder/Sense/Segment.md#add) | [Add](COM_Reference/Methods/Add_segments_Method.md)  
Insert Segment |  | None | None  
Delete Segment |  | [SENSe:SEGMent:DELete](GP-IB_Command_Finder/Sense/Segment.md#del) | [Remove](COM_Reference/Methods/Remove_Method.md)  
Delete All Segments |  | [SENSe:SEGMent:DELete:ALL](GP-IB_Command_Finder/Sense/Segment.md#delall) | None  
Segment Table... | X-Axis Point Spacing | [SENSe:SEGMent:X:SPACing](GP-IB_Command_Finder/Sense/Segment.md#X AXIS) | [XAxisPointSpacing](COM_Reference/Properties/XAxisPointSpacing_Property.md)  
Allow Arbitrary Segments | [SENSe:SEGMent:ARBitrary](GP-IB_Command_Finder/Sense/Segment.md#arb) | [AllowArbitrarySegments](COM_Reference/Properties/AllowArbitrarySegments_Property.md)  
Display Center/Span Freq | [SENSe:SEGMent:FREQuency:CENTer](GP-IB_Command_Finder/Sense/Segment.md#cent) [SENSe:SEGMent:FREQuency:SPAN](GP-IB_Command_Finder/Sense/Segment.md#span) | [CenterFrequency](COM_Reference/Properties/CenterFreq_Property.md) [FrequencySpan](COM_Reference/Properties/Frequency_Span_Property.md)  
Save Table | None | None  
Load Table | None | None  
Independent Settings Per Segment |  |   
Vector Averaging | [SENSe:SEGMent:SA:VAVerage](GP-IB_Command_Finder/Sense/Segment.md#SENSe:SEGMent:SA:VAVerage) [SENSe:SEGMent:SA:VAVerage:CONTrol](GP-IB_Command_Finder/Sense/Segment.md#SENSe:SEGMent:SA:VAVerage:CONTrol) | [SAVectorAverage](COM_Reference/Properties/SAVectorAverage_Property.md) [SAVectorAverageOption](COM_Reference/Properties/SAVectorAverageOption_Property.md)  
Video Bandwidth | [SENSe:SEGMent:SA:VIDeobw](GP-IB_Command_Finder/Sense/Segment.md#SENSe:SEGMent:SA:VIDeobw) [SENSe:SEGMent:SA:VIDeobw:CONTrol](GP-IB_Command_Finder/Sense/Segment.md#SENSe:SEGMent:SA:VIDeobw:CONTrol) | [SAVideoBandwidth](COM_Reference/Properties/SAVideoBandwidth_Property.md) [SAVideoAverageOption](COM_Reference/Properties/SAVectorAverageOption_Property.md)  
Reference Tone | [SENSe:SEGMent:SA:MTReference](GP-IB_Command_Finder/Sense/Segment.md#SENSe:SEGMent:SA:MTReference) [SENSe:SEGMent:SA:MTReference:CONTrol](GP-IB_Command_Finder/Sense/Segment.md#SENSe:SEGMent:SA:MTReference:CONTrol) [SENSe:SEGMent:SA:MTReference:MAX?](GP-IB_Command_Finder/Sense/Segment.md#SENSe:SEGMent:SA:MTReference:MAX) [SENSe:SEGMent:SA:MTReference:MIN?](GP-IB_Command_Finder/Sense/Segment.md#SENSe:SEGMent:SA:MTReference:MIN) | [SAMTReference](COM_Reference/Properties/SAMTReference_Property.md) [SAMTReferenceFreqOption](COM_Reference/Properties/SAMTReferenceFreqOption_Property.md)  
SA Data Threshold | [SENSe:SEGMent:SA:DTHReshold](GP-IB_Command_Finder/Sense/Segment.md#SENSe:SEGMent:SA:DTHReshold) [SENSe:SEGMent:SA:DTHReshold:CONTrol](GP-IB_Command_Finder/Sense/Segment.md#SENSe:SEGMent:SA:DTHReshold:CONTrol) | [SADataThreshold](COM_Reference/Properties/SADataThreshold_Property.md) [SADataThresholdOption](COM_Reference/Properties/SADataThresholdOption_Property.md)  
Show Table | Auto | None | None  
On | [DISPlay:WINDow:TABLe](GP-IB_Command_Finder/Display.md#tabl) | [ShowTable](COM_Reference/Methods/Show_Table_Method.md)  
SA Coherence Tab Commands  
Softkey | Sub-item | SCPI | COM  
SA Multitone | On/Off | [SENSe:SA:IMAGe:COHerence[:STATe]](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:IMAGe:COHerence:STATe) | [MultiToneImageRejectEnable](COM_Reference/Properties/MultiToneImageRejectEnable_Property.md)  
Tone Spacing |  | [SENSe:SA:IMAGe:COHerence:SPACing](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:IMAGe:COHerence:SPACing) | [MultiToneImageRejectSpacing](COM_Reference/Properties/MultiToneImageRejectSpacing_Property.md)  
Reference Tone |  | [SENSe:SA:IMAGe:COHerence:REFerence](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:IMAGe:COHerence:REFerence) | [MultiToneImageRejectReference](COM_Reference/Properties/MultiToneImageRejectReference_Property.md)  
Data Display | Show All | [SENSe:SA:IMAGe:COHerence:DATa](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:IMAGe:COHerence:DATa) | [MultiToneImageRejectDataDisplay](COM_Reference/Properties/MultiToneImageRejectDataDisplay_Property.md)  
Zero the Non-Tones | [SENSe:SA:IMAGe:COHerence:DATa](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:IMAGe:COHerence:DATa) | [MultiToneImageRejectDataDisplay](COM_Reference/Properties/MultiToneImageRejectDataDisplay_Property.md)  
Detector Bypass | On/Off | [SENSe:SA:DETector:BYPass:[STATe]](GP-IB_Command_Finder/Sense/SA.md#detBypassState) | [EnableDetectorBypass](COM_Reference/Properties/DetectorBypassState_Property.md)  
| Reject up to harmonic | [SENSe:SA:IMAGe:COHerence:HREJect](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:IMAGe:COHerence:HREJect) | [MultiToneImageRejectHarmonic](COM_Reference/Properties/MultiToneImageRejectHarmonic_Property.md)

