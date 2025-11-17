##### Write/Read

|

##### [About Marker Types](../../../S4_Collect/Markers.md#types)  
  
---|---  
  
## Type (Marker) Property

* * *

#### Description

|  Sets and reads the marker type.  
---|---  
  
####  VB Syntax

|  mark.Type = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan |  A [Marker](../Objects/Marker_Object.md) (object)  
value |  (enum NAMarkerType) \- Marker Type. Choose from:  
0 - naMarkerType_Normal - the X-axis value for a normal marker will always be
determined by the measurement data of the marker. 1 - naMarkerType_Fixed -
retains and keeps its x-axis value at the time the marker type is set.  
  
#### Return Type

|  Long Integer  
  
#### Default

|  naMarkerType_Normal  
  
#### Examples

|  mark.Type = naMarkerType_Normal 'Write  
MrkType = mark.Type 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Type(tagNAMarkerType *pVal)  
HRESULT put_Type(tagNAMarkerType newVal)  
  
#### Interface

|  IMarker

