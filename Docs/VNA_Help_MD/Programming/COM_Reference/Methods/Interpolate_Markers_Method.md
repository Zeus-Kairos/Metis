##### Write-only

|

##### [About Markers](../../../S4_Collect/Markers.md)  
  
---|---  
  
## InterpolateMarkers Method

* * *

#### Description

|  Turns All Marker Interpolation ON and OFF for the measurement. Marker
interpolation enables X-axis resolution between the discrete data values. The
analyzer will calculate the x and y-axis data values between discrete data
points. To override this property for individual markers, use the
[Interpolated](../Properties/Interpolated_Property.md) property.  
---|---  
  
####  VB Syntax

|  meas.Interpolate = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas |  A Measurement (object)  
value |  (boolean)  
False \- Turns interpolation OFF for all markers in the measurement  
True \- Turns interpolation ON for all markers in the measurement  
  
#### Return Type

|  Boolean  
  
#### Default

|  True (ON)  
  
#### Examples

|  meas.Interpolate = 1  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT InterpolateMarkers(VARIANT_BOOL bNewVal)  
  
####  Interface

|  IMeasurement

