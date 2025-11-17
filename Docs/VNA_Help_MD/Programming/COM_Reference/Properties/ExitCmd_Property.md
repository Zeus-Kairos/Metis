##### Write/Read

|

##### [About External DC Devices](../../../System/Configure_a_DC_Device.md)  
  
---|---  
  
# ExitCmd Property

* * *

#### Description

|  Sets and returns the Disable I/O command for an external DC Source and an
external DC Meter.  
---|---  
  
####  VB Syntax

|  extDC.ExitCmd = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
extDC |  A [ExternalDCDevice](../Objects/ExternalDCDevice_Object.md) (object)  
value |  (String) The SCPI command used to disable the DC Source and DC Meter.  
  
#### Return Type

|  String  
  
#### Default

|  " " Empty String  
  
#### Examples

|  extDC.ExitCmd = "OUTP OFF" 'Write value = extDC.ExitCmd 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_ExitCmd( BSTR* cmd); HRESULT put_ExitCmd( BSTR cmd);  
  
#### Interface

|  IExternalDCDevice3  
  
* * *

