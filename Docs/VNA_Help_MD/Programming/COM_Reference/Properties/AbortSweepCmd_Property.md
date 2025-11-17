##### Write/Read

|

##### [About External DC Devices](../../../System/Configure_a_DC_Device.md)  
  
---|---  
  
# AbortSweepCmd Property

* * *

#### Description

|  Sets and returns the Abort Sweep command for an external DC Source and an
external DC Meter.  
---|---  
  
####  VB Syntax

|  extDC.AbortSweepCmd = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
extDC |  A [ExternalDCDevice](../Objects/ExternalDCDevice_Object.md) (object)  
value |  (String) The SCPI command used to abort or reset the DC Source or DC Meter.  
  
#### Return Type

|  String  
  
#### Default

|  " " Empty String  
  
#### Examples

|  extDC.AbortSweepCmd = "ABORt" 'Write value = extDC.AbortSweepCmd 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_AbortSweepCmd( BSTR* cmd); HRESULT put_AbortSweepCmd( BSTR
cmd);  
  
#### Interface

|  IExternalDCDevice3  
  
* * *

