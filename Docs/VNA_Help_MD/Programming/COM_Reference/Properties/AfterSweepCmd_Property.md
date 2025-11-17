##### Write/Read

|

##### [About External DC Devices](../../../System/Configure_a_DC_Device.md)  
  
---|---  
  
# AfterSweepCmd Property

* * *

#### Description

|  Sets and returns the After Sweep command for an external DC Source and an
external DC Meter.  
---|---  
  
####  VB Syntax

|  extDC.AfterSweepCmd = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
extDC |  A [ExternalDCDevice](../Objects/ExternalDCDevice_Object.md) (object)  
value |  (String) The SCPI command to be sent at the end of a sweep.  
  
#### Return Type

|  String  
  
#### Default

|  " " Empty String  
  
#### Examples

|  extDC.AfterSweepCmd = "OUTP OFF" 'Write value = extDC.AfterSweepCmd 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_AfterSweepCmd( BSTR* cmd); HRESULT put_AfterSweepCmd( BSTR
cmd);  
  
#### Interface

|  IExternalDCDevice3  
  
* * *

