##### Read only

## GetSourceByRole Method

* * *

#### Description

|  Returns the name of a source that is assigned to the specified role. Note:
For non-converter channels, use
[chan.RoleDevice](../Properties/RoleDevice_Property.md)  
---|---  
  
####  VB Syntax

|  source = conv.GetSourceByRole (role)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
source |  (String) Source name, from [Source Configuration dialog](../../../System/Configure_an_External_Device.md#ext_source_config), that is assigned to the specified role.  
conv |  A [Converter Object](../Objects/Converter_Object.md)  
role |  (String) Role for which the source name will be returned. Use [GetSourceRoles](GetSourceRoles_Method.md) for a list of valid roles.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  RF2Source = conv.GetSourceByRole ("RF2")  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT GetSourceByRole(BSTR roleID, BSTR deviceName);  
  
#### Interface

|  IConverter  
  
* * *

