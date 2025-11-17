##### Write-only

|

##### [ About Path Configurator](../../../S1_Settings/Path_Configurator.md)  
  
---|---  
  
## LoadConfiguration Method

* * *

#### Description

|  Loads the named configuration onto the specified channel. Note: Loading a
stored configuration will over-write MANY RF and [IF path
configuration](../../../IFAccess/IF_Path_Configuration.htm) settings. Make
your measurement settings AFTER recalling a stored configuration, NOT before.
Use [Configurations Method](../Properties/Configurations_Property.md) to
return the configuration names that are stored on the VNA.  
---|---  
  
####  VB Syntax

|  pathMgr.LoadConfiguration ch, name  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pathMgr |  [PathConfigurationManager](../Objects/PathConfigurationManager_Object.md) (object)  
ch |  (Long) Channel number of the configuration to be saved.  
name |  (String) Configuration name. "Default" is the default factory configuration.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  path.LoadConfiguration 2, "myMixer"  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT LoadConfiguration (long channelNum, BSTR configName );  
  
#### Interface

|  IPathConfigurationManager  
  
* * *

