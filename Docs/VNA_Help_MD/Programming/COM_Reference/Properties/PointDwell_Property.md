##### Write/Read

|

##### [About Ext DC Devices](../../../System/Configure_a_DC_Device.md)  
  
---|---  
  
## PointDwell Property

* * *

#### Description

|  Sets and returns the "Dwell Before/After Point" value for an external DC
Device which can be configured as either a DC Meter or a DC Source.  
---|---  
  
####  VB Syntax

|  extDC.PointDwell = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
extDC |  An [ExternalDCDevice](../Objects/ExternalDCDevice_Object.md) (object)  
value |  (Double) For DC Meter, the dwell time (in seconds) before making a data point measurement. For DC Source, the dwell time (in seconds) after making a data point setting.  
  
#### Return Type

|  Double  
  
#### Default

|  3 milliseconds  
  
#### Examples

|  extDC.PointDwell = 10e-3 'Write  
dwell = extDC.PointDwell 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PointDwell (double *pValue) HRESULT put_PointDwell (double
newVal)  
  
#### Interface

|  IExternalDCDevice  
  
* * *

* * *

