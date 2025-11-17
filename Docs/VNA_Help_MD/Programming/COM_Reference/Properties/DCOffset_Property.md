##### Write/Read

|

##### [About Ext DC Devices](../../../System/Configure_a_DC_Device.md)  
  
---|---  
  
## DCOffset Property

* * *

#### Description

|  Sets and returns the offset correction value for an external DC Device
which can be configured as either a DC Meter or a DC Source.  
---|---  
  
####  VB Syntax

|  extDC.DCOffset = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
extDC |  An [ExternalDCDevice](../Objects/ExternalDCDevice_Object.md) (object)  
value |  (Double) DC offset value. The VNA will display readings from a DC Meter as: Display = (Meas'd value - Offset) * Scale The VNA will adjust the output from a DC Source as: Output = (Set value - Offset) * Scale  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  extDC.DCOffset = 4 'Write  
offset = extDC.DCOffset 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_DCOffset (double *pValue) HRESULT put_DCOffset (double newVal)  
  
#### Interface

|  IExternalDCDevice  
  
* * *

* * *

