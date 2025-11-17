##### Write/Read

|

##### [About Reference Markers](../../../S4_Collect/Markers.md#reference)  
  
---|---  
  
## ReferenceMarkerState Property

* * *

#### Description

|  Turn ON or OFF the reference marker.  
---|---  
  
####  VB Syntax

|  meas.ReferenceMarkerState = state  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  A [Measurement](../Objects/Measurement_Object.md) (object)  
state |  (boolean) - True \- turns the reference marker ON False - turns the reference marker OFF  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  meas.ReferenceMarkerState = True  
reference = meas.ReferenceMarkerState  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_ReferenceMarkerState(VARIANT_BOOL bState)  
HRESULT put_ReferenceMarkerState(VARIANT_BOOL* bState)  
  
#### Interface

|  IMeasurement

