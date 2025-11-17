##### Write only

## AssignSourceToRole Method

* * *

#### Description

|  Assigns a configured source to the specified role. Use
[chan.RoleDevice](../Properties/RoleDevice_Property.md) for non-converter
channels.  
---|---  
  
####  VB Syntax

|  conv.AssignSourceToRole role, source  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
conv |  A [Converter Object](../Objects/Converter_Object.md)  
role |  (String) Role to which the external source is assigned. Choose from: For IMDX and IMSX, choose from: "RF2" "LO1" "LO2" For all other converter applications, choose from: "LO1" "LO2"  
source |  (String) Source name from [Source Configuration dialog](../../../System/Configure_an_External_Device.md#ext_source_config).  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  conv.AssignSourceToRole "LO1", "LO1Name"  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT AssignSourceToRole(BSTR roleID, BSTR deviceName);  
  
#### Interface

|  IConverter  
  
* * *

  

