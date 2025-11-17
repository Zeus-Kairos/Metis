##### Write/Read

|

##### [About Marker Search](../../../S4_Collect/Markers.md#Searching)  
  
---|---  
  
## SearchFunction Property

* * *

#### Description

|  Emulates the Tracking function in the marker search dialog box. The value
you choose for SearchFunction will determine the type of search that takes
place when the [Tracking](Tracking_Property.md) property is set true. The
tracking function finds the selected search function every sweep. In effect,
turning Tracking ON is the same as executing one of the "Search..." methods
(such as SearchMin, SearchMax) for every sweep.  
---|---  
  
####  VB Syntax

|  mark.SearchFunction = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
mark |  A [Marker](../Objects/Marker_Object.md) (object)  
value |  (enum NAMarkerFunction) - search function. Choose from: 0 - naMarkerFunction_None 1 - naMarkerFunction_Min 2 - naMarkerFunction_Max 3 - naMarkerFunction_Target 4 - naMarkerFunction_NextPeak 5 - naMarkerFunction_PeakRight 6 - naMarkerFunction_PeakLeft 7 - naMarkerFunction_Compression  
  
#### Return Type

|  Long Integer  
  
#### Default

|  0 \- naMarkerFunction_None  
  
#### Examples

|  mark.SearchFunction = naMarkerFunction_Target 'When this marker is set to
track, it will track the Target value.  
searchfunction = mark.SearchFunction 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_SearchFunction(tagNAMarkerFunction *pVal)  
HRESULT put_SearchFunction(tagNAMarkerFunction newVal)  
  
#### Interface

|  IMarker

