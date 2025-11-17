##### Write/Read

|

##### [About Marker Search](../../../S4_Collect/Markers.md#Searching)  
  
---|---  
  
## PeakThreshold Property

* * *

#### Description

|  Sets peak threshold for the specified marker. If a peak (using the criteria
set with [PeakExcursion](Peak_Excursion_Property.md)) is below this reference
value, it will not be considered when searching for peaks.  
---|---  
  
####  VB Syntax

|  mark.PeakThreshold = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
mark |  A [Marker](../Objects/Marker_Object.md) (object)  
value |  (single) - Peak Threshold. Choose any number between:  
-500 and 500  
  
#### Return Type

|  Single  
  
#### Default

|  -100db  
  
#### Examples

|  mark.PeakThreshold = 1 'Write  
PkThresh = mark.PeakThreshold 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_PeakThreshold(float *pVal)  
HRESULT put_PeakThreshold(float newVal)  
  
#### Interface

|  IMarker

