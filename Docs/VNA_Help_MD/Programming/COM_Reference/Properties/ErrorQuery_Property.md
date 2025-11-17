##### Write/Read

|

##### [About External DC Devices](../../../System/Configure_a_DC_Device.md)  
  
---|---  
  
# ErrorQuery Property

* * *

#### Description

|  Sets and returns the Error Query command for an external DC Source and an
external DC Meter.  
---|---  
  
####  VB Syntax

|  extDC.ErrorQuery = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
extDC |  A [ExternalDCDevice](../Objects/ExternalDCDevice_Object.md) (object)  
value |  (String) The SCPI command for returning DC Source and DC Meter errors.  
  
#### Return Type

|  String  
  
#### Default

|  "SYST:ERR?"  
  
#### Examples

|  extDC.ErrorQuery = "SYST:ERR?" 'Write value = extDC.ErrorQuery 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_ErrorQuery( BSTR* cmd); HRESULT put_ErrorQuery( BSTR cmd);  
  
#### Interface

|  IExternalDCDevice3  
  
* * *

