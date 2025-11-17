# PathElement Object

* * *

### Description

Provides access to the settings for the PathElement object.

### Accessing the PathElement object in VB

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>) Dim chan
as Channel  
Set chan = app.ActiveChannel Dim pathConfig As PathConfiguration  
Set pathConfig = chan.PathConfiguration Dim element as PathElement  
Set element = pathConfig.PathElement("Src1")  
---  
  
### Accessing the PathElement object in C#

Type pnaType = Type.GetTypeFromProgID("AgilentPNA835x.Application", "PNA-NAME-
HERE"); AgilentPNA835x.Application pna =
(AgilentPNA835x.Application)Activator.CreateInstance(pnaType);
AgilentPNA835x.Channel chan = (AgilentPNA835x.Channel)pna.ActiveChannel;
AgilentPNA835x.PathConfiguration path =
(AgilentPNA835x.PathConfiguration)chan.get_PathConfiguration();
path.get_Element("Port1RefMxr").Value = "External";  
---  
  
Note: To learn how to make configuration (element) settings, see this [Path
Configuration
Example](../../COM_Example_Programs/PathConfiguration_Example.htm) Also see
this [list of configurable elements and settings.](../../RF_PathConfig.md)  
---  
  
### See Also:

  * [Path Configurator](../../../S1_Settings/Path_Configurator.md)

  * [PathConfigurationManager Object](PathConfigurationManager_Object.md)

  * [PathConfiguration Object](PathConfiguration_Object.md)

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Methods

|

### Interface

[See History](Preferences_Object.md#history) | 

### Description  
  
---|---|---  
None |  |   
  
### Properties

|

### Interface

[See History](Preferences_Object.md#history) | 

### Description  
  
[Name](../Properties/Name_element_Property.md) |  IPathElement |  Returns the name of the element.  
[Parent](../Properties/Parent_Property.md) |  IPathElement |  Returns a pointer to the Parent Object ([PathConfiguration](PathConfiguration_Object.md))  
[Value](../Properties/Value_element_Property.md) |  IPathElement |  Read / Write get the current setting for the element.  
[Values](../Properties/Values_Property.md) |  IPathElement |  Returns all valid settings for the element.  
  
###  IPathElement History

Interface |  Introduced with VNA Rev:  
---|---  
IPathElement |  7.2  
|

