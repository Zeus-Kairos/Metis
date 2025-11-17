# System Commands

Main |  System  
Setup |  Print |  Help |  Service  
---|---|---|---|---  
  
Main Tab Commands  
---  
Softkey | Sub-item | SCPI |  COM  
Show Taskbar |  | None |  None  
Move App to Back |  | None |  None  
Minimize Application |  | None |  None  
Exit |  | None |  [app.Quit](COM_Reference/Methods/Quit_Method.md)  
Security... |  | [SYSTem:SECurity[:LEVel]](GP-IB_Command_Finder/System.md#Security) |  [app.SecurityLevel](COM_Reference/Properties/SecurityLevel_Property.md)  
Control Panel... |  | None |  None  
Manage Files... | List Files | [MMEMory:CATalog](GP-IB_Command_Finder/Memory.md#cat) |  None  
Copy Files | [MMEMory:COPY](GP-IB_Command_Finder/Memory.md#copy) |  None  
Move Files | [MMEMory:MOVE](GP-IB_Command_Finder/Memory.md#move) |  None  
Delete Files | [MMEMory:DELete](GP-IB_Command_Finder/Memory.md#del) |  None  
System Setup Tab Commands  
Softkey | Sub-item | SCPI |  COM  
Next/Prev Keys | Trace | None |  None  
Channel | None |  None  
Window | None |  None  
Sheet | None |  None  
Preferences... | Avg: On Preset set two-point Group Delay Aperture | [SYSTem:PREFerences:ITEM:GDELay:TWOPoint](GP-IB_Command_Finder/System_Preferences.md#groupDelay) |  [TwoPointGroupDelayAperture](COM_Reference/Properties/TwoPointGroupDelayAperture_Property.md)  
Avg: Calculate Group Delay using legacy PNA Math |  [SYSTem:PREFerences:ITEM:GDELay:LEGacy](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:ITEM:GDELay:LEGacy) |  [LegacyGroupDelayApertureMath](COM_Reference/Properties/LegacyGroupDelayApertureMath_Property.md)  
Cal: Always merge when saving Cal in Cal Set | None |  None  
Cal: Always use Internal trigger during cal | None |  None  
Cal: ECal Extrapolation for IMD | None |  None  
Cal: For Frequency Offset, use Primary frequencies | [SENSe:CORRection:PREFerences:CALibration[:FOM]:RANGe](GP-IB_Command_Finder/Sense/Sense_Correction.md#PrefCalFOM) |  [FrequencyOffsetRangeForCalComputations](COM_Reference/Properties/FrequencyOffsetRangeForCalComputations_Property.md)  
Cal: (SCPI only) Auto-generate a User Cal Set | [SENSe:CORRection:CSET:CREate](GP-IB_Command_Finder/Sense/CorrCset.md#create) |  [calMgr.CreateCalSet](COM_Reference/Methods/CreateCalSet_Method.md)  
Cal: (SCPI only) Auto-save to current Cal Set | [SENSe:CORRection:PREFerence:CSET:SAVE](GP-IB_Command_Finder/Sense/Sense_Correction.md#CsetSave) |  [RemoteCalStoragePreference](COM_Reference/Properties/RemoteCalStoragePreference_Property.md)  
Cal: Turn off RF Power after calibration | [SYSTem:PREFerence:ITEM:CALibration:SAFE[:STATe]](GP-IB_Command_Finder/System_Preferences.md#ItemCalSafeStat) | None  
Cal: Use legacy behavior for Series-C & Shunt-L fixtures |  [SYSTem:PREFerences:ITEM:FIXTure:CIRCuit:DEFAults](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:ITEM:FIXTure:CIRCuit:DEFAults) |  None  
Cal: Use Unknown thru math for SOLT methods | [SYSTem:PREFerence:ITEM:USOLt](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:ITEM:USOLt) |  None  
Display: Selected trace changes width briefly | None |  None  
Display: Selected trace is wider | None |  None  
Display: Touchscreen On | [SYSTem:TOUChscreen[:STATe]](GP-IB_Command_Finder/System.md#touchscreen) |  [Touchscreen](COM_Reference/Properties/Touchscreen_Property.md)  
Ext Device: De-activate on Preset and Recall | [SYSTem:PREFerences:ITEM:EDEV:DPOLicy](GP-IB_Command_Finder/System_Preferences.md#PrefEdevDpol) |  [ExternalDeviceDeActivatePolicy](COM_Reference/Properties/ExternalDeviceDeActivatePolicy_Property.md)  
Ext Reference: Modify Settings on Preset and Recall | [SYSTem:PREFerences:ITEM:ROSCillator:RECall](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:ITEM:ROSCillator:RECall) |  None  
Limit: Draw failed trace segments in red | [SYSTem:PREFerences:ITEM:RTOF](GP-IB_Command_Finder/System_Preferences.md#rtof) |  [RedTraceOnFail](COM_Reference/Properties/RedTraceOnFail_Property.md)  
Limit: Draw limit lines in red | [SYSTem:PREFerences:ITEM:REDLimits](GP-IB_Command_Finder/System_Preferences.md#Redlimits) |  [DrawLimitLinesInRed](COM_Reference/Properties/DrawLimitLinesInRed_Property.md)  
Limit: Test the nearest measurement point | None |  None  
Marker: Coupling controls on/off state of markers | [SYSTem:PREFerences:ITEM:MCControl](GP-IB_Command_Finder/System_Preferences.md#markerCouplControl) |  [MarkCoupControlsMkrState](COM_Reference/Properties/MarkCoupControlsMkrState_Property.md)  
Marker: On Preset, Coupled Markers is On | [SYSTem:PREFerences:ITEM:MCPreset](GP-IB_Command_Finder/System_Preferences.md#MarkerCouplPreset) |  [MarkCoupControlsMkrState](COM_Reference/Properties/MarkCoupControlsMkrState_Property.md)  
Marker: On Preset, Coupling Method is Channel | [SYSTem:PREFerences:ITEM:MCMethod](GP-IB_Command_Finder/System_Preferences.md#markerCoupleMethod) |  [MarkCoupMethPresetIsChan](COM_Reference/Properties/MarkCoupMethPresetIsChan_Property.md)  
Marker: On Preset, set BW/Notch search reference to Peak | [SYSTem:PREFerences:ITEM:MARKer:BANDwidth:SEARch](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:ITEM:MARKer:BANDwidth:SEARch) |  [BandwidthSearch](COM_Reference/Properties/BandwidthSearch_Property.md)  
Marker: Programming treats Mkr 10 as Reference | [SYSTem:PREFerences:ITEM:REFMarker](GP-IB_Command_Finder/System_Preferences.md#REFMarker) |  [TreatMkr10AsReference](COM_Reference/Properties/TreatMkr10AsReference_Property.md)  
Marker: Use single marker for marker search | [SYSTem:PREFerences:ITEM:MARKer:SINGle](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:ITEM:MARKer:SINGle) |  [SingleMarkerSearch](COM_Reference/Properties/SingleMarkerSearch_Property.md)  
Meas: Mathematical offset for receiver attenuation | [SYSTem:PREFerences:ITEM:OFFSet:RCV](GP-IB_Command_Finder/System_Preferences.md#prefRCV) |  [OffsetReceiverAttenuator](COM_Reference/Properties/OffsetReceiverAttenuator_Property.md)  
Meas: Mathematical offset for source attenuation | [SYSTem:PREFerences:ITEM:OFFSet:SRC](GP-IB_Command_Finder/System_Preferences.md#prefSRC) |  [OffsetSourceAttenuator](COM_Reference/Properties/OffsetSourceAttenuator_Property.md)  
Memory: Data Math 8510 Mode | None |  None  
Memory: Interpolate ON is default condition | [SYSTem:PREFerences:ITEM:MINTerpolate](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:ITEM:MINTerpolate) |  [InterpolateMemoryIsDefault](COM_Reference/Properties/InterpolateMemoryIsDefault_Property.md)  
Power: On Preset turn power off | [SYSTem:PREFerences:ITEM:PRESet:POWer](GP-IB_Command_Finder/System_Preferences.md#PowerState) |  [PresetPowerState](COM_Reference/Properties/PresetPowerState_Property.md)  
Power: On Preset turn power on | [SYSTem:PREFerences:ITEM:PRESet:POWer](GP-IB_Command_Finder/System_Preferences.md#PowerState) |  [PresetPowerState](COM_Reference/Properties/PresetPowerState_Property.md)  
Power: Report source unleveled events as errors | [SYSTem:ERRor:REPort:SUNLeveled](GP-IB_Command_Finder/System.md#unlevel) |  [EnableSourceUnleveledEvents](COM_Reference/Properties/EnableSourceUnleveledEvents_Property.md)  
Power: Report when receiver is overloaded | [SYSTem:PREFerences:ITEM:RECeivers:CERRor](GP-IB_Command_Finder/System_Preferences.md#RecError) |  [ReportReceiverOverload](COM_Reference/Properties/ReportReceiverOverload_Property.md)  
Power: Force RF power Off at the end of sweep | [SYSTem:PREFerences:ITEM:RETRace:POWer](GP-IB_Command_Finder/System_Preferences.md#freqRetrace) |  [PowerOnDuringRetraceMode](COM_Reference/Properties/PowerOnDuringRetraceMode_Property.md)  
Power: Turn Source Power Off when receiver is overloaded | [SYSTem:PREFerences:ITEM:RECeivers:OVERload:POWer](GP-IB_Command_Finder/System_Preferences.md#overloadOFF) |  [RFOffOnReceiverOverload](COM_Reference/Properties/RFOffOnReceiverOverload_Property.md)  
Power: Use Start Power during Power Sweep retrace | [SYSTem:PREFerences:ITEM:PSRTrace](GP-IB_Command_Finder/System_Preferences.md#pwrSwpRetrace) |  [PowerSweepRetracePowerMode](COM_Reference/Properties/PowerSweepRetracePowerMode_Property.md)  
Preset: Confirm preset | [SYSTem:PREFerences:ITEM:PRESet:CONFirm](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:ITEM:PRESet:CONFirm) |  [ConfirmPreset](COM_Reference/Properties/ConfirmPreset_Property.md)  
Preset: On Preset show Quick Start dialog | [SYSTem:PREFerences:ITEM:QSTart](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:ITEM:QSTart) |  [ShowQuickStartOnPreset](COM_Reference/Properties/ShowQuickStartOnPreset_Property.md)  
Recall: Softkey order is most recently used | None |  None  
Scale: On Preset Couple Scale to Window | None |  None  
Sweep: On Preset set Sweep Mode to Stepped | None |  None  
Sweep: Use only ramp sweeps for Auto Sweep Mode | [SYSTem:PREFerences:ITEM:ASMRamp](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:ITEM:ASMRamp) |  None  
System: Enable sound | [SYSTem:BEEP:STATe](GP-IB_Command_Finder/System.md#beepStat) |  None  
System: On Power-on show dialog if detect mm testset | None |  None  
System: On Power-on show Keys toolbar | [SYSTem:PREFerences:ITEM:Keys](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:ITEM:KEYS) |  [ShowkeysToolbarAtPowerOn](COM_Reference/Properties/ShowKeysToolbarAtPowerOn.md)  
System: Use keyboard to navigate softkeys | [SYSTem:PREFerences:ITEM:SOFTkeys:NAVigation](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:ITEM:SOFTkeys:NAVigation) |  None  
System: Use parallel processing |  [SYSTem:PREFerences:ITEM:CORRection:PARallel:PROCess](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:ITEM:CORRection:PARallel:PROCess) |  None  
System: Set front panel remote state when a SCPI command is received | [SYSTem:PREFerences:ITEM:REMote:AUTO[:STATe]](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:ITEM:REMote:AUTO:STATe) |  None  
Trigger: External Trigger Out is Global | [TRIGger:PREFerences:AIGLobal](GP-IB_Command_Finder/Trigger_SCPI.md#PrefGlobal) |  [AuxTriggerScopeIsGlobal](COM_Reference/Properties/AuxTriggerScopeIsGlobal_Property.md)  
Data Saves... | [MMEMory:STORe:DATA](GP-IB_Command_Finder/Memory.md#StoreData) |  [SaveData](COM_Reference/Methods/SaveData_Method.md)  
Power Limit... | [SYSTem:POWer:LIMit](GP-IB_Command_Finder/System.md#powerLimit) |  [Limit](COM_Reference/Properties/Limit_Property.md)  
Transparency... | None |  None  
User Preset... | [SYSTem:UPReset](GP-IB_Command_Finder/System.md#UPreset) |  [UserPreset](COM_Reference/Methods/UserPreset_Method.md)  
Page Setup... | [Hardcopy](GP-IB_Command_Finder/Hardcopy.md) |  None  
Disp Colors... | [See Display](CF_Display_Commands.md) |  [See Display](CF_Display_Commands.md)  
Print Colors... | [See Display](CF_Display_Commands.md) | [See Display](CF_Display_Commands.md)  
Global Sources...  
Power On (All Channels) |  None |  None  
Global Sources Ignore "Power ON" Setting |  [SYSTem:PREFerences:SOURce:GLOBal:POFF:IGNore[:STATe]](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:SOURce:GLOBal:POFF:IGNore:STATe) |  None  
Global |  [SYSTem:PREFerences:SOURce:GLOBal[:STATe]](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:SOURce:GLOBal:STATe) |  None  
State |  [SYSTem:PREFerences:SOURce:GLOBal:OUTPut[:STATe]](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:SOURce:GLOBal:OUTPut:STATe) |  None  
Frequency |  [SYSTem:PREFerences:SOURce:GLOBal:FREQuency](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:SOURce:GLOBal:FREQuency) |  None  
Power |  [SYSTem:PREFerences:SOURce:GLOBal:POWer](GP-IB_Command_Finder/System_Preferences.md#SYSTem:PREFerences:SOURce:GLOBal:POWer) |  None  
Sound |  |  |  None  
Remote Interface... | GPIB Address | None |  [app.GPIBAddress](COM_Reference/Properties/GPIBAddress_Property.md)  
SICL Enabled | None |  [app.SICL](COM_Reference/Properties/SICL_Property.md)  
SICL Address | None |  [app.SICLAddress](COM_Reference/Properties/SICLAddress_Property.md)  
Automatically Enable on Startup | None |  None  
Sockets Enabled | None |  None  
Telnet Enabled | None |  None  
HiSLIP Enabled | None |  [HiSLIPPort](COM_Reference/Properties/HiSLIPPort_Property.md)  
HiSLIP Address | None |  [HiSLIPAddress](COM_Reference/Properties/HiSLIPAddress_Property.md)  
Enable Remote Drive Access | [SYSTem:COMMunicate:DRIVe:ENABle?](GP-IB_Command_Finder/SystCommunicate.md#SYSTem:COMMunicate:DRIVe:ENABle) |  None  
Show SCPI Parser Console | None |  None  
Monitor GPIB Bus | None |  None  
|  |  |  [LANConfigurationInitialize](COM_Reference/Methods/LANConfigurationInitialize_Method.md)  
|  |  |  None  
Print Tab Commands  
Softkey | Sub-item | SCPI |  COM  
Print... |  | [HCOPy:DPRinter](GP-IB_Command_Finder/Hardcopy.md#dPrinter) |  [DoPrint](COM_Reference/Methods/Do_Print_Method.md)  
Print to File... |  | [HCOPy:FILE](GP-IB_Command_Finder/Hardcopy.md#file) |  [PrintToFile](COM_Reference/Methods/PrintToFile_Method.md)  
Page Setup... |  | [Hardcopy](GP-IB_Command_Finder/Hardcopy.md) |  None  
Print Colors... | Pen  
Background | [DISPlay:COLor:BACKground](GP-IB_Command_Finder/Display_Colors.md#back) |  [Background](COM_Reference/Properties/Background_Property.md)  
Active Background | [DISPlay:COLor:ABACkground](GP-IB_Command_Finder/Display_Colors.md#ActiveBack) |  [ActiveBackground](COM_Reference/Properties/ActiveBackground_Property.md)  
Grid | [DISPlay:COLor:GRAT2](GP-IB_Command_Finder/Display_Colors.md#grat2) |  [Grid](COM_Reference/Properties/Grid_Property.md)  
Active Labels, Grid frame | [DISPlay:COLor:GRAT1](GP-IB_Command_Finder/Display_Colors.md#grat1) |  [ActiveLabels](COM_Reference/Properties/ActiveLabels_Property.md)  
Inactive Window Labels | [DISPlay:COLor:ILABel](GP-IB_Command_Finder/Display_Colors.md#inLabel) |  [InactiveLabels](COM_Reference/Properties/InactiveLabels_Property.md)  
Failed Trace | [DISPlay:COLor:LIM1](GP-IB_Command_Finder/Display_Colors.md#limit) |  [FailedTraces](COM_Reference/Properties/FailedTraces_Property.md)  
N Trace: Data and Limits | [DISPlay:COLor:TRACe:DATA](GP-IB_Command_Finder/Display_Colors.md#traceData) |  [DataAndLimits](COM_Reference/Properties/DataAndLimits_Property.md)  
N Trace: Memory | [DISPlay:COLor:TRACe:MEMory](GP-IB_Command_Finder/Display_Colors.md#memory) |  [Memory](COM_Reference/Properties/Memory_Property.md)  
N Trace: Markers | [DISPlay:COLor:TRACe:MARKer](GP-IB_Command_Finder/Display_Colors.md#marker) |  [Markers](COM_Reference/Properties/Markers_Property.md)  
N Trace: Memory Markers | [DISPlay:COLor:TRACe:MMARker](GP-IB_Command_Finder/Display_Colors.md#mmarker) |  [MemoryMarkers](COM_Reference/Properties/MemoryMarkers_Property.md)  
Change Color... | None |  None  
Reset Color | [DISPlay:COLor:RESet](GP-IB_Command_Finder/Display_Colors.md#reset) |  None  
Color Theme  
Save Theme... | [DISPlay:COLor:STORe](GP-IB_Command_Finder/Display_Colors.md#store) |  [StoreTheme](COM_Reference/Methods/StoreTheme_Method.md)  
Recall Theme... | [DISPlay:COLor:LOAD](GP-IB_Command_Finder/Display_Colors.md#load) |  [LoadTheme](COM_Reference/Methods/LoadTheme_Method.md)  
Reset Theme | [DISPlay:COLor:RESet](GP-IB_Command_Finder/Display_Colors.md#reset) |  [ResetTheme](COM_Reference/Methods/ResetTheme_Method.md)  
Help Tab Commands  
Softkey | Sub-item | SCPI |  COM  
NA Help... |  | None |  None  
On The Web... |  | None |  None  
Error Display... | Enable Messages | [DISPlay:ANNotation:MESSage:STATe](GP-IB_Command_Finder/Display.md#message) |  None  
Status bar Display | [DISPlay:ANNotation[:STATus]](GP-IB_Command_Finder/Display.md#annstatus) |  [app.ShowStatusBar](COM_Reference/Methods/Show_Status_Bar_Method.md)  
Confirmation Dialog boxes | None |  None  
View Error Log... |  | None |  None  
Tech Support |  PathWave Calibration Advisor Commands |  [SYSTem:CAPability:LICenses:FEATure:CATalog?](GP-IB_Command_Finder/SystCapability.md#SYSTem:CAPability:LICenses:FEATure:CATalog) [SYSTem:CAPability:LICenses:FEATure:ENABle?](GP-IB_Command_Finder/SystCapability.md#SYSTem:CAPability:LICenses:FEATure:ENABle) [SYSTem:SERVice:MANagement:CALibration:INFormation?](GP-IB_Command_Finder/System_Service_SCPI.md#SYSTem:SERVice:MANagement:CALibration:INFormation) [SYSTem:SERVice:MANagement:CALibration:INTerval:DEFault](GP-IB_Command_Finder/System_Service_SCPI.md#SYSTem:SERVice:MANagement:CALibration:INTerval:DEFault) [SYSTem:SERVice:MANagement:CALibration:INTerval:TYPE?](GP-IB_Command_Finder/System_Service_SCPI.md#SYSTem:SERVice:MANagement:CALibration:INTerval:TYPE) [SYSTem:SERVice:MANagement:CALibration:INTerval[:VALue]](GP-IB_Command_Finder/System_Service_SCPI.md#SYSTem:SERVice:MANagement:CALibration:INTerval_:VALue) [SYSTem:SERVice:MANagement:CALibration:NOTification:ENABle](GP-IB_Command_Finder/System_Service_SCPI.md#SYSTem:SERVice:MANagement:CALibration:NOTification:ENABle) [SYSTem:SERVice:MANagement:CALibration:PASScode:CHANge](GP-IB_Command_Finder/System_Service_SCPI.md#SYSTem:SERVice:MANagement:CALibration:PASScode:CHANge) [SYSTem:SERVice:MANagement:CALibration:PASScode[:VALue]](GP-IB_Command_Finder/System_Service_SCPI.md#SYSTem:SERVice:MANagement:CALibration:PASScode:VALue) [SYSTem:SERVice:MANagement:CALibration:PERiodic:ENABle](GP-IB_Command_Finder/System_Service_SCPI.md#SYSTem:SERVice:MANagement:CALibration:PERiodic:ENABle) [SYSTem:SERVice:MANagement:CALibration:REMinder](GP-IB_Command_Finder/System_Service_SCPI.md#SYSTem:SERVice:MANagement:CALibration:REMinder) |  None None None None None None None None None None None  
About NA... |  | None |  None  
Service Tab Commands  
Softkey | Sub-item | SCPI |  COM  
Update Firmware |  |  None |  None  
Verification |  | None |  None  
Adjustment Routines... |  | None |  None  
Diagnostics |  | None |  None  
Option Enable |  | None |  None

