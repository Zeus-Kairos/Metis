##### Write-only

|

##### [ About Path Configurator](../../../S1_Settings/Path_Configurator.md)  
  
---|---  
  
## Store Method

* * *

#### Description

|  Saves the path configuration currently associated with channel (ch) to the
specified configuration name. This command is identical to
PathConfigurationManager.[StoreConfiguration
Method](StoreConfiguration_Method.htm)  
---|---  
  
####  VB Syntax

|  pathMgr.StoreConfiguration ch, name  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pathMgr |  [PathConfigurationManager](../Objects/PathConfigurationManager_Object.md) (object)  
ch |  (Long) Channel number of the configuration to be saved.  
name |  (String) Configuration name. Factory configurations can NOT be overwritten. Specifying the name of a pre-defined factory configuration will result in an error.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  path.StoreConfiguration(2) "myMixer"  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT StoreConfiguration( long channelNum, BSTR configName );  
  
#### Interface

|  IPathConfigurationManager  
  
* * *

