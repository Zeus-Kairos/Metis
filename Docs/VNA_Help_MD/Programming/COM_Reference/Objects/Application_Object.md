# Application Object

* * *

Description

The Application object is the highest object in the VNA [object
model](The_Analyzer_Object_Model.htm). This object presents methods and
properties that affect the entire analyzer, rather than a specific channel or
measurement. For example, the application object provides the GetIDString
method. There's only one ID string for the instrument, unrelated to the
channel or parameter being measured. Likewise, the TriggerSignal Property is
global to the instrument. You can elect to use an internally generated (free
run) trigger or a manual trigger. Either way, that type of trigger generation
will be used on all measurements, on all channels. Therefore, it is under the
Application object.

### Accessing the Application object

This object is unique in that you must create this object rather than just get
a handle to it.

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)

Replace <analyzerName> with the full computer name of your VNA. For example,
"My VNA". See [Change Computer
Name](../../../S0_Start/ComputerProperties.htm).

### See Also:

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Getting a Handle to an Object](../../Learning_about_COM/Getting_a_Handle_to_an_Object.md).

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

  * [Superseded commands](../../Replacement_Commands.md)

(Bold Methods or Properties provide access to a child object)

### Methods

|

### Interface

[See History](Application_Object.md#Interface) | 

### Description  
  
---|---|---  
[ActivateWindow](../Methods/ActivateWindow_Method.md) |  IApplication |  Makes a window object the Active Window.  
[AllowAllEvents](../Methods/AllowAllEvents_Method.md) |  IApplication |  Monitors all events  
[AllowEventCategory](../Methods/AllowEventCategory_Method.md) |  IApplication |  Monitors an event category  
[AllowEventMessage](../Methods/AllowEventMessage_Method.md) |  IApplication |  Monitors an event  
[AllowEventSeverity](../Methods/AllowEventSeverity_Method.md) |  IApplication |  Monitors an event severity level  
[BuildHybridKit](../Methods/Build_Hybrid_Kit_Method.md) |  IApplication |  Defines the user kit as port1kit + port2kit.  
[Channel](Channel_Object.md) |  IApplication |  Returns a handle to the channel object for the supplied channel number.  
[Configure](../Methods/Configure_Method.md) |  IApplication9 |  Restarts as an "N-port" VNA using the specified multiport test set.  
[CreateCustomMeasurementEx](../Methods/CreateCustomMeasurementEx_Method.md) |  IApplication3 |  Creates a new custom measurement with initialization.  
[CreateCustomMeasurement](../Methods/CreateCustomMeasurement_Method.md) |  IApplication |  Superseded with [CreateCustomMeasurementEx Method](../Methods/CreateCustomMeasurementEx_Method.md)  
[CreateMeasurement](../Methods/CreateMeasurement_Method.md) |  IApplication |  Creates a new measurement.  
[CreateSParameter](../Methods/Create_SParameter_Method.md) |  IApplication |  Creates a new S-Parameter measurement.  
[CreateSParameterEx](../Methods/Create_SParameterEX_Method.md) |  IApplication |  Superseded with [Create SParameter Method](../Methods/Create_SParameter_Method.md)  
[DeleteShortCut](../Methods/DeleteShortCut_Method.md) |  IApplication |  Removes a macro (shortcut) from the list of macros  
[DisallowAllEvents](../Methods/DisallowAllEvents_Method.md) |  IApplication |  Monitors NO events  
[DoPrint](../Methods/Do_Print_Method.md) |  IApplication |  Prints the screen to the active Printer.  
[ExecuteShortcut](../Methods/Execute_Shortcut_Method.md) |  IApplication |  Executes a macro (shortcut) stored in the analyzer.  
[GetAuxIO](../Methods/Get_AuxIO_Method.md) |  IApplication |  Returns a handle to the AuxIO interface  
[GetCalManager](../Methods/Get_CalManager_Method.md) |  IApplication |  Returns a handle to the CalManager interface  
[GetExternalTestSetIO](../Methods/Get_ExternalTestSetIO_Method.md) |  IApplication |  Returns a handle to the ExternalTestSet IO interface  
[GetIPConfigurationStruct](../Methods/GetIPConfigurationStruct_Method.md) |  IApplication14 |  Returns an NA_IPConfiguration data structure which contains information about the current status of the VNA computer networking configuration.  
[GetLicenses](../Methods/Licenses_Property.md) |  IApplication23 |  Returns the list of licenses.  
[GetMaterialHandlerIO](../Methods/Get_MaterialHandlerIO_Method.md) |  IApplication |  Returns a handle to the MaterialHandlerIO interface  
[GetShortcut](../Methods/Get_Shortcut_Method.md) |  IApplication |  Returns the title and path of the specified macro (shortcut).  
[LANConfigurationInitialize](../Methods/LANConfigurationInitialize_Method.md) |  IApplication13 |  Resets the VNA LAN configuration.  
[LaunchCalWizard](../Methods/LaunchCalWizard_Method.md) |  IApplication |  Launches the Cal Wizard  
[LaunchDialog](../Methods/LaunchDialog_Method.md) |  IApplication10 |  Launches the specified dialog box.  
[ManualTrigger](../Methods/Manual_Trigger_Method.md) |  IApplication |  Triggers the analyzer when TriggerSignal = naTriggerManual.  
[Preset](../Methods/Preset_Method.md) |  IApplication |  Resets the analyzer to factory defined default settings.  
[PrintToFile](../Methods/PrintToFile_Method.md) |  IApplication |  Saves the screen data to bitmap (.bmp) file of the screen.  
[PutShortcut](../Methods/Put_Shortcut_Method.md) |  IApplication |  Puts a Macro (shortcut) file into the analyzer.  
[Quit](../Methods/Quit_Method.md) |  IApplication |  Ends the Network Analyzer application.  
[Recall](../Methods/Recall_Method.md) |  IApplication |  Recalls a measurement state, calibration state, or both from the hard drive into the analyzer.  
[RecallKits](../Methods/Recall_Kits_Method.md) |  IApplication |  Recalls the calibration kits definitions that were stored with the SaveKits command.  
[Reset](../Methods/Reset_Method.md) |  IApplication |  Removes all existing windows and measurements.  
[RestoreCalKitDefaults](../Methods/Restore_Cal_Kit_Defaults_Method.md) |  IApplication |  Restores the factory defaults for the specified kit.  
[RestoreCalKitDefaultsAll](../Methods/Restore_Cal_Kit_Defaults_All_Method.md) |  IApplication |  Restores the factory defaults for all kits.  
[Save](../Methods/Save_Method.md) |  IApplication |  Saves instrument state and calibration files to disk  
[SaveCitiDataData](../Methods/SaveCitiDataData_Method.md) |  IApplication5 |  Saves UNFORMATTED trace data to .cti file. Superseded with [SaveData](../Methods/SaveData_Method.md)  
[SaveCitiFormattedData](../Methods/SaveCitiFormattedData_Method.md) |  IApplication5 |  Saves FORMATTED trace data to .cti file. Superseded with [SaveData](../Methods/SaveData_Method.md)  
[SaveData](../Methods/SaveData_Method.md) |  IApplication18 |  Saves trace data to files on disk.  
[SaveKits](../Methods/Save_Kits_Method.md) |  IApplication |  Saves all cal kits to disk.  
[SetFailOnOverRange](../Methods/SetFailOnOverRange_Method.md) |  IApplication |  Causes over range values to return an error code  
[SetIPConfiguration](../Methods/SetIPConfiguration_Method.md) |  IApplication14 |  Modifies settings of the VNAs computer networking configuration.  
[ShowStatusBar](../Methods/Show_Status_Bar_Method.md) |  IApplication |  Shows and Hides the Status Bar.  
[ShowStimulus](../Methods/Show_Stimulus_Method.md) |  IApplication |  Shows and Hides Stimulus information.  
[ShowTitleBars](../Methods/Show_Title_Bars_Method.md) |  IApplication |  Shows and Hides the Title Bars.  
[ShowToolbar](../Methods/Show_Toolbar_Method.md) |  IApplication |  Shows and Hides the specified Toolbar.  
[UserPreset](../Methods/UserPreset_Method.md) |  IApplication7 |  Performs a User Preset.  
[UserPresetLoadFile](../Methods/UserPresetLoadFile_Method.md) |  IApplication7 |  Loads an existing instrument state file (.sta or .cst) to be used for User Preset.  
[UserPresetSaveState](../Methods/UserPresetSaveState_Method.md) |  IApplication7 |  Saves the current instrument settings as UserPreset.sta.  
  
### Properties

|

###

|

### Description  
  
[ActiveCalKit](../Properties/Active_Cal_Kit_Property.md) |  IApplication |  Returns a pointer to the kit identified by kitNumber.  
[ActiveChannel](../Properties/Active_Channel_Property.md) |  IApplication |  Returns a handle to the Active Channel object.  
[ActiveMeasurement](../Properties/Active_Measurement_Property.md) |  IApplication |  Returns a handle to the Active Measurement object.  
[ActiveNAWindow](../Properties/Active_NAWindow_Property.md) |  IApplication |  Returns a handle to the Active Window object.  
[ArrangeWindows](../Properties/Arrange_Windows_Property.md) |  IApplication |  Sets or returns the arrangement of all the windows.  
[AuxiliaryTriggerCount](../Properties/AuxiliaryTriggerCount_Property.md) |  IApplication11 |  Returns the number of Aux trigger input / output connector pairs in the instrument.  
[CalKitType](../Properties/CalKitType_Property.md) |  IApplication |  Sets or returns the calibration kit type for to be used for calibration or for kit modification. Shared with the CalKit object.  
[Capabilities](Capabilities_Object.md) |  IApplication4 |  Return capabilities of the remote VNA.  
[Channels](Channels_Collection.md) |  IApplication |  Collection for iterating through the channels  
[CoupledMarkers](../Properties/CoupledMarkers_Property.md) |  IApplication |  Sets (or reads) coupled markers ON and OFF  
[CoupledMarkersMethod](../Properties/CoupledMarkersMethod_Property.md) |  IApplication20 |  Set and reads the scope of coupled markers.  
[DateTime](../Properties/DateTime_Property.md) |  IApplication22 |  Returns the system date and time.  
[DisplayAutomationErrors](../Properties/DisplayAutomationErrors.md) |  IApplication2 |  Enables or disables automation error messages from being displayed on the screen. U  
[DisplayGlobalPassFail](../Properties/DisplayGlobalPassFail_Property.md) |  IApplication6 |  Shows or hides the dialog which displays global pass/fail results.  
[E5091Testsets](E5091Testset_Collection.md) |  IApplication8 |  Collection to control the E5091A testset.  
[ENRFile](ENRFile_Object.md) |  IApplication13 |  Manages Noise ENR files.  
[ExternalALC](../Properties/External_ALC_Property.md) |  IApplication |  Sets or returns the source of the analyzer leveling control.  
[ExternalDevices](ExternalDevices_Collection.md) |  IApplication16 |  Collection to control External Devices  
[ExternalTestsets](ExternalTestsets_Collection.md) |  IApplication9 |  Collection to control External Test sets.  
[FIFO](FIFO_Object.md) |  IApplication15 |  Controls FIFO settings  
[GlobalPowerLimit](GlobalPowerLimit_Object.md) |  IApplication17 |  Controls Global Power Limit settings  
[GPIBAddress](../Properties/GPIBAddress_Property.md) |  IApplication8 |  Sets and returns the VNA GPIB address.  
[GPIBMode](../Properties/GPIBMode_Property.md) |  IApplication |  Makes the analyzer the system controller or a talker/listener.  
[GridLineType](../Properties/GridLineType_Property.md) |  IApplication17 |  Set and return the line type of the window grid (solid | dotted)  
[IDString](../Properties/IDString_Property.md) |  IApplication |  Returns the model, serial number and software revision of the analyzer  
[InterfaceControl](InterfaceControl_Object.md) |  IApplication8 |  Control the Interface control features.  
[IOConfiguration](IOConfiguration_Object.md) |  IApplication19 |  Provides access to IO Configuration commands  
[LANConfiguration](../Properties/LANConfiguration_Property.md) |  IApplication13 |  Returns the current status of the VNA computer networking configuration.  
[LXIDeviceIDState](../Properties/LXIDeviceIDState_Property.md) |  IApplication14 |  Displays the LAN Status dialog with LAN Status Indicator showing IDENTIFY.  
[LocalLockoutState](../Properties/LocalLockoutState_Property.md) |  IApplication4 |  Prevents use of the mouse, keyboard, and front panel while your program is running.  
[Measurement](Measurement_Object.md) |  IApplication |  Create and manage measurements  
[Measurements](Measurements_Collection.md) |  IApplication |  Collection for iterating through the Application measurements.  
[MessageText](../Properties/Message_Text_Method.md) |  IApplication |  Returns text for the specified eventID  
[NaWindows](NAWindows_Collection.md) |  IApplication |  Collection for iterating through the Application windows.  
[NoiseSourceState](../Properties/NoiseSourceState_Property.md) |  IApplication13 |  Sets and Reads the ON | OFF state of the noise source  
[NumberOfPorts](../Properties/NumberOfPorts_Property.md) |  IApplication |  Returns the number of hardware test ports on the VNA  
[Options](../Properties/Options_Property.md) |  IApplication |  Returns the options on the analyzer  
[PathConfigurationManager](PathConfigurationManager_Object.md) |  IApplication11 |  Provides access to hardware configuration.  
[Port Extensions](Port_Extension_Object.md) |  IApplication |  Superseded with [Fixturing Object](Fixturing_Object.md)  
[Preferences](Preferences_Object.md) |  IApplication5 |  Preferences for many VNA settings..  
[ScpiStringParser](SCPIStringParser_Object.md) |  IApplication |  Provides the ability to send a SCPI command from within the COM command.  
[SecurityLevel](../Properties/SecurityLevel_Property.md) |  IApplication4 |  Turns ON or OFF the display of frequency information.  
[SICL](../Properties/SICL_Property.md) |  IApplication5 |  Allows control of the VNA via SICL  
[SICLAddress](../Properties/SICLAddress_Property.md) |  IApplication8 |  Sets and returns the VNA SICL address  
[SourcePowerCalibrator](SourcePowerCalibrator_Object.md) |  IApplication2 |  Allows capability for performing source power calibrations.  
[SourcePowerState](../Properties/Source_Power_State_Property.md) |  IApplication |  Turns Source Power ON and OFF.  
[SystemImpedanceZ0](../Properties/SystemImpedanceZ0_Property.md) |  IApplication |  Sets the analyzer impedance value.  
[SystemName](../Properties/SystemName_Property.md) |  IApplication |  Returns the full computer name of the VNA.  
[Touchscreen](../Properties/Touchscreen_Property.md) |  IApplication12 |  Enables and disables touchscreen.  
[TriggerDelay](../Properties/TriggerDelay_Property.md) |  IApplication |  Sets or returns the delay time for a trigger.  
[TriggerSetup](TriggerSetup_Object.md) |  IApplication4 |  Controls triggering for the entire VNA application.  
[TriggerSignal](../Properties/Trigger_Signal_Property.md) |  IApplication |  Superseded with [Source Property](../Properties/Source_Property.md)  
[TriggerType](../Properties/Trigger_Type_Property.md) |  IApplication |  Superseded with [Scope Property](../Properties/Scope_Property.md)  
[UncertaintyManager](UncertaintyManager_Object.md) |  IApplication20 |  Returns a handle to the (Dynamic) Uncertainty Manager application.  
[UserPresetEnable](../Properties/UserPresetEnable_Property.md) |  IApplication7 |  'Checks' and 'clears' the enable box on the User Preset dialog box.  
[VelocityFactor](../Properties/Velocity_Factor_Property.md) |  IApplication |  Sets the velocity factor to be used with Electrical Delay, Port Extensions, and Time Domain marker distance calculations.  
[Visible](../Properties/Visible_Property.md) |  IApplication |  Makes the Network Analyzer application visible or not visible.  
[WindowState](../Properties/Window_State_Property.md) |  IApplication |  Sets or returns the window setting of Maximized, Minimized, or Normal. Shared with the NAWindow Object  
  
### Events

|

### Interface

|

### Description  
  
[OnCalEvent](../Events/OnCalEvent.md) |  IApplication |  Triggered by a calibration event.  
[OnChannelEvent](../Events/OnChannelEvent.md) |  IApplication |  Triggered by a channel event.  
[OnDisplayEvent](../Events/OnDisplayEvent.md) |  IApplication |  Triggered by a display event.  
[OnHardwareEvent](../Events/OnHardwareEvent.md) |  IApplication |  Triggered by a hardware event.  
[OnMeasurementEvent](../Events/OnMeasurementEvent.md) |  IApplication |  Triggered by a measurement event.  
[OnSCPIEvent](../Events/OnSCPIEvent.md) |  IApplication |  Triggered by a SCPI event.  
[OnSystemEvent](../Events/OnSystemEvent.md) |  IApplication |  Triggered by a system event.  
[OnUserEvent](../Events/OnUserEvent.md) |  IApplication |  For future use  
  
### IApplication History

Interface |  Introduced with VNA Rev:  
---|---  
IApplication |  1.0  
IApplication2 |  3.0  
IApplication3 |  3.2  
IApplication4 |  3.5  
IApplication5 |  4.0  
IApplication6 |  5.0  
IApplication7 |  5.0  
IApplication8 |  5.2  
IApplication9 |  6.0  
IApplication10 |  7.20  
IApplication11 |  7.20  
IApplication12 |  7.21  
IApplication13 |  8.0  
IApplication14 |  8.2  
IApplication15 |  8.34  
IApplication16 |  9.0  
IApplication17 |  9.0  
IApplication18 |  9.2  
IApplication19 |  10.0  
IApplication20 |  10.40  
IApplication22 |  10.45  
IApplication23 |  A.12.70  
  
* * *

