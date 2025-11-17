# Setup Commands - Modulation Distortion and Modulation Distortion Converters
Measurement Class

Only the Main Setup commands corresponding to the Modulation Distortion and
Modulation Distortion Converters measurement class are documented here. All
other commands are identical to the Setup commands for the Standard
measurement class and can be accessed by clicking [here](CF_Setup_Commands_-
_Standard.htm) or by clicking on the softtabs on the graphic below.

Click [here](CF_Setup_Commands.md) to view links to Setup commands for all
Measurement Classes.

Main |  [Layout](CF_Setup_Commands_-_Standard.md#Customize_Meas_Commands) |  [System  
Setup](CF_System_Commands.htm#System_Setup_Tab_Commands) |  [Internal  
Hardware](CF_Setup_Commands_-_Standard.htm#Internal_Hardware_Commands) |  [External  
Hardware](CF_Setup_Commands_-_Standard.htm#External_Hardware_Commands)  
---|---|---|---|---  
  
Main Tab Commands  
---  
Softkey | Sub-item |  SCPI |  COM  
MOD/MODX Setup... | Sweep Tab  
Sweep Type |  [SENSe:DISTortion:SWEep:TYPE](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:TYPE) |  None  
Carrier Frequency |  [SENSe:DISTortion:SWEep:CARRier:FREQuency](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:SA:COHerence:DISTortion:SWEep:CARRier:FREQuency) |  None  
SA Center |  [SENSe:FREQuency:CENTer](GP-IB_Command_Finder/Sense/Frequency.md#cent) |  [chan.CenterFrequency](COM_Reference/Properties/CenterFreq_Property.md)  
SA Start |  [SENSe:FREQuency:STARt](GP-IB_Command_Finder/Sense/Frequency.md#start) |  [chan.StartFrequency](COM_Reference/Properties/Start_Frequency_Property.md)  
SA Span |  [SENSe:FREQuency:SPAN](GP-IB_Command_Finder/Sense/Frequency.md#span) [SENSe:FREQuency:SPAN:FULL](GP-IB_Command_Finder/Sense/Frequency.md#SpanFull) |  [chan.FrequencySpan](COM_Reference/Properties/Frequency_Span_Property.md) [FrequencySpanFull](COM_Reference/Methods/FrequencySpanFull_Method.md)  
SA Stop |  [SENSe:FREQuency:STOP](GP-IB_Command_Finder/Sense/Frequency.md#stop) |  [chan.StopFrequency](COM_Reference/Properties/Stop_Frequency_Property.md)  
Noise BW | [SENSe:SA:BANDwidth:NOISe](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:SA:BANDwidth:NOISe) [SENSe:SA:BANDwidth:NOISe:AUTO](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:SA:BANDwidth:NOISe:AUTO) | None None  
Set Power At | [SENSe:DISTortion:SWEep:POWer:CARRier:LEVel](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:POWer:CARRier:LEVel) [SENSe:DISTortion:SWEep:POWer:CARRier:LEVel:PORT](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:POWer:CARRier:LEVel:PORT) | None None  
S-Param Power At DUT In/Out | [SENSe:DISTortion:SWEep:POWer:SPARam:LEVel](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:POWer:SPARam:LEVel) [SENSe:DISTortion:SWEep:POWer:CARRier:LEVel:PORT](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:POWer:CARRier:LEVel:PORT) | None None  
Power Sweep...  
Power Sweep Type |  [ENSe:DISTortion:SWEep:POWer:CARRier:LEVel:TYPE](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:POWer:CARRier:LEVel:TYPE) |  None  
Ramp Power Sweep Type |  |   
Start Power At |  [SENSe:DISTortion:SWEep:POWer:CARRier:RAMP:LEVel:STARt](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:POWer:CARRier:RAMP:LEVel:STARt) |  None  
Stop Power At |  [SENSe:DISTortion:SWEep:POWer:CARRier:RAMP:LEVel:STOP](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:POWer:CARRier:RAMP:LEVel:STOP) |  None  
Number of Powers |  [SENSe:DISTortion:SWEep:POWer:CARRier:RAMP:POINts](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:POWer:CARRier:RAMP:POINts) |  None  
Noise BW |  [SENSe:DISTortion:SWEep:POWer:CARRier:LIST:NBW](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:POWer:CARRier:LIST:NBW) |  None  
Auto-Increase NBW at High Powers |  [SENSe:DISTortion:SWEep:POWer:CARRier:RAMP:NBW:AUTO](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:POWer:CARRier:RAMP:NBW:AUTO) |  None  
List Power Sweep Type |  |   
Power |  [SENSe:DISTortion:SWEep:POWer:CARRier:LIST:LEVel](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:POWer:CARRier:LIST:LEVel) |  None  
Src Atten Fixed Atten Custom |  [SENSe:DISTortion:SWEep:POWer:CARRier:LIST:SOURce:ATTenuation](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:POWer:CARRier:LIST:SOURce:ATTenuation) [SENSe:DISTortion:SWEep:POWer:CARRier:LIST:SOURce:ATTenuation:MODE](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:POWer:CARRier:LIST:RECeiver:ATTenuation:MODE) [SENSe:DISTortion:SWEep:POWer:CARRier:LIST:SOURce:ATTenuation:MODE](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:POWer:CARRier:LIST:RECeiver:ATTenuation:MODE) |  None None None  
Rcvr Atten Fixed Atten Custom |  [SENSe:DISTortion:SWEep:POWer:CARRier:LIST:RECeiver:ATTenuation](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:POWer:CARRier:LIST:RECeiver:ATTenuation) [SENSe:DISTortion:SWEep:POWer:CARRier:LIST:RECeiver:ATTenuation:MODE](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:POWer:CARRier:LIST:RECeiver:ATTenuation:MODE) [SENSe:DISTortion:SWEep:POWer:CARRier:LIST:RECeiver:ATTenuation:MODE](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:POWer:CARRier:LIST:RECeiver:ATTenuation:MODE) |  None None None  
Noise BW Fixed NBW Custom Auto-Increase |  [SENSe:DISTortion:SWEep:POWer:CARRier:LIST:NBW](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:POWer:CARRier:LIST:NBW) [SENSe:DISTortion:SWEep:POWer:CARRier:LIST:NBW:MODE](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:POWer:CARRier:LIST:NBW:MODE) [SENSe:DISTortion:SWEep:POWer:CARRier:LIST:NBW:MODE](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:POWer:CARRier:LIST:NBW:MODE) [SENSe:DISTortion:SWEep:POWer:CARRier:LIST:NBW:MODE](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:POWer:CARRier:LIST:NBW:MODE) |  None None None None  
Add Row |  [SENSe:DISTortion:SWEep:POWer:CARRier:LIST:ADD](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:POWer:CARRier:LIST:ADD) |  None  
Delete Row |  [SENSe:DISTortion:SWEep:POWer:CARRier:LIST:DELete](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:POWer:CARRier:LIST:DELete) |  None  
Load... |  [SENSe:DISTortion:SWEep:POWer:CARRier:LIST:LOAD](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:POWer:CARRier:LIST:LOAD) |  None  
Save... |  [SENSe:DISTortion:SWEep:POWer:CARRier:LIST:SAVE](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:POWer:CARRier:LIST:SAVE) |  None  
DC Sources...  
Enable DC Outputs |  [SOURce:DC:ENABle](GP-IB_Command_Finder/SourceDC.md#Enable) |  [EnableAllOutput](COM_Reference/Properties/EnableAllOutput_Property.md)  
State ON|OFF|PerPort |  [SOURce:DC:STATe](GP-IB_Command_Finder/SourceDC.md#state) |  [State](COM_Reference/Properties/State_DC_Property.md)  
Start DC |  [SOURce:DC:Start](GP-IB_Command_Finder/SourceDC.md#start) |  [Start](COM_Reference/Properties/Start_DC_Property.md)  
Stop DC |  [SOURce:DC:Stop](GP-IB_Command_Finder/SourceDC.md#stop) |  [Stop](COM_Reference/Properties/Stop_DC_Property.md)  
Limits... |  |   
State |  [SOURce:DC:STATe](GP-IB_Command_Finder/SourceDC.md#state) |  [State](COM_Reference/Properties/State_DC_Property.md)  
Min |  [SOURce:DC:LIMit:MINimum](GP-IB_Command_Finder/SourceDC.md#SOURce:DC:LIMit:MINimum) |  [LimitMin](COM_Reference/Properties/LimitMin_Property.md)  
Max |  [SOURce:DC:LIMit:MAXimum](GP-IB_Command_Finder/SourceDC.md#SOURce:DC:LIMit:MAXimum) |  [LimitMax](COM_Reference/Properties/LimitMax_Property.md)  
Sweep Details...  
Force RF Power OFF at the End of Sweep - System Preference |  [SENSe:DISTortion:SWEep:RETRace:POWer](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:SA:COHerence:DISTortion:SWEep:RETRace:POWer) |  None  
|  Delay Before Start of Sweep |  [SENSe:SWEep:DWELl:SDELay](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#SweepDelay) |  [SweepDelay](COM_Reference/Properties/Sweep_Delay_Property.md)  
Delay Before Distortion Measurement |  [SENSe:DISTortion:SWEep:DWELl](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:DWELl) |  None  
|  Enable S-Param Sweep |  [SENSe:DISTortion:SWEep:SPARam[:STATe]](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:SPARam:STATe) |  None  
S-Param Source |  [SENSe:DISTortion:SWEep:SPARam:TYPE](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:SPARam:TYPE) |  None  
S-Param Freq Step |  [SENSe:DISTortion:SWEep:SPARam:STEP](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:SPARam:STEP) |  None  
S-Param IFBW |  [SENSe:DISTortion:SWEep:SPARam:BWIDth](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:SPARam:BWIDth) |  None  
Re-use Previous S-Parameter Measurements |  [SENSe:DISTortion:SWEep:SPARam:REUSe](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:SPARam:REUSe) |  None  
RF Path Tab  
| VNA Source Attenuator Include | [SOURce:POWer:ATTenuation](GP-IB_Command_Finder/source.md#attval) [SENSe:DISTortion:PATH:SOURce:ATTenuation:INCLude](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:PATH:SOURce:ATTenuation:INCLude) | [chan.Attenuator](COM_Reference/Properties/Attenuator_Property.md) None  
Nominal Source Amp | [SENSe:DISTortion:PATH:SOURce:NOMinal:AMPLifier](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:SA:COHerence:DISTortion:PATH:SOURce:NOMinal:AMPLifier) | None  
DUT Input | [SENSe:DISTortion:PATH:DUT:INPut](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:SA:COHerence:DISTortion:PATH:DUT:INPut) | None  
Nominal DUT Gain | [SENSe:DISTortion:PATH:DUT:NOMinal:GAIN](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:SA:COHerence:DISTortion:PATH:DUT:NOMinal:GAIN) | None  
DUT Output | [SENSe:DISTortion:PATH:DUT:OUTPut](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:SA:COHerence:DISTortion:PATH:DUT:OUTPut) | None  
Nominal DUT NF |  [SENSe:DISTortion:PATH:DUT:NOMinal:NF](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:SA:COHerence:DISTortion:PATH:DUT:NOMinal:NF) |  None  
Nominal DUT NF Include | [SENSe:DISTortion:PATH:DUT:NOMinal:NF:INCLude](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:PATH:DUT:NOMinal:NF:INCLlude) | None  
Receiver Attenuator | [SOURce:POWer:ATTenuation:RECeiver:TEST](GP-IB_Command_Finder/source.md#SOURce:POWer:ATTenuation:RECeiver:TEST) | None  
| RF Path Config... | [SENSe:PATH:CONFig:ELEMent[:STATe]](GP-IB_Command_Finder/Sense/Path.md#state) | [Element](COM_Reference/Properties/Element_Property.md)  
[Offsets and Limits...](CF_Power_Commands_-_Standard.md#Offsets_and_Limits) |  |   
Mixer Tab  
Converter Stages |  [SENSe:MIXer:STAGe](GP-IB_Command_Finder/Sense/MIXerSCPI.md#Stage) |  [LOStage](COM_Reference/Properties/LOStage_Property.md)  
Enable Embedded LO |  [SENSe:MIXer:ELO:STATe](GP-IB_Command_Finder/Sense/MixrEmbedLO.md#state) |  [IsOn](COM_Reference/Properties/IsOn_Property.md)  
Setup...  
Enable Embedded LO |  [SENSe:MIXer:ELO:STATe](GP-IB_Command_Finder/Sense/MixrEmbedLO.md#state) |  [IsOn](COM_Reference/Properties/IsOn_Property.md)  
Tuning Method |  [SENSe:MIXer:ELO:TUNing:MODE](GP-IB_Command_Finder/Sense/MixrEmbedLO.md#mode) |  [TuningMode](COM_Reference/Properties/TuningMode_Property.md)  
Tune every |  [SENSe:MIXer:ELO:TUNing:INTerval](GP-IB_Command_Finder/Sense/MixrEmbedLO.md#interval) |  [TuningSweepInterval](COM_Reference/Properties/TuningSweepInterval_Property.md)  
Broadband Search |  [SENSe:MIXer:ELO:TUNing:SPAN](GP-IB_Command_Finder/Sense/MixrEmbedLO.md#span) |  [BroadbandTuningSpan](COM_Reference/Properties/BroadbandTuningSpan_Property.md)  
Noise BW |  [SENSe:MIXer:ELO:TUNing:NBW](GP-IB_Command_Finder/Sense/MixrEmbedLO.md#SENSe:MIXer:ELO:TUNing:NBW) |  None  
Max Iterations |  [SENSe:MIXer:ELO:TUNing:ITERations](GP-IB_Command_Finder/Sense/MixrEmbedLO.md#iteration) |  [MaxPreciseTuningIterations](COM_Reference/Properties/MaxPreciseTuningIterations_Property.md)  
Tolerance |  [SENSe:MIXer:ELO:TUNing:TOLerance](GP-IB_Command_Finder/Sense/MixrEmbedLO.md#tolerance) |  [PreciseTuningTolerance](COM_Reference/Properties/PreciseTuningTolerance_Property.md)  
LO Frequency Delta |  [SENSe:MIXer:ELO:LO:DELTa](GP-IB_Command_Finder/Sense/MixrEmbedLO.md#delta) |  [LOFrequencyDelta](COM_Reference/Properties/LOFrequencyDelta_Property.md)  
Default |  [SENSe:MIXer:ELO:RESet](GP-IB_Command_Finder/Sense/MixrEmbedLO.md#SENSe_ch_:MIXer:ELO:RESet) |  [ResetLOFrequency](COM_Reference/Methods/ResetLOFrequency_Method.md) [ResetTuningParameters](COM_Reference/Methods/ResetTuningParameters_Method.md)  
Input |  [SENSe:DISTortion:SWEep:CARRier:FREQuency](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:SA:COHerence:DISTortion:SWEep:CARRier:FREQuency) |  None  
Output |  [SENSe:MIXer:OUTPut:FREQuency:SIDE](GP-IB_Command_Finder/Sense/MIXerSCPI.md#OUTput_SIDE) |  [OutputSideband](COM_Reference/Properties/OutputSideband-Converter_Property.md)  
Fractional Multiplier - Numerator |  [SENSe:MIXer:LO:FREQuency:NUMerator](GP-IB_Command_Finder/Sense/MIXerSCPI.md#LO_NUM) |  [LONumerator](COM_Reference/Properties/LONumerator_Property.md)  
Fractional Multiplier - Denominator |  [SENSe:MIXer:LO:FREQuency:DENominator](GP-IB_Command_Finder/Sense/MIXerSCPI.md#LO_DEN) |  [LODenominator](COM_Reference/Properties/LODenominator_Property.md)  
LO/LO1/LO2 |  [SENSe:MIXer:LO:FREQuency:FIXed](GP-IB_Command_Finder/Sense/MIXerSCPI.md#LO_FIX) |  [LOFixedFrequency](COM_Reference/Properties/LOFixedFrequency_Property.md)  
IF |  [SENSe:MIXer:IF:FREQuency:SIDE](GP-IB_Command_Finder/Sense/MIXerSCPI.md#IF_SIDE) |  [IFSideband](COM_Reference/Properties/IFSideband-Converter_Property.md)  
Source Name |  [SENSe:MIXer:LO:NAME](GP-IB_Command_Finder/Sense/MIXerSCPI.md#name) [SENSe:ROLE:DEVice](GP-IB_Command_Finder/Sense/Role.md#Device) [SENSe:ROLE:CATalog?](GP-IB_Command_Finder/Sense/Role.md#catalog) |  [LOName](COM_Reference/Properties/LOName_Property.md) [RoleDevice](COM_Reference/Properties/RoleDevice_Property.md) [DefinedRoles](COM_Reference/Properties/DefinedRoles_Property.md)  
Power |  [SENSe:MIXer:LO:POWer](GP-IB_Command_Finder/Sense/MIXerSCPI.md#LO_POWer) |  [LOPower](COM_Reference/Properties/LOPower_Property.md)  
Leveling |  [SOURce:POWer:ALC[:MODE]](GP-IB_Command_Finder/source.md#ALCMode) |  [ALCLevelingMode](COM_Reference/Properties/ALCLevelingMode_Property.md)  
Attenuator |  [SOURce:POWer:ATTenuation](GP-IB_Command_Finder/source.md#attval) |  [chan.Attenuator](COM_Reference/Properties/Attenuator_Property.md)  
Save... |  [SENSe:MIXer:SAVE](GP-IB_Command_Finder/Sense/MIXerSCPI.md#Save) |  [SaveFile](COM_Reference/Methods/SaveFile_Method.md)  
Load... |  [SENSe:MIXer:LOAD](GP-IB_Command_Finder/Sense/MIXerSCPI.md#Load) |  [LoadFile](COM_Reference/Methods/LoadFile_Method.md)  
Modulate Tab  
Source |  [SENSe:DISTortion:MODulate:SOURce](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:SA:COHerence:DISTortion:MODulate:SOURce) |  None  
Add Source... | [SENSe:ROLE:DEVice](GP-IB_Command_Finder/Sense/Role.md#Device) | [AssignSourceToRole](COM_Reference/Methods/AssignSourceToRole_Method.md)  
Load File... | [SOURce:MODulation:FILE:LOAD](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:LOAD) | None  
Create... |  |   
Edit... |  |   
Properties... | [SOURce:MODulation:FILE:CORRection:CATalog?](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:CORRection:CATalog) [SOURce:MODulation:FILE:CORRection:DELete?](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:CORRection:DELete) | None None  
Enable Modulation | [SOURce:MODulation[:STATe]](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:STATe) | [IsEnhancedModulationControl](COM_Reference/Properties/IsEnhancedModulationControl_Property.md)  
Source Correction |  [SOURce:CORRection[:SELect]](GP-IB_Command_Finder/SourceModulation.md#SOURce:CORRection:SELec) | None  
Enable LO Feedthru Monitor | [SENSe:SA:COHerence:LO:FTHRu:MONitor[:STATe]](GP-IB_Command_Finder/Sense/SA.md#SENS_SA_COH_LO_FTHR_MON_STAT) | None  
Enable Pulse | None  | None  
[Source Cal...](CF_Cal_Commands_-_MOD.md#Src_Mod_Cal) |  |   
[Pulse Setup...](CF_Sweep_Commands_-_MOD.md#Pulse_Setup) |  |   
LO Monitor...  
Enable LO Feedthru Monitor | [SENSe:SA:COHerence:LO:FTHRu:MONitor[:STATe]](GP-IB_Command_Finder/Sense/SA.md#SENS_SA_COH_LO_FTHR_MON_STAT) | None  
Threshold Type | [SENSe:SA:COHerence:LO:FTHRu:MONitor:TYPE](GP-IB_Command_Finder/Sense/SA.md#SENS_SA_COH_LO_FTHR_MON_TYPE) | None  
Threshold Level | [SENSe:SA:COHerence:LO:FTHRu:MONitor:TOLerance](GP-IB_Command_Finder/Sense/SA.md#SENS_SA_COH_LO_FTHR_MON_TOL) | None  
Measure LO at | [SENSe:SA:COHerance:LO:FTHRu:MONitor:RECeiver](GP-IB_Command_Finder/Sense/SA.md#SENS_SA_COH_LO_FTHR_MON_REC) | None  
Create/Edit Mod File...  
Modulation Type | [SOURce:MODulation:FILE:TYPE](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:TYPE) | None  
Source Name | [SENSe:DISTortion:MODulate:SOURce](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:SA:COHerence:DISTortion:MODulate:SOURce) | None  
Sample Rate | [SOURce:MODulation:FILE:SIGNal:SRATe](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:SRATe) [SOURce:MODulation:FILE:SIGNal:SRATe:AUTO](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:SRATe:AUTO) [SOURce:MODulation:FILE:SIGNal:SRATe:CALCulated?](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:SRATe:CALCulated) [SOURce:MODulation:FILE:SIGNal:COMPact:OFILe:SRATe](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:COMPact:OFILe:SRATe) | None None None None  
Filename | [SOURce:MODulation:FILE:SIGNal:COMPact:OFILe](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:COMPact:OFILe) | None  
Signal Span | [SOURce:MODulation:FILE:SIGNal:SPAN](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:SPAN) [SOURce:MODulation:FILE:SIGNal:SPAN:CALCulated?](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:SPAN:CALCulated) [SOURce:MODulation:FILE:SIGNal:SPAN:PRIority](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:SPAN:PRIority) | None None None  
Tone Spacing | [SOURce:MODulation:FILE:SIGNal:TONE:SPACing](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:TONE:SPACing) [SOURce:MODulation:FILE:SIGNal:TONE:SPACing:CALCulated?](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:TONE:SPACing:CALCulated) [SOURce:MODulation:FILE:SIGNal:TONE:SPACing:PRIority](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:TONE:SPACing:PRIority) | None None None  
Number of Tones | [SOURce:MODulation:FILE:SIGNal:TONE:NUMBer](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:TONE:NUMBer) [SOURce:MODulation:FILE:SIGNal:TONE:NUMBer:CALCulated?](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:TONE:NUMBer:CALCulated) [SOURce:MODulation:FILE:SIGNal:TONE:NUMBer:PRIority](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:TONE:NUMBer:PRIority) [SOURce:MODulation:FILE:SIGNal:TONE:NUMBer:ROUNd](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:TONE:NUMBer:ROUNd) | None None None None  
Peak-to-Avg | [SOURce:MODulation:FILE:SIGNal:COMPact:PAVG?](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:COMPact:PAVG) [SOURce:MODulation:FILE:SIGNal:COMPact:PAVG:CALCulated?](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:COMPact:PAVG:CALCulated) [SOURce:MODulation:FILE:SIGNal:COMPact:PAVG:PRIority](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:COMPact:PAVG:PRIority) [SOURce:MODulation:FILE:SIGNal:PAVG:CALCulated?](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:PAVG:CALCulated) | None None None None  
Carrier Offset | [SOURce:MODulation:FILE:SIGNal:CARRier:OFFSet](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:CARRier:OFFSet) | None  
Nmbr of Subcarriers |  [SOURce:MODulation:FILE:SIGNal:COMPact:SUBCarrier:NUMBer](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:COMPact:SUBCarrier:NUMBer) |  None  
Sub Span |  [SOURce:MODulation:FILE:SIGNal:COMPact:SUBCarrier:SPAN](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:COMPact:SUBCarrier:SPAN) |  None  
Sub Offset |  [SOURce:MODulation:FILE:SIGNal:COMPact:SUBCarrier:OFFSet](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:COMPact:SUBCarrier:OFFSet) |  None  
Phase Type | [SOURce:MODulation:FILE:SIGNal:PHASe:TYPE](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:PHASe:TYPE) | None  
Fixed | [SOURce:MODulation:FILE:SIGNal:PHASe:FIXed](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:PHASe:FIXed) | None  
Random Phase Seed | [SOURce:MODulation:FILE:SIGNal:PHASe:RANDom:SEED](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:PHASe:RANDom:SEED) | None  
Nmbr of Notches | [SOURce:MODulation:FILE:SIGNal:NPR:NOTCh:NUMBer](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:NPR:NOTCh:NUMBer) | None  
Notch Location | [SOURce:MODulation:FILE:SIGNal:NPR:NOTCh:LOCation](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:NPR:NOTCh:LOCation) | None  
Notch1 Span | [SOURce:MODulation:FILE:SIGNal:NPR:NOTCh:SPAN](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:NPR:NOTCh:SPAN) | None  
Notch1 Offset | [SOURce:MODulation:FILE:SIGNal:NPR:NOTCh:OFFSet](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:NPR:NOTCh:OFFSet) | None  
Signal Start Time | [SOURce:MODulation:FILE:SIGNal:COMPact:TIME:STARt](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:COMPact:TIME:STARt) [SOURce:MODulation:FILE:SIGNal:COMPact:TIME:STARt:CALCulated?](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:COMPact:TIME:STARt:CALCulated) [SOURce:MODulation:FILE:SIGNal:COMPact:TIME:STARt:PRIority](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:COMPact:TIME:STARt:PRIority) | None None None  
Number of Files | [SOURce:MODulation:FILE:SIGNal:COMPact:FILE:NUMBer](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:COMPact:FILE:NUMBer) [SOURce:MODulation:FILE:SIGNal:COMPact:FILE:SELect](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:COMPact:FILE:SELect) | None None  
DAC Scaling | [SOURce:MODulation:FILE:SIGNal:DAC:SCALing](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:DAC:SCALing) | None  
Enable Optimizer | [SOURce:MODulation:FILE:SIGNal:OPTimize:ENABle](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:OPTimize:ENABle) | None  
Setup... (Optimizer Setup)  
Reject up to Harmonic Number | [SOURce:MODulation:FILE:SIGNal:OPTimize:HREJect](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:OPTimize:HREJect) | None  
Reject Nyquist Frequencies | [SOURce:MODulation:FILE:SIGNal:OPTimize:NYQReject:ENABle](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:OPTimize:NYQReject:ENABle) | None  
Preserve Burst Characteristics of Original Signal | [SOURce:MODulation:FILE:SIGNal:OPTimize:BURSt:PREServe:ENABle](GP-IB_Command_Finder/SourceModulation.md#SOURce_MODulation_FILE_SIGNal_OPTimize_BURSt_PREServe) | None  
Enable Brick-wall Filter For Spectral Leakage | [SOURce:MODulation:FILE:SIGNal:OPTimize:FILTer:ENABle](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:OPTimize:FILTer:ENABle) | None  
Enable Spectral Leakage Tapering Window With [n] Taps | [SOURce:MODulation:FILE:SIGNal:OPTimize:FILTer:TAPS](GP-IB_Command_Finder/SourceModulation.md#SOURce_MODulation_FILE_SIGNal_OPTimize_FILTer_TAPS) | None  
|  Tolerance Type | [SOURce:MODulation:FILE:SIGNal:OPTimize:TYPE](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:OPTimize:TYPE) | None  
Frequency Tolerance | [SOURce:MODulation:FILE:SIGNal:OPTimize:FREQuency:TOLerance](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:OPTimize:FREQuency:TOLerance_) | None  
Min Waveform Period | [SOURce:MODulation:FILE:SIGNal:OPTimize:MIN:WAVeform:PERiod](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:OPTimize:MIN:WAVeform:PERiod) | None  
Min Number of Tones | [SOURce:MODulation:FILE:SIGNal:OPTimize:MIN:TONE:NUMBer](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:OPTimize:MIN:TONE:NUMBer) | None  
Max Tone Spacing | [SOURce:MODulation:FILE:SIGNal:OPTimize:MAX:TONE:SPacing](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:OPTimize:MAX:TONE:SPACing) | None  
Display | None | None  
Number of Samples | None | None  
Calculated Sample Rate | [SOURce:MODulation:FILE:SIGNal:SRATe:CALCulated?](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:SRATe:CALCulated) | None  
Measurement Time | None | None  
Filename | [SOURce:MODulation:FILE:LOAD](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:LOAD) [SOURce:MODulation:FILE:SAVE](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SAVE) | None None  
Calculate | None | None  
Save... | [SOURce:MODulation:FILE:SAVE](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SAVE) | None  
Recall... | [SOURce:MODulation:FILE:LOAD](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:LOAD) | None  
Edit... (Edit Multitone)  
Tone |  [SOURce:MODulation:FILE:TONE:COUNt?](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:TONE:NUMBer) |  None  
Frequency |  [SOURce:MODulation:FILE:TONE:FREQuency?](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:TONE:FREQuency) |  None  
Power (dBm) |  [SOURce:MODulation:FILE:TONE:POWer](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:TONE:POWer) |  None  
Phase (deg) |  [SOURce:MODulation:FILE:TONE:PHASe](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:TONE:PHASe) |  None  
State |  [SOURce:MODulation:FILE:TONE[:STATe]](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:TONE:STATe) |  None  
Set All Tones |  [SOURce:MODulation:FILE:TONE:ALL[:STATe]](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:TONE:ALL:STATe) |  None  
Display |  None |  None  
Go To Row |  None |  None  
Save... |  [SOURce:MODulation:FILE:TONE:SAVE](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:TONE:SAVE) |  None  
Load... |  [SOURce:MODulation:FILE:TONE:LOAD](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:TONE:LOAD) |  None  
Defaults | [SOURce:MODulation:FILE:INITialize](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:INITialize) | None  
Properties... | None | None  
Create Digital Modulation  
Number of Carriers |  [SOURce:MODulation:FILE:SIGNal:DIGital:CARRier:NUMBer](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:DIGital:CARRier:NUMBer:) |  None  
Calculated Carrier Spacing |  [SOURce:MODulation:FILE:SIGNal:DIGital:CARRier:SPACing:CALCulated](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:DIGital:CARRier:SPACing:CALCulated) |  None  
Carrier Spacing |  [SOURce:MODulation:FILE:SIGNal:DIGital:CARRier:SPACing](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:DIGital:CARRier:SPACing) |   
Constellation File |  [SOURce:MODulation:FILE:SIGNal:DIGital:CFILe](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:DIGital:CFILe) |   
Alpha/BT |  [SOURce:MODulation:FILE:SIGNal:DIGital:FILTer:ALPHa](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:DIGital:FILTer:ALPHa) |   
Filter Type |  [SOURce:MODulation:FILE:SIGNal:DIGital:FILTer:TYPE](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:DIGital:FILTer:TYPE) |   
Modulation Format |  [SOURce:MODulation:FILE:SIGNal:DIGital:FORMat](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:DIGital:FORMat) |   
Quadrature Error |  [SOURce:MODulation:FILE:SIGNal:DIGital:QUADrature:ERRor](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:DIGital:QUADrature:ERRor) |   
Random Seed |  [SOURce:MODulation:FILE:SIGNal:DIGital:RANDom:SEED](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:DIGital:RANDom:SEED) |   
Calculated Number of Symbols |  [SOURce:MODulation:FILE:SIGNal:DIGital:SYMBol:NUMBer:CALCulated](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:DIGital:SYMBol:NUMBer:CALCulated) |   
Number of Symbols |  [SOURce:MODulation:FILE:SIGNal:DIGital:SYMBol:NUMBer](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:DIGital:SYMBol:NUMBer) |   
Calculated Symbol Rate |  [SOURce:MODulation:FILE:SIGNal:DIGital:SYMBol:RATE:CALCulated](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:DIGital:SYMBol:RATE:CALCulated) |   
Symbol Rate |  [SOURce:MODulation:FILE:SIGNal:DIGital:SYMBol:RATE](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE:SIGNal:DIGital:SYMBol:RATE) |   
|  Create DPD...  
DPD Select Procedure Dialog  
Procedure |  [SOURce:DPD:PROCedure](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:PROCedure) |  None  
Select Ideal Waveform |  [SOURce:DPD:FILE:LOAD:IDEal](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:FILE:LOAD:IDEal) |  None  
Select DPD Model |  [SOURce:DPD:FILE:LOAD:MODel](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:FILE:LOAD:MODel) |  None  
Save DPD As |  [SOURce:DPD:FILE:SAVE](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:FILE:SAVE) |  None  
| DPD Model |  [SOURce:DPD:MODel:TYPE](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:MODel:TYPE) |  None  
Create Model Using | [SOURce:DPD:MODel:USE:DIRect](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:MODel:USE:DIRect) |  None  
Cal Setup Dialog |  |   
DUT-EVM |  |   
Span | [SOURce:DPD:CORRection:COLLection:DUT:EVM:SPAN](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:CORRection:COLLection:DUT:EVM:SPAN) |  None  
Max Iterations | [SOURce:DPD:CORRection:COLLection:DUT:EVM:ITERations](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:CORRection:COLLection:DUT:EVM:ITERations) |  None  
Desired Tolerance | [SOURce:DPD:CORRection:COLLection:DUT:EVM:TOLerance](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:CORRection:COLLection:DUT:EVM:TOLerance) |  None  
DUT-ACP |  |   
Enable/Disable | [SOURce:DPD:CORRection:COLLection:DUT:ACP:ENABle](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:CORRection:COLLection:DUT:ACP:ENABle) |  None  
Span | [SOURce:DPD:CORRection:COLLection:DUT:ACP:SPAN](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:CORRection:COLLection:DUT:ACP:SPAN) |  None  
Guard Band | [SOURce:DPD:CORRection:COLLection:DUT:ACP:GBANd](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:CORRection:COLLection:DUT:ACP:GBANd) |  None  
Max Iterations | [SOURce:DPD:CORRection:COLLection:DUT:ACP:ITERations](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:CORRection:COLLection:DUT:ACP:ITERations) |  None  
Desired Tolerance | [SOURce:DPD:CORRection:COLLection:DUT:ACP:TOLerance](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:CORRection:COLLection:DUT:ACP:TOLerance) |  None  
Src- Power At DUT Out |  |   
Enable/Disable | [SOURce:DPD:CORRection:COLLection:POWer:ENABle](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:CORRection:COLLection:POWer:ENABle) |  None  
Span | [SOURce:DPD:CORRection:COLLection:POWer:SPAN](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:CORRection:COLLection:POWer:SPAN) |  None  
Max Iterations | [SOURce:DPD:CORRection:COLLection:POWer:ITERations](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:CORRection:COLLection:POWer:ITERations) |  None  
Desired Tolerance | [SOURce:DPD:CORRection:COLLection:POWer:TOLerance](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:CORRection:COLLection:POWer:TOLerance) |  None  
Src-LO Feedthru |  |   
Enable/Disable | [SOURce:DPD:CORRection:COLLection:LO:FTHRu:ENABle](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:CORRection:COLLection:LO:FTHRu:ENABle) |  None  
Max Iterations | [SOURce:DPD:CORRection:COLLection:LO:FTHRu:ITERations](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:CORRection:COLLection:LO:FTHRu:ITERations) |  None  
Desired Tolerance | [SOURce:DPD:CORRection:COLLection:LO:FTHRu:TOLerance](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:CORRection:COLLection:LO:FTHRu:TOLerance) |  None  
Src- |  |   
Enable/Disable | [SOURce:DPD:CORRection:COLLection:DISTortion:ENABle](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:CORRection:COLLection:DISTortion:ENABle) |  None  
Type | [SOURce:DPD:CORRection:COLLection:DISTortion:TYPE](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:CORRection:COLLection:DISTortion:TYPE) |  None  
Span | [SOURce:DPD:CORRection:COLLection:DISTortion:SPAN](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:CORRection:COLLection:DISTortion:SPAN) |  None  
Max Iterations | [SOURce:DPD:CORRection:COLLection:DISTortion:ITERations](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:CORRection:COLLection:DISTortion:ITERations) |  None  
Desired Tolerance | [SOURce:DPD:CORRection:COLLection:DISTortion:TOLerance](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:CORRection:COLLection:DISTortion:TOLerance) |  None  
Cal Detals Dialog |   
DAC Scaling | [SOURce:DPD:DAC:SCALing](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:DAC:SCALing) |  None  
Maximum PAPR Expansion | [SOURce:DPD:PAPR:EXPansion:MAXimum](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:PAPR:EXPansion:MAXimum) |  None  
Backoff For Linear Gain Measurement | [SOURce:DPD:MEASure:LINGain:POWer:BACKoff](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:MEASure:LINGain:POWer:BACKoff) | None  
During Direct DPD, Measure DUT Linear Gain | [SOURce:DPD:MEASure:LINGain:ENABle](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:MEASure:LINGain:ENABle) |  None  
Modulation Cal Dialog  
Calibrate | [SOURce:DPD:CORRection:COLLection:ACQuire](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:CORRection:COLLection:ACQuire) |  None  
Status | [SOURce:DPD:CORRection:COLLection:ACQuire:STATus?](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:CORRection:COLLection:ACQuire:STATus) |  None  
Modeling Dialog  
Polynomial Order | [SOURce:DPD:MODel:MEMPoly:ORDer](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:MODel:MEMPoly:ORDer) |  None  
Past Memory (-) | [SOURce:DPD:MODel:MEMPoly:MEMory:PAST](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:MODel:MEMPoly:MEMory:PAST) |  None  
Future Memory (+) | [SOURce:DPD:MODel:MEMPoly:MEMory:FUTure](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:MODel:MEMPoly:MEMory:FUTure) |  None  
Crossterm Equations | [SOURce:DPD:MODel:MEMPoly:CROSsterm](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:MODel:MEMPoly:CROSsterm) |  None  
Memory Operators | [SOURce:DPD:MODel:DYNGain:MEMory:OPERator:M[1-4]:ENABle](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:MODel:DYNGain:MEMory:OPERator:M:ENABle) |  None  
Number Power Segments | [SOURce:DPD:MODel:DYNGain:POWer:SEGMent:COUNt](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:MODel:DYNGain:POWer:SEGMent:COUN) |  None  
Memory Past Depth |  [SOURce:DPD:MODel:DYNGain:MEMory:PAST](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:DYNGain:MEMory:PAST) |  None  
Memory Future Depth | [SOURce:DPD:MODel:DYNGain:MEMory:FUTure](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:MODel:DYNGain:MEMory:FUTure) |  None  
Memory Stepsize | [SOURce:DPD:MODel:DYNGain:MEMory:STEP](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:MODel:DYNGain:MEMory:STEP) |  None  
Create Model or  
Apply Model |  [SOURce:DPD:MODel:CREate](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:MODel:CREate) [SOURce:DPD:MODel:APPLy](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:MODel:APPLy) |  None None  
Cal Model | [SOURce:DPD:MODel:CALibrate](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:MODel:CAL) |  None  
Model Status | [SOURce:DPD:MODel:STATus?](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:MODel:STATus) |  None  
Model Details Dialog  
Interpolation Type | [SOURce:DPD:MODel:DYNGain:INTerpolate:TYPE](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:MODel:DNYGain:INTerpolate:TYPE) |  None  
Min Points Per Power Segment | [SOURce:DPD:MODel:DYNGain:POWer:SEGMent:POINt:COUNt:MINimum](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:MODel:DYNGain:POWer:SEGMent:POINt:COUNt:MIN) | None  
Optimize DPD Model | [SOURce:DPD:MODel:DYNGain:OPTimize:ENABle](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:MODel:DYNGain:OPTimize:ENABle) |  None  
Use Waveform Compacted By, Level | [SOURce:DPD:MODel:DYNGain:OPTimize:COMPact:LEVel](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:MODel:DYNGain:OPTimize:COMPact:LEVel) |  None  
Use Waveform Compacted By, Auto | [SOURce:DPD:MODel:DYNGain:OPTimize:COMPact:AUTO](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:MODel:DYNGain:OPTimize:COMPact:AUTO) |  None  
NMSE Optimization Goal, State | [SOURce:DPD:MODel:DYNGain:OPTimize:NMSE:INCL](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:MODel:DYNGain:OPTimize:NMSE:INCLude) |  None  
NMSE Optimization Goal, Value | [SOURce:DPD:MODel:DYNGain:OPTimize:NMSE:GOAL](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:MODel:DYNGain:OPTimize:NMSE:GOAL) |  None  
Optimize Memory Operators | [SOURce:DPD:MODel:DYNGain:OPTimize:MEMory:OPERator:INCLude](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:DYNGain:OPTimize:MEMory:OPERator:INCLude) |  None  
| Measure Tab  
Measurement Type | [SENSe:DISTortion:MEASure:BAND:TYPE](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:SA:COHerence:DISTortion:MEASure:BAND:TYPE) | None  
Autofill | [SENSe:DISTortion:MEASure:BAND:AUTofill](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:MEASure:BAND:AUTofill) | None  
Carrier |  [SENSe:DISTortion:SWEep:CARRier:FREQuency](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:SA:COHerence:DISTortion:SWEep:CARRier:FREQuency) [SENSe:DISTortion:MEASure:BAND:CARRier:IBW](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:SA:COHerence:DISTortion:MEASure:BAND:CARRier:IBW) [SENSe:DISTortion:MEASure:BAND:CARRier:OFFSet](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:SA:COHerence:DISTortion:MEASure:BAND:CARRier:OFFSet) |  None  
| ACPLo |  [SENSe:DISTortion:MEASure:BAND:ACP:LOWer:IBW](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:SA:COHerence:DISTortion:MEASure:BAND:ACP:LOWer:IBW) [SENSe:DISTortion:MEASure:BAND:ACP:LOWer:OFFSet](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:SA:COHerence:DISTortion:MEASure:BAND:ACP:LOWer:OFFSet) |  None None  
ACPUp |  [SENSe:DISTortion:MEASure:BAND:ACP:LOWer:IBW](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:SA:COHerence:DISTortion:MEASure:BAND:ACP:LOWer:IBW) [SENSe:DISTortion:MEASure:BAND:ACP:LOWer:OFFSet](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:SA:COHerence:DISTortion:MEASure:BAND:ACP:LOWer:OFFSet) |  None None  
Notch |  [SENSe:DISTortion:MEASure:BAND:NOTCh:IBW](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:SA:COHerence:DISTortion:MEASure:BAND:NOTCh:IBW) [SENSe:DISTortion:MEASure:BAND:NOTCh:OFFSet](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:SA:COHerence:DISTortion:MEASure:BAND:NOTCh:OFFSet) |  None None  
Measurement Details  
Distortion Measurement Correlation Aperture |  [SENSe:DISTortion:MEASure:CORRelation:APERture](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:SA:COHerence:DISTortion:MEASure:ANALysis:BW) [SENSe:DISTortion:MEASure:CORRelation:APERture:AUTO[:STATe]](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:SA:COHerence:DISTortion:MEASure:ANALysis:BW:AUTO:STATe) |  None None  
ADC Anti-alias Filter | [SENSe:DISTortion:ADC:FILTer:TYPE](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:SA:COHerence:DISTortion:ADC:FILTer:TYPE) | None  
|  Modulation Filter |  [SENSe:DISTortion:MEASure:FILTer](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:MEASure:FILTer) |  None  
Alpha |  [SENSe:DISTortion:MEASure:FILTer:ALPHa](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:MEASure:FILTer:ALPHa) |  None  
Symbol Rate |  [SENSe:DISTortion:MEASure:FILTer:SRATe](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:MEASure:FILTer:SRATe) [SENSe:DISTortion:MEASure:FILTer:SRATe:AUTO[:STATe]](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:MEASure:FILTer:SRATe:AUTO:STATe) |  None None  
|  EVM Normalization | [SENSe:DISTortion:EVM:NORMalize](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:EVM:NORMalize) | None  
|  Phase Stitching | [SENSe:DISTortion:PHASe:STITching:TYPE](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#DistPhasStitType) | None  
|  Nominal DUT NF | [SENSe:DISTortion:PATH:DUT:NOMinal:NF](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:SA:COHerence:DISTortion:PATH:DUT:NOMinal:NF) | None  
ADVANCED - Measurement Band Table  
Add Band  
|  [SENSe:DISTortion:MEASure:BAND:ADD](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:SA:COHerence:DISTortion:MEASure:BAND:ADD) [SENSe:DISTortion:MEASure:BAND:COUNt?](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:SA:COHerence:DISTortion:MEASure:BAND:COUNt) [SENSe:DISTortion:MEASure:BAND:NAME](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:SA:COHerence:DISTortion:MEASure:BAND:NAME) |  None None None  
Delete Band | [SENSe:DISTortion:MEASure:BAND:DELete](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:SA:COHerence:DISTortion:MEASure:BAND:DELete) | None  
Autofill from Mod File | None | None  
Reset Bands to defaults | [SENSe:DISTortion:MEASure:BAND:INITialize](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:SA:COHerence:DISTortion:MEASure:BAND:INITialize) | None  
  
Meas Class... |  |  [CALCulate:MEASure:DEFine](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:DEFine) |  [CreateCustomMeasurementEx](COM_Reference/Methods/CreateCustomMeasurementEx_Method.md)  
---|---|---|---  
Quick Start... |  S-Param |  [CALCulate:MEASure:PARameter](GP-IB_Command_Finder/Calculate/MeasurePARameter.md#CALCulate:MEASure:PARameter) |  [CreateSParameterEx](COM_Reference/Methods/Create_SParameterEX_Method.md)  
Balanced |  [CALCulate:MEASure:PARameter](GP-IB_Command_Finder/Calculate/MeasurePARameter.md#CALCulate:MEASure:PARameter) |  [BalSMeasurement](COM_Reference/Properties/BalSMeasurement_Property.md) [BBalMeasurement](COM_Reference/Properties/BBalMeasurement_Property.md) [SBalMeasurement](COM_Reference/Properties/SBalMeasurement_Property.md) [SSBMeasurement](COM_Reference/Properties/SSBMeasurement_Property.md)  
Other |  [CALCulate:MEASure:PARameter](GP-IB_Command_Finder/Calculate/MeasurePARameter.md#CALCulate:MEASure:PARameter) |  [CreateSParameterEx](COM_Reference/Methods/Create_SParameterEX_Method.md)

