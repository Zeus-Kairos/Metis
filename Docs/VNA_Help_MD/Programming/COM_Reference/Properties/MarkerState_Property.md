##### Write/Read

|

##### [About Markers](../../../S4_Collect/Markers.md)  
  
---|---  
  
## MarkerState Property

* * *

#### Description

|  Sets or returns the ON / OFF state of the specified marker.  
---|---  
  
####  VB Syntax

|  meas.MarkerState (n) = state  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas |  A Measurement (object)  
n |  (Long Integer) Marker number to turn on or off.  
state |  (boolean) -  
True - turns the specified marker ON  
False - turns the specified marker OFF  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  meas.MarkerState(1) = True  
reference = meas.MarkerState(2)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_MarkerState(long markerNum, VARIANT_BOOL bState)  
HRESULT put_MarkerState(long markerNum, VARIANT_BOOL* bState)  
  
#### Interface

|  IMeasurement3

