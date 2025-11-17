# CalManager Object

* * *

### Description

Use this interface to list, save, and delete Cal Sets.

### Accessing the CalManager object

Get a handle to a the CalManager with the
app.[GetCalManager](../Methods/Get_CalManager_Method.md) Method.

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim mgr as ICalManager  
Set mgr = app.GetCalManager

### See Also:

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

  * [Superseded commands](../../Replacement_Commands.md)

(Bold Methods or Properties provide access to a child object)

### Methods

|

### Interface

[See History](CalManager_Object.md#Interface1) | 

### Description  
  
---|---|---  
[AllowChannelToSweepDuringCalAcquisition](../Methods/AllowChannelToSweepDuringCalAcquisition_Method.md) | ICalManager5 | Specifies the channel to sweep during a Calibration.  
[CalibrateAllChannels](CalibrateAllChannels_Object.md) | ICalManager9 | Provides access to CalibrateAllChannels object.  
[CascadeS2PFiles](../Methods/CascadeS2PFiles_Method.md) | ICalManager10 | Creates a single S2P file from two existing files.  
[CharacterizeFixture](../Methods/CharacterizeFixture_Method.md) | ICalManager10 | Characterizes an adapter/fixture based on two calsets.  
[CreateCalSet](../Methods/CreateCalSet_Method.md) | ICalManager | Creates a new Cal Set  
[CreateCustomCal](../Methods/CreateCustomCal_Method.md) | ICalManager2 | Creates an FCA cal object.  
[CreateCustomCalEx](../Methods/CreateCustomCalEx_Method.md) | ICalManager5 | Creates a custom cal object.  
[Deembed](../Methods/Deembed_Method.md) | ICalManager8 | De-embeds a fixture from an existing Cal Set based on an S2P file.  
[DeleteCalSet](../Methods/DeleteCalSet_Method.md) | ICalManager | Deletes a Cal Set  
[DisplayNAWindowDuringCalAcquisition](../Methods/DisplayNAWindowDuringCalAcquisition_Method.md) | ICalManager5 | Set the 'show' state of the window to be displayed during a calibration.  
[DisplayOnlyCalWindowDuringCalAcquisition](../Methods/DisplayOnlyCalWindowDuringCalAcquisition_Method.md) | ICalManager5 | Clears the flags for windows to be shown during calibrations.  
[Embed](../Methods/Embed_Method.md) | ICalManager8 | Embeds a fixture into an existing Cal Set based on an S2P file.  
[ENREmbedAdapter](../Methods/ENREmbedAdapter_Method.md) | ICalManager11 | Generate a new ENR file by embedding an adapter to an existing ENR file.  
[EnumerateCalSets](../Methods/EnumerateCalSets_Method.md) | ICalManager4 | Returns an array of Cal Set names being stored on the VNA.  
[GetCalSetByGUID](../Methods/Get_CalSetByGUID_Method.md) | ICalManager | Get a handle to a Cal Set  
[GetCalSetCatalog](../Methods/Get_CalSetCatalog_Method.md) | ICalManager | Superseded with [EnumerateCalSets](../Methods/EnumerateCalSets_Method.md)  
[GetCalSetUsageInfo](../Methods/Get_CalSetUsageInfo_Method.md) | ICalManager | Returns the Cal Set ID and Error Term ID currently in use  
[GetCalTypes](../Methods/Get_CalTypes_Method.md) | ICalManager2 | Query for a list of available calibration types.  
[GetEcalUserCharacterizer](../Methods/GetEcalUserCharacterizer_Method.md) | ICalManager6 | Returns the ECalUserCharacterizer object.  
[SaveCalSets](../Methods/Save_CalSets_Method.md) | ICalManager | Superseded with [CalSet.Save](../Methods/Save_CalSet_Method.md)  
[SweepOnlyCalChannelDuringCalAcquisition](../Methods/SweepOnlyCalChannelDuringCalAcquisition_Method.md) | ICalManager5 | Clears ALL flags for channels to sweep during calibration.  
[ZeroTermsInS4PFile](../Methods/ZeroTermsInS4PFile.md) | ICalManager12 | Creates a new S4P file.  
  
### Properties

|

###

|

###  
  
[CalibrateAllChannelsEx](CalibrateAllChannels_Object.md) | ICalManager13 | Provides access to CalibrateAllChannels object for setting up more than one CalibrateAllChannels instances. This command takes an input calibration number. See the programming example.  
[CalSets Collection](CalSets_Collection.md) | ICalManager | Collection for iterating through all the Cal Sets in the analyzer.  
[ECalModules Collection](ECalModules_Collection.md) | ICalManager7 | Collection of ECal Modules that are connected to the VNA.  
[GuidedCalibration](GuidedCalibration_Object.md) | ICalManager3 | Used to perform a Guided Calibration.  
[PhaseReferenceCalibration](PhaseReferenceCalibration_Object.md) | ICalManager9 | Used to perform a Phase Reference Calibration.  
  
###  ICalManager History

Interface | Introduced with VNA Rev:  
---|---  
ICalManager | 2.0  
CalManager2 | 3.1  
CalManager3 | 3.5  
CalManager4 | 5.0  
ICalManager5 | 8.0  
ICalManager6 | 8.3  
ICalManager7 | 8.5  
ICalManager8 | 9.33  
ICalManager9 |   
ICalManager10 | 10.15  
ICalManager11 | 12.50.01  
ICalManager12 |   
ICalManager13 | 12.90

