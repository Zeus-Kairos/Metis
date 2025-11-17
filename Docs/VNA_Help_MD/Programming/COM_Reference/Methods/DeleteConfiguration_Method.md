##### Write-only

|

##### [ About Path Configurator](../../../S1_Settings/Path_Configurator.md)  
  
---|---  
  
## DeleteConfiguration Method

* * *

#### Description

|  Deletes the specified configuration name from the VNA. The factory
configurations cannot be deleted. This is the only method of programmatically
distinguishing a factory configuration from a user-named configuration.  
---|---  
  
####  VB Syntax

|  pathMgr.DeleteConfiguration name  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pathMgr |  [PathConfigurationManager](../Objects/PathConfigurationManager_Object.md) (object)  
name |  (String) Configuration name to be deleted.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  path.DeleteConfiguration "myMixer"  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT StoreConfiguration (long channelNum, BSTR configName );  
  
#### Interface

|  IPathConfigurationManager  
  
* * *

