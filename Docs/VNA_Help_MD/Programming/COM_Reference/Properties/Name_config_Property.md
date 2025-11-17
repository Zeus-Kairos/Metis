##### Read-only

|

##### [About Path
Configurator](../../../S0_Start/Traces_Channels_and_Windows.htm#trace)  
  
---|---  
  
## Name (PathConfig) Property

* * *

#### Description

|  Returns the name of the current configuration only if NO individual element
settings had been changed since selecting or storing a configuration. When
element settings change, the path configuration name is cleared.  
---|---  
  
####  VB Syntax

|  name = pathConfig.Name  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
name |  (String) Variable to store the returned configuration name.  
pathConfig |  A [PathConfiguration](../Objects/PathConfiguration_Object.md) (object)  
  
#### Return Type

|  String  
  
#### Default

|  'default' \- name of the default factory configuration  
  
#### Examples

|  name=pathConf.Name  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Name(BSTR* ppName)  
  
#### Interface

|  IPathConfiguration  
  
* * *

