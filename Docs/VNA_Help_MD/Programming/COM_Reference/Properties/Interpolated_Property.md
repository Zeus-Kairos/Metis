##### Write/Read

|

##### [About Markers](../../../S4_Collect/Markers.md)  
  
---|---  
  
## Interpolated Property

* * *

#### Description

|  Turns marker Interpolation ON and OFF. Marker interpolation enables X-axis
resolution beyond the discrete data values. The analyzer will calculate the x
and y-axis data values between discrete data points. Use
meas.[Interpolate](../Methods/Interpolate_Markers_Method.md) to change
interpolation of all markers in a measurement. This command will override the
measurement setting.  
---|---  
  
####  VB Syntax

|  mark.Interpolated = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
mark |  A [Marker](../Objects/Marker_Object.md) (object)  
value |  (boolean)  
False \- Turns interpolation OFF True \- Turns interpolation ON  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Examples

|  mark.Interpolated = True 'Write  
interpolate = mark.Interpolated 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Interpolated(VARIANT_BOOL *pVal)  
HRESULT put_Interpolated(VARIANT_BOOL newVal)  
  
#### Interface

|  IMarker

