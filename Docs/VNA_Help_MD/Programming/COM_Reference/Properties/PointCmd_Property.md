##### Write/Read

|

##### [About External DC Devices](../../../System/Configure_a_DC_Device.md)  
  
---|---  
  
# PointCmd Property

* * *

#### Description

|  Sets and returns the Point Read Commands for an external DC Meter or Point
Set Commands for an external DC Source.  
---|---  
  
####  VB Syntax

|  extDC.PointCmd = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
extDC |  An [ExternalDCDevice](../Objects/ExternalDCDevice_Object.md) (object)  
value |  (String) For DC Source, sets the Point Set Commands. Use {%f} to specify a double value and {%d} to specify an integer. For DC Meter, sets the Point Read Commands (for example, meas:volt?).  
  
#### Return Type

|  String  
  
#### Default

|  " " Empty String  
  
#### Examples

|  extDC.PointCmd = "sour1:volt {%f}" 'Write  
value = extDC.PointCmd 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PointCmd(BSTR* cmd) HRESULT put_PointCmd(BSTR cmd)  
  
#### Interface

|  IExternalDCDevice3  
  
* * *

