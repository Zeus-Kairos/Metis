##### Write/Read

|

##### [About External DC Devices](../../../System/Configure_a_DC_Device.md)  
  
---|---  
  
# IDQuery Property

* * *

#### Description

|  Sets and returns the ID Query command for an external DC Source and an
external DC Meter.  
---|---  
  
####  VB Syntax

|  extDC.IDQuery = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
extDC |  A [ExternalDCDevice](../Objects/ExternalDCDevice_Object.md) (object)  
value |  (String) The SCPI command for returning DC Source and DC Meter ID string.  
  
#### Return Type

|  String  
  
#### Default

|  "*IDN?"  
  
#### Examples

|  extDC.IDQuery = "*IDN?" 'Write value = extDC.IDQuery 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_IDQuery( BSTR* cmd); HRESULT put_IDQuery( BSTR cmd);  
  
#### Interface

|  IExternalDCDevice3  
  
* * *

