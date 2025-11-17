##### Write/Read

|

##### [About Ext DC Devices](../../../System/Configure_a_DC_Device.md)  
  
---|---  
  
## DCScale Property

* * *

#### Description

|  Sets and returns the scale correction value for an external DC Device which
can be configured as either a DC Meter or a DC Source.  
---|---  
  
####  VB Syntax

|  extDC.DCScale = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
extDC |  An [ExternalDCDevice](../Objects/ExternalDCDevice_Object.md) (object)  
value |  (Double) DC scale value. The VNA will display readings from a DC Meter as: Display = (Meas'd value - Offset) * Scale The VNA will adjust the output from a DC Source as: Output = (Set value - Offset) * Scale  
  
#### Return Type

|  Double  
  
#### Default

|  1  
  
#### Examples

|  extDC.DCScale = -2 'Write  
slope = extDC.DCScale 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_DCScale (double *pValue) HRESULT put_DCScale (double newVal)  
  
#### Interface

|  IExternalDCDevice  
  
* * *

* * *

