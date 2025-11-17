##### Read only

## GetSourceRoles Method

* * *

#### Description

|  Returns the defined role names ("RF2", "LO1"). Note: For non-converter
channels, use [chan.RoleDevice](../Properties/RoleDevice_Property.md)  
---|---  
  
####  VB Syntax

|  roles = conv.GetSourceRoles ( )  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
roles |  (Variant array) Variable to store returned list of valid roles.  
conv |  A [Converter Object](../Objects/Converter_Object.md)  
  
#### Return Type

|  Variant  
  
#### Default

|  Not Applicable  
  
#### Examples

|  roles = conv.GetSourceRoles( )  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT GetSourceRoles(VARIANT* roles);  
  
#### Interface

|  IConverter  
  
* * *

