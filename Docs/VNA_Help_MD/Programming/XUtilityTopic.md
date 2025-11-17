[File](FileTopic.md) | [Instrument](XTraceChanTopic.md) | [Response](XResponseTopic.md) | [Stimulus](XStimulusTopic.md) | [Utility](XUtilityTopic.md) | [Cal](CalTopic.md) | [Apps](MixerTopic.md) | [Remote ONLY](DataTopic.md)

* * *

[Save /Recall](FileTopic.md#Save) | [Manage Files](FileTopic.md#files) | [Manage Folders](FileTopic.md#folders) | [Print](FileTopic.md#Print) | [Read Clock](FileTopic.md#clock)  
[Preset (User)](XUtilityTopic.md#User) | [Security](XUtilityTopic.md#Security) | [Configure](XUtilityTopic.md#Configure)  
[Hdwr & Capabilities](XUtilityTopic.md#Capabilities) | [Macros](XUtilityTopic.md#Macro) | [Status](XUtilityTopic.md#Status) | [Events](XUtilityTopic.md#Events) | Rear Panel | [Read Temperature](XUtilityTopic.md#Temperature) | [GPIB Pass-through](XUtilityTopic.md#passthru) | VISA Pass-through | [Preferences](XUtilityTopic.md#pref)

[LXI](XUtilityTopic.md#LXI) | Error Messages | mmWave

Preset / User |  SCPI |  COM  
---|---|---  
Preset |  [SYSTem:PRESet](GP-IB_Command_Finder/System.md#pre) [*RST](GP-IB_Command_Finder/Common_Commands.md#rst) |  [app.Preset](COM_Reference/Methods/Preset_Method.md)  
Preset plus delete window |  [SYSTem:FPReset](GP-IB_Command_Finder/System.md#Fpre) |  [app.Reset](COM_Reference/Methods/Reset_Method.md)  
User Preset |  [SYSTem:UPReset](GP-IB_Command_Finder/System.md#UPreset) |  [app.UserPreset](COM_Reference/Methods/UserPreset_Method.md)  
Load User Preset file |  [SYSTem:UPReset:LOAD](GP-IB_Command_Finder/System.md#UPresetLoad) |  [app.UserPresetLoadFile](COM_Reference/Methods/UserPresetLoadFile_Method.md)  
Save Current state as User Preset |  [SYSTem:UPReset:SAVE](GP-IB_Command_Finder/System.md#UpresetSave) |  [app.UserPresetSaveState](COM_Reference/Methods/UserPresetSaveState_Method.md)  
Enable Front Panel for User Preset |  [SYSTem:UPReset:FPANel](GP-IB_Command_Finder/System.md#UpreFpanel) |  [app.UserPresetEnable](COM_Reference/Properties/UserPresetEnable_Property.md)  
Quit application |  None |  [app.Quit](COM_Reference/Methods/Quit_Method.md)  
  
Security  
---  
Frequency Blanking |  [SYSTem:SECurity[:LEVel]](GP-IB_Command_Finder/System.md#Security) |  [app.SecurityLevel](COM_Reference/Properties/SecurityLevel_Property.md)  
  
Configure  
---  
Local Lockout |  [Local Lockout](GP-IB_Command_Finder/Local_Lockout.md) |  [app.LocalLockoutState](COM_Reference/Properties/LocalLockoutState_Property.md)  
Set and return GPIB address |  None |  [app.GPIBAddress](COM_Reference/Properties/GPIBAddress_Property.md)  
Set VNA to GPIB system controller or talker/listener |  None |  [app.GPIBMode](COM_Reference/Properties/GPIBMode_Property.md)  
Set and return SICL address |  None |  [app.SICLAddress](COM_Reference/Properties/SICLAddress_Property.md)  
Control the VNA via SICL |  None |  [app.SICL](COM_Reference/Properties/SICL_Property.md)  
Return Full computer name |  None |  [app.SystemName](COM_Reference/Properties/SystemName_Property.md)  
System Impedance |  [SENSe:CORRection:IMPedance:INPut:MAGNitude](GP-IB_Command_Finder/Sense/Sense_Correction.md#imped) |  [SystemImpedanceZ0](COM_Reference/Properties/SystemImpedanceZ0_Property.md)  
Load Test Set Config file and Restart VNA. |  [SYSTem:CONFigure](GP-IB_Command_Finder/System.md#config) |  [app.Configure](COM_Reference/Methods/Configure_Method.md)  
Hardware |  [Instrument Menu](XTraceChanTopic.md) |  [Instrument Menu](XTraceChanTopic.md)  
IO Configuration |  None |  [IOConfiguration Object](COM_Reference/Objects/IOConfiguration_Object.md)  
Modify the manufacturer name |  [SYSTem:PERSona:MANufacturer](GP-IB_Command_Finder/System.md#SYSTem:PERSona:MANufacturer) |  None  
Reset to original manufacturer identification |  [SYSTem:PERSona:MANufacturer:DEFault](GP-IB_Command_Finder/System.md#SYSTem:PERSona:MANufacturer:DEFault) |  None  
Modify the product model |  [SYSTem:PERSona:MODel](GP-IB_Command_Finder/System.md#SYSTem:PERSona:MODel) |  None  
Reset to original product model name |  [SYSTem:PERSona:MODel:DEFault](GP-IB_Command_Finder/System.md#SYSTem:PERSona:MODel:DEFault) |  None  
Set and return Source Port Control |  [SYSTem:ISPControl[:STATe]](GP-IB_Command_Finder/System.md#SYST_ISPContol_STATe) |  None  
  
Hardware and Capabilities  
---  
DSP Revision |  [SYSTem:CONFigure:REVision:DSP?](GP-IB_Command_Finder/System.md#confDSP) |  [DspRevision](COM_Reference/Properties/DSPRevision_Property.md)  
DSP FPGA |  [SYSTem:CONFigure:REVision:DSPFpga?](GP-IB_Command_Finder/System.md#confDSPF) |  [DspFpgaRevision](COM_Reference/Properties/DspFpgaRevision_Property.md)  
CPU Speed |  [SYSTem:CONFigure:REVision:CPU?](GP-IB_Command_Finder/System.md#confCPU) |  [CpuRevision](COM_Reference/Properties/CpuRevision_Property.md)  
Returns the Synthesizer Revision number. |  [SYSTem:CONFigure:REVision:PNA:SYNthesizer:VERSion?](GP-IB_Command_Finder/System.md#SYSTem:CONFigure:REVision:PNA:SYNthesizer:VERSion) |  None  
Hostname |  [SYSTem:COMMunicate:LAN:HOSTname?](GP-IB_Command_Finder/SystCommunicate.md#commLAN) |  [LANConfiguration](COM_Reference/Properties/LANConfiguration_Property.md) [GetIPConfigurationStruct](COM_Reference/Methods/GetIPConfigurationStruct_Method.md) [SystemName](COM_Reference/Properties/SystemName_Property.md)  
Disk Drive Version |  [SYSTem:DISK:REVision?](GP-IB_Command_Finder/System.md#SYSTem:DISK:REVision) |  None  
Set and return the coupler state |  [SYSTem:FCORrection:CHANnel:COUPler[:STATe]](GP-IB_Command_Finder/System.md#SYSTem:FCORrection:CHANnel:COUPler:STATe) |  None  
Returns the word size (32 or 64). |  [SYSTem:CONFigure:BIT?](GP-IB_Command_Finder/System.md#SYSTem:CONFigure:BIT) |  None  
Many queries regarding the capability of a specific VNA |  [SYSTem:CAPability](GP-IB_Command_Finder/SystCapability.md) |  [Capabilities Object](COM_Reference/Objects/Capabilities_Object.md)  
  
Macros  
---  
Execute Macro |  [SYSTem:SHORtcut:EXECute](GP-IB_Command_Finder/System.md#MacroExecute) |  [app.ExecuteShortcut](COM_Reference/Methods/Execute_Shortcut_Method.md)  
Delete Macro |  [SYSTem:SHORtcut:DELete](GP-IB_Command_Finder/System.md#MacroDelete) |  [app.DeleteShortCut](COM_Reference/Methods/DeleteShortCut_Method.md)  
Write macro path, argument, and title |  [SYSTem:SHORtcut:PATH](GP-IB_Command_Finder/System.md#MacroPath) [SYSTem:SHORtcut:ARGuments](GP-IB_Command_Finder/System.md#MacroArgue) [SYSTem:SHORtcut:TITLe](GP-IB_Command_Finder/System.md#MacroTitle) |  [app.PutShortcut](COM_Reference/Methods/Put_Shortcut_Method.md)  
Read macro path, argument, and title |  [app.GetShortcut](COM_Reference/Methods/Get_Shortcut_Method.md)  
  
Status Commands  
---  
Status Registers |  [GP-IB/Status Registers](GP-IB_Command_Finder/Status.md) |  N/A  
*OPC;*WAI |  [GP-IB/Common_Commands](GP-IB_Command_Finder/Common_Commands.md) |  N/A  
  
Events  
---  
AllowAllEvents Method |  None |  [app.AllowAllEvents](COM_Reference/Methods/AllowAllEvents_Method.md)  
AllowEventCategory Method |  None |  [app.AllowEventCategory](COM_Reference/Methods/AllowEventCategory_Method.md)  
AllowEventMessage Method |  None |  [app.AllowEventMessage](COM_Reference/Methods/AllowEventMessage_Method.md)  
AllowEventSeverity Method |  None |  [app.AllowEventSeverity](COM_Reference/Methods/AllowEventSeverity_Method.md)  
DisallowAllEvents Method |  None |  [app.DisallowAllEvents](COM_Reference/Methods/DisallowAllEvents_Method.md)  
MessageText Method |  None |  [app.MessageText](COM_Reference/Properties/Message_Text_Method.md)  
OnCalEvent |  None |  [app.OnCalEvent](COM_Reference/Events/OnCalEvent.md)  
OnChannelEvent |  None |  [app.OnChannelEvent](COM_Reference/Events/OnChannelEvent.md)  
OnDisplayEvent |  None |  [app.OnDisplayEvent](COM_Reference/Events/OnDisplayEvent.md)  
OnHardwareEvent |  None |  [app.OnHardwareEvent](COM_Reference/Events/OnHardwareEvent.md)  
OnMeasurementEvent |  None |  [app.OnMeasurementEvent](COM_Reference/Events/OnMeasurementEvent.md)  
OnSCPIEvent |  None |  [app.OnSCPIEvent](COM_Reference/Events/OnSCPIEvent.md)  
OnSystemEvent |  None |  [app.OnSystemEvent](COM_Reference/Events/OnSystemEvent.md)  
OnUserEvent |  None |  [app.OnUserEvent](COM_Reference/Events/OnUserEvent.md)  
SetFailOnOverRange |  None |  [app.SetFailOnOverRange](COM_Reference/Methods/SetFailOnOverRange_Method.md)  
  
Rear Panel Connector Controls  
---  
Material Handler I/O Connector |  [GPIB/Control](GP-IB_Command_Finder/ControlHandler.md) |  [MaterialHandler IO](COM_Reference/Objects/HWMaterialHandlerIO_Object.md)  
External Test Set Connector |  [GPIB/Control](GP-IB_Command_Finder/ControlExt.md) |  [External Test Set](COM_Reference/Objects/HWExternalTestSetIO_Object.md)  
Power I/O Connector - Analog IN/Out |  [Control SCPI](GP-IB_Command_Finder/ControlAux.md) |  [InputVoltageEX](COM_Reference/Properties/InputVoltageEX_Property.md) [get OutputVoltage](COM_Reference/Methods/get_OutputVoltage_Method.md) [put OutputVoltage](COM_Reference/Methods/put_OutputVoltage_Method.md)  
  
Read Temperature  
---  
Read temperature on the receiver microcircuit. |  [SENSe:TEMPerature?](GP-IB_Command_Finder/Sense/Temperature.md) |  [ReceiverTemperature](COM_Reference/Properties/ReceiverTemperature_Property.md)  
  
GPIB Pass Through  
---  
Open a GPIB pass-through session |  [SYSTem:COMMunicate:GPIB:RDEVice:OPEN](GP-IB_Command_Finder/SystCommunicate.md#open) |  None  
Write string data to the GPIB pass-through device. |  [SYSTem:COMMunicate:GPIB:RDEVice:WRITe](GP-IB_Command_Finder/SystCommunicate.md#write) |  None  
Write data to the GPIB pass-through device - with header. |  [SYSTem:COMMunicate:GPIB:RDEVice:WBLock](GP-IB_Command_Finder/SystCommunicate.md#WBlock) |  None  
Write data to the GPIB pass-through device - without header. |  [SYSTem:COMMunicate:GPIB:RDEVice:WBINary](GP-IB_Command_Finder/SystCommunicate.md#wbinary) |  None  
Reads string data from the GPIB pass-through device. |  [SYSTem:COMMunicate:GPIB:RDEVice:READ?](GP-IB_Command_Finder/SystCommunicate.md#read) |  None  
Closes a GPIB pass-through session |  [SYSTem:COMMunicate:GPIB:RDEVice:CLOSe](GP-IB_Command_Finder/SystCommunicate.md#close) |  None  
Closes ALL GPIB pass-through sessions |  [SYSTem:COMMunicate:GPIB:RDEVice:RESet](GP-IB_Command_Finder/SystCommunicate.md#reset) |  None  
  
VISA Pass Through  
---  
Open a VISA pass-through session |  [SYSTem:COMMunicate:VISA:RDEVice:OPEN](GP-IB_Command_Finder/SystCommunicate.md#VISA_Open) |  [Open](COM_Reference/Methods/Open_VISAPassthrough_Method.md)  
Write string data to the VISA pass-through device. |  [SYSTem:COMMunicate:VISA:RDEVice:WRITe](GP-IB_Command_Finder/SystCommunicate.md#VISA_Write) |  [WriteString](COM_Reference/Methods/WriteString_VISAPassthrough_Method.md)  
Write data to the VISA pass-through device - without header. |  [SYSTem:COMMunicate:VISA:RDEVice:WBINary](GP-IB_Command_Finder/SystCommunicate.md#VISA_WBINary) |  [WriteBinary](COM_Reference/Methods/WriteBinary.md)  
Returns list of visa address strings or aliases. |  [SYSTem:COMMunicate:VISA:RDEVice:FIND?](GP-IB_Command_Finder/SystCommunicate.md#VISA_FIND) |  [Find](COM_Reference/Methods/Find_VISAPassthrough_Method.md)  
Sets timeout value for VISA pass-through commands. |  [SYSTem:COMMunicate:VISA:RDEVice:TIMeout](GP-IB_Command_Finder/SystCommunicate.md#VISA_Session_Timeout) |  [GetVISATimeout](COM_Reference/Methods/GetVISATimeout_Method.md) [SetVISATimeout](COM_Reference/Methods/SetVISATimeout_Method.md)  
Reads string data from the VISA pass-through device. |  [SYSTem:COMMunicate:VISA:RDEVice:READ?](GP-IB_Command_Finder/SystCommunicate.md#VISA_Read) |  [ReadString](COM_Reference/Methods/ReadString_VISAPassthrough_Method.md)  
Reads data from the VISA pass-through device as a Safe Array of variants. |  None |  [ReadBinary](COM_Reference/Methods/ReadBinary_Method.md)  
Reads binary data in a more compact form of Safe Array. |  None |  [ReadBinaryCompact](COM_Reference/Methods/ReadBinaryCompact_Method.md)  
Closes a VISA pass-through session |  [SYSTem:COMMunicate:VISA:RDEVice:CLOSe](GP-IB_Command_Finder/SystCommunicate.md#VISA_Close) |  [Close](COM_Reference/Methods/Close_VISAPassthrough_Method.md)  
Closes ALL VISA pass-through sessions |  [SYSTem:COMMunicate:VISA:RDEVice:RESet](GP-IB_Command_Finder/SystCommunicate.md#VISA_Reset) |  [Reset](COM_Reference/Methods/Reset_VISAPassthrough_Method.md)  
  
Preferences  
---  
Reset Preference default settings |  [SYSTem:PREFerences:DEFault](GP-IB_Command_Finder/System_Preferences.md#PrefDefault) |  [RestoreDefaults](COM_Reference/Methods/RestoreDefaults_Method.md)  
Touchscreen ON | Off |  [SYSTem:TOUChscreen[:STATe]](GP-IB_Command_Finder/System.md#touchscreen) |  [Touchscreen Property](COM_Reference/Properties/Touchscreen_Property.md)  
Selected trace is wider |  None |  None  
Selected trace changes width briefly |  None |  None  
Cal: Auto-save User Cal Set |  [SENSe:CORRection:PREFerence:CSET:SAVE](GP-IB_Command_Finder/Sense/Sense_Correction.md#CsetSave) |  [RemoteCalStoragePreference](COM_Reference/Properties/RemoteCalStoragePreference_Property.md)  
Cal: For Guided Cal, set external trigger |  [SENSe:CORRection:PREFerence:TRIG:FREE](GP-IB_Command_Finder/Sense/Sense_Correction.md#PrefTrig) |  [PreferInternalTriggerOnChannelSingle](COM_Reference/Properties/PreferInternalTriggerOnChannelSingle_Property.md)  
Cal: For Unguided Cal, set external trigger |  [SENSe:CORRection:PREFerence:TRIG:FREE](GP-IB_Command_Finder/Sense/Sense_Correction.md#PrefTrig) |  [PreferInternalTriggerOnUnguidedCal](COM_Reference/Properties/PreferInternalTriggerOnUnguidedCal_Property.md)  
Cal: Simulated Cal Behavior |  [SENSe:CORRection:PREFerence:SIMCal](GP-IB_Command_Finder/Sense/Sense_Correction.md#Simcal) |  None  
Cal: Use Primary FOM (for mmWave) |  [SENSe:CORRection:PREFerence:CALibration[:FOM]:RANGe](GP-IB_Command_Finder/Sense/Sense_Correction.md#PrefCalFOM) |  [FrequencyOffsetRangeForCalComputations](COM_Reference/Properties/FrequencyOffsetRangeForCalComputations_Property.md)  
Cal: Use legacy behavior for Series-C & Shunt-L fixtures |  [SYSTem:PREFerences:ITEM:FIXTure:CIRCuit:DEFAults](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:ITEM:FIXTure:CIRCuit:DEFAults) |  None  
Cal: Use Unknown thru math for SOLT methods |  [SYSTem:PREFerence:ITEM:USOLt](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:ITEM:USOLt) |  None  
Memory: Data Math 8510 Mode |  None |  None  
Power: RF power On during frequency sweep retrace |  [SYSTem:PREFerences:ITEM:RETRace:POWer](GP-IB_Command_Finder/System_Preferences.md#freqRetrace) |  [PowerOnDuringRetraceMode](COM_Reference/Properties/PowerOnDuringRetraceMode_Property.md)  
Power: Power Sweep Retrace |  [SYSTem:PREFerences:ITEM:PSRTrace](GP-IB_Command_Finder/System_Preferences.md#pwrSwpRetrace) |  [PowerSweepRetracePowerMode](COM_Reference/Properties/PowerSweepRetracePowerMode_Property.md)  
Trigger: External Trigger OUT is Global |  [TRIGger:PREFerences:AIGLobal](GP-IB_Command_Finder/Trigger_SCPI.md#PrefGlobal) |  [AuxTriggerScopeIsGlobal](COM_Reference/Properties/AuxTriggerScopeIsGlobal_Property.md)  
Meas: Port 1 Noise Tuner Switch state |  [SYSTem:PREFerences:ITEM:SWITch:DEF](GP-IB_Command_Finder/System_Preferences.md#Switch) |  [Port1NoiseTunerSwitchPresetsToExternal](COM_Reference/Properties/Port1NoiseTunerSwitchPresetsToExternal_Property.md)  
Meas: Mathematical offset for receiver attenuation |  [SYSTem:PREFerences:ITEM:OFFSet:RCV](GP-IB_Command_Finder/System_Preferences.md#prefRCV) |  [OffsetReceiverAttenuator](COM_Reference/Properties/OffsetReceiverAttenuator_Property.md)  
Meas: Mathematical offset for source attenuation |  [SYSTem:PREFerences:ITEM:OFFSet:SRC](GP-IB_Command_Finder/System_Preferences.md#prefSRC) |  [OffsetSourceAttenuator](COM_Reference/Properties/OffsetSourceAttenuator_Property.md)  
Limit: Draw failed trace segments in red |  [SYSTem:PREFerences:ITEM:RTOF](GP-IB_Command_Finder/System_Preferences.md#rtof) |  [RedTraceOnFail](COM_Reference/Properties/RedTraceOnFail_Property.md)  
Limit: Draw limit lines in red |  [SYSTem:PREFerences:ITEM:REDLimits](GP-IB_Command_Finder/System_Preferences.md#Redlimits) |  [DrawLimitLinesInRed](COM_Reference/Properties/DrawLimitLinesInRed_Property.md)  
Marker: Programming treats Mkr 10 as Reference |  [SYSTem:PREFerences:ITEM:REFMarker](GP-IB_Command_Finder/System_Preferences.md#REFMarker) |  [TreatMkr10AsReference](COM_Reference/Properties/TreatMkr10AsReference_Property.md)  
**Marker: On Preset, Coupled Markers is ON** |  [SYSTem:PREFerences:ITEM:MCPreset](GP-IB_Command_Finder/System_Preferences.md#MarkerCouplPreset) |  [MarkCoupPresetIsOn](COM_Reference/Properties/MarkCoupPresetIsOn_Property.md)  
**Marker:** On Preset, Coupling Method is Channel |  [SYSTem:PREFerences:ITEM:MCMethod](GP-IB_Command_Finder/System_Preferences.md#markerCoupleMethod) |  [MarkCoupMethPresetIsChan](COM_Reference/Properties/MarkCoupMethPresetIsChan_Property.md)  
**Marker: Coupling controls on|off state of markers.** |  [SYSTem:PREFerences:ITEM:MCControl](GP-IB_Command_Finder/System_Preferences.md#markerCouplControl) |  [MarkCoupControlsMkrState](COM_Reference/Properties/MarkCoupControlsMkrState_Property.md)  
Marker: Use single marker for marker search |  [SYSTem:PREFerences:ITEM:MARKer:SINGle](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:ITEM:MARKer:SINGle) |  [SingleMarkerSearch](COM_Reference/Properties/SingleMarkerSearch_Property.md)  
Marker: Sets the bandwidth search preference |  [SYSTem:PREFerences:ITEM:MARKer:BANDwidth:SEARch](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:ITEM:MARKer:BANDwidth:SEARch) |  [BandwidthSearch](COM_Reference/Properties/BandwidthSearch_Property.md)  
Ext Device: de-activate on PRESET and recall. |  [SYSTem:PREFerences:ITEM:EDEV:DPOLicy](GP-IB_Command_Finder/System_Preferences.md#PrefEdevDpol) |  [ExternalDeviceDeActivatePolicy](COM_Reference/Properties/ExternalDeviceDeActivatePolicy_Property.md)  
Avg: On PRESET set two-point group delay aperture |  [SYSTem:PREFerences:ITEM:GDELay:TWOPoint](GP-IB_Command_Finder/System_Preferences.md#groupDelay) |  [TwoPointGroupDelayAperture](COM_Reference/Properties/TwoPointGroupDelayAperture_Property.md)  
Power: On PRESET always turn power ON |  [SYSTem:PREFerences:ITEM:PRESet:POWer](GP-IB_Command_Finder/System_Preferences.md#PowerState) |  [PresetPowerState](COM_Reference/Properties/PresetPowerState_Property.md)  
Power: Report source unleveled events as errors |  [SYSTem:ERRor:REPort:SUNLeveled](GP-IB_Command_Finder/System.md#unlevel) |  [EnableSourceUnleveledEvents](COM_Reference/Properties/EnableSourceUnleveledEvents_Property.md)  
Power: Turn source power OFF when receiver is overloaded |  [SYSTem:PREFerences:ITEM:RECeivers:OVERload:POWer](GP-IB_Command_Finder/System_Preferences.md#overloadOFF) |  [RFOffOnReceiverOverload](COM_Reference/Properties/RFOffOnReceiverOverload_Property.md)  
Power: Report when receiver is overloaded |  [SYSTem:PREFerences:ITEM:RECeivers:CERRor](GP-IB_Command_Finder/System_Preferences.md#RecError) |  [ReportReceiverOverload](COM_Reference/Properties/ReportReceiverOverload_Property.md)  
Preset: Confirm preset |  [SYSTem:PREFerences:ITEM:PRESet:CONFirm](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:ITEM:PRESet:CONFirm) |  [ConfirmPreset](COM_Reference/Properties/ConfirmPreset_Property.md)  
Preset: On PRESET show Quick Start dialog |  [SYSTem:PREFerences:ITEM:QSTart](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:ITEM:QSTart) |  [ShowQuickStartOnPreset](COM_Reference/Properties/ShowQuickStartOnPreset_Property.md)  
Controls the on/off state of the preference, "Use keyboard to navigate softkeys" |  [SYSTem:PREFerences:ITEM:SOFTkeys:NAVigation](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:ITEM:SOFTkeys:NAVigation) |  None  
Sweep: Use only ramp sweeps for Auto Sweep Mode |  [SYSTem:PREFerences:ITEM:ASMRamp](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:ITEM:ASMRamp) |  None  
System: Enable Sound |  [SYSTem:BEEPer:STATe](GP-IB_Command_Finder/System.md#beepStat) |  None  
System: Set limit test warning sound |  [SYSTem:BEEPer:WARNing:IMMediate](GP-IB_Command_Finder/System.md#SYSTem:BEEPer:WARNing:IMMediate) |  None  
System: Set sound after operation completion |  [SYSTem:BEEPer:COMPlete:IMMediate](GP-IB_Command_Finder/System.md#SYSTem:BEEPer:COMPlete:IMMediate) |  None  
System: On Power-on show Keys toolbar |  [SYSTem:PREFerences:ITEM:Keys](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:ITEM:KEYS) |  [ShowkeysToolbarAtPowerOn](COM_Reference/Properties/ShowKeysToolbarAtPowerOn.md)  
System: Use parallel processing |  [SYSTem:PREFerences:ITEM:CORRection:PARallel:PROCess](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:ITEM:CORRection:PARallel:PROCess) |  None  
System: Set front panel remote state when a SCPI command is received |  [SYSTem:PREFerences:ITEM:REMote:AUTO[:STATe]](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:ITEM:REMote:AUTO:STATe) |  None  
Ext Reference: Modify Settings on Preset and Recall |  [SYSTem:PREFerences:ITEM:ROSCillator:RECall](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:ITEM:ROSCillator:RECall) |  None  
More buttons  
Define Data Saves |  [See File Menu](FileTopic.md) |  [See File Menu](FileTopic.md)  
User Preset |  [See Preset](XUtilityTopic.md#User) |  [See Preset](XUtilityTopic.md#User)  
Printer Page Setup |  [Hardcopy](GP-IB_Command_Finder/Hardcopy.md) |  None  
Power Limit |  [See Power Limits](XStimulusTopic.md#Limits) |  [See Power Limits](XStimulusTopic.md#Limits)  
Display and Print Colors |  [See Display](XTraceChanTopic.md#DisplaySetup) |  [See Display](XTraceChanTopic.md#DisplaySetup)  
  
LXI  
---  
Returns Structured status of the VNA networking configuration. |  None |  [GetIPConfigurationStruct](COM_Reference/Methods/GetIPConfigurationStruct_Method.md)  
Returns string status of the VNA networking configuration. |  None |  [LANConfiguration](COM_Reference/Properties/LANConfiguration_Property.md)  
Resets the VNA LAN configuration. |  None |  [LANConfigurationInitialize](COM_Reference/Methods/LANConfigurationInitialize_Method.md)  
Modifies settings of the VNA computer networking configuration. |  None |  [SetIPConfiguration](COM_Reference/Methods/SetIPConfiguration_Method.md)  
Displays the LAN Status dialog with LAN Status Indicator showing IDENTIFY. |  [LXI:IDEN](GP-IB_Command_Finder/LXI.md) |  [LXIDeviceIDState](COM_Reference/Properties/LXIDeviceIDState_Property.md)  
  
Error Messages  
---  
Enable the display of Error Messages |  [DISPlay:ANNotation:MESSage:STATe](GP-IB_Command_Finder/Display.md#message) |  None  
Timed vs Dialog messages |  None |  None  
  
#### Millimeter-Wave Commands  
  
---  
![](../assets/images/N5291A_Config_Dialog.png) ![](../assets/images/mmWaveBandedDialog1.png) |  [SYSTem:CONFigure:MWAVe:CONF:ACTive](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:CONFiguration:ACTive) |  None  
[SYSTem:CONFigure:MWAVe:CONF:ADD](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:CONFiguration:ADD) |  None  
[SYSTem:CONFigure:MWAVe:CONF:CATalog?](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:CONFiguration:CATalog) |  None  
[SYSTem:CONFigure:MWAVe:CONF:REMove](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:CONFiguration:REMove) |  None  
[SYSTem:CONFigure:MWAVe:FREQuency:LO:MULTiplier](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:FREQuency:LO:MULTiplier) |  None  
[SYSTem:CONFigure:MWAVe:FREQuency:LO:SOURce](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:FREQuency:LO:SOURce) |  None  
[SYSTem:CONFigure:MWAVe:FREQuency:LO:STARt?](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:FREQuency:LO:STARt) |  None  
[SYSTem:CONFigure:MWAVe:FREQuency:LO:STOP?](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:FREQuency:LO:STOP) |  None  
[SYSTem:CONFigure:MWAVe:FREQuency:RF:MULTiplier](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:FREQuency:RF:MULTiplier) |  None  
[SYSTem:CONFigure:MWAVe:FREQuency:RF:SOURce](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:FREQuency:RF:SOURce) |  None  
[SYSTem:CONFigure:MWAVe:FREQuency:RF:STARt?](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:FREQuency:RF:STARt) |  None  
[SYSTem:CONFigure:MWAVe:FREQuency:RF:STOP?](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:FREQuency:RF:STOP) |  None  
[SYSTem:CONFigure:MWAVe:FREQuency:STARt](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:FREQuency:STARt) |  None  
[SYSTem:CONFigure:MWAVe:FREQuency:STOP](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:FREQuency:STOP) |  None  
[SYSTem:CONFigure:MWAVe:TSET:ALC](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:TSET:ALC) |  None  
[SYSTem:CONFigure:MWAVe:TSET:CATalog?](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:TSET:CATalog) |  None  
[SYSTem:CONFigure:MWAVe:TSET:MIXer](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:TSET:MIXer) |  None  
[SYSTem:CONFigure:MWAVe:TSET:NAME](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:TSET:NAME) |  None  
[SYSTem:CONFigure:MWAVe:TSET:PORT](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:TSET:PORT) |  None  
[SYSTem:CONFigure:MWAVe:TSET:POWer:LIMit](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:TSET:POWer:LIMit) |  None  
[SYSTem:CONFigure:MWAVe:TSET:POWer:OFFSet](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:TSET:POWer:OFFSet) |  None  
[SYSTem:CONFigure:MWAVe:TSET:POWer:SLOPe](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:TSET:POWer:SLOPe) |  None  
[SYSTem:CONFigure:MWAVe:TSET:RPANel](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:TSET:RPANel) |  None  
[SYSTem:CONFigure:MWAVe:CONF:ACTive:CALibration:DATE](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:CONF:ACTive:CALibration:DATE) |  None  
[SYSTem:CONFigure:MWAVe:CONF:ACTive:CALibration:TIME](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:CONF:ACTive:CALibration:TIME) |  None  
[SYSTem:CONFigure:MWAVe:TSET:PORT:COUNt?](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:TSET:PORT:COUNt) |  None  
[SYSTem:CONFigure:MWAVe:CONF:ACTive:MODel?](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:CONF:ACTive:MODel) |  None  
[SYSTem:CONFigure:MWAVe:CONF:ACTive:OPTion?](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:CONF:ACTive:OPTion) |  None  
[SYSTem:CONFigure:MWAVe:CONF:ACTive:PORT{1:4}:CALibration:DATE](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:CONF:ACTive:PORT:CALibration:DATE) |  None  
[SYSTem:CONFigure:MWAVe:CONF:ACTive:PORT{1:4}:CALibration:TIME](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:CONF:ACTive:PORT:CALibration:TIME) |  None  
[SYSTem:CONFigure:MWAVe:CONF:ACTive:PORT{1:4}:MODel?](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:CONF:ACTive:PORT:MODel) |  None  
[SYSTem:CONFigure:MWAVe:CONF:ACTive:PORT{1:4}:OPTion?](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:CONF:ACTive:PORT:OPTion) |  None  
[SYSTem:CONFigure:MWAVe:CONF:ACTive:PORT{1:4}:SERial?](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:CONF:ACTive:PORT:SERial) |  None  
[SYSTem:CONFigure:MWAVe:CONF:ACTive:SERial?](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:CONF:ACTive:SERial) |  None  
[SYSTem:CONFigure:MWAVe:SERial?](GP-IB_Command_Finder/SystConfig_mmWave.md#SYSTem:CONFigure:MWAVe:SERial) |  None  
  
* * *

