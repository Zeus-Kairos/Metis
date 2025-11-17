##### Write/Read

|

##### [About External DC Devices](../../../System/Configure_a_DC_Device.md)  
  
---|---  
  
# BeforeSweepCmd Property

* * *

#### Description

|  Sets and returns the Before Sweep command for an external DC Source and an
external DC Meter.  
---|---  
  
####  VB Syntax

|  extDC.BeforeSweepCmd = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
extDC |  A [ExternalDCDevice](../Objects/ExternalDCDevice_Object.md) (object)  
value |  (String) The SCPI command to be sent at the beginning of a sweep.  
  
#### Return Type

|  String  
  
#### Default

|  " " Empty String  
  
#### Examples

|  extDC.BeforeSweepCmd = "OUTP ON" 'Write value = extDC.BeforeSweepCmd 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_BeforeSweepCmd( BSTR* cmd); HRESULT put_BeforeSweepCmd( BSTR
cmd);  
  
#### Interface

|  IExternalDCDevice3  
  
* * *

