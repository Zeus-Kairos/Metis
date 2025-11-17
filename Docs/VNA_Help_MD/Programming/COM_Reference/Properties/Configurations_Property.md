##### Read-only

|

##### [ About Path Configurator](../../../S1_Settings/Path_Configurator.md)  
  
---|---  
  
## Configurations Property

* * *

#### Description

|  Returns an array of stored configuration names that can be used with
[DeleteConfiguration Method](../Methods/DeleteConfiguration_Method.md)
and.[LoadConfiguration Method](../Methods/LoadConfiguration_Method.md)  
---|---  
  
####  VB Syntax

|  names = pathMgr.Configurations  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
names |  (Variant array) Variable to store the returned configuration names.  
pathMgr |  [PathConfigurationManager](../Objects/PathConfigurationManager_Object.md) (object)  
  
#### Return Type

|  Variant array  
  
#### Default

|  Not Applicable  
  
#### Examples

|  names = path.Configurations  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Configurations (VARIANT* configurations );  
  
#### Interface

|  IPathConfigurationManager  
  
* * *

