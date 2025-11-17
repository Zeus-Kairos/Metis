# PathConfiguration Object

* * *

### Description

Provides access to the path configuration currently active on the channel
object.

To load, store, or delete a configuration, see
[ConfigurationManager](PathConfigurationManager_Object.md) Object.

### Accessing the PathConfiguration object in VB

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim chan as Channel  
Set chan = app.ActiveChannel  
  
Dim pathConfig As PathConfiguration  
Set pathConfig = chan.PathConfiguration

### Accessing the PathConfiguration object in C#

Type pnaType = Type.GetTypeFromProgID("AgilentPNA835x.Application", "PNA-NAME-
HERE");  AgilentPNA835x.Application pna =
(AgilentPNA835x.Application)Activator.CreateInstance(pnaType);
AgilentPNA835x.Channel chan = (AgilentPNA835x.Channel)pna.ActiveChannel;
AgilentPNA835x.PathConfiguration path =
(AgilentPNA835x.PathConfiguration)chan.get_PathConfiguration();  
---  
  
Note: To learn how to make configuration (element) settings, see this [Path
Configuration
Example](../../COM_Example_Programs/PathConfiguration_Example.htm) Also see
this [list of configurable elements and settings.](../../RF_PathConfig.md)  
---  
  
### See Also:

  * [PathConfigurationManager Object](PathConfigurationManager_Object.md)

  * [PathElement Object](PathElement_Object.md)

  * [Path Configurator](../../../S1_Settings/Path_Configurator.md) UI

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

### Methods

|

### Interface

[See History](Preferences_Object.md#history) | 

### Description  
  
---|---|---  
[CopyFrom](../Methods/CopyFrom_Method.md) |  IPathConfiguration2 |  Copy the mechanical switch settings and attenuator settings from the specified channel to the active channel.  
[Store](../Methods/Store_Method.md) |  IPathConfiguration |  Saves the current configuration to the specified name.  
  
### Properties

|

### Interface

[See History](Preferences_Object.md#history) | 

### Description  
  
[DescriptiveText](../Properties/DescriptiveText_Property.md) |  IPathConfiguration |  Write and read descriptive text associated with the configuration.  
[Elements](../Properties/Elements_Property.md) |  IPathConfiguration |  Collection of Elements that can be configured (switches and so forth). See the [list of elements](../../RF_PathConfig.md) and settings.  
[Element](../Properties/Element_Property.md) |  IPathConfiguration |  Returns a handle to a [IPathElement](PathElement_Object.md) object.  
[Name](../Properties/Name_config_Property.md) |  IPathConfiguration |  Returns the name of the current configuration.  
[Parent](../Properties/Parent_Property.md) |  IPathConfiguration |  Returns a pointer to the parent COM object (Channel).  
  
###  IPathConfiguration History

Interface |  Introduced with VNA Rev:  
---|---  
IPathConfiguration |  7.2  
IPathConfiguration2 |  9.4

