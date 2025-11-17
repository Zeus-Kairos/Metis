##### Write/Read

|

##### [About Marker Search](../../../S4_Collect/Markers.md#Searching)  
  
---|---  
  
## TargetValue Property

* * *

#### Description

|  Sets the target value for the marker when doing Target Searches
([SearchTargetLeft](../Methods/Search_Target_Left_Method.md),
[SearchTarget](../Methods/Search_Target_Method.md),
[SearchTargetRight](../Methods/Search_Target_Right_Method.md)).  
---|---  
  
####  VB Syntax

|  mark.TargetValue = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
mark |  A [Marker](../Objects/Marker_Object.md) (object)  
value |  (single) - Target value. Choose any number between: -500 and 500  
  
#### Return Type

|  Single  
  
#### Default

|  0  
  
#### Examples

|  mark.TargetValue = 10.5 'Write  
target = mark.TargetValue 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_TargetValue(float *pVal)  
HRESULT put_TargetValue(float newVal)  
  
#### Interface

|  IMarker

