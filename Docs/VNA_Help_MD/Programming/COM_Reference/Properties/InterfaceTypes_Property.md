##### Read-only

|

##### [About IO
Configuration](../../Learning_about_GPIB/How_to_Configure_for_GPIB_SCPI_and_SICL.htm)  
  
---|---  
  
## InterfaceTypes Property

* * *

#### Description

|  Returns the valid interface types for the VNA.  
---|---  
  
####  VB Syntax

|  value = IOConfig.InterfaceTypes  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Variant) variable to store the returned information.  
IOConfig |  An [IOConfiguration](../Objects/IOConfiguration_Object.md) object.  
  
#### Return Type

|  Array of strings  
  
#### Default

|  Not Applicable  
  
#### Examples

|  values = IO.InterfaceTypes For i = lbound(values) to ubound(values)
Wscript.echo values(i) next  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT InterfaceTypes(VARIANT* recognizedTypes);  
  
#### Interface

|  IIOConfiguration  
  
* * *

