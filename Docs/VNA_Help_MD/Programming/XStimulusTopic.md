[File](FileTopic.md) | [Instrument](XTraceChanTopic.md) | [Response](XResponseTopic.md) | [Stimulus](XStimulusTopic.md) | [Utility](XUtilityTopic.md) | [Cal](CalTopic.md) | [Apps](MixerTopic.md) | [Remote ONLY](DataTopic.md)

* * *

[Frequency](XStimulusTopic.md#Frequency) | [Offset](XStimulusTopic.md#Offset) | [Power](XStimulusTopic.md#Power) | [ALC](XStimulusTopic.md#ALC) | [Recvr Lvl](XStimulusTopic.md#ReceiverLevel) | [Source Ports](XStimulusTopic.md#sourceports)| [# Points](XStimulusTopic.md#Sweep) | [Trigger](XStimulusTopic.md#Trigger) :[Ext](XStimulusTopic.md#ExtTrig) | Auxiliary Trigger  
Sweep settings:..[Time](XStimulusTopic.md#Sweep) | [Setup](XStimulusTopic.md#Setup) | [Segment](XStimulusTopic.md#seg) | Power | [Phase](XStimulusTopic.md#Phase) | Pulse Setup | [DC Sources](XStimulusTopic.md#DC) | Multi-Dimensional Sweep | Global Source

See [Remotely Specifying a Source Port](Remotely_Specifying_a_Source_Port.md)
.

Description |  SCPI |  COM  
---|---|---  
Frequency  
Start Freq |  [SENSe:FREQuency:STARt](GP-IB_Command_Finder/Sense/Frequency.md#start) |  [chan.StartFrequency](COM_Reference/Properties/Start_Frequency_Property.md)  
Stop Freq |  [SENSe:FREQuency:STOP](GP-IB_Command_Finder/Sense/Frequency.md#stop) |  [chan.StopFrequency](COM_Reference/Properties/Stop_Frequency_Property.md)  
Center Freq |  [SENSe:FREQuency:CENTer](GP-IB_Command_Finder/Sense/Frequency.md#cent) |  [chan.CenterFrequency](COM_Reference/Properties/CenterFreq_Property.md)  
Span |  [SENSe:FREQuency:SPAN](GP-IB_Command_Finder/Sense/Frequency.md#span) |  [chan.FrequencySpan](COM_Reference/Properties/Frequency_Span_Property.md)  
CW Frequency |  [SENSe:FREQuency:CW](GP-IB_Command_Finder/Sense/Frequency.md#cw) |  [chan.CWFrequency](COM_Reference/Properties/CW_Frequency_Property.md)  
Number of Points |  [SENSe:SWEep:POINts](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssp) |  [chan.NumberOfPoints](COM_Reference/Properties/Number_of__Points_Property.md)  
Step size |  [SENSe:SWEep:STEP](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#Step) |  [FrequencyStep Property](COM_Reference/Properties/FrequencyStep_Property.md)  
  
Frequency Offset Commands  
---  
Freq Offset ON/Off |  [SENSe:FOM[:STATe]](GP-IB_Command_Finder/Sense/FOM.md#state) |  [FOM.State](COM_Reference/Properties/State_Property.md)  
Read available ranges |  [SENSe:FOM:CATalog?](GP-IB_Command_Finder/Sense/FOM.md#cat) |   
Read number of ranges |  [SENSe:FOM:COUNt?](GP-IB_Command_Finder/Sense/FOM.md#count) |  [RangeCount](COM_Reference/Properties/RangeCount_Property.md)  
X-Axis display range |  [SENSe:FOM:DISPlay:SELect](GP-IB_Command_Finder/Sense/FOM.md#select) |  [DisplayRange](COM_Reference/Properties/DisplayRange_Property.md)  
Read range name |  [SENSe:FOM:RANGe:NAME?](GP-IB_Command_Finder/Sense/FOM.md#NameQuery) |  [Name FOMRange](COM_Reference/Properties/Name_FOMRange_Property.md)  
Read range number |  [SENSe:FOM:RNUM?](GP-IB_Command_Finder/Sense/FOM.md#rnum) |  [rangeNumber](COM_Reference/Properties/rangeNumber.md)  
Set range coupling |  [SENSe:FOM:RANGe:COUPled](GP-IB_Command_Finder/Sense/FOM.md#coupled) |  [Coupled](COM_Reference/Properties/Coupled_Property.md)  
Set sweep type |  [SENSe:FOM:RANGe:SWEep:TYPE](GP-IB_Command_Finder/Sense/FOM.md#SwpType) |  [SweepType](COM_Reference/Properties/Sweep_Type_Property.md)  
Set CW freq |  [SENSe:FOM:RANGe:FREQuency:CW](GP-IB_Command_Finder/Sense/FOM.md#FCW) |  [CWFrequency](COM_Reference/Properties/CW_Frequency_Property.md)  
Set start freq |  [SENSe:FOM:RANGe:FREQuency:STARt](GP-IB_Command_Finder/Sense/FOM.md#FStart) |  [StartFrequency](COM_Reference/Properties/Start_Frequency_Property.md)  
Set stop freq |  [SENSe:FOM:RANGe:FREQuency:STOP](GP-IB_Command_Finder/Sense/FOM.md#FStop) |  [StopFrequency](COM_Reference/Properties/Stop_Frequency_Property.md)  
Set offset value |  [SENSe:FOM:RANGe:FREQuency:OFFSet](GP-IB_Command_Finder/Sense/FOM.md#Offset) |  [Offset](COM_Reference/Properties/Offset_Property.md)  
Set divisor value |  [SENSe:FOM:RANGe:FREQuency:DIVisor](GP-IB_Command_Finder/Sense/FOM.md#divisor) |  [Divisor](COM_Reference/Properties/Divisor_Property.md)  
Set multiplier value |  [SENSe:FOM:RANGe:FREQuency:MULTiplier](GP-IB_Command_Finder/Sense/FOM.md#Multipy) |  [Multiplier](COM_Reference/Properties/Multiplier_Property.md)  
Freq. Offset Segment Sweep  
ON|OFF |  [SENSe:FOM:RANGe:SEGMent](GP-IB_Command_Finder/Sense/FOMSegm.md#add) |  [State](COM_Reference/Properties/State_Property.md)  
Add a segment |  [SENSe:FOM:RANGe:SEGMent:ADD](GP-IB_Command_Finder/Sense/FOMSegm.md#add) |  [FOM.Add](COM_Reference/Objects/FOM_Collection.md)  
Delete a segment |  [SENSe:FOM:RANGe:SEGMent:DELete](GP-IB_Command_Finder/Sense/FOMSegm.md#delete) |  [Remove](COM_Reference/Methods/Remove_Method.md)  
Count the segments |  [SENSe:FOM:RANGe:SEGMent: COUNT?](GP-IB_Command_Finder/Sense/FOMSegm.md#count) |  [Count](COM_Reference/Properties/Count_Property.md)  
Center Frequency |  [SENSe:FOM:RANGe:SEGMent:FREQuency:CENTer](GP-IB_Command_Finder/Sense/FOMSegm.md#FreqCenter) |  [CenterFrequency](COM_Reference/Properties/CenterFreq_Property.md)  
Frequency Span |  [SENSe:FOM:RANGe:SEGMent:FREQuency:SPAN](GP-IB_Command_Finder/Sense/FOMSegm.md#FreqSpan) |  [FrequencySpan](COM_Reference/Properties/Frequency_Span_Property.md)  
Start Frequency |  [SENSe:FOM:RANGe:SEGMent:FREQuency:STARt](GP-IB_Command_Finder/Sense/FOMSegm.md#FreqStart) |  [StartFrequency](COM_Reference/Properties/Start_Frequency_Property.md)  
Stop Frequency |  [SENSe:FOM:RANGe:SEGMent:FREQuency:STOP](GP-IB_Command_Finder/Sense/FOMSegm.md#FreqStop) |  [Stop Frequency](COM_Reference/Properties/Stop_Frequency_Property.md)  
Number of Points |  [SENSe:FOM:RANGe:SEGMent:SWEep:POINts](GP-IB_Command_Finder/Sense/FOMSegm.md#Points) |  [Number of Points](COM_Reference/Properties/Number_of__Points_Property.md)  
IF Bandwidth value |  [SENSe:FOM:RANGe:SEGMent:BWID](GP-IB_Command_Finder/Sense/FOMSegm.md#ifbw) |  [IF Bandwidth](COM_Reference/Properties/IF_Bandwidth_Property.md)  
IF Bandwidth control |  [SENSe:FOM:RANGe:SEGMent:BWID:CONTrol](GP-IB_Command_Finder/Sense/FOMSegm.md#IFBWControl) |  [IF BandwidthOption](COM_Reference/Properties/IF_Bandwidth_Option_Property.md)  
Source Power value |  [SENSe:FOM:RANGe:SEGMent:POWer](GP-IB_Command_Finder/Sense/FOMSegm.md#powerLevel) |  [Test Port Power](COM_Reference/Properties/Test_Port_Power_Property.md)  
Source Power control |  [SENSe:FOM:RANGe:SEGMent:POWer:CONTrol](GP-IB_Command_Finder/Sense/FOMSegm.md#powerControl) |  [Source Power Option](COM_Reference/Properties/Source_Power_Option_Property.md)  
Sweep time value |  [SENSe:FOM:RANGe:SEGMent:SWEep:TIME](GP-IB_Command_Finder/Sense/FOMSegm.md#time) |  [Sweep Time](COM_Reference/Properties/Sweep_Time_Property.md)  
Sweep time control |  [SENSe:FOM:RANGe:SEGMent:SWEep:TIME:CONTrol](GP-IB_Command_Finder/Sense/FOMSegm.md#timeControl) |  [TimeOption](COM_Reference/Properties/SweepTimeOption_Property.md)  
Test Set Switch |  [ROUT:PATH:LOOP:R1](GP-IB_Command_Finder/Route_SCPI.md) |  [chan.R1InputPath](COM_Reference/Properties/R1inputPath_Property.md)  
  
Power Settings See [Remotely Specifying a Source
Port](Remotely_Specifying_a_Source_Port.htm) .  
---  
Power ON | OFF |  [OUTP](GP-IB_Command_Finder/Output.md) |  [app.SourcePowerState](COM_Reference/Properties/Source_Power_State_Property.md)  
Source Power (Auto | ON | OFF) |  [SOURce:POWer:MODE](GP-IB_Command_Finder/source.md#Mode) |  [SourcePortMode](COM_Reference/Properties/SourcePortMode_Property.md)  
Power Value |  [SOURce:POWer[:LEVel][:IMMediate][:AMPLitude]](GP-IB_Command_Finder/source.md#pwrval) |  [chan.TestPortPower](COM_Reference/Properties/Test_Port_Power_Property.md)  
Port Selection |  [SENSe:SWepE:SRCPort](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#sss) |  [chan.TestPortPower](COM_Reference/Properties/Test_Port_Power_Property.md)  
Couple Ports OFF | ON |  [SOURce:POWer:COUPle](GP-IB_Command_Finder/source.md#cplON) |  [chan.CouplePorts](COM_Reference/Properties/Couple_Ports_Property.md)  
Attenuator Mode Auto|Manual |  [SOURce:POWer:ATTenuation:Auto](GP-IB_Command_Finder/source.md#attauto) |  [chan.AttenuatorMode](COM_Reference/Properties/Attenuator_Mode_Property.md)  
Attenuation Value |  [SOURce:POWer:ATTenuation](GP-IB_Command_Finder/source.md#attval) |  [chan.Attenuator](COM_Reference/Properties/Attenuator_Property.md)  
Power Slope ON | OFF |  [SOURce:POWer:SLOPe:STATe](GP-IB_Command_Finder/source.md#slpON) |  [chan.PowerSlopeState](COM_Reference/Properties/PowerSlopeState_Property.md)  
Power Slope Value |  [SOURce:POWer:SLOPe](GP-IB_Command_Finder/source.md#slope) |  [chan.PowerSlope](COM_Reference/Properties/Power_Slope_Property.md)  
Receiver Attenuation |  [SENSe:POWer:ATTenuator](GP-IB_Command_Finder/Sense/Power.md) |  [chan.ReceiverAttenuator](COM_Reference/Properties/Receiver_Attenuator_Property.md)  
Receiver Reference Attenuation |  [SOURce:POWer:ATTenuation:RECeiver:REFerence](GP-IB_Command_Finder/source.md#SOURce:POWer:ATTenuation:RECeiver:REFerence) |  None  
Receiver Test Attenuation |  [SOURce:POWer:ATTenuation:RECeiver:TEST](GP-IB_Command_Finder/source.md#SOURce:POWer:ATTenuation:RECeiver:TEST) |  None  
Shutdown or Restart System |  [SYSTem:POFF](GP-IB_Command_Finder/System.md#shutdown) |  None  
See also [Power Range](DataTopic.md#Power_Range) remote commands |  |   
  
Power Limit and Offsets  
---  
Set power limit |  [SYSTem:POWer:LIMit](GP-IB_Command_Finder/System.md#powerLimit) |  [Limit](COM_Reference/Properties/Limit_Property.md)  
Set Calibration power limit |  [SYSTem:POWer:LIMit:CALibration](GP-IB_Command_Finder/System.md#PowLimCal) |  None  
Power limit ON/OFF |  [SYSTem:POWer:LIMit:STATe](GP-IB_Command_Finder/System.md#PowerLimState) |  [State](COM_Reference/Properties/State_GPL_Property.md)  
Power limit UI lock |  [SYSTem:POWer:LIMit:LOCK](GP-IB_Command_Finder/System.md#PowerLock) |  [Lock](COM_Reference/Properties/Lock_Property.md)  
Set offset value |  [SOURce:POWer:ALC:MODE:RECeiver:OFFSet](GP-IB_Command_Finder/SourceRxLeveling.md#recOffset) |  [PowerOffset](COM_Reference/Properties/PowerOffset_Property.md)  
  
Receiver Leveling  
---  
Rx Level ON|OFF |  [SOURce:POWer:ALC:MODE:RECeiver](GP-IB_Command_Finder/SourceRxLeveling.md#RecLevMode) |  [State](COM_Reference/Properties/State_rx_Property.md)  
Select the reference receiver |  [SOURce:POWer:ALC:MODE:RECeiver:REFerence](GP-IB_Command_Finder/SourceRxLeveling.md#RecRef) |  [ReferenceReceiver](COM_Reference/Properties/ReferenceReceiver_Property.md)  
Sets all ports to pre-sweep or point leveling mode for the specified channel. |  [SOURce:POWer:ALC[:MODE]:RECeiver:ACQuisition:MODE](GP-IB_Command_Finder/SourceRxLeveling.md#SOURce:POWer:ALC:MODE:RECeiver:ACQ:MODE) |  None  
Enables or disables the receiver leveling maximum iteration search function. |  [SOURce:POWer:ALC[:MODE]:RECeiver:ITERation:ENABle](GP-IB_Command_Finder/SourceRxLeveling.md#SOURce:POWer:ALC:MODE:RECeiver:ITERation:ENABle) |  None  
Set maximum iterations |  [SOURce:POWer:ALC:MODE:RECeiver:ITERation:VALue](GP-IB_Command_Finder/SourceRxLeveling.md#recIteration) |  [IterationNumber](COM_Reference/Properties/IterationNumber_Property.md)  
Set tolerance |  [SOURce:POWer:ALC:MODE:RECeiver:TOLerance](GP-IB_Command_Finder/SourceRxLeveling.md#recToler) |  [Tolerance](COM_Reference/Properties/Tolerance_Property.md)  
Set offset value |  [SOURce:POWer:ALC:MODE:RECeiver:OFFSet](GP-IB_Command_Finder/SourceRxLeveling.md#recOffset) |  [PowerOffset](COM_Reference/Properties/PowerOffset_Property.md)  
Separate IFBW |  [SOURce:POWer:ALC:MODE:RECeiver:FAST](GP-IB_Command_Finder/SourceRxLeveling.md#RecFast) |  [FastMode](COM_Reference/Properties/FastMode_Property.md)  
Set Rx IFBW |  [SOURce:POWer:ALC:MODE:RECeiver:IFBW](GP-IB_Command_Finder/SourceRxLeveling.md#recIFBW) |  [LevelingIFBW](COM_Reference/Properties/LevelingIFBW_Property.md)  
Safe mode ON|OFF |  [SOURce:POWer:ALC:MODE:RECeiver:SAFE](GP-IB_Command_Finder/SourceRxLeveling.md#recSafeMode) |  [SafeMode](COM_Reference/Properties/SafeMode_Property.md)  
Safe mode Max power |  [SOURce:POWer:ALC:MODE:RECeiver:SAFE:MAX](GP-IB_Command_Finder/SourceRxLeveling.md#recSafeMax) |  [PowerMax](COM_Reference/Properties/PowerMax_Property.md)  
Safe mode Min power |  [SOURce:POWer:ALC:MODE:RECeiver:SAFE:MIN](GP-IB_Command_Finder/SourceRxLeveling.md#recSafeMin) |  [PowerMin](COM_Reference/Properties/PowerMin_Property.md)  
Use Last Result for Source Power Cal |  [SOURce:POWer:ALC:MODE:RECeiver:LSPC](GP-IB_Command_Finder/SourceRxLeveling.md#LSPC) |  [LastLevelingAsSPC](COM_Reference/Properties/LastLevelingAsSPC_Property.md)  
Sets the specific PULSe4 behavior. |  [SENSe:PULSe4:MODE](GP-IB_Command_Finder/Sense/Pulse.md#SENSe:PULSe4:OPTion:MODE) |  None  
Sets all ports to pre-sweep or point leveling mode for the specified channel. |  [SOURce:POWer:ALC[:MODE]:RECeiver:ACQuisition:MODE](GP-IB_Command_Finder/SourceRxLeveling.md#SOURce:POWer:ALC:MODE:RECeiver:ACQ:MODE) |  None  
Enables or disables the receiver leveling maximum iteration search function. |  [SOURce:POWer:ALC[:MODE]:RECeiver:ITERation:ENABle](GP-IB_Command_Finder/SourceRxLeveling.md#SOURce:POWer:ALC:MODE:RECeiver:ITERation:ENABle) |  None  
  
ALC Leveling  
---  
Returns list of valid ALC Leveling Modes |  [SOURce:POWer:ALC:MODE:CATalog?](GP-IB_Command_Finder/source.md#ALCModeCat) |  [GetSupportedALCModes](COM_Reference/Methods/GetSupportedALCModes_Method.md)  
Set ALC Mode |  [SOURce:POWer:ALC[:MODE]](GP-IB_Command_Finder/source.md#ALCMode) |  [ALCLevelingMode](COM_Reference/Properties/ALCLevelingMode_Property.md)  
  
Specifying Source Ports See [Remotely Specifying a Source
Port](Remotely_Specifying_a_Source_Port.htm).  
---  
Returns the number of source ports. |  None |  [SourcePortCount](COM_Reference/Properties/SourcePortCount_Property.md)  
Returns the string names of source ports. |  [SOURce:CATalog?](GP-IB_Command_Finder/source.md#Cat) |  [SourcePortNames](COM_Reference/Properties/SourcePortNames_Property.md)  
Returns the source port number of the specified string port name. |  None |  [GetPortNumber](COM_Reference/Methods/GetPortNumber_Method.md)  
  
IF Bandwidth  
---  
IF Bandwidth |  [SENSe:BANDwidth | BWIDth[:RESolution]](GP-IB_Command_Finder/Sense/Sense_Bandwidth.md#res) |  [chan.IFBandwidth](COM_Reference/Properties/IF_Bandwidth_Property.md)  
Previous IF Bandwidth |  None |  [chan.Previous_IFBandwidth](COM_Reference/Methods/Previous_IF_Bandwidth_Method.md)  
Next IFBandwidth |  None |  [chan.Next_IFBandwidth](COM_Reference/Methods/Next_IF_Bandwidth_Method.md)  
Reduce IF BW |  [SENSe:BANDwidth | BWIDth:TRACk](GP-IB_Command_Finder/Sense/Sense_Bandwidth.md#track) |  [chan.ReduceIFBW](COM_Reference/Properties/ReduceIFBW_Property.md)  
  
Sweep  
---  
Sweep Time Value |  [SENSe:SWEep:TIME:AUTO](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#sst) |  [chan.SweepTime](COM_Reference/Properties/Sweep_Time_Property.md)  
Returns the time the first point of a Time Sweep is measured. |  [SENSe:SWEep:TIME:STARt?](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#SENSe:SWEep:TIME:STARt) |  None  
Sets the time the analyzer takes to complete one sweep. |  [SENSe:SWEep:TIME[:STOP]](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#SENSe:SWEep:TIME:STOP) |  None  
  
Sweep Setup  
---  
Number of Points |  [SENSe:SWEep:POINts](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssp) |  [chan.NumberOfPoints](COM_Reference/Properties/Number_of__Points_Property.md)  
Sweep Type (Lin | Pwr | CW | Seg | Phase) |  [SENSe:SWEep:TYPE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssty) |  [chan.SweepType](COM_Reference/Properties/Sweep_Type_Property.md)  
Sweep Generation (Stepped | Analog) |  [SENSe:SWEep:GENeration](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssg) |  [chan.SweepGenerationMode](COM_Reference/Properties/Sweep_Generation_Mode_Property.md)  
Dwell Time Value |  [SENSe:SWEep:DWEL](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssd) |  [chan.DwellTime](COM_Reference/Properties/Dwell_Time_Property.md)  
Dwell Time Auto set the minimum dwell time |  [SENSe:SWEep:DWEL:AUTO](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssda) |  [chan.DwellTime](COM_Reference/Properties/Dwell_Time_Property.md)  
Sweep Delay |  [SENSe:SWEep:DWELl:SDELay](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#SweepDelay) |  [SweepDelay](COM_Reference/Properties/Sweep_Delay_Property.md)  
Alternate Sweeps |  [SENSe:COUPle](GP-IB_Command_Finder/Sense/Couple.md) |  [chan.AlternateSweep](COM_Reference/Properties/Alternate_Sweep_Property.md)  
External ALC |  [SOURce:POWer:DETector](GP-IB_Command_Finder/source.md#det) |  [app.ExternalALC](COM_Reference/Properties/External_ALC_Property.md)  
Enable Point Sweep |  [SENSe:SWEep:GENeration:POINtsweep](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#GenPoint) |  [PointSweepState](COM_Reference/Properties/PointSweepState_Property.md)  
Fast Sweep |  [SENSe:SWEep:SPEed](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#SweepSpeed) |  [SweepSpeedMode](COM_Reference/Properties/SweepSpeedMode_Property.md)  
Fast CW |  [SENSe:SWEep:TYPE:FACW](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#swpTypeFASTCW) |  [FastCWPointCount](COM_Reference/Properties/FastCWPointCount_Property.md)  
Set shift LO maximum frequency |  [SENSe:SWEep:SLOCal:MAXimum](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#SlocalMax) |  None  
Turn shift LO on or off |  [SENSe:SWEep:SLOCal:STATe](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#SlocalState) |  None  
Returns whether or not the VNA has the low frequency extension (LFE) installed. |  [SYSTem:CAPability:HARDware:LFEXtension:EXISts?](GP-IB_Command_Finder/SystCapability.md#SYSTem:CAPability:HARDware:LFEXtensions:EXISts) |  [HasLowFrequencyExtension](COM_Reference/Properties/HasLowFrequencyExtension_Property.md)  
Turns ON or OFF low frequency extension |  [SENSe:SWEep:LFEXtension:STATe](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#SENSe:SWEep:LFEXtension:STATe) |  [LowFrequencyExtension](COM_Reference/Properties/LowFrequencyExtension_Property.md)  
Power Sweep  
Start Power |  [SOURce:POWer:STARt](GP-IB_Command_Finder/source.md#start) |  [chan.StartPower](COM_Reference/Properties/Start_Power_Property.md)  
Stop Power |  [SOURce:POWer:STOP](GP-IB_Command_Finder/source.md#stop) |  [chan.StopPower](COM_Reference/Properties/Stop_Power_Property.md)  
Center |  [SOURce:POWer:CENTer](GP-IB_Command_Finder/source.md#cent) |   
Span |  [SOURce:POWer:SPAN](GP-IB_Command_Finder/source.md#span) |   
Segment Sweep  
ON|OFF |  [SENSe:SEGMent[:STATe]](GP-IB_Command_Finder/Sense/Segment.md#segON) |  [Seg.State](COM_Reference/Properties/State_Property.md)  
Add a segment |  [SENSe:SEGMent:ADD](GP-IB_Command_Finder/Sense/Segment.md#add) |  [Segs.Add](COM_Reference/Methods/Add_segments_Method.md)  
Delete a segment |  [SENSe:SEGMent:DELete](GP-IB_Command_Finder/Sense/Segment.md#del) |  [segments.Remove](COM_Reference/Methods/Remove_Method.md)  
Delete all segments |  [SENSe:SEGMent:DELete:ALL](GP-IB_Command_Finder/Sense/Segment.md#delall) |  None  
Count the segments |  [SENSe:SEGMent:COUNt](GP-IB_Command_Finder/Sense/Segment.md#count) |  [chans.Count](COM_Reference/Properties/Count_Property.md)  
Read the segment number |  None |  [seg.SegmentNumber](COM_Reference/Properties/Segment_Number_Property.md)  
Segment Center Frequency |  [SENSe:SEGMent:FREQuency:CENTer](GP-IB_Command_Finder/Sense/Segment.md#cent) |  [chan.centerFrequency](COM_Reference/Properties/CenterFreq_Property.md)  
Segment Frequency Span |  [SENSe:SEGMent:FREQuency:SPAN](GP-IB_Command_Finder/Sense/Segment.md#span) |  [chan.FrequencySpan](COM_Reference/Properties/Frequency_Span_Property.md)  
Segment Start Frequency |  [SENSe:SEGMent:FREQuency:STARt](GP-IB_Command_Finder/Sense/Segment.md#start) |  [Chan.StartFrequency](COM_Reference/Properties/Start_Frequency_Property.md)  
Segment Stop Frequency |  [SENSe:SEGMent:FREQuency:STOP](GP-IB_Command_Finder/Sense/Segment.md#stop) |  [Chan.StopFrequency](COM_Reference/Properties/Stop_Frequency_Property.md)  
Number of Points |  [SENSe:SEGMent:SWEep:POINt](GP-IB_Command_Finder/Sense/Segment.md#point) |  [seg.NumberOfPoints](COM_Reference/Properties/Number_of__Points_Property.md)  
IF Bandwidth |  [SENSe:SEGMent:BWIDth](GP-IB_Command_Finder/Sense/Segment.md#bdwval) |  [seg.IFBandwidth](COM_Reference/Properties/IF_Bandwidth_Property.md)  
IF Bandwidth Option |  [SENSe:SEGMent:BWIDth:CONTrol](GP-IB_Command_Finder/Sense/Segment.md#bdwON) |  [segs.IFBandwidthOption](COM_Reference/Properties/IF_Bandwidth_Option_Property.md)  
IF Bandwidth Per Port |  [SENSe:SEGMent:BWIDth:PORT:CONTrol](GP-IB_Command_Finder/Sense/Segment.md#BwidthPortCtrl) |  [PortIFBandwidthOption](COM_Reference/Properties/PortIFBandwidthOption_Property.md) [PortIFBandwidth](COM_Reference/Properties/PortIFBandwidth_Property.md)  
Sweep Delay Time |  [SENSe:SEGMent:SWEep:DELay](GP-IB_Command_Finder/Sense/Segment.md#Delay) |  [DelayOption](COM_Reference/Properties/DelayOption_Property.md) [Delay](COM_Reference/Properties/Delay_\(Segment_Sweep\)_Property.md)  
Sweep Dwell |  [SENSe:SEGMent:SWEep:DWELl](GP-IB_Command_Finder/Sense/Segment.md#Dweli) |  [SweepTimeOption](COM_Reference/Properties/SweepTimeOption_Property.md) [DwellTime](COM_Reference/Properties/Dwell_Time_Property.md)  
Sweep Mode |  [SENSe:SEGMent:SWEep:GENeration](GP-IB_Command_Finder/Sense/Segment.md#Gen) |  [SweepModeOption](COM_Reference/Properties/SweepModeOption_Property.md) [SweepMode](COM_Reference/Properties/SweepMode_Property.md)  
Total Sweep Points |  [SENSe:SEGMent:SWEep:POINts:TOTal?](GP-IB_Command_Finder/Sense/Segment.md#SENSe:SEGMent:SWEep:POINts:TOTal) |  [NumberOfPoints](COM_Reference/Properties/Number_of__Points_Property.md)  
Total Sweep Time |  [SENSe:SEGMent:SWEep:TIME:TOTal?](GP-IB_Command_Finder/Sense/Segment.md#SENSe:SEGMent:SWEep:TIME:TOTal) |  None  
Source Power |  [SENSe:SEGMent:POWer](GP-IB_Command_Finder/Sense/Segment.md#pwrval) |  [chan.TestPortPower](COM_Reference/Properties/Test_Port_Power_Property.md)  
Source Power Option |  [SENSe:SEGMent:POWer:CONTrol](GP-IB_Command_Finder/Sense/Segment.md#pwrON) |  [segs.SourcePowerOption](COM_Reference/Properties/Source_Power_Option_Property.md)  
X-Axis Point Spacing |  [SENSe:SEGMent:X:SPACing](GP-IB_Command_Finder/Sense/Segment.md#X AXIS) |  [chan.XAxisPointSpacing](COM_Reference/Properties/XAxisPointSpacing_Property.md)  
Allow Arbitrary Segments |  [SENSe:SEGMent:ARBitrary](GP-IB_Command_Finder/Sense/Segment.md#arb) |  [segs.AllowArbitrarySegments](COM_Reference/Properties/AllowArbitrarySegments_Property.md)  
Upload a segment table |  [SENSe:SEGMent:LIST](GP-IB_Command_Finder/Sense/Segment.md#list) |  [SetAllSegmernts](COM_Reference/Methods/SetAllSegments_Method.md)  
Download a segment table |  [SENSe:SEGMent:LIST](GP-IB_Command_Finder/Sense/Segment.md#list) |  [GetAllSegments](COM_Reference/Methods/GetAllSegments_Method.md)  
Sweep delay ON|OFF |  [SENSe:SEGMent:SWEep:DELay:CONTrol](GP-IB_Command_Finder/Sense/Segment.md#DelayControl) |  [DelayOption](COM_Reference/Properties/DelayOption_Property.md)  
Sweep dwell ON|OFF |  [SENSe:SEGMent:SWEep:DWELl:CONTrol](GP-IB_Command_Finder/Sense/Segment.md#DweliControl) |  [SweepTimeOption](COM_Reference/Properties/SweepTimeOption_Property.md)  
IF Bandwidth resolution |  [SENSe:SEGMent:BWIDth:PORT[:RESolution]](GP-IB_Command_Finder/Sense/Segment.md#BwidthPort) |  [PortIFBandwidthOption](COM_Reference/Properties/PortIFBandwidthOption_Property.md) [PortIFBandwidth](COM_Reference/Properties/PortIFBandwidth_Property.md)  
Sets or returns the SA data threshold |  [SENSe:SEGMent:SA:DTHReshold](GP-IB_Command_Finder/Sense/Segment.md#SENSe:SEGMent:SA:DTHReshold) |  [SADataThreshold](COM_Reference/Properties/SADataThreshold_Property.md)  
Specifies whether SA Data Threshold can be set independently for each segment |  [SENSe:SEGMent:SA:DTHReshold:CONTrol](GP-IB_Command_Finder/Sense/Segment.md#SENSe:SEGMent:SA:DTHReshold:CONTrol) |  [SADataThresholdOption](COM_Reference/Properties/SADataThresholdOption_Property.md)  
Sets or returns the SA multitone reference |  [SENSe:SEGMent:SA:MTReference](GP-IB_Command_Finder/Sense/Segment.md#SENSe:SEGMent:SA:MTReference) |  [SAMTReference](COM_Reference/Properties/SAMTReference_Property.md)  
Specifies whether SA Reference Tone can be set independently for each segment |  [SENSe:SEGMent:SA:MTReference:CONTrol](GP-IB_Command_Finder/Sense/Segment.md#SENSe:SEGMent:SA:MTReference:CONTrol) |  [SAMTReferenceFreqOption](COM_Reference/Properties/SAMTReferenceFreqOption_Property.md)  
Queries the maximum value of the SA Reference Tone  |  [SENSe:SEGMent:SA:MTReference:MAX?](GP-IB_Command_Finder/Sense/Segment.md#SENSe:SEGMent:SA:MTReference:MAX) |  None  
Queries the minimum value of the SA Reference Tone  |  [SENSe:SEGMent:SA:MTReference:MIN?](GP-IB_Command_Finder/Sense/Segment.md#SENSe:SEGMent:SA:MTReference:MIN) |  None  
Sets or returns the SA vector average |  [SENSe:SEGMent:SA:VAVerage](GP-IB_Command_Finder/Sense/Segment.md#SENSe:SEGMent:SA:VAVerage) |  [SAVectorAverage](COM_Reference/Properties/SAVectorAverage_Property.md)  
Specifies whether SA Vector Averaging can be set independently for each segment |  [SENSe:SEGMent:SA:VAVerage:CONTrol](GP-IB_Command_Finder/Sense/Segment.md#SENSe:SEGMent:SA:VAVerage:CONTrol) |  [SAVectorAverageOption](COM_Reference/Properties/SAVectorAverageOption_Property.md)  
Sets or returns the SA video bandwidth |  [SENSe:SEGMent:SA:VIDeobw](GP-IB_Command_Finder/Sense/Segment.md#SENSe:SEGMent:SA:VIDeobw) |  [SAVideoBandwidth](COM_Reference/Properties/SAVideoBandwidth_Property.md)  
Sets or returns the noise figure bandwidth. |  [SENSe:SEGMent:NFBW](GP-IB_Command_Finder/Sense/Segment.md#SENSe:SEGMent:NFBW) |  [NoiseFigureBW](COM_Reference/Properties/NoiseFigureBW_Property.md)  
Turns ON or OFF the noise figure bandwidth setting. |  [SENSe:SEGMent:NFBW:CONTrol](GP-IB_Command_Finder/Sense/Segment.md#SENSe:SEGMent:NFBW:CONTrol) |  [NoiseFigureBWOption](COM_Reference/Properties/NoiseFigureBWOption_Property.md)  
Specifies whether SA Video Bandwidth can be set independently for each segment |  [SENSe:SEGMent:SA:VIDeobw:CONTrol](GP-IB_Command_Finder/Sense/Segment.md#SENSe:SEGMent:SA:VIDeobw:CONTrol) |  [SAVideoAverageOption](COM_Reference/Properties/SAVectorAverageOption_Property.md)  
  
Source Phase Control / Sweep  
---  
Phase Sweep type |  [SENSe:SWEep:TYPE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssty) |  [SweepType](COM_Reference/Properties/Sweep_Type_Property.md)  
Set fixed phase value |  [SOURce:PHASe [:FIXed]](GP-IB_Command_Finder/SourcePhase.md#fixed) |  [FixedPhase](COM_Reference/Properties/FixedPhase_Property.md)  
Phase sweep start value |  [SOURce:PHASe:STARt](GP-IB_Command_Finder/SourcePhase.md#start) |  [StartPhase](COM_Reference/Properties/StartPhase_Property.md)  
Phase sweep stop value |  [SOURce:PHASe:STOP](GP-IB_Command_Finder/SourcePhase.md#stop) |  [StopPhase](COM_Reference/Properties/StopPhase_Property.md)  
Phase parameter |  [SOURce:PHASe:PARameter](GP-IB_Command_Finder/SourcePhase.md#parameter) |  [PhaseParameter](COM_Reference/Properties/PhaseParameter_Property.md)  
Set Phase control mode |  [SOURce:PHASe:PARameter:MODE](GP-IB_Command_Finder/SourcePhase.md#parameterMode) |  [PhaseControlMode](COM_Reference/Properties/PhaseControlMode_Property.md)  
Set reference port |  [SOURce:PHASe:PARameter:PORT](GP-IB_Command_Finder/SourcePhase.md#paramPort) |  [PhaseReferencePort](COM_Reference/Properties/PhaseReferencePort_Property.md)  
Read available phase control modes for the port |  [SOURce:PHASe:PARameter:MODE:CAT?](GP-IB_Command_Finder/SourcePhase.md#paramModeCat) |  [PhaseParameterModes](COM_Reference/Properties/PhaseParameterModes_Property.md)  
Couple sweep settings |  [SOURce:PHASe:CONTrol:COUPle](GP-IB_Command_Finder/SourcePhase.md#coupleState) |  [CouplePhasePortSettings](COM_Reference/Properties/CouplePhasePortSettings_Property.md)  
Set number of sweep iterations |  [SOURce:PHASe:CONTrol:ITERation](GP-IB_Command_Finder/SourcePhase.md#iteration) |  [PhaseIterationNumber](COM_Reference/Properties/PhaseIterationNumber_Property.md)  
Set sweep tolerance |  [SOURce:PHASe:CONTrol:TOLerance](GP-IB_Command_Finder/SourcePhase.md#tolerance) |  [PhaseTolerance](COM_Reference/Properties/PhaseTolerance_Property.md)  
Set and read an array of phase offsets. |  [SOURce:PHASe:CORRection:DATA](GP-IB_Command_Finder/SourcePhase.md#corrData) |  [PhaseCorrectionData](COM_Reference/Properties/PhaseCorrectionData_Property.md)  
Use phase offset array. |  [SOURce:PHASe:CORRection:STATe](GP-IB_Command_Finder/SourcePhase.md#corrState) |  [PhaseCorrectionEnabled](COM_Reference/Properties/PhaseCorrectionEnabled_Property.md)  
Set and read an array of ratioed power offsets. |  [SOURce:PHASe:POFFset:CORRection:DATA](GP-IB_Command_Finder/SourcePhase.md#poffCorrData) |  [RatioedPowerCorrectionData](COM_Reference/Properties/RatioedPowerCorrectionData_Property.md)  
Use power offset array. |  [SOURce:PHASe:POFFset:CORRection:STATe](GP-IB_Command_Finder/SourcePhase.md#poffCorrState) |  [RatioedPowerCorrectionEnabled](COM_Reference/Properties/RatioedPowerCorrectionEnabled_Property.md)  
Set the fixed power ratioed value |  [SOURce:PHASe:POFFset:FIXed](GP-IB_Command_Finder/SourcePhase.md#poffsetFixed) |  [FixedRatioedPower](COM_Reference/Properties/FixedRatioedPower_Property.md)  
Set the start power ratioed value. |  [SOURce:PHASe:POFFset:STARt](GP-IB_Command_Finder/SourcePhase.md#poffStart) |  [StartRatioedPower](COM_Reference/Properties/StartRatioedPower_Property.md)  
Set the stop power ratioed value. |  [SOURce:PHASe:POFFset:STOP](GP-IB_Command_Finder/SourcePhase.md#poffStop) |  [StopRatioedPower](COM_Reference/Properties/StopRatioedPower_Property.md)  
Returns the available internal ports that the external port can be set to. |  [SOURce:PHASe:EXTernal:CATalog?](GP-IB_Command_Finder/SourcePhase.md#SOURce:PHASe:EXTernal:CATalog) |  None  
Sets and returns the internal port that the external port is routed through. |  [SOURce:PHASe:EXTernal:PORT](GP-IB_Command_Finder/SourcePhase.md#SOURce:PHASe:EXTernal:PORT) |  None  
Returns the available phase control modes for the specified port. |  [SOURce:PHASe:MODE:CATalog?](GP-IB_Command_Finder/SourcePhase.md#SOURce:PHASe:MODE:CATalog) |  None  
Sets and returns the Phase Control mode. |  [SOURce:PHASe:MODE[:VALue]](GP-IB_Command_Finder/SourcePhase.md#SOURce:PHASe:MODE:VALue) |  None  
Returns the available parameters. |  [SOURce:PHASe:PARameter[:CATalog?](GP-IB_Command_Finder/SourcePhase.md#SOURce:PHASe:PARameter:CATalog) |  None  
Sets and returns the ratioed receivers (parameter) to use for phase control. |  [SOURce:PHASe:PARameter[:VALue]](GP-IB_Command_Finder/SourcePhase.md#SOURce:PHASe:PARameter:VALue) |  None  
Returns the available ports that can be used as phase control reference ports for the phase controlled port. |  [SOURce:PHASe:REFerence:CATalog?](GP-IB_Command_Finder/SourcePhase.md#SOURce:PHASe:REFerence:CATalog) |  None  
Sets and returns the reference port for the Phase Control measurement. |  [SOURce:PHASe:REFerence:PORT](GP-IB_Command_Finder/SourcePhase.md#SOURce:PHASe:REFerence:PORT) |  None  
|  |   
  
Trigger Source (where trigger comes from)  
---  
Source (Int | Ext | Manual) |  [TRIGger[:SEQuence]:SOURce](GP-IB_Command_Finder/Trigger_SCPI.md#tss) |  [trigSetup.Source](COM_Reference/Properties/Source_Property.md)  
Internal | Manual |  [INITiate:CONTinuous](GP-IB_Command_Finder/Initiate.md#cont) |  None  
Trigger! (for Manual Source) |  [INITiate[:IMMediate]](GP-IB_Command_Finder/Initiate.md#immed) |  [app.ManualTrigger](COM_Reference/Methods/Manual_Trigger_Method.md)  
Scope (what is triggered)  
Scope (Global | Channel) |  [TRIGger[:SEQuence]:SCOPe](GP-IB_Command_Finder/Trigger_SCPI.md#tssc) |  [trigSetup.Scope](COM_Reference/Properties/Scope_Property.md)  
Channel Settings (how the channel responds to triggers)  
Continuous |  [SENSe:SWEep:MODE CONTinous](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssm) |  [chan.Continuous](COM_Reference/Methods/Continuous_Method.md)  
Read Continuous Mode |  None |  [chan.IsContinuous](COM_Reference/Properties/IsContinuous_Property.md)  
Number of Groups |  [SENSe:SWEep:GROup:COUNt](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssgc) |  [chan.NumberOfGroups](COM_Reference/Methods/Number_Of_Groups_Method.md)  
Read Groups |  None |  [chan.GetNumberOfGroups](COM_Reference/Methods/Get_NumberOfGroups_Method.md)  
Hold |  [SENSe:SWEep:MODE HOLD](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssm) |  [chan.Hold](COM_Reference/Methods/Hold_Method.md)  
Hold Mode (read-only) |  None |  [chan.IsHold](COM_Reference/Properties/IsHold_Property.md)  
All channels in Hold |  [SYSTem:CHANnels:HOLD](GP-IB_Command_Finder/System.md#hold) |  [chans.Hold](COM_Reference/Methods/HoldChan_Method.md)  
All channels Resume |  [SYSTem:CHANnels:RESume](GP-IB_Command_Finder/System.md#resume) |  [chans.Resume](COM_Reference/Methods/Resume_Method.md)  
Single |  [SENSe:SWEep:MODE SINGle](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssm) |  [chan.Single](COM_Reference/Methods/Single_Method.md)  
Trigger Mode |  [SENSe:SWEep:TRIGger:MODE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#Mode) |  [chan.TriggerMode](COM_Reference/Properties/Trigger_Mode_Property.md)  
Restart |  [INITiate[:IMMediate]](GP-IB_Command_Finder/Initiate.md#immed) |  None  
Abort |  [ABORt](GP-IB_Command_Finder/Abort.md) |  [chan.Abort](COM_Reference/Methods/Abort_Method.md)  
  
External Meas Trigger Input  
---  
Scope (Global/Chan) |  [TRIGger[:SEQuence]:SCOPe](GP-IB_Command_Finder/Trigger_SCPI.md#tssc) |  [trigSetup.Scope](COM_Reference/Properties/Scope_Property.md)  
Trigger Delay (Global) |  [TRIGger:DELay](GP-IB_Command_Finder/Trigger_SCPI.md#delay) |  [app.TriggerDelay](COM_Reference/Properties/TriggerDelay_Property.md)  
Trigger Delay (Channel) |  [SENSe:SWEep:TRIGger:DELay](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#Delay) |  [chan.ExternalTriggerDelay](COM_Reference/Properties/ExternalTriggerDelay_Property.md)  
MeasTrigIn/ Hand I/O |  [TRIGger:ROUTE:INPut](GP-IB_Command_Finder/Trigger_SCPI.md#input) |  [ExternalTriggerConnectionBehavior](COM_Reference/Properties/ExternalTriggerConnectionBehavior_Property.md)  
Level or Edge |  [TRIGger:TYPE](GP-IB_Command_Finder/Trigger_SCPI.md#type) |  [ExternalTriggerConnectionBehavior](COM_Reference/Properties/ExternalTriggerConnectionBehavior_Property.md)  
Neg/Low or Pos/High |  [TRIGger:SLOPE](GP-IB_Command_Finder/Trigger_SCPI.md#slope) |  [ExternalTriggerConnectionBehavior](COM_Reference/Properties/ExternalTriggerConnectionBehavior_Property.md)  
Accept Trigger Before Armed |  [CONTrol:SIGNal:TRIGger:ATBA](GP-IB_Command_Finder/Control.md#atba) |  [AcceptTriggerBeforeArmed](COM_Reference/Properties/AcceptTriggerBeforeArmed_Property.md)  
Ready for Trigger Indicator (Out)  
MeasTrig Rdy/ Hand I/O |  [TRIGger:ROUTE:READy](GP-IB_Command_Finder/Trigger_SCPI.md#Ready) [CONTrol:SIGNal:STReamline:RTRigger[:STATe]](GP-IB_Command_Finder/Control.md#SigStrRtr) [CONTrol:SIGNal:PXI:RTRigger[:STATe]](GP-IB_Command_Finder/Control.md#SigPxiRtr) [CONTrol:SIGNal:STReamline:RTRigger:ROUTe](GP-IB_Command_Finder/Control.md#SigStrRtrRout) [CONTrol:SIGNal:PXI:RTRigger:ROUTe](GP-IB_Command_Finder/Control.md#SigPxiRtrRout) |  None  
Checks if the PNA is ready for a hardware trigger |  [TRIGger:STATus:READy?](GP-IB_Command_Finder/Trigger_SCPI.md#TRIGger:STATus:READy) |  [ReadyForTriggerStatus](COM_Reference/Properties/ReadyForTriggerStatus_Property.md)  
High / Low |  [TRIGger:READy:POLarity](GP-IB_Command_Finder/Trigger_SCPI.md#ReadyPolarity) |  [ReadyForTriggerPolarity](COM_Reference/Properties/ReadyForTriggerPolarity_Property.md)  
  
Auxiliary Triggering (PNA-X and N522x models)  
---  
Which AuxTrig connector pair being used. |  N/A |  [Number](COM_Reference/Properties/Number_Property.md)  
How many Aux connector pairs. |  [TRIGger:AUXiliary:COUNt?](GP-IB_Command_Finder/Trigger_SCPI.md#auxCount) |  [AuxiliaryTriggerCount](COM_Reference/Properties/AuxiliaryTriggerCount_Property.md)  
AUX TRIG OUT  
Enable |  [TRIGger:CHANnel:AUXiliary](GP-IB_Command_Finder/Trigger_SCPI.md#auxEnable) |  [Enable](COM_Reference/Properties/Enable_Property.md)  
Global or Channel Pref. |  [TRIGger:PREFerence:AIGLobal](GP-IB_Command_Finder/Trigger_SCPI.md#PrefGlobal) |  [AuxTriggerScopeIsGlobal](COM_Reference/Properties/AuxTriggerScopeIsGlobal_Property.md)  
Polarity (Pos/Neg) |  [TRIGger:CHANnel:AUXiliary:OPOLarity](GP-IB_Command_Finder/Trigger_SCPI.md#auxOpolarity) |  [TriggerOutPolarity](COM_Reference/Properties/TriggerOutPolarity_Property.md)  
Position (Before/After acq) |  [TRIGger:CHANnel:AUXiliary:POSition](GP-IB_Command_Finder/Trigger_SCPI.md#auxPosition) |  [TriggerOutPosition](COM_Reference/Properties/TriggerOutPosition_Property.md)  
OUT Pulse width |  [TRIGger:CHANnel:AUXiliary:DURation](GP-IB_Command_Finder/Trigger_SCPI.md#AuxDuration) |  [TriggerOutDuration](COM_Reference/Properties/TriggerOutDuration_Property.md)  
Point or Sweep. |  [TRIGger:CHANnel:AUXiliary:INTerval](GP-IB_Command_Finder/Trigger_SCPI.md#auxInterval) |  [TriggerOutInterval](COM_Reference/Properties/TriggerOutInterval_Property.md)  
Rear SMB |  [CONTrol:SIGNal:STReamline:TRIGger:OUTPut[:STATe]](GP-IB_Command_Finder/Control.md#SigStrTrifOutp) [CONTrol:SIGNal:STReamline:TRIGger:OUTPut:ROUTe](GP-IB_Command_Finder/Control.md#SigStrTrigOutpRout) |   
Backplane |  [CONTrol:SIGNal:PXI:TRIGger:OUTPut[:STATe]](GP-IB_Command_Finder/Control.md#SigPxiTrigOutp) [CONTrol:SIGNal:PXI:TRIGger:OUTPut:ROUTe](GP-IB_Command_Finder/Control.md#SigPxiTrigOutpRout)[ ](GP-IB_Command_Finder/Control.md#SigPxiRtrRout) |   
AUX TRIG (Ready) IN |  |   
Enable Handshake |  [TRIGger:CHANnel:AUXiliary:HANDshake](GP-IB_Command_Finder/Trigger_SCPI.md#AuxHandshake) |  [HandshakeEnable](COM_Reference/Properties/HandshakeEnable_Property.md)  
Edge or Level Level NOT in UI. |  [TRIGger:CHANnel:AUXiliary:TYPE](GP-IB_Command_Finder/Trigger_SCPI.md#auxType) |  [TriggerInType](COM_Reference/Properties/TriggerInType_Property.md)  
Polarity High/leading or Low/trailing. |  [TRIGger:CHANnel:AUXiliary:IPOLarity](GP-IB_Command_Finder/Trigger_SCPI.md#auxIpolarity) |  [TriggerInPolarity](COM_Reference/Properties/TriggerInPolarity_Property.md)  
Delay |  [TRIGger:CHANnel:AUXiliary:DELay](GP-IB_Command_Finder/Trigger_SCPI.md#AuxDelay) |  [Delay](COM_Reference/Properties/Delay_trigger_Property.md)  
  
Pulse Measurement Setup (PNA-X)  
---  
Pulse Meas Mode |  [SENSe:SWEep:PULSe:MODE](GP-IB_Command_Finder/Sense/SweepPulse.md#mode) |  [PulseMeasMode](COM_Reference/Properties/PulseMeasMode_Property.md)  
Autodetect Pulse mode |  [SENSe:SWEep:PULSe:DETectmode](GP-IB_Command_Finder/Sense/SweepPulse.md#detectmode) |  [AutoDetection](COM_Reference/Properties/AutoDetection_Property.md)  
Set Pulse Mode (Narrow | Wide) |  [SENSe:SWEep:PULSe:WIDeband](GP-IB_Command_Finder/Sense/SweepPulse.md#wideband) |  [WideBandDectionState](COM_Reference/Properties/WideBandDectionState_Property.md)  
Autoselect IFBW |  [SENS:SWEep:PULSe:CWTime[:AUTO]](GP-IB_Command_Finder/Sense/SweepPulse.md#CWSweepAuto) |  [AutoIFBandWidth](COM_Reference/Properties/AutoIFBandWidth_Property.md)  
Autoselect IF Gain |  [SENSe:SWEep:PULSe:IFGain](GP-IB_Command_Finder/Sense/SweepPulse.md#IFGain) |  None  
Autoselect Pulse clock period |  [SENSe:SWEep:PULSe:PRF](GP-IB_Command_Finder/Sense/SweepPulse.md#prf) |  [AutoOptimizePRF](COM_Reference/Properties/AutoOptimizePRF_Property.md)  
Autoselect Width and Delay |  [SENSe:SWEep:PULSe:TIMing](GP-IB_Command_Finder/Sense/SweepPulse.md#timing) |  [AutoPulseTiming](COM_Reference/Properties/AutoPulseTiming_Property.md)  
Autoselect Pulse Gens |  [SENSe:SWEep:PULSe:DRIVe](GP-IB_Command_Finder/Sense/SweepPulse.md#drive) |  [AutoSelectPulseGen](COM_Reference/Properties/AutoSelectPulseGen_Property.md)  
Autoselect CW Sweep Time |  [SENSe:SWEep:PULSe:CWTime](GP-IB_Command_Finder/Sense/SweepPulse.md#CWSweepAuto) |  [AutoCWSweepTime](COM_Reference/Properties/AutoCWSweepTime_Property.md)  
  
Pulse (manual) Settings |  |   
---|---|---  
Set master pulse frequency |  [SENSe:SWEep:PULSe:MASTer:FREQuency](GP-IB_Command_Finder/Sense/SweepPulse.md#MasterFreq) |  [MasterFrequency](COM_Reference/Properties/MasterFrequency_Property.md)  
Set master pulse period |  [SENSe:SWEep:PULSe:MASTer:PERiod](GP-IB_Command_Finder/Sense/SweepPulse.md#MasterPeriod) |  [MasterPeriod](COM_Reference/Properties/MasterPeriod_Property.md)  
Set master pulse width |  [SENSe:SWEep:PULSe:MASTer:WIDTh](GP-IB_Command_Finder/Sense/SweepPulse.md#MasterWidth) |  [MasterWidth](COM_Reference/Properties/MasterWidth_Property.md)  
Set pulse start time |  [SENSe:SWEep:PULSe:PROFile:STARt](GP-IB_Command_Finder/Sense/SweepPulse.md#SWEep:PULSe:PROFile:STARt) |  [PulseProfileStart](COM_Reference/Properties/PulseProfileStart_Property.md)  
Set pulse stop time |  [SENSe:SWEep:PULSe:PROFile:STOP](GP-IB_Command_Finder/Sense/SweepPulse.md#SWEep:PULSe:PROFile:STOP) |  [PulseProfileStop](COM_Reference/Properties/PulseProfileStop_Property.md)  
  
Pulse Generators (PNA-X)  
---  
Enable Pulse output ON | OFF |  [SENSe:PULSe<n>[:STATe]](GP-IB_Command_Finder/Sense/Pulse.md#state) |  [State](COM_Reference/Properties/State_pulse_Property.md)  
Set Pulse Period for ALL pulse generators |  [SENSe:PULSe:PERiod](GP-IB_Command_Finder/Sense/Pulse.md#period) |  [Period](COM_Reference/Properties/Period_Property.md)  
Set Pulse Delay |  [SENSe:PULSe<n>:DELay](GP-IB_Command_Finder/Sense/Pulse.md#delay) |  [Delay](COM_Reference/Properties/Delay_pulse_Property.md)  
Set Pulse Width |  [SENSe:PULSe<n>:WIDTh](GP-IB_Command_Finder/Sense/Pulse.md#width) |  [Width](COM_Reference/Properties/Width_Property.md)  
Set Pulse delay increment |  [SENSe:PULSe<n>:DINCrement](GP-IB_Command_Finder/Sense/Pulse.md#dincrement) |  [DelayIncrement](COM_Reference/Properties/DelayIncrement_Property.md)  
Enables Subpoint triggering |  [SENSe:PULSe<n>:SUBPointtrig](GP-IB_Command_Finder/Sense/Pulse.md#subPoint) |  [SubPointTrigger](COM_Reference/Properties/SubPointTrigger_Property.md)  
Set Pulse Invert |  [SENSe:PULSe<n>:INVert](GP-IB_Command_Finder/Sense/Pulse.md#invert) |  [Invert](COM_Reference/Properties/Invert_Property.md)  
Internal Pulse Modulator Enable [Choose from element value 8 or 9](../IFAccess/IF_Path_Configuration.md#8) |  [SENSe:PATH:CONFig:ELEMent](GP-IB_Command_Finder/Sense/Path.md#state) |  [Element](COM_Reference/Properties/Element_Property.md) [Value](COM_Reference/Properties/Value_element_Property.md)  
Returns the ADC delay. |  [SENSe:PULSe:HDELay:ADC?](GP-IB_Command_Finder/Sense/Pulse.md#SENSe:PULSe:HWDelay:ADC) |  [ADCDelay](COM_Reference/Properties/FixedADCDelay_Property.md)  
Sets the time lag between the pulse drive signal and the actual RF output. |  [SENSe:PULSe:HDELay:MODulator](GP-IB_Command_Finder/Sense/Pulse.md#SENSe:PULSe:HWDelay:MODulator) |  [ModulatorDelay](COM_Reference/Properties/ModulatorDelay_Property.md)  
Enables / Disables offset delays. |  [SENSe:PULSe:HDELay[:STATe]](GP-IB_Command_Finder/Sense/Pulse.md#SENSe:PULSe:HWDelay:STATe) |  [EnableOffsetDelays](COM_Reference/Properties/EnableOffsetDelays_Property.md)  
Sets and reads the device being controlled by the pulse generator output. |  [SENSe:PULSe:MTIMing:DEVice](GP-IB_Command_Finder/Sense/Pulse.md#SENSe:PULSe:MTIMing:DEVice) |  [PulseTimingDevice](COM_Reference/Properties/PulseTimingDevice_Property.md)  
Enable pulse4 to monitor ADC activity. |  [SENSe:PULSe4:OPTion](GP-IB_Command_Finder/Sense/Pulse.md#SENSe:PULSe4:OPTion) |  [Pulse4OutAsADCActivity](COM_Reference/Properties/Pulse4OutAsADCActivity_Property.md)  
Sets the specific PULSe4 behavior. |  [SENSe:PULSe4:MODE](GP-IB_Command_Finder/Sense/Pulse.md#SENSe:PULSe4:OPTion:MODE) |  None  
  
External Pulse Trigger (PNA-X)  
---  
PulseSyncIn Trigger Polarity |  [SENSe:PULSe:TPOLarity](GP-IB_Command_Finder/Sense/Pulse.md#TPolarity) |  [TriggerInPolarity](COM_Reference/Properties/TriggerInPolarity_Property.md)  
PulseSyncIn Trigger Type |  [SENSe:PULSe:TTYPe](GP-IB_Command_Finder/Sense/Pulse.md#TType) |  [TriggerInType](COM_Reference/Properties/TriggerInType_Property.md)  
Sync receiver to Pulse0 (enable pulse0) |  [SENSe:PULSe[:STATe]](GP-IB_Command_Finder/Sense/Pulse.md#state) |  [pulse.State](COM_Reference/Properties/State_pulse_Property.md)  
Pulse Trigger Source [Choose element and setting](../IFAccess/IF_Path_Configuration.md#6) |  [SENSe:PATH:CONFig:ELEMent](GP-IB_Command_Finder/Sense/Path.md#state) |  [Element](COM_Reference/Properties/Element_Property.md) [Value](COM_Reference/Properties/Value_element_Property.md)  
  
[IF Path Configuration](../IFAccess/IF_Path_Configuration.md#elements)  
---  
  
DC Source Control [See Ext DC Device commands](XTraceChanTopic.md#DC) |  |   
---|---|---  
Source names catalog |  [SOURce:DC:CATalog?](GP-IB_Command_Finder/SourceDC.md#names) |  [Sources](COM_Reference/Properties/Sources_Property.md)  
Enable source outputs |  [SOURce:DC:ENABle](GP-IB_Command_Finder/SourceDC.md#Enable) |  [EnableAllOutput](COM_Reference/Properties/EnableAllOutput_Property.md)  
Source state |  [SOURce:DC:STATe](GP-IB_Command_Finder/SourceDC.md#state) |  [State](COM_Reference/Properties/State_DC_Property.md)  
Start DC |  [SOURce:DC:STARt](GP-IB_Command_Finder/SourceDC.md#start) |  [Start](COM_Reference/Properties/Start_DC_Property.md)  
Stop DC |  [SOURce:DC:STOP](GP-IB_Command_Finder/SourceDC.md#stop) |  [Stop](COM_Reference/Properties/Stop_DC_Property.md)  
Data |  [SOURce:DC:DATA](GP-IB_Command_Finder/SourceDC.md#data) |  [ListData](COM_Reference/Properties/ListData_Property.md)  
Set and return the Max DC limit value for a DC source |  [SOURce:DC:LIMit:MAXimum](GP-IB_Command_Finder/SourceDC.md#SOURce:DC:LIMit:MAXimum) |  [LimitMax](COM_Reference/Properties/LimitMax_Property.md)  
Set and return the Min DC limit value for a DC source |  [SOURce:DC:LIMit:MINimum](GP-IB_Command_Finder/SourceDC.md#SOURce:DC:LIMit:MINimum) |  [LimitMin](COM_Reference/Properties/LimitMin_Property.md)  
  
Multi-Dimensional Sweep  
---  
Set and read the order for the specified DC source in the multi-dimensional sweep. |  **SOURce:DC:DIMension:ORDer** |  [DCOrder](COM_Reference/Properties/DCOrder_Property.md)  
Set and read the specified DC sources ON/OFF state in the multi-dimensional sweep. |  **SOURce:DC:DIMension[:STATe]** |  [DCState](COM_Reference/Properties/DCState_Property.md)  
Read the names of source domains in the multi-dimensional sweep whose state is ON and whose dimension order is the specified dimension order. |  **SOURce:DIMension:CATalog?** |  [DimensionCatalog](COM_Reference/Properties/DimensionCatalog_Property.md)  
Read the highest dimension order in the multi-dimensional sweep. |  **SOURce:DIMension:COUNt?** |  [DimensionCount](COM_Reference/Properties/DimensionCount_Property.md)  
Set and read the point count for the specified dimension order in the multi-dimensional sweep. |  **SOURce:DIMension:POINts** |  [DimensionPointCount](COM_Reference/Properties/DimensionPointCount_Property.md)  
Set and read the repeat count for the specified dimension order in the multi-dimensional sweep. |  **SOURce:DIMension:REPeat:COUNt** |  [DimensionRepeatCount](COM_Reference/Properties/DimensionRepeatCount_Property.md)  
Set and read the source frequency domains order in the multi-dimensional sweep. |  **SOURce:FREQuency:DIMension:ORDer** |  [SourcePortFrequencyOrder](COM_Reference/Properties/SourcePortFrequencyOrder_Property.md)  
Set and read the source frequency domains ON/OFF state in the multi-dimensional sweep. |  **SOURce:FREQuency:DIMension[:STATe]** |  [SourcePortFrequencyState](COM_Reference/Properties/SourcePortFrequencyState_Property.md)  
Set and read the fixed frequency value for a specific port. |  **SOURce:FREQuency:FIXed** |  [SourcePortFixedFrequency](COM_Reference/Properties/SourcePortFixedFrequency_Property.md)  
Set and read the start frequency value for a specific port. |  **SOURce:FREQuency:STARt** |  [SourcePortStartFrequency](COM_Reference/Properties/SourcePortStartFrequency_Property.md)  
Set and read the stop frequency value for a specific port. |  **SOURce:FREQuency:STOP** |  [SourcePortStopFrequency](COM_Reference/Properties/SourcePortStopFrequency_Property.md)  
Set and read the source phase domains order in the multi-dimensional sweep. |  **SOURce:PHASe:DIMension:ORDer** |  [SourcePortPhaseOrder](COM_Reference/Properties/SourcePortPhaseOrder_Property.md)  
Set and read the source phase domains ON/OFF state in the multi-dimensional sweep. |  **SOURce:PHASe:DIMension[:STATe]** |  [SourcePortPhaseState](COM_Reference/Properties/SourcePortPhaseState_Property.md)  
Set and read the source power domains order in the multi-dimensional sweep. |  **SOURce:POWer:DIMension:ORDer** |  [SourcePortPowerOrder](COM_Reference/Properties/SourcePortPowerOrder_Property.md)  
Set and read the source power domains ON/OFF state in the multi-dimensional sweep. |  **SOURce:POWer:DIMension[:STATe]** |  [SourcePortPowerState](COM_Reference/Properties/SourcePortPowerState_Property.md)  
  
Global Source Commands  
---  
Set and return the frequency of the specified global source. |  [SYSTem:PREFerences:SOURce:GLOBal:FREQuency](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:SOURce:GLOBal:FREQuency) |  None  
Set and return the output state of the specified global source. |  [SYSTem:PREFerences:SOURce:GLOBal:OUTPut[:STATe]](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:SOURce:GLOBal:OUTPut:STATe) |  None  
Set and return the global sources that ignore the power off setting. |  [SYSTem:PREFerences:SOURce:GLOBal:POFF:IGNore[:STATe]](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:SOURce:GLOBal:POFF:IGNore:STATe) |  None  
Set and return the power of the specified global source. |  [SYSTem:PREFerences:SOURce:GLOBal:POWer](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:SOURce:GLOBal:POWer) |  None  
Set and return the global state of the specified global source. |  [SYSTem:PREFerences:SOURce:GLOBal[:STATe]](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:SOURce:GLOBal:STATe) |  None  
Loads the internal source modulation file. |  [SYSTem:PREFerences:SOURce:GLOBal:MODulation:LOAD](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:SOURce:GLOBal:MODulation:LOAD) |  None  
Returns the name of the currently loaded internal source modulation file. |  [SYSTem:PREFerences:SOURce:GLOBal:MODulation:FILE?](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:SOURce:GLOBal:MODulation:NAME) |  None  
Set and return the state of the specified internal source modulation port. |  [SYSTem:PREFerences:SOURce:GLOBal:MODulation[:STATe]](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:SOURce:GLOBal:MODulation:STATe) |  None  
  
* * *

![](../assets/images/Tp.gif)

