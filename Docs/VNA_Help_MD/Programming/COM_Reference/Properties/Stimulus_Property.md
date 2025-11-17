##### Write/Read

|

##### [About Markers](../../../S4_Collect/Markers.md)  
  
---|---  
  
## Stimulus Property

* * *

#### Description

|  Sets and reads the X-Axis value of the marker. If the marker is a delta
marker, the value will be relative to the reference marker. See Reference
Marker example below. See Also: [Read Y-axis value](Value_Property.md).  
---|---  
  
####  VB Syntax

|  mark.Stimulus = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
mark |  A [Marker](../Objects/Marker_Object.md) (object)  
value |  (double) - X-Axis value. Choose any number within the full span of the channel or User Range (if set).  
  
#### Return Type

|  Double  
  
#### Default

|  First activated Marker turns ON in the middle of the X-axis range.
Subsequent markers turn ON at the position of the most recently active marker.  
  
#### Examples

|  mark.Stimulus = 3e9 'Write XVal = mark.Stimulus 'Read  Get, then Set the
Reference Marker X-axis location  
dim RefMarkerX  
RefMarkerX = app.ActiveMeasurement.GetReferenceMarker.Stimulus  
app.ActiveMeasurement.GetReferenceMarker.Stimulus = 1.23e9  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Stimulus(double *pVal) HRESULT put_Stimulus(double newVal)  
  
#### Interface

|  IMarker  
  
* * *

