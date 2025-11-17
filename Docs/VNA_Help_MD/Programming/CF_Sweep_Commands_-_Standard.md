# Sweep Commands - Standard Measurement Class

Click [here](CF_Sweep_Commands.md) to view links to Sweep commands for all
Measurement Classes.

Main |  Sweep Timing |  Source Control |  Segment Table  
---|---|---|---  
  
Main Tab Commands  
---  
Softkey | Sub-item | SCPI | COM  
Number of Points |  | [SENSe:SWEep:POINts](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssp) | [NumberOfPoints](COM_Reference/Properties/Number_of__Points_Property.md)  
Sweep Type | Linear Frequency | [SENSe:SWEep:TYPE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssty) | [SweepType](COM_Reference/Properties/Sweep_Type_Property.md)  
Log Frequency | [SENSe:SWEep:TYPE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssty) | [SweepType](COM_Reference/Properties/Sweep_Type_Property.md)  
Power Sweep | [SENSe:SWEep:TYPE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssty) | [SweepType](COM_Reference/Properties/Sweep_Type_Property.md)  
CW Time | [SENSe:SWEep:TYPE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssty) | [SweepType](COM_Reference/Properties/Sweep_Type_Property.md)  
Segment Sweep | [SENSe:SWEep:TYPE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssty) | [SweepType](COM_Reference/Properties/Sweep_Type_Property.md)  
Phase Sweep | [SENSe:SWEep:TYPE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssty) | [SweepType](COM_Reference/Properties/Sweep_Type_Property.md)  
Start |  | [SENSe:FREQuency:STARt](GP-IB_Command_Finder/Sense/Frequency.md#start) | [StartFrequency](COM_Reference/Properties/Start_Frequency_Property.md)  
Stop |  | [SENSe:FREQuency:STOP](GP-IB_Command_Finder/Sense/Frequency.md#stop) | [StopFrequency](COM_Reference/Properties/Stop_Frequency_Property.md)  
X-axis Type |  | [SENSe:FOM:DISPlay:SELect](GP-IB_Command_Finder/Sense/FOM.md#select) | [DisplayRange](COM_Reference/Properties/DisplayRange_Property.md)  
[Sweep Setup...](CF_Setup_Commands_-_Standard.md#Main_Commands) |  |  |   
Sweep Timing Tab Commands  
Softkey | Sub-item | SCPI | COM  
Sweep Time | Auto | [SENSe:SWEep:TIME:AUTO](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssta) | [chan.SweepTime](COM_Reference/Properties/Sweep_Time_Property.md)  
Manual | [SENSe:SWEep:TIME[:STOP]](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#sst) | [chan.SweepTime](COM_Reference/Properties/Sweep_Time_Property.md)  
Dwell Time |  | [SENSe:SWEep:DWELl](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssd) | [DwellTime](COM_Reference/Properties/Dwell_Time_Property.md)  
Sweep Delay |  | [SENSe:SWEep:DWELl:SDELay](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#SweepDelay) | [SweepDelay](COM_Reference/Properties/Sweep_Delay_Property.md)  
Sweep Mode | AUTO |  [SENSe:SWEep:GENeration](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssg) | [SweepGenerationMode](COM_Reference/Properties/Sweep_Generation_Mode_Property.md)  
STEPPED  |  [SENSe:SWEep:GENeration](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssg) | [SweepGenerationMode](COM_Reference/Properties/Sweep_Generation_Mode_Property.md)  
Sweep Sequence | STD | [SENSe:SWEep:GENeration:POINtsweep](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#GenPoint) | [PointSweepState](COM_Reference/Properties/PointSweepState_Property.md)  
POINT | [SENSe:SWEep:GENeration:POINtsweep](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#GenPoint) | [PointSweepState](COM_Reference/Properties/PointSweepState_Property.md)  
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
Annotation - Primary, Source, Receivers, Source2, Source3 | [SENSe:FOM:RANGe:NAME?](GP-IB_Command_Finder/Sense/FOM.md#NameQuery) | [Name](COM_Reference/Properties/Name_FOMRange_Property.md)  
X-Axis Point Spacing | [SENSe:FOM:RANGe:SEGMent:SWEep:POINts](GP-IB_Command_Finder/Sense/FOMSegm.md#Points) | [NumberOfPoints](COM_Reference/Properties/Number_of__Points_Property.md)  
Pulse Setup... |  Pulse Measurement  
Off |  [SENSe:SWEep:PULSe:MODE](GP-IB_Command_Finder/Sense/SweepPulse.md#mode) | [PulseMeasMode](COM_Reference/Properties/PulseMeasMode_Property.md)  
Standard Pulse |  [SENSe:SWEep:PULSe:MODE](GP-IB_Command_Finder/Sense/SweepPulse.md#mode) | [PulseMeasMode](COM_Reference/Properties/PulseMeasMode_Property.md)  
Pulse Profile |  [SENSe:SWEep:PULSe:MODE](GP-IB_Command_Finder/Sense/SweepPulse.md#mode) | [PulseMeasMode](COM_Reference/Properties/PulseMeasMode_Property.md)  
Pulse Timing  
Pulse Width |  [SENSe:SWEep:PULSe:PRIMary:WIDth](GP-IB_Command_Finder/Sense/SweepPulse.md#MasterWidth) | [PrimaryWidth](COM_Reference/Properties/MasterWidth_Property.md)  
Pulse Period |  [SENSe:SWEep:PULSe:PRIMary:PERiod](GP-IB_Command_Finder/Sense/SweepPulse.md#MasterPeriod) | [PrimaryPeriod](COM_Reference/Properties/MasterPeriod_Property.md)  
Pulse Frequency |  [SENSe:SWEep:PULSe:PRIMary:FREQuency](GP-IB_Command_Finder/Sense/SweepPulse.md#MasterFreq) | [PrimaryFrequency](COM_Reference/Properties/MasterFrequency_Property.md)  
Properties  
Autoselect Pulse Detection Method |  [SENSe:SWEep:PULSe:DETectmode[:AUTO]](GP-IB_Command_Finder/Sense/SweepPulse.md#detectmode) | [AutoDetection](COM_Reference/Properties/AutoDetection_Property.md)  
Narrowband |  [SENSe:SWEep:PULSe:WIDeband[:STATe]](GP-IB_Command_Finder/Sense/SweepPulse.md#wideband) | [WideBandDectionState](COM_Reference/Properties/WideBandDectionState_Property.md)  
Wideband |  [SENSe:SWEep:PULSe:WIDeband[:STATe]](GP-IB_Command_Finder/Sense/SweepPulse.md#wideband) | [WideBandDectionState](COM_Reference/Properties/WideBandDectionState_Property.md)  
SW Gating |  [SENSe:SWEep:PULSe:SWGate](GP-IB_Command_Finder/Sense/SweepPulse.md#swgate) | [SoftwareGateState](COM_Reference/Properties/SoftwareGateState_Property.md)  
Autoselect IF Path Gain and Loss |  [SENSe:SWEep:PULSe:IFGain[:AUTO]](GP-IB_Command_Finder/Sense/SweepPulse.md#IFGain) | None  
IF Path... |  [SENSe:PATH:CONFig:ELEMent[:STATe]](GP-IB_Command_Finder/Sense/Path.md#state) | [Element](COM_Reference/Properties/Element_Property.md)  
Optimize Pulse Frequency |  [SENSe:SWEep:PULSe:PRF[:AUTO]](GP-IB_Command_Finder/Sense/SweepPulse.md#prf) | [AutoOptimizePRF](COM_Reference/Properties/AutoOptimizePRF_Property.md)  
Autoselect Profile Sweep Time |  [SENSe:SWEep:PULSe:MODE](GP-IB_Command_Finder/Sense/SweepPulse.md#mode) | [PulseMeasMode](COM_Reference/Properties/PulseMeasMode_Property.md)  
IFBW |  [SENSe:SWEep:PULSe:CWTime[:AUTO]](GP-IB_Command_Finder/Sense/SweepPulse.md#CWSweepAuto) | [AutoIFBandWidth](COM_Reference/Properties/AutoIFBandWidth_Property.md)  
Sweep Time |  [SENSe:SWEep:TIME[:STOP]](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#sst) | [chan.SweepTime](COM_Reference/Properties/Sweep_Time_Property.md)  
Number of Points |  [SENSe:SWEep:POINts](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssp) | [NumberOfPoints](COM_Reference/Properties/Number_of__Points_Property.md)  
|  |   
Measurement Timing  
Width |  [SENSe:SWEep:PULSe:TIMing](GP-IB_Command_Finder/Sense/SweepPulse.md#timing) | [AutoPulseTiming](COM_Reference/Properties/AutoPulseTiming_Property.md)  
Delay |  [SENSe:SWEep:PULSe:TIMing](GP-IB_Command_Finder/Sense/SweepPulse.md#timing) | [AutoPulseTiming](COM_Reference/Properties/AutoPulseTiming_Property.md)  
Pulse Gen |  [SENSe:SWEep:PULSe:MODE](GP-IB_Command_Finder/Sense/SweepPulse.md#mode) | [PulseMeasMode](COM_Reference/Properties/PulseMeasMode_Property.md)  
Master Pulse Trigger |  [SENSe:PATH:CONFig:ELEMent[:STATe]](GP-IB_Command_Finder/Sense/Path.md#state) | [Element](COM_Reference/Properties/Element_Property.md)  
Primary Clock |  [SENSe:SWEep:PULSe:PRIMary:CLOCk](GP-IB_Command_Finder/Sense/SweepPulse.md#SENSe:SWEep:PULSe:PRIMary:CLOCk) |  None  
Autoselect Width & Delay |  [SENSe:SWEep:PULSe:TIMing](GP-IB_Command_Finder/Sense/SweepPulse.md#timing) | [AutoPulseTiming](COM_Reference/Properties/AutoPulseTiming_Property.md)  
Autoselect Pulse Generators |  [SENSe:SWEep:PULSe:DRIVe[:AUTO]](GP-IB_Command_Finder/Sense/SweepPulse.md#drive) | [AutoSelectPulseGen](COM_Reference/Properties/AutoSelectPulseGen_Property.md)  
Pulse Generators...  
Width |  [SENSe:PULSe:WIDTh](GP-IB_Command_Finder/Sense/Pulse.md#width) | [Width](COM_Reference/Properties/Width_Property.md)  
Delay |  [SENSe:PULSe:DELay](GP-IB_Command_Finder/Sense/Pulse.md#delay) | [Delay](COM_Reference/Properties/Delay_pulse_Property.md)  
Invert |  [SENSe:PULSe:INVert](GP-IB_Command_Finder/Sense/Pulse.md#invert) | [Invert](COM_Reference/Properties/Invert_Property.md)  
Enable |  [SENSe:PULSe[:STATe]](GP-IB_Command_Finder/Sense/Pulse.md#state) | [State](COM_Reference/Properties/State_pulse_Property.md)  
Trigger |  [SENSe:PATH:CONFig:ELEMent[:STATe]](GP-IB_Command_Finder/Sense/Path.md#state) | [Element](COM_Reference/Properties/Element_Property.md)  
Frequency |  [SENSe:SWEep:PULSe:MASTer:FREQuency](GP-IB_Command_Finder/Sense/SweepPulse.md#MasterFreq) | [MasterFrequency](COM_Reference/Properties/MasterFrequency_Property.md)  
Period |  [SENSe:SWEep:PULSe:MASTer:PERiod](GP-IB_Command_Finder/Sense/SweepPulse.md#MasterPeriod) | [MasterPeriod](COM_Reference/Properties/MasterPeriod_Property.md)  
Enable Source x Modulator |  [SENSe:PATH:CONFig:ELEMent[:STATe]](GP-IB_Command_Finder/Sense/Path.md#state) | [Element](COM_Reference/Properties/Element_Property.md)  
Modulator Drive |  [SENSe:PATH:CONFig:ELEMent[:STATe]](GP-IB_Command_Finder/Sense/Path.md#state) | [Element](COM_Reference/Properties/Element_Property.md)  
Offset Pulse using Modulator and ADC Delays |  [SENSe:PULSe:HWDelay[:STATe]](GP-IB_Command_Finder/Sense/Pulse.md#SENSe:PULSe:HWDelay:STATe) |  [EnableOffsetDelays](COM_Reference/Properties/EnableOffsetDelays_Property.md)  
Modulator Delay |  [SENSe:PULSe:HWDelay:MODulator](GP-IB_Command_Finder/Sense/Pulse.md#SENSe:PULSe:HWDelay:MODulator) |  [ModulatorDelay](COM_Reference/Properties/ModulatorDelay_Property.md)  
Fixed ADC Delay |  [SENSe:PULSe:HWDelay:ADC?](GP-IB_Command_Finder/Sense/Pulse.md#SENSe:PULSe:HWDelay:ADC) |  [FixedADCDelay](COM_Reference/Properties/FixedADCDelay_Property.md)  
Synchronize ADCs using pulse trigger |  [SENSe:PATH:CONFig:ELEMent[:STATe]](GP-IB_Command_Finder/Sense/Path.md#state) | [Element](COM_Reference/Properties/Element_Property.md)  
Pulse4 Output Indicates |  [SENSe:PULSe4:OPTion](GP-IB_Command_Finder/Sense/Pulse.md#SENSe:PULSe4:OPTion) | [Pulse4OutAsADCActivity](COM_Reference/Properties/Pulse4OutAsADCActivity_Property.md)  
All ADC Activity |  [SENSe:PULSe4:OPTion:MODE ALL](GP-IB_Command_Finder/Sense/Pulse.md#SENSe:PULSe4:OPTion:MODE) |  None  
Trace ADC Activity |  [SENSe:PULSe4:OPTion:MODE TRACe](GP-IB_Command_Finder/Sense/Pulse.md#SENSe:PULSe4:OPTion:MODE) |  None  
Pulse Trigger... |  |   
Trigger Source |  [SENSe:PATH:CONFig:ELEMent[:STATe]](GP-IB_Command_Finder/Sense/Path.md#state) | [Element](COM_Reference/Properties/Element_Property.md)  
Trigger Level/Edge |  [SENSe:PULSe:TTYPe](GP-IB_Command_Finder/Sense/Pulse.md#TType) | [TriggerInType](COM_Reference/Properties/TriggerInType_Property.md)  
Synchronize ADCs using pulse trigger |  [SENSe:PULSe[:STATe]](GP-IB_Command_Finder/Sense/Pulse.md#state) | [State](COM_Reference/Properties/State_pulse_Property.md)  
[Trigger...](CF_Trigger_Commands.md) |  |   
Balanced Source... | Topology  
BAL | [CALCulate:FSIMulator:BALun:TOPology:BALanced](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#topBAL1) |   
BAL-BAL | [CALCulate:FSIMulator:BALun:TOPology:BBALanced](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#topBBAL) | [SetBBPorts](COM_Reference/Methods/SetBBPorts_Method.md)  
BAL-SE | [CALCulate:FSIMulator:BALun:TOPology:BALSended](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#topBALS) | [SetBSPorts](COM_Reference/Methods/SetBSPorts_Method.md)  
SE-BAL | [CALCulate:FSIMulator:BALun:TOPology:SBALanced](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#topSBAL) | [SetSBPorts](COM_Reference/Methods/SetSBPorts_Method.md)  
SE-SE-BAL | [CALCulate:FSIMulator:BALun:TOPology:SSBalanced](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#topSSB) | [SetSSBPorts](COM_Reference/Methods/SetSSBPorts_Method.md)  
Stimulus  
Single Ended | [CALCulate:FSIMulator:BALun:STIMulus:MODE](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#StimMode) | [Mode](COM_Reference/Properties/Mode_Property.md)  
True Mode | [CALCulate:FSIMulator:BALun:STIMulus:MODE](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#StimMode) | [Mode](COM_Reference/Properties/Mode_Property.md)  
Forward True Mode | [CALCulate:FSIMulator:BALun:STIMulus:MODE](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#StimMode) | [Mode](COM_Reference/Properties/Mode_Property.md)  
Reverse True Mode | [CALCulate:FSIMulator:BALun:STIMulus:MODE](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#StimMode) | [Mode](COM_Reference/Properties/Mode_Property.md)  
Source Only Mode | [CALCulate:FSIMulator:BALun:STIMulus:MODE](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#StimMode) | [Mode](COM_Reference/Properties/Mode_Property.md)  
Balanced Port Offset  
Phase Offset | [CALCulate:FSIMulator:BALun:BPORt:OFFSet:PHASe](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#BPortOffsetPhase) | [BalPort1PhaseOffset](COM_Reference/Properties/BalPort1PhaseOffset_Property.md) [BalPort2PhaseOffset](COM_Reference/Properties/BalPort2PhaseOffset_Property.md)  
Offset as fixture | [CALCulate:FSIMulator:BALun:FIXTure:OFFSet:PHASe](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#trueOffsetPhase) | [PhaseAsFixture](COM_Reference/Properties/PhaseAsFixture_Property.md)  
Power Offset | [CALCulate:FSIMulator:BALun:BPORt:OFFSet:POWer](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#BPortOffsPower) | BalPort1PowerOffset [BalPort2PowerOffset](COM_Reference/Properties/BalPort2PowerOffset_Property.md)  
Offset as fixture | [CALCulate:FSIMulator:BALun:FIXTure:OFFSet:POWer](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#trueOffsetPower) | [PowerAsFixture](COM_Reference/Properties/PowerAsFixture_Property.md)  
Phase Sweep (CW Time Only)  
Enable Phase Sweep | [CALCulate:FSIMulator:BALun:PHASe:SWEep:STATe](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#phaseSweepState) | [PhaseSwpState](COM_Reference/Properties/PhaseSwpState_Property.md)  
Sweep Phase On | None | None  
Start Phase | [CALCulate:FSIMulator:BALun:BPORt:SWEep:PHAse:STARt](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#bPortPhaseStart) | [BalPort1StartPhase](COM_Reference/Properties/BalPort1StartPhase_Property.md) [BalPort2StartPhase](COM_Reference/Properties/BalPort2StartPhase_Property.md)  
Stop Phase | [CALCulate:FSIMulator:BALun:BPORt:SWEep:PHAse:STOP](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#bPortPhaseStop) | [BalPort1StopPhase](COM_Reference/Properties/BalPort1StopPhase_Property.md) [BalPort2StopPhase](COM_Reference/Properties/BalPort2StopPhase_Property.md)  
Offset as fixture | [CALCulate:FSIMulator:BALun:FIXTure:PHASe](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md#FixtSweepPhase) | [PhaseSwpAsFixture](COM_Reference/Properties/PhaseSwpAsFixture_Property.md)  
Phase Control... | Phase Control Dialog |  |   
Sweep Type | [SENSe:SWEep:TYPE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssty) | [SweepType](COM_Reference/Properties/Sweep_Type_Property.md)  
Phase | [SOURce:PHASe[:FIXed]](GP-IB_Command_Finder/SourcePhase.md#fixed) | [FixedPhase](COM_Reference/Properties/FixedPhase_Property.md)  
Start Phase | [SOURce:PHAse:STARt](GP-IB_Command_Finder/SourcePhase.md#start) | [StartPhase](COM_Reference/Properties/StartPhase_Property.md)  
Stop Phase | [SOURce:PHAse:STOP](GP-IB_Command_Finder/SourcePhase.md#stop) | [StopPhase](COM_Reference/Properties/StopPhase_Property.md)  
Phase Control | [SOURce:PHASe:MODE:CATalog?](GP-IB_Command_Finder/SourcePhase.md#SOURce:PHASe:MODE:CATalog) [SOURce:PHAse:MODE[:VALue]](GP-IB_Command_Finder/SourcePhase.md#SOURce:PHASe:MODE:VALue) | None [PhaseControlMode](COM_Reference/Properties/PhaseControlMode_Property.md)  
Reference Port | [SOURce:PHASe:REFerence:CATalog?](GP-IB_Command_Finder/SourcePhase.md#SOURce:PHASe:REFerence:CATalog) [SOURce:PHASe:REFerence:PORT](GP-IB_Command_Finder/SourcePhase.md#SOURce:PHASe:REFerence:PORT) | None [PhaseReferencePort](COM_Reference/Properties/PhaseReferencePort_Property.md)  
Ext. Source Port | [SOURce:PHASe:EXTernal:CATalog?](GP-IB_Command_Finder/SourcePhase.md#SOURce:PHASe:EXTernal:CATalog) [SOURce:PHASe:EXTernal:PORT](GP-IB_Command_Finder/SourcePhase.md#SOURce:PHASe:EXTernal:PORT) | None None  
Control Parameter | [SOURce:PHAse:PARameter:CATalog?](GP-IB_Command_Finder/SourcePhase.md#SOURce:PHASe:PARameter:CATalog) [SOURce:PHAse:PARameter[:VALue]](GP-IB_Command_Finder/SourcePhase.md#SOURce:PHASe:PARameter:VALue) | None [PhaseParameter](COM_Reference/Properties/PhaseParameter_Property.md)  
Phase Leveling Tolerance | [SOURce:PHASe:CONTrol:TOLerance](GP-IB_Command_Finder/SourcePhase.md#tolerance) | [PhaseTolerance](COM_Reference/Properties/PhaseTolerance_Property.md)  
Leveling Max Iterations | [SOURce:PHASe:CONTrol:ITERation](GP-IB_Command_Finder/SourcePhase.md#iteration) | [PhaseIterationNumber](COM_Reference/Properties/PhaseIterationNumber_Property.md)  
Power Leveling Tolerance | [SOURce:POWer:ALC[:MODE]:RECeiver:TOLerance](GP-IB_Command_Finder/SourceRxLeveling.md#recToler) | [Tolerance](COM_Reference/Properties/Tolerance_Property.md)  
Leveling IFBW | [SOURce:POWer:ALC[:MODE]:RECeiver:IFBW](GP-IB_Command_Finder/SourceRxLeveling.md#recIFBW) | [LevelingIFBW](COM_Reference/Properties/LevelingIFBW_Property.md)  
Power Ratio | [SOURce:PHASe:POFFset:FIXed](GP-IB_Command_Finder/SourcePhase.md#poffsetFixed) | [FixedRatioedPower](COM_Reference/Properties/FixedRatioedPower_Property.md)  
Start Power | [SOURce:POWer:PORT:STARt](GP-IB_Command_Finder/source.md#PortStart) | [StartPower](COM_Reference/Properties/Start_Power_Property.md)  
Stop Power | [SOURce:POWer:PORT:STOP](GP-IB_Command_Finder/source.md#PortStop) | [StopPower](COM_Reference/Properties/Stop_Power_Property.md)  
[Receiver Leveling...](CF_Power_Commands_-_Standard.md#Receiver_Leveling) |  |   
Phase Control Setup Dialog |  |   
Setup... |  |   
Referenced to | [SOURce:PHASe:PARameter:PORT](GP-IB_Command_Finder/SourcePhase.md#paramPort) | [PhaseReferencePort](COM_Reference/Properties/PhaseReferencePort_Property.md)  
Control Parameter | [SOURce:PHAse:PARameter](GP-IB_Command_Finder/SourcePhase.md#parameter) | [PhaseParameter](COM_Reference/Properties/PhaseParameter_Property.md)  
Background Sweep Properties |  |   
Apply Settings to All Ports | [SOURce:PHAse:PARameter:MODE](GP-IB_Command_Finder/SourcePhase.md#parameterMode) | [PhaseControlMode](COM_Reference/Properties/PhaseControlMode_Property.md)  
Use Leveling IFBW | [SOURce:POWer:ALC[:MODE]:RECeiver:IFBW](GP-IB_Command_Finder/SourceRxLeveling.md#recIFBW) | [LevelingIFBW](COM_Reference/Properties/LevelingIFBW_Property.md)  
Tolerance | [SOURce:PHASe:CONTrol:TOLerance](GP-IB_Command_Finder/SourcePhase.md#tolerance) | [PhaseTolerance](COM_Reference/Properties/PhaseTolerance_Property.md)  
Max Iterations | [SOURce:PHASe:CONTrol:ITERation](GP-IB_Command_Finder/SourcePhase.md#iteration) | [PhaseIterationNumber](COM_Reference/Properties/PhaseIterationNumber_Property.md)  
DC Source... |  Enable DC Outputs |  [SOURce:DC:ENABle](GP-IB_Command_Finder/SourceDC.md#Enable) | [EnableAllOutput](COM_Reference/Properties/EnableAllOutput_Property.md)  
State |  [SOURce:DC:STATe](GP-IB_Command_Finder/SourceDC.md#state) | [State](COM_Reference/Properties/State_DC_Property.md)  
Start DC |  [SOURce:DC:STARt](GP-IB_Command_Finder/SourceDC.md#start) |  [Start](COM_Reference/Properties/Start_DC_Property.md)  
Stop DC |  [SOURce:DC:STOP](GP-IB_Command_Finder/SourceDC.md#stop) |  [Stop](COM_Reference/Properties/Stop_DC_Property.md)  
Limits...  
State |  [SOURce:DC:STATe](GP-IB_Command_Finder/SourceDC.md#state) |  [State](COM_Reference/Properties/State_DC_Property.md)  
Min |  [SOURce:DC:LIMIt:MINimum](GP-IB_Command_Finder/SourceDC.md#SOURce:DC:LIMit:MINimum) |  [LimitMin](COM_Reference/Properties/LimitMin_Property.md)  
Max |  [SOURce:DC:LIMIt:MAXimum](GP-IB_Command_Finder/SourceDC.md#SOURce:DC:LIMit:MAXimum) |  [LimitMax](COM_Reference/Properties/LimitMax_Property.md)  
Shift LO |  |  [SENSe:SWEep:SLOCal:STATe](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#SlocalState) [SENSe:SWEep:SLOCal:MAXimum](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#SlocalMax) |   
LF Extension |  On/Off |  [SENSe:SWEep:LFEXtension:STATe](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#SENSe:SWEep:LFEXtension:STATe) [SYSTem:CAPability:HARDware:LFEXtension:EXISts?](GP-IB_Command_Finder/SystCapability.md#SYSTem:CAPability:HARDware:LFEXtensions:EXISts) |  [LowFrequencyExtension](COM_Reference/Properties/LowFrequencyExtension_Property.md) [HasLowFrequencyExtension](COM_Reference/Properties/HasLowFrequencyExtension_Property.md)  
Global Source |  Power On (All Channels) |  None |  None  
Global Sources Ignore "Power ON" Setting |  [SYSTem:PREFerences:SOURce:GLOBal:POFF:IGNore[:STATe]](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:SOURce:GLOBal:POFF:IGNore:STATe) |  None  
Global |  [SYSTem:PREFerences:SOURce:GLOBal[:STATe]](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:SOURce:GLOBal:STATe) |  None  
State |  [SYSTem:PREFerences:SOURce:GLOBal:OUTPut[:STATe]](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:SOURce:GLOBal:OUTPut:STATe) |  None  
Frequency |  [SYSTem:PREFerences:SOURce:GLOBal:FREQuency](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:SOURce:GLOBal:FREQuency) |  None  
Power |  [SYSTem:PREFerences:SOURce:GLOBal:POWer](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:SOURce:GLOBal:POWer) |  None  
Modulation |  [SYSTem:PREFerences:SOURce:GLOBal:MODulation:LOAD](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:SOURce:GLOBal:MODulation:LOAD) [SYSTem:PREFerences:SOURce:GLOBal:MODulation:NAME?](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:SOURce:GLOBal:MODulation:NAME) [SYSTem:PREFerences:SOURce:GLOBal:MODulation[:STATe]](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:SOURce:GLOBal:MODulation:STATe) |  None None None  
Segment Table Tab Commands  
Softkey | Sub-item | SCPI | COM  
Add Segment |  | [SENSe:SEGMent:ADD](GP-IB_Command_Finder/Sense/Segment.md#add) | [Add](COM_Reference/Methods/Add_segments_Method.md)  
Insert Segment |  | None | None  
Delete Segment |  | [SENSe:SEGMent:DELete](GP-IB_Command_Finder/Sense/Segment.md#del) | [Remove](COM_Reference/Methods/Remove_Method.md)  
Delete All Segments |  | [SENSe:SEGMent:DELete:ALL](GP-IB_Command_Finder/Sense/Segment.md#delall) | None  
Segment Table... | X-Axis Point Spacing | [SENSe:SEGMent:X:SPACing](GP-IB_Command_Finder/Sense/Segment.md#X AXIS) | [XAxisPointSpacing](COM_Reference/Properties/XAxisPointSpacing_Property.md)  
Allow Arbitrary Segments | [SENSe:SEGMent:ARBitrary](GP-IB_Command_Finder/Sense/Segment.md#arb) | [AllowArbitrarySegments](COM_Reference/Properties/AllowArbitrarySegments_Property.md)  
Display Center/Span Freq | [SENSe:SEGMent:FREQuency:CENTer](GP-IB_Command_Finder/Sense/Segment.md#cent) [SENSe:SEGMent:FREQuency:SPAN](GP-IB_Command_Finder/Sense/Segment.md#span) | [CenterFrequency](COM_Reference/Properties/CenterFreq_Property.md) [FrequencySpan](COM_Reference/Properties/Frequency_Span_Property.md)  
Save Table | None | [ExportCSVfile](COM_Reference/Methods/ExportCSVfile_Method.md)  
Load Table | None | [ImportCSVfile](COM_Reference/Methods/ImportCSVfile_Method.md)  
Independent Settings Per Segment |  |   
Power Level | [SENSe:SEGMent:POWer[:LEVel]](GP-IB_Command_Finder/Sense/Segment.md#pwrval) | [TestPortPower](COM_Reference/Properties/Test_Port_Power_Property.md)  
IF Bandwidth | [SENSe:SEGMent:BWIDth[:RESolution]](GP-IB_Command_Finder/Sense/Segment.md#bdwval) | [IFBandwidth](COM_Reference/Properties/IF_Bandwidth_Property.md)  
IF Bandwidth Per Port | [SENSe:SEGMent:BWIDth|BANDwidth:PORT[:RESolution]:CONTrol](GP-IB_Command_Finder/Sense/Segment.md#BwidthPortCtrl) | [PortIFBandwidthOption](COM_Reference/Properties/PortIFBandwidthOption_Property.md) [PortIFBandwidth](COM_Reference/Properties/PortIFBandwidth_Property.md)  
Sweep Time | [SENSe:SEGMent:SWEep:TIME](GP-IB_Command_Finder/Sense/Segment.md#time) | [SweepTimeOption](COM_Reference/Properties/SweepTimeOption_Property.md) [SweepTime](COM_Reference/Properties/Sweep_Time_Property.md)  
Dwell Time | [SENSe:SWEep:DWELl](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssd) | [DwellTime](COM_Reference/Properties/Dwell_Time_Property.md)  
Delay | [SENSe:SEGMent:SWEep:DELay](GP-IB_Command_Finder/Sense/Segment.md#Delay) | [DelayOption](COM_Reference/Properties/DelayOption_Property.md) [Delay](COM_Reference/Properties/Delay_\(Segment_Sweep\)_Property.md)  
Sweep Mode | [SENSe:SEGMent:SWEep:GENeration:CONTrol](GP-IB_Command_Finder/Sense/Segment.md#GenControl) | [SweepModeOption](COM_Reference/Properties/SweepModeOption_Property.md) [SweepMode](COM_Reference/Properties/SweepMode_Property.md)  
Shift LO | [SENSe:SEGMent:SHLO](GP-IB_Command_Finder/Sense/Segment.md#Shlo) [SENSe:SEGMent:SHLO:CONTrol](GP-IB_Command_Finder/Sense/Segment.md#ShloControl) | [ShiftLO](COM_Reference/Properties/ShiftLO.md) [ShiftLOOption](COM_Reference/Properties/ShiftLOOption_Property.md)  
Receiver Atten Per Port | [SENSe:SEGMent:POWer:ATTenuation:RECeiver:REFerence](GP-IB_Command_Finder/Sense/Segment.md#SEGMattRECref) [SENSe:SEGMent:POWer:ATTenuation:RECeiver:CONTrol](GP-IB_Command_Finder/Sense/Segment.md#ATTrecCONT) | None None  
Handler Port A |  [SENSe:SEGMent:HANDler:A:CONTrol](GP-IB_Command_Finder/Sense/Segment.md#handler_A_control_state) [SENSe:SEGMent:HANDler:A](GP-IB_Command_Finder/Sense/Segment.md#handler_A_control_value) |  None  
Show Table | Auto | None | None  
On | [DISPlay:WINDow:TABLe](GP-IB_Command_Finder/Display.md#tabl) | [ShowTable](COM_Reference/Methods/Show_Table_Method.md)

