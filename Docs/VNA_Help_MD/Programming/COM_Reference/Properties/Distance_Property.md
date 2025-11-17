##### Write/Read

|

##### [About Distance Markers](../../../Time/TimeDomain.md#Distance)  
  
---|---  
  
## Distance Property

* * *

#### Description

|  Set or query marker distance on a time domain trace. The Write command
moves the marker to the specified distance value. Once moved, you can read the
[Y axis](Value_Property.md) value or [read the X-axis
time](Stimulus_Property.htm) value. (Distance is calculated from the X-axis
time value.) The Read command reads the distance of the marker. If the marker
is set as delta, the WRITE and READ data is relative to the reference marker.  
---|---  
  
####  VB Syntax

|  mark.Distance = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
mark |  A [Marker](../Objects/Marker_Object.md) (object)  
value |  (double) \- Marker distance in the unit of measure specified with [DistanceMarkerUnit Property](DistanceMarkerUnit_Property.md)  
  
#### Return Type

|  Double  
  
#### Default

|  Not Applicable  
  
#### Examples

|  mark.Distance = 3e9 'Write  
XVal = mark.Distance 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Distance(double *pVal); HRESULT put_Distance(double newVal);  
  
#### Interface

|  IMarker2

