##### Write/Read

|

##### [About Reference Markers](../../../S4_Collect/Markers.md#reference)  
  
---|---  
  
## DeltaMarker Property

* * *

#### Description

|  Sets a marker as a delta marker. The reference marker must already be
turned ON. See [meas.ReferenceMarkerState](ReferenceMarkerState_Property.md)  
---|---  
  
####  VB Syntax

|  mark.DeltaMarker = state  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
mark |  A [Marker](../Objects/Marker_Object.md) (object)  
state |  (boolean) - True - marker is a delta marker False - marker is NOT a delta marker  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  mark.DeltaMarker = True 'Write  
delta = mark.DeltaMarker 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_DeltaMarker(VARIANT_BOOL bState)  
HRESULT put_DeltaMarker(VARIANT_BOOL *bState)  
  
#### Interface

|  IMarker

