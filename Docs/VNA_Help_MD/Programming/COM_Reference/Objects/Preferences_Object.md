# Preferences Object

* * *

### Description

Sets the preferences for the behavior of several properties.

### Accessing the Preferences object

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim pref As Preferences  
Set pref = app.Preferences

### See Also:

  * [VNA Preferences](../../../System/Preferences.md)

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

(Bold Methods or Properties provide access to a child object)

### Methods

|  | 

###  
  
---|---|---  
[RestoreDefaults](../Methods/RestoreDefaults_Method.md) | IPreferences9 | Restores preference settings to their factory defaults.  
  
### Properties

|

### Interface

[See History](Preferences_Object.md#history) | 

### Description  
  
[AuxTriggerScopeIsGlobal](../Properties/AuxTriggerScopeIsGlobal_Property.md) | IPreferences5 | Sets the External Trigger OUT behavior to have either Global or Channel scope.  
[BandwidthSearch](../Properties/BandwidthSearch_Property.md) | IPreferences18 | Sets the bandwidth search preference to start a bandwidth or notch search in either peak or marker mode.  
[CitiContents](../Properties/CitiContents_Property.md) | IPreferences | Specifies the contents of subsequent citifile saves. Superseded with [SaveData](../Methods/SaveData_Method.md)  
[CitiFormat](../Properties/CitiFormat_Property.md) | IPreferences | Specifies the format of subsequent citifile saves. Superseded with [SaveData](../Methods/SaveData_Method.md)  
[ConfirmPreset](../Properties/ConfirmPreset_Property.md) | IPreferences18 | Set and return preset confirmation.  
[DisplayColors](ComColors_Object.md) | IPreferences10 | Provides access to the [ComColors](ComColors_Object.md) Object.  
[EnableSourceUnleveledEvents](../Properties/EnableSourceUnleveledEvents_Property.md) | IPreferences6 | Specifies whether or not to report Source Unleveled errors as system events.  
[ExternalDeviceDeActivatePolicy](../Properties/ExternalDeviceDeActivatePolicy_Property.md) | IPreferences10 | External Devices remain activated or are de-activated when the VNA is Preset or when a Instrument State is recalled.  
[FrequencyOffsetRangeForCalComputations](../Properties/FrequencyOffsetRangeForCalComputations_Property.md) | IPreferences10 | Specifies the FOM frequency range to use when performing calibration.  
[IMDECalExtrapolation](../Properties/IMDECalExtrapolation_Property.md) | IPreferences14 | Allow ECal beyond stop frequency for IMD apps.  
[InterpolateMemoryIsDefault](../Properties/InterpolateMemoryIsDefault_Property.md) | IPreferences17 | Sets and reads the state of the memory data interpolation default preference.  
[LegacyGroupDelayApertureMath](../Properties/LegacyGroupDelayApertureMath_Property.md) | IPreferences19 | Sets the group delay aperture to use the legacy computation method.  
[MarkCoupControlsMkrState](../Properties/MarkCoupControlsMkrState_Property.md) | IPreferences15 | Coupled Marker controls marker state.  
[MarkCoupMethPresetIsChan](../Properties/MarkCoupMethPresetIsChan_Property.md) | IPreferences15 | Coupled Marker state at Preset.  
[MarkCoupPresetIsOn](../Properties/MarkCoupPresetIsOn_Property.md) | IPreferences15 | Coupled Marker Method at Preset.  
[OffsetReceiverAttenuator](../Properties/OffsetReceiverAttenuator_Property.md) | IPreferences6 | Mathematically offset the test port receiver.  
[OffsetSourceAttenuator](../Properties/OffsetSourceAttenuator_Property.md) | IPreferences6 | Mathematically offset the reference receiver.  
[Port1NoiseTunerSwitchPresetsToExternal](../Properties/Port1NoiseTunerSwitchPresetsToExternal_Property.md) | IPreferences8 | Sets default setting for Noise Figure switch.  
[PowerOnDuringRetraceMode](../Properties/PowerOnDuringRetraceMode_Property.md) | IPreferences4 | Specify whether to turn RF power ON or OFF during a retrace for single-band frequency or segment sweeps ONLY.  
[PowerSweepRetracePowerMode](../Properties/PowerSweepRetracePowerMode_Property.md) | IPreferences3 | At the end of a power sweep, specifies whether to maintain source power at the start or stop power level.  
[PreferInternalTriggerOnChannelSingle](../Properties/PreferInternalTriggerOnChannelSingle_Property.md) | IPreferences2 | Sets the preference for chan.Single behavior.  
[PreferInternalTriggerOnUnguidedCal](../Properties/PreferInternalTriggerOnUnguidedCal_Property.md) | IPreferences2 | Set the preference for the trigger behavior when performing an Unguided calibration.  
[PrefSourcePowerCalFromCalset](../Properties/PreferSourcePowerCalFromCalset_Property.md) | IPreferences | Enable or disable source power cal in the calset.  
[PresetPowerState](../Properties/PresetPowerState_Property.md) | IPreferences11 | Set and return the Preset Power ON/OFF state.  
[PrintColors](ComColors_Object.md) | IPreferences10 | Provides access to the [ComColors](ComColors_Object.md) Object.  
[RecallSoftkeysMostRecent](../Properties/RecallSoftkeysMostRecent_Property.md) | IPreferences13 | List files for recall on softkeys by name or alphabetically.  
[RemoteCalStoragePreference](../Properties/RemoteCalStoragePreference_Property.md) | IPreferences7 | Specifies the default manner in which calibrations performed via SCPI or COM are to be stored.  
[ReportReceiverOverload](../Properties/ReportReceiverOverload_Property.md) | IPreferences12 | Set whether to display receiver overload warnings.  
[RFOffOnReceiverOverload](../Properties/RFOffOnReceiverOverload_Property.md) | IPreferences12 | Set whether to turn source power OFF when a receiver is overloaded.  
[ShowKeysToolbarAtPowerOn](../Properties/ShowKeysToolbarAtPowerOn.md) | IPreferences16 | Show Keys toolbar at power on.  
[ShowQuickStartOnPreset](../Properties/ShowQuickStartOnPreset_Property.md) | IPreferences13 | Show Quick Start dialog on PRESET.  
[SingleMarkerSearch](../Properties/SingleMarkerSearch_Property.md) | IPreferences18 | Set and return whether to use one marker for marker search.  
[SnPFormat](../Properties/SnPFormat_Property.md) | IPreferences | Specifies the format of subsequent .S1P, .S2P, .S3P file saves.  
[TreatMkr10AsReference](../Properties/TreatMkr10AsReference_Property.md) | IPreferences15 | Sets and returns the reference marker preference.  
[TwoPointGroupDelayAperture](../Properties/TwoPointGroupDelayAperture_Property.md) | IPreferences11 | Sets Group Delay Aperture default to 2 points.  
  
###  IPreferences History

Interface | Introduced with VNA Rev:  
---|---  
IPreferences | 4.0  
IPreferences2 | 6.0  
IPreferences3 | 7.2  
IPreferences4 | 6.04  
IPreferences5 | 7.10  
IPreferences6 | 7.20  
IPreferences7 | 7.21  
IPreferences8 | 8.0  
IPreferences9 | 8.2  
IPreferences10 | 9.0  
IPreferences11 | 9.20  
IPreferences12 | 9.30  
IPreferences13 | 9.50  
IPreferences14 | 10.0  
IPreferences15 | 10.40  
IPreferences16 | 10.49  
IPreferences17 | 10.49  
IPreferences18 | 12.70  
IPreferences19 | 13.80

