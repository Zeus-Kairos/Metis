##### Write/Read

|

##### [About Ext DC Devices](../../../System/Configure_a_DC_Device.md)  
  
---|---  
  
## SweepDwell Property

* * *

#### Description

|  Sets and returns the "Dwell Before Sweep" value for an external DC Device
which can be configured as either a DC Meter or a DC Source.  
---|---  
  
####  VB Syntax

|  extDC.SweepDwell = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
extDC |  An [ExternalDCDevice](../Objects/ExternalDCDevice_Object.md) (object)  
value |  (Double) The dwell time (in seconds) before making a new sweep.  
  
#### Return Type

|  Double  
  
#### Default

|  1 milliseconds  
  
#### Examples

|  extDC.SweepDwell = 10e-3 'Write  
dwell = extDC.SweepDwell 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SweepDwell (double *pValue) HRESULT put_SweepDwell (double
newVal)  
  
#### Interface

|  IExternalDCDevice  
  
* * *

* * *

