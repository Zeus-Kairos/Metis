##### Write/Read

|

##### [About Marker Search](../../../S4_Collect/Markers.md#Searching)  
  
---|---  
  
## Tracking Property

* * *

#### Description

|  This property, when on, executes the search function
[(marker.SearchFunction)](Search_Function_Property.md) every sweep. In
effect, turning Tracking ON is the same as executing one of the immediate,
one-time, "Search..." methods (such as
[SearchMin](../Methods/Search_Min_Method.md),
[SearchMax](../Methods/Search_Max_Method.md)) for every sweep.  
---|---  
  
####  VB Syntax

|  mark.Tracking = state  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
mark |  A [Marker](../Objects/Marker_Object.md) (object)  
state |  (boolean) \- Tracking state. Choose from: False - Tracking OFF True - Tracking ON  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  mark.Tracking = False 'Write  
markTracking = mark.Type 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_Tracking(VARIANT_BOOL bOn)  
HRESULT get_Tracking(VARIANT_BOOL * pbOn)  
  
#### Interface

|  IMarker

