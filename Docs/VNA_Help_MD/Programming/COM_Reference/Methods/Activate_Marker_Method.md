##### Write-only

|

##### [About Markers](../../../S4_Collect/Markers.md)  
  
---|---  
  
## ActivateMarker Method

* * *

#### Description

|  Makes a marker the Active Marker. Use
meas.[ActiveMarker](../Properties/ActiveMarker_Property.md) to read the
number of the active marker.  
---|---  
  
####  VB Syntax

|  meas.ActivateMarker(Mnum)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas |  A [Measurement](../Objects/Measurement_Object.md) (object)  
Mnum |  (long integer) \- the number of the marker to make active. Choose any marker number from 1 to 15.  
  
#### Return Type

|  None  
  
#### Default

|  Not Applicable  
  
#### Examples

|  meas.ActivateMarker(1)'Write  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT ActivateMarker(long lMarkerNumber)  
  
#### Interface

|  IMeasurement  
  
#### Remarks

|  Use [ReferenceMarkerState](../Properties/ReferenceMarkerState_Property.md)
to control the Reference marker.

