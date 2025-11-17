# Setup Commands - Spectrum Analyzer Measurement Class

Only the Main and Layout Setup commands corresponding to the Spectrum Analyzer
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
SA Setup... | SA Tab  
Sweep Type | [SENSe:SWEep:TYPE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssty) | [SourceSweepType](COM_Reference/Properties/SourceSweepType_Property.md) [SourceSweepType2](COM_Reference/Properties/SourceSweepType2_Property.md)  
Start | [SENSe:FREQuency:STARt](GP-IB_Command_Finder/Sense/Frequency.md#start) | [chan.StartFrequency](COM_Reference/Properties/Start_Frequency_Property.md)  
Stop | [SENSe:FREQuency:STOP](GP-IB_Command_Finder/Sense/Frequency.md#stop) | [chan.StopFrequency](COM_Reference/Properties/Stop_Frequency_Property.md)  
Center | [SENSe:FREQuency:CENTer](GP-IB_Command_Finder/Sense/Frequency.md#cent) | [chan.CenterFrequency](COM_Reference/Properties/CenterFreq_Property.md)  
Span | [SENSe:FREQuency:SPAN](GP-IB_Command_Finder/Sense/Frequency.md#span) [SENSe:FREQuency:SPAN:FULL](GP-IB_Command_Finder/Sense/Frequency.md#SpanFull) | [chan.FrequencySpan](COM_Reference/Properties/Frequency_Span_Property.md) [FrequencySpanFull](COM_Reference/Methods/FrequencySpanFull_Method.md)  
Number of Points | [SENSe:SWEep:POINts](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssp) | [chan.NumberOfPoints](COM_Reference/Properties/Number_of__Points_Property.md)  
Resolution Bandwidth | [SENSe:SA:BANDwidth:RESolution:CATalog?](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:BANDwidth:RESolution:CATalog) [SENSe:SA:BANDwidth:[RESolution]](GP-IB_Command_Finder/Sense/SA.md#BandRes) [SENSe:SA:BANDwidth:[RESolution]:AUTO](GP-IB_Command_Finder/Sense/SA.md#bandResAuto) [SENSe:SA:BANDwidth:RESolution MIN](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:BANDwidth:RESolution) [SENSe:SA:BANDwidth:RESolution MAX](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:BANDwidth:RESolution) | [ResBWList](COM_Reference/Properties/ResBWList_\(Spectrum_Analyzer\)_Property.md) [ResolutionBW](COM_Reference/Properties/ResolutionBW_\(SA\)_Property.md) [ResolutionBWMode](COM_Reference/Properties/ResolutionBWMode_Property.md) [ResolutionBWMin](COM_Reference/Properties/ResolutionBWMin.md) [ResolutionBWMax](COM_Reference/Properties/ResolutionBWMax.md)  
Video Bandwidth | [SENSe:SA:BANDwidth:VIDeo](GP-IB_Command_Finder/Sense/SA.md#video) [SENSe:SA:BANDwidth:VIDeo:AUTO](GP-IB_Command_Finder/Sense/SA.md#videoAuto) [SENSe:SA:BANDwidth:VIDeo MIN](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:BANDwidth:VIDeo) [SENSe:SA:BANDwidth:VIDeo MAX](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:BANDwidth:VIDeo) | [VideoBW](COM_Reference/Properties/VideoBW_Property.md) [VideoBWMode](COM_Reference/Properties/VideoBWMode_Property.md) [VideoBWMin](COM_Reference/Properties/VideoBWMin.md) [VideoBWMax](COM_Reference/Properties/VideoBWMax.md)  
Detector Type | [SENSe:SA:DETector:FUNCtion](GP-IB_Command_Finder/Sense/SA.md#detFunction) | [DetectorFunction](COM_Reference/Properties/DetectorFunction_Property.md)  
Detector Bypass | [SENSe:SA:DETector:BYPass:[STATe]](GP-IB_Command_Finder/Sense/SA.md#detBypassState) | [EnableDetectorBypass](COM_Reference/Properties/DetectorBypassState_Property.md)  
Averaging Type | [SENSe:SA:BANDwidth:VIDeo:AVER:TYPE](GP-IB_Command_Finder/Sense/SA.md#vidAverType) | [VideoAveragingType](COM_Reference/Properties/VideoAveragingType_Property.md)  
| [SENSe:SA:BANDwidth:VIDEO:AVERage:COUNt?](GP-IB_Command_Finder/Sense/SA.md#vidAverCount) | [VideoAveragingCount](COM_Reference/Properties/VideoAveragingCount_Property.md)  
Receiver Attenuators | [SENSe:POWer:ATTenuator](GP-IB_Command_Finder/Sense/Power.md) [SOURce:POWer:ATTenuation:RECeiver:TEST](GP-IB_Command_Finder/source.md#SOURce:POWer:ATTenuation:RECeiver:TEST) (Spectrum Analysis for M980xA, P50xxA/B) | [Receiver Attenuator](COM_Reference/Properties/Receiver_Attenuator_Property.md)  
Source Tab  
Power On (All Channels) | [SOURce:POWer:MODE](GP-IB_Command_Finder/source.md#Mode) | [SourcePortMode](COM_Reference/Properties/SourcePortMode_Property.md)  
Port Powers Coupled | [SOURce:POWer:COUPle](GP-IB_Command_Finder/source.md#cplON) | [CouplePorts](COM_Reference/Properties/Couple_Ports_Property.md)  
State | [SOURce:PULSe[:STATe]](GP-IB_Command_Finder/source.md#SOURce:PULSe:STATe) [SOURce:PULSe:EXISts?](GP-IB_Command_Finder/source.md#SOURce:PULSe:EXISts) | None None  
Type | [SENSe:SA:SOURce:SWEep:TYPE](GP-IB_Command_Finder/Sense/SA.md#sourSweepType) | [SourceSweepType](COM_Reference/Properties/SourceSweepType_Property.md) [SourceSweepType2](COM_Reference/Properties/SourceSweepType2_Property.md)  
Frequency | [SENSe:SA:SOURce:FREQuency:STARt](GP-IB_Command_Finder/Sense/SA.md#SourFreqStart) [SENSe:SA:SOURce:FREQuency:STOP](GP-IB_Command_Finder/Sense/SA.md#sourFreqStop) | [SourceStartFrequency](COM_Reference/Properties/SourceStartFrequency_Property.md) [SourceStopFrequency](COM_Reference/Properties/SourceStopFrequency_Property.md)  
Power | [SENSe:SA:SOURce:POWer:STARt](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:SOURce:POWer:STARt) [SENSe:SA:SOURce:POWer:STOP](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:SOURce:POWer:STOP) [SENSe:SA:SOURce:POWer[:VALue]](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:SOURce:POWer_:VALue) | [SourceStartPower](COM_Reference/Properties/SourceStartPower_Property.md) [SourceStopPower](COM_Reference/Properties/SourceStopPower_Property.md) [SourcePower](COM_Reference/Properties/SourcePower_Property.md)  
Phase | [SOURce:PHASe:FIXed](GP-IB_Command_Finder/SourcePhase.md#fixed) | [FixedPhase](COM_Reference/Properties/FixedPhase_Property.md)  
[Pulse Setup...](CF_Sweep_Commands_-_SA.md) |  |   
IQMod - Modulation settings dialog  
Enable Modulation | [SOURce:MODulation[:STATe]](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:STATe) | None  
Modulation Filename | [SOURce:MODulation:LOAD](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:LOAD) | None  
Show File Properties |  |   
Modulation File Name | [SOURce:MODulation:FILE?](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE) | None  
Source Name | [SOURce:CATalog?](GP-IB_Command_Finder/source.md#Cat) | [SourcePortNames](COM_Reference/Properties/SourcePortNames_Property.md)  
Sample Rate | [SOURce:MODulation:FILE:SIGNal:SRATe?](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:SRATe) [SOURce:MODulation:ARB:CLOCk:SRATe?](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:DARB:CLOCk) | None None  
Number of Samples | None | None  
Modulation Type | [SOURce:MODulation:FILE:TYPE?](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:TYPE) | None  
Signal Span | [SOURce:MODulation:FILE:SIGNal:SPAN?](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:SPAN) [SOURce:MODulation:FILE:SIGNal:SPAN:CALCulated?](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:SPAN:CALCulated) [SOURce:MODulation:FILE:SIGNal:SPAN:PRIority?](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:SPAN:PRIority) | None None None  
Equivalent Continuous Span | [CALCulate:MEASure:SA:MARKer:BPOWer:SPAN?](GP-IB_Command_Finder/Calculate/MeasureSA.md#CALCulate:MEASure:SA:MARKer:BPOWer:SPAN) | [BandpowerSpan](COM_Reference/Properties/BandpowerSpan_Property.md)  
Tone Spacing | [SOURce:MODulation:FILE:SIGNal:OPTimize:MAX:TONE:SPacing?](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:OPTimize:MAX:TONE:SPACing) | None  
Waveform Period | [SOURce:MODulation:FILE:SIGNal:OPTimize:MIN:WAVeform:PERiod?](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:OPTimize:MIN:WAVeform:PERiod) | None  
Number of Tones | [SOURce:MODulation:FILE:SIGNal:OPTimize:MIN:TONE:NUMBer?](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:OPTimize:MIN:TONE:NUMBer) | None  
Peak-to-Avg | [SOURce:MODulation:FILE:SIGNal:PAVG:CALCulated?](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:PAVG:CALCulated) | None  
Carrier Offset | [SOURce:MODulation:FILE:SIGNal:CARRier:OFFSet?](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:CARRier:OFFSet) | None  
DAC Scaling | [SOURce:MODulation:FILE:SIGNal:DAC:SCALing?](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:DAC:SCALing) | None  
Phase Type | [SOURce:MODulation:FILE:SIGNal:PHASe:TYPE?](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:PHASe:TYPE) | None  
Random Phase Seed | [SOURce:MODulation:FILE:SIGNal:PHASe:RANDom:SEED?](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:PHASe:RANDom:SEED) | None  
Number of Notches | [SOURce:MODulation:FILE:SIGNal:NPR:NOTCh:NUMBer?](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:NPR:NOTCh:NUMBer) | None  
Notch Location | [SOURce:MODulation:FILE:SIGNal:NPR:NOTCh:LOCation?](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:NPR:NOTCh:LOCation) | None  
Notch1 Span | [SOURce:MODulation:FILE:SIGNal:NPR:NOTCh:SPAN?](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:NPR:NOTCh:SPAN) | None  
Notch1 Offset | [SOURce:MODulation:FILE:SIGNal:NPR:NOTCh:OFFSet?](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:NPR:NOTCh:OFFSet) | None  
Receiver RBW | None | None  
Measurement Time | None | None  
[Create/Edit Mod File...](CF_Setup_Commands_-_MOD.md#Create_Edit_Mod_File) |  |   
Autoset Frequencies and Coherence for current modulation | [SOURce:MODulation:AUTO:SA[:STATe]](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:AUToset:SA:STATe) | None  
Immediate Autoset | [SOURce:MODulation:AUTO:IMMediate](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:AUToset:IMMediate) | None  
Autoset NPR Markers | [SOURce:MODulation:AUTO:NPR[:STATe]](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:AUToset:NPR:STATe) | None  
NPR Band Guard | [SOURce:MODulation:AUTO:NPR:GBANd](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:AUToset:NPR:GBANd) | None  
Autoset ACPR Markers | [SOURce:MODulation:AUTO:ACPR[:STATe]](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:AUToset:ACPR:STATe) | None  
ACPR Band Guard | [SOURce:MODulation:AUTO:ACPR:GBANd](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:AUToset:ACPR:GBANd) | None  
Enable Modulation Correction | [SOURce:MODulation:CORRection[:STATe]](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:CORRection:STATe) | None  
[Calibrate Modulation...](CF_Cal_Commands_-_MOD.md#Src_Mod_Cal) |  |   
Source Power | [SENSe:SA:SOURce:POWer[:VALue]](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:SOURce:POWer_:VALue) | None  
[Source Path Amplification (= Power Offset)](CF_Power_Commands_-_MOD.md) |  |   
For SA Analysis Marker commands for getting measurement data, refer to [SA Analysis Tab Commands](CF_Markers_Commands.md#SA_Analysis_Tab_Commands). |  |   
RF source sweep order | [SENSe:SA:SOURce:SWEep:FIRst[:DIMension]](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:SOURce:SWEep:FIRst) | [SourceSweepFirstDimension](COM_Reference/Properties/SourceSweepFirstDimension_Property.md)  
Path Configuration... | [SENSe:PATH:CONFig:ELEMent[:STATe]](GP-IB_Command_Finder/Sense/Path.md#state) | [Element](COM_Reference/Properties/Element_Property.md)  
[Power and Attenuator...](CF_Power_Commands_-_SA.md) |  |   
[External Devices...](CF_Setup_Commands_-_Standard.md#External_Hardware_Commands) |  |   
Coherence Tab  
Enable multitone | [SENSe:SA:COHerence:MULTitone[:STATe]](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:IMAGe:COHerence:STATe) | [MultiToneEnable](COM_Reference/Properties/MultiToneImageRejectEnable_Property.md)  
Tone Spacing | [SENSe:SA:COHerence:MULTitone:SPACing](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:IMAGe:COHerence:SPACing) | [MultiToneSpacing](COM_Reference/Properties/MultiToneImageRejectSpacing_Property.md)  
Waveform Period | [SENSe:SA:COHerence:MULTitone:PERiod](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:IMAGe:COHerence:PERiod) | [MultiTonePeriod](COM_Reference/Properties/MultiToneImageRejectPeriod_Property.md)  
Reference Tone | [SENSe:SA:COHerence:MULTitone:REFerence](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:IMAGe:COHerence:REFerence) | [MultiToneReference](COM_Reference/Properties/MultiToneImageRejectReference_Property.md)  
Reject up to harmonic | [SENSe:SA:COHerence:MULTitone:HREJect](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:IMAGe:COHerence:HREJect) | [MultiToneHarmonicRejection](COM_Reference/Properties/MultiToneImageRejectHarmonic_Property.md)  
Nyquist protect order | [SENSe:SA:COHerence:MULTitone:NYQReject](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:COHerence:MULTitone:NYQReJect) | [MultiToneNyquistProtection](COM_Reference/Properties/MultiToneNyquistProtection_Property.md)  
Vector averaging | [SENSe:SA:COHerence:VECTor:AVERage[:STATe]](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:COHerence:VECTor:AVERage:STATe) [SENSe:SA:COHerence:VECTor:AVERage:VALue](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:COHerence:VECTor:AVERage:VALue) | [VectorAverageEnable](COM_Reference/Properties/VectorAverageEnable_Property.md) [VectorAverageValue](COM_Reference/Properties/VectorAverageValue_Property.md) [VectorAverageValueMax](COM_Reference/Properties/VectorAverageMax.md)  
Data Display | [SENSe:SA:COHerence:MULTitone:DATA](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:IMAGe:COHerence:DATa) | [MultiToneDataDisplay](COM_Reference/Properties/MultiToneImageRejectDataDisplay_Property.md)  
Multitone settings are valid | [SENSe:SA:COHerence:MULTitone:VALid](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:COHerence:MULTitone:VALid) | [MultiToneSettingsValid](COM_Reference/Properties/MultitoneSettingsValid_Property.md)  
Compute Phases | [SENSe:SA:COHerence:PHASe[:STATe]](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:COHerence:PHASe:STATe) | [PhaseProcessState](COM_Reference/Properties/PhaseProcessState_Property.md)  
Display Phases if Tone Power > | [SENSe:SA:COHerence:PHASe:DISPlay:LEVel](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:COHerence:PHASe:DISPlay:LEVel) | [PhaseDisplayMinLevel](COM_Reference/Properties/PhaseDisplayMinLevel_Property.md)  
Enable Phase Stitching from HW timestamps | [SENSe:SA:COHerence:PHASe:STITching:HWTStamp[:STATe]](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:COHerence:PHASe:STITching:HWTStamp) | None  
Enable Phase Stitching from overlapped areas | [SENSe:SA:COHerence:PHASe:STITching[:STATe]](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:COHerence:PHASe:STITching:STATe) [SENSe:SA:COHerence:PHASe:STITching:COMmon[:STATe]](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:COHerence:PHASe:STITching:COMmon:STATe) | None None  
Stitch Phases if Tone Power > | [SENSe:SA:COHerence:PHASe:STITching:LEVel](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:COHerence:PHASe:STITching:LEVel) | None  
Receiver for Stitching | [SENSe:SA:COHerence:PHASe:STITching:RECeiver:NAME](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:COHerence:PHASe:STITching:RECeiver:NAME) | None  
Auto | [SENSe:SA:COHerence:PHASe:STITching:RECeiver:AUTO[:STATe]](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:COHerence:PHASe:STITching:RECeiver:AUTO:STATe) | None  
Compute time domain IQ | [SENSe:SA:DATA:IQ[:STATe]](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:DATA:IQ:STATe) [SENSe:SA:DATA:IQ:GET?](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:DATA:IQ:GET) | None None  
Auto Fill IQ settings | [SENSe:SA:DATA:IQ:AUTofill](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:DATA:IQ:AUTOfill) | None  
Receivers | [SENSe:VSA:DATA:SA:RECievers](GP-IB_Command_Finder/Sense/SA.md#SENSe:VSA:DATA:SA:RECeivers) | None  
IQ keeps aligned with SA center, span, coherence | [SENSe:SA:DATA:IQ:ALIgned[:STATe]](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:DATA:IQ:ALIgned:STATe) | None  
VSA Setup...  
Connect VSA | [SENSe:VSA:CONNect[:STATe]](GP-IB_Command_Finder/Sense/VSA.md#SENSe:VSA:CONNect) | None  
Enable Digital Trigger | [SENSe:VSA:DTRigger[:STATe]](GP-IB_Command_Finder/Sense/VSA.md#SENSe:VSA:DTRigger:STATe) | None  
Autotune Spectrum | [SENSe:VSA:SPECtrum:AUTOtune](GP-IB_Command_Finder/Sense/VSA.md#SENSe:VSA:SPECtrum:AUTOset) | None  
Show VSA | [SENSe:VSA:SHOW](GP-IB_Command_Finder/Sense/VSA.md#SENSe:VSA:SHOW) | None  
Stream Data to VSA | [SENSe:VSA:DATA:STReam[:STATe]](GP-IB_Command_Finder/Sense/VSA.md#SENSe:VSA:DATA:STReam) | None  
Select Data | [SENSe:VSA:DATA:SA:RECievers](GP-IB_Command_Finder/Sense/SA.md#SENSe:VSA:DATA:SA:RECeivers) (SA channels only) [SENSe:VSA:DATA:MOD:PIN1[:STATe]](GP-IB_Command_Finder/Sense/VSA.md#SENSe:VSA:DATA:MOD:PIN1:STATe) (MOD/MODX channels only) [SENSe:VSA:DATA:MOD:POU2[:STATe]](GP-IB_Command_Finder/Sense/VSA.md#SENSe:VSA:DATA:MOD:POU2:STATe) (MOD/MODX channels only) [SENse:VSA:DATA:MOD:PINWav[:STATe]](GP-IB_Command_Finder/Sense/VSA.md#SENSe:VSA:DATA:MOD:PINWav:STATe) (MOD/MODX channels only) | None None None None  
Saved State Includes VSA state ( all channels) | [SENSe:VSA:SAVe:INCLude[STATe] ](GP-IB_Command_Finder/Sense/VSA.md#SENSe:VSA:SAVe:INCLude:STATe) | None  
VSA Status... | [SENSe:VSA:STAtus:REPort?](GP-IB_Command_Finder/Sense/VSA.md#SENSe:VSA:STAtus:REPort) | None  
Trig. & Pulse Tab  
Advanced Trigger Mode | [SENSe:SA:TRIGer:LEVel[:STATe]](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:TRIGer:LEVel:STATe) | [TriggerADCLevelState](COM_Reference/Properties/TriggerADCLevelState_Property.md)  
ADC Level | [SENSe:SA:TRIGer:LEVel[:STATe]](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:TRIGer:LEVel:STATe) [SENSe:SA:TRIGer:LEVel:VALue](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:TRIGer:LEVel:VALue) | [TriggerADCLevelState](COM_Reference/Properties/TriggerADCLevelState_Property.md) [TriggerADCLevelValue](COM_Reference/Properties/TriggerADCLevelValue_Property.md)  
Periodic Counter | [SENSe:SA:TRIGer:PERCounter[:STATe]](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:TRIGer:PERCounter:STATe) [SENSe:SA:TRIGer:PERCounter:VALue](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:TRIGer:PERCounter:VALue) | [TriggerPeriodicCounterState](COM_Reference/Properties/TriggerPeriodicCounterState_Property.md) [TriggerPeriodicCounterValue](COM_Reference/Properties/TriggerPeriodicCounterValue_Property.md)  
[Trigger...](CF_Trigger_Commands.md#Trigger) |  |   
[Pulse Gen Config...](CF_Sweep_Commands_-_SA.md) |  |   
Advanced Tab  
RBW Shape | [SENSe:SA:BANDwidth:SHAPe](GP-IB_Command_Finder/Sense/SA.md#bandShape) | [BandwidthShape](COM_Reference/Properties/BandwidthShape_\(SA\)_Property.md)  
Image Reject Type | [SENSe:SA:IMAGe:REJect](GP-IB_Command_Finder/Sense/SA.md#imagRej) | [ImageRejectMethod](COM_Reference/Properties/ImageReject_Property.md)  
Image Reject Strength | [SENSe:SA:IMAGe:STRENgth](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:IMAGe:STRENgth) | [ImageRejectStrength](COM_Reference/Properties/ImageRejectStrength_Property.md)  
RBW/VBW | [SENSe:SA:BANDwidth:VIDeo:RATio](GP-IB_Command_Finder/Sense/SA.md#bandVidRatio) | [ResolutionBWVideoBWRatio](COM_Reference/Properties/ResolutionBWVideoBWRatio_Property.md)  
Span/RBW | [SENSe:SA:FREQuency:SPAN:BANDwidth[:RESolution]:RATio](GP-IB_Command_Finder/Sense/SA.md#freqSpanBWRat) | [SpanResolutionBWRatio](COM_Reference/Properties/SpanResolutionBWRatio_Property.md)  
CF Step Size | [SENSe:FREQuency:CENTer:STEP:SIZE](GP-IB_Command_Finder/Sense/Frequency.md#StepSize) [SENSe:FREQuency:CENTer:STEP:AUTO](GP-IB_Command_Finder/Sense/Frequency.md#STEPAUTO) | [CenterFrequencyStepSize](COM_Reference/Properties/CenterFrequencyStepSize_Property.md) [CenterFrequencyStepSizeMode](COM_Reference/Properties/CenterFrequencyStepSizeMode_Property.md)  
Occupied BW search min | [SENSe:SA:BANDwidth:SEARch:OCCupied:MIN](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:BANDwidth:SEARch:OCCupied:MIN) | [SearchOccupiedBWMinFreq](COM_Reference/Properties/SearchOccupiedBWMinFreq_Property.md)  
Enable DC Outputs | [SOURce:DC:ENABle](GP-IB_Command_Finder/SourceDC.md#Enable) | [EnableAllOutput](COM_Reference/Properties/EnableAllOutput_Property.md)  
Enable DC Sweep | [SENSe:SA:SOURce:DC:SWEep[:STATe]](GP-IB_Command_Finder/Sense/SA.md#DC:SWEep:STATe) | [DCSourceSweepState](COM_Reference/Properties/DCSourceSweepState.md)  
Number of DC levels | [SENSe:SA:SOURce:DC:SWEep:POINt](GP-IB_Command_Finder/Sense/SA.md#DC:SWEep:POINt) | [DCSourcePointCount](COM_Reference/Properties/DCSourcePointCount_Property.md)  
Sweep Order | [SENSe:SA:SOURce:DC:SWEep:FIRst[:DIMension]](GP-IB_Command_Finder/Sense/SA.md#DC:SWEep:FIRst:DIMension) | [DCSourceSweepFirstDimension](COM_Reference/Properties/DCSourceSweepFirstDimension_Property.md)  
| [SENSe:SA:FREQuency:TUNE:IMMediate](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:FREQuency:TUNE:IMMediate) | [FrequencyAutoTune](COM_Reference/Methods/FrequencyAutoTune_Method.md)  
Enable Frequency Converter Configuration | [SENSe:SA:FREQuency:CONVerter[:STATe]](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:FREQuency:CONVerter:STATe) | None  
Source | [SENSe:SA:FREQuency:CONVerter:INPut:SOURce](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:FREQuency:CONVerter:INPut:SOURce) | None  
Port (input) | [SENSe:SA:FREQuency:CONVerter:INPut:PORT](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:FREQuency:CONVerter:INPut:PORT) | None  
Center (input) | [SENSe:SA:FREQuency:CONVerter:INPut:CENTer](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:FREQuency:CONVerter:INPut:CENTer) | None  
Inverted | [SENSe:SA:FREQuency:CONVerter:OUTPut:INVerted](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:FREQuency:CONVerter:OUTPut:INVerted) | None  
Port (output) | [SENSe:SA:FREQuency:CONVerter:OUTPut:PORT](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:FREQuency:CONVerter:OUTPut:PORT) | None  
Center (output) | [SENSe:SA:FREQuency:CONVerter:OUTPut:CENTer](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:FREQuency:CONVerter:OUTPut:CENTer) | None  
Output center offset | [SENSe:SA:FREQuency:CONVerter:OUTPut:OFFSet](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:FREQuency:CONVerter:OUTPut:OFFSet) | None  
[DC Sources...](CF_Setup_Commands_-_Standard.md#External_Hardware_Commands) |  |   
[Embedded LO](CF_Setup_Commands_-_MOD.md#Setup) |  |   
IF Tab  
ADC Filter | [SENSe:SA:ADC:FILTer](GP-IB_Command_Finder/Sense/SA.md#FFT_Width) | [ADCFilter](COM_Reference/Properties/FFTWidthMode_Property.md)  
ADC Filter Auto | [SENSe:SA:ADC:FILTer:AUTO](GP-IB_Command_Finder/Sense/SA.md#ADC_FILTer_AUTO) | [EnableADCFilterAuto](COM_Reference/Properties/ADCFilterAuto.md)  
DFT Bandwidth Auto | [SENSe:SA:DFT:BANDwidth:AUTO](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:DFT:BANDwidth:AUTO) | [AutoBandwidth](COM_Reference/Properties/AutoBandwidth_Property.md)  
Narrow - DFT Min | [SENSe:SA:DFT:BANDwidth:NARRow:MIN](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:DFT:BANDwidth:NARRow:MIN) | [BandwidthNarrowMin](COM_Reference/Properties/BandwidthNarrowMin_Property.md)  
Narrow - DFT Max | [SENSe:SA:DFT:BANDwidth:NARRow:MAX](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:DFT:BANDwidth:NARRow:MAX) | [BandwidthNarrowMax](COM_Reference/Properties/BandwidthNarrowMax_Property.md)  
Wide - DFT Min | [SENSe:SA:DFT:BANDwidth:WIDE:MIN](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:DFT:BANDwidth:WIDE:MIN) | [BandwidthWideMin](COM_Reference/Properties/BandwidthWideMin_Property.md)  
Wide - DFT Max | [SENSe:SA:DFT:BANDwidth:WIDE:MAX](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:DFT:BANDwidth:WIDE:MAX) | [BandwidthWideMax](COM_Reference/Properties/BandwidthWideMax_Property.md)  
IF Gain | [SENSe:PATH:CONFig:ELEMent[:STATe]](GP-IB_Command_Finder/Sense/Path.md#state) | [Element](COM_Reference/Properties/Element_Property.md)  
IF Config... | [SENSe:PATH:CONFig:ELEMent[:STATe]](GP-IB_Command_Finder/Sense/Path.md#state) | [Element](COM_Reference/Properties/Element_Property.md)  
Processing Tab  
DFT Type | [SENSe:SA:DFT:TYPE](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:DFT:TYPE) | [Type](COM_Reference/Properties/Type_Property.md)  
|  | None  None None None None None None  
IQ Carrier Frequency | [SENSe:SA:DATA:IQ:CARRier:FREQuency](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:DATA:IQ:CARRier:FREQuency) | None  
IQ Sample Rate | [SENSe:SA:DATA:IQ:SAMPle:RATE](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:DATA:IQ:SAMPle:RATE) | None  
Number of IQ Pairs | [SENSe:SA:DATA:IQ:SAMPle:COUNt](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:DATA:IQ:SAMPle:COUNt) | None  
|  |   
Acq. Time for 1 LO | [SENSe:SA:ADC:ACQTime?](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:ADC:ACQTime) | [AcquisitionTime](COM_Reference/Properties/AcquisitionTime.md)  
Span LOs count | [SENSe:SA:LO:COUNt?](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:LO:NUMBer) | [LOCount](COM_Reference/Properties/LONumber_Property.md)  
Span bins count | [SENSe:SA:SPAN:BINS:COUNt?](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:SPAN:BINS:COUNt) | [SpanBinsCount](COM_Reference/Properties/SpanBinsCount_Property.md)  
DFT resolution | [SENSe:SA:DFT:RESolution?](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:DFT:RESolution) | [Resolution](COM_Reference/Properties/Resolution_Property.md)  
DFT record size | [SENSe:SA:DFT:RECord:SIZE?](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:DFT:RECord:SIZE) | [RecordSize](COM_Reference/Properties/RecordSize_Property.md)  
ADC record size | [SENSe:SA:ADC:RECord:SIZE:VALue?](GP-IB_Command_Finder/Sense/SA.md#FFT_ADC_Record_Size_Value) | [ForceADCRecordSize](COM_Reference/Properties/ForceADCRecordSize_Property.md)  
IQ record duration | [SENSe:SA:DATA:IQ:DURation?](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:DATA:IQ:DURation) | None  
VSA IQ pairs count |  | None  
Valid IQ Settings | [SENSe:SA:DATA:IQ:ERRor:TEXT?](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:DATA:IQ:ERRor:TEXT) [SENSe:SA:DATA:IQ:ERRor[:CODE]?](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:DATA:IQ:ERRor:CODE) | None  None  
Display image reject traces | [SENSe:SA:TRACe:IMAGe[:STATe]](GP-IB_Command_Finder/Sense/SA.md#Image_Reject_State) | [EnableImageRejectTraces](COM_Reference/Properties/ImageRejectTracesState_Property.md)  
ADC & LO Tab  
Sample Frequency | [SENSe:SA:ADC:SAMPle:RATE](GP-IB_Command_Finder/Sense/SA.md#ADCSampleRate) [SENSe:SA:ADC:SAMPle:RATE:AUTO](GP-IB_Command_Finder/Sense/SA.md#ADC_Sample_Rate_Auto) | [ADCSampleRate](COM_Reference/Properties/ADCSampleRate_Property.md) [EnableADCSampleRateAuto](COM_Reference/Properties/ADCSampleRateAuto_Property.md)  
Enable FIR for 25 MHz | [SENSe:SA:ADC:SAMPle:DECimation:FIR](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:ADC:SAMPle:DECimation:FIR) | [ADCEnableFIRFor25Mhz](COM_Reference/Properties/ADCEnableFIRFor25Mhz_Property.md)  
Dithering | [SENSe:SA:ADC:DITHer:[STATe]](GP-IB_Command_Finder/Sense/SA.md#ADC:DITHer) | [EnableADCDither](COM_Reference/Properties/ADC_Dithering_Property.md)  
Overrange warning percent | [SENSe:SA:ADC:OVERload:PERCent](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:ADC:OVERload:PERCent) [SENSe:SA:ADC:OVERload:COUNt?](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:ADC:OVERload:COUNt) [SENSe:SA:ADC:OVERload:LIST?](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:ADC:OVERload:LIST) | None  None  None  
Show ADC Ranges... | [SENSe:SA:ADC:RANGe:PERCent[:MAXimum]?](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:ADC:RANGe:PERCent:MAXimum) [SENSe:SA:ADC:RANGe:PERCent:MINimum?](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:ADC:RANGe:PERCent:MINimum) [SENSe:SA:ADC:RANGe:PERCent:RECeiver?](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:ADC:RANGe:PERCent:RECeiver) | None  None  None  
Force ADC record size | [SENSe:SA:ADC:RECord:SIZE:VALue?](GP-IB_Command_Finder/Sense/SA.md#FFT_ADC_Record_Size_Value) [SENSe:SA:ADC:RECord:SIZE:FORCe:VALue](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:ADC:RECord:SIZE:FORCe:VALue) [SENSe:SA:ADC:RECord:SIZE:FORCe[:STATe]](GP-IB_Command_Finder/Sense/SA.md#FFT_ADC_Record_Size) [SENSe:SA:ADC:RECord:SIZE:MAX?](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:ADC:RECord:SIZE:MAX) [SENSe:SA:ADC:RECord:SIZE:MIN?](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:ADC:RECord:SIZE:MIN) | [ADCRecordSize](COM_Reference/Properties/ADCRecordSize_Property.md) [ForceADCRecordSize](COM_Reference/Properties/ForceADCRecordSize_Property.md) [EnableForceADCRecordSize](COM_Reference/Properties/EnableForceADCRecordSize_Property.md) [ADCRecordSizeMax](COM_Reference/Properties/ADCRecordSizeMax_Property.md) [ADCRecordSizeMin](COM_Reference/Properties/ADCRecordSizeMin_Property.md)  
Stacking | [SENSe:SA:ADC:STACking:VALue](GP-IB_Command_Finder/Sense/SA.md#ADC_Stacking) [SENSe:SA:ADC:STACking:STATe](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:ADC:STACking:STATe) | [ADCStacking](COM_Reference/Properties/ADCStackingValue_Property.md) [ADCStackingState](COM_Reference/Properties/ADCStackingState.md) [ADCStackingMax](COM_Reference/Properties/ADCStackingMax_Property.md)  
Multiple Recording | [SENSe:SA:ADC:MREC[:STATe]](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:ADC:MREC:STATe) | [ADCMultRecState](COM_Reference/Properties/ADCMultRecState_Property.md)  
Chunk size | [SENSe:SA:ADC:MREC:SIZE](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:ADC:MREC:SIZE) | [ADCMultRecSize](COM_Reference/Properties/ADCMultRecSize_Property.md)  
Chunk period | [SENSe:SA:ADC:MREC:PERiod](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:ADC:MREC:PERiod) | [ADCMultRecPeriod](COM_Reference/Properties/ADCMultRecPeriod_Property.md)  
Randomize LO | [SENSe:SA:LO:RANDom[:STATe]](GP-IB_Command_Finder/Sense/SA.md#LoRandState) | [EnableRandomizedLO](COM_Reference/Properties/RandomizedLO_Property.md)  
Enable baseband X-axis mode (LO independent sweep) | [SENSe:SA:LO:BASeband[:STATe]](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:LO:BASeband:STATe) | None  
Force LO to frequency | [SENSe:SA:LO:FREQ:FORCe](GP-IB_Command_Finder/Sense/SA.md#FFTFreqMode) [SENSe:SA:LO:FREQ:VALue](GP-IB_Command_Finder/Sense/SA.md#FFT_FREQ_VALue) [SENSe:SA:LO:FORCe:OFFSet:DIVider](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:LO:FORCe:OFFSet:DIVider) [SENSe:SA:LO:FORCe:OFFSet:MULtiplier](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:LO:FORCe:OFFSet:MULtiplier) [SENSe:SA:LO:FORCe:OFFSet:SOURce](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:LO:FORCe:OFFSet:SOURce) | [EnableForce LOToFrequency](COM_Reference/Properties/EnableForceFFTToFrequency_Property.md) [ForceLOToFrequency](COM_Reference/Properties/ForceFFTToFrequency_Property.md) None None None  
Data Tab  
Data Format | [SENSe:SA:DATA:TYPE](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:DATA:TYPE) | [DataFormat](COM_Reference/Properties/DataFormat_Property.md)  
Export receivers | [SENSe:SA:DATA:RECeivers:LIST](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:DATA:RECeivers:LIST) [SENSe:SA:DATA:RECeivers?](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:DATA:RECeivers) | [ExportReceiverSetList](COM_Reference/Properties/ExportReceiverSetList_Property.md) [ExportReceiverList](COM_Reference/Properties/ExportReceiverList_Property.md)  
Don't save data below threshold | [SENSe:SA:DATA:THReshold[:STATe]](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:DATA:THReshold_:STATe) [SENSe:SA:DATA:THReshold:VALue](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:DATA:THReshold:VALue) | [DataLevelThresholdEnabled](COM_Reference/Properties/DataLevelTresholdEnabled_Property.md) [DataLevelThreshold](COM_Reference/Properties/DataLevelTreshold_Property.md)  
DFT bins count | [SENSe:SA:DATA:BINs:COUNt?](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:DATA:BINs:COUNt) | [DataBinCount](COM_Reference/Properties/DataBinCount_Property.md)  
Receivers count | [SENSe:SA:DATA:RECeivers:COUNt?](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:DATA:RECeivers:COUNt) | [ExportReceiverCount](COM_Reference/Properties/ExportReceiverCount_Property.md)  
Export to binary file | [SENSe:SA:DATA:FILE:BINary[:STATe]](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:DATA:FILE:BINary:STATe) | [BinaryFileEnabled](COM_Reference/Properties/BinaryFileEnabled_Property.md)  
Export to text file | [SENSe:SA:DATA:FILE:TEXT[:STATe]](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:DATA:FILE:TEXT:STATe) | [TextFileEnabled](COM_Reference/Properties/TextFileEnabled_Property.md)  
Verbose mode | [SENSe:SA:DATA:FILE:TEXT:VERBose[:STATe]](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:DATA:FILE:TEXT:VERBose:STATe) | [FileVerboseEnabled](COM_Reference/Properties/FileVerboseEnabled_Property.md)  
Erase files each new sweep | [SENSe:SA:DATA:FILE:ERASe[:STATe]](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:DATA:FILE:ERAse:STATe) | [FileEraseEachSweep](COM_Reference/Properties/FileEraseEachSweep_Property.md)  
File name prefix | [SENSe:SA:DATA:FILE:PREFix](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:DATA:FILE:PREFix) | [FilePrefix](COM_Reference/Properties/FilePrefix_Property.md)  
Record size (bytes) | [SENSe:SA:DATA:SIZE?](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:DATA:SIZE) [SENSe:SA:DATA:SIZE:BIN?](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:DATA:SIZE:BIN) [SENSe:SA:DATA:SIZE:LOW?](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:DATA:SIZE:LOW) [SENSe:SA:DATA:SIZE:HIGH?](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:DATA:SIZE:HIGH) | [DataByteSize](COM_Reference/Properties/DataByteSize_Property.md) [DataBytesPerBin](COM_Reference/Properties/DataBytesPerBin_Property.md) [DataByteSizeLOW](COM_Reference/Properties/DataByteSizeLSB_Property.md) [DataByteSizeHIGH](COM_Reference/Properties/DataByteSizeMSB_Property.md)  
Export markers with data files | [SENSe:SA:DATA:FILE:TEXT:MARKers[:STATe]](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:DATA:FILE:TEXT:MARKers:STATe) | [DataExportMarkersEnabled](COM_Reference/Properties/DataExportMarkersEnabled_Property.md)  
Export all markers to a single file | [None](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:DATA:FILE:TEXT:MARKers:ALL:STATe) | None  
Export to FIFO buffer | [SENSe:SA:DATA:FIFO[:STATe]](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:DATA:FIFO:STATe) | [FIFOEnabled](COM_Reference/Properties/FIFOEnabled_Property.md)  
Export to shared memory | [SENSe:SA:DATA:SHARed[:STATe]](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:DATA:SHARed:STATe) | [MemShareEnabled](COM_Reference/Properties/MemShareEnabled_Property.md)  
Share name | [SENSe:SA:DATA:SHARed:NAME](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:DATA:SHARed:NAMe) | [MemShareName](COM_Reference/Properties/MemShareName_Property.md)  
| [SENSe:SA:DATA:STARt?](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:DATA:STARt) | [DataFirstRFBin](COM_Reference/Properties/DataFirstRFBin_Property.md)  
Export to binary file | [SENSe:SA:DATA:IQ:FILE:BINary[:STATe]](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:DATA:IQ:FILE:BINary:STATe) | None  
Export to text file | [SENSe:SA:DATA:IQ:FILE:TEXT[:STATe]](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:DATA:IQ:FILE:TEXT:STATe) | None  
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

