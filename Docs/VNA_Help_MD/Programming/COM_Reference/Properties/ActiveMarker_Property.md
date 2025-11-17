##### Read-only

|

##### [About Markers](../../../S4_Collect/Markers.md)  
  
---|---  
  
## ActiveMarker Property

* * *

#### Description

|  Returns a handle to the Active Marker object. You can either (1) use the
handle directly to access Marker properties and methods, or (2) set a variable
to the Marker object. The variable retains a handle to the original object if
another Marker becomes active.  
---|---  
  
####  VB Syntax

|  1) meas.ActiveMarker.<setting>  
or  
2) Set mark = meas.ActiveMarker  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas |  (object) - An Measurement object  
<setting> |  A marker property (or method) and arguments  
mark |  (object) - A marker object  
  
#### Return Type

|  marker object  
  
#### Default

|  None  
  
#### Examples

|  Public mark as marker  
Set mark = meas.ActiveMarker  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_ActiveMarker(IMarker** marker)  
  
#### Interface

|  IMeasurement

