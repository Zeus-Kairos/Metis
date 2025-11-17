##### Write/Read

|

##### [About External DC Devices](../../../System/Configure_a_DC_Device.md)  
  
---|---  
  
# InitCmd Property

* * *

#### Description

|  Sets and returns the Enable I/O command for an external DC Source and an
external DC Meter.  
---|---  
  
####  VB Syntax

|  extDC.InitCmd = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
extDC |  A [ExternalDCDevice](../Objects/ExternalDCDevice_Object.md) (object)  
value |  (String) The SCPI command used to enable the DC Source and DC Meter.  
  
#### Return Type

|  String  
  
#### Default

|  " " Empty String  
  
#### Examples

|  extDC.InitCmd = "OUTP ON" 'Write value = extDC.InitCmd 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_InitCmd( BSTR* cmd); HRESULT put_InitCmd( BSTR cmd);  
  
#### Interface

|  IExternalDCDevice3  
  
* * *

