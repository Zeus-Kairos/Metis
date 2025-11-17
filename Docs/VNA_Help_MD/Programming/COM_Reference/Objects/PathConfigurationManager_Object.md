# PathConfigurationManager Object

* * *

### Description

These commands allow configurations to be stored, loaded, or deleted on the
VNA.

To make path configuration settings, see [PathConfiguration
Object](PathConfiguration_Object.htm) and the [PathElement
Object](PathElement_Object.htm)

### Accessing the PathConfigurationManager object

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim pathConfig As PathConfigurationManager  
Set pathConfig = app.PathConfigurationManager

Note: To learn how to make configuration (element) settings, see this [Path
Configuration
Example](../../COM_Example_Programs/PathConfiguration_Example.htm) Also see
this [list of configurable elements and settings.](../../RF_PathConfig.md)  
---  
  
### See Also:

  * [Path Configuration Example](../../COM_Example_Programs/PathConfiguration_Example.md)

  * [Path Configurator](../../../S1_Settings/Path_Configurator.md)

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Methods

|

### Interface

[See History](Preferences_Object.md#history) | 

### Description  
  
---|---|---  
[DeleteConfiguration](../Methods/DeleteConfiguration_Method.md) |  IPathConfigurationManager |  Deletes the specified configuration from the VNA.  
[LoadConfiguration](../Methods/LoadConfiguration_Method.md) |  IPathConfigurationManager |  Loads the named configuration.  
[StoreConfiguration](../Methods/StoreConfiguration_Method.md) |  IPathConfigurationManager |  Saves the path configuration  
  
### Properties

|

### Interface

[See History](Preferences_Object.md#history) | 

### Description  
  
[Configurations](../Properties/Configurations_Property.md) |  IPathConfigurationManager |  Returns a list of configuration names stored in the VNA.  
[Parent](../Properties/Parent_Property.md) |  IPathConfigurationManager |  Returns a handle to the Application object.  
  
###  IPathConfigurationManager History

Interface |  Introduced with VNA Rev:  
---|---  
IPathConfigurationManager |  7.2  
|

