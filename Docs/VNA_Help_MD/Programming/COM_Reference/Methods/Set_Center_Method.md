##### Write-only

|

##### [About Marker Functions](../../../S4_Collect/Markers.md#functions)  
  
---|---  
  
## SetCenter Method

* * *

#### Description

|  Changes the center stimulus to the stimulus value of the marker. The start
stimulus stays the same and the stop is adjusted. This command does not work
with channels that are in [CW](../../../S1_Settings/Sweep.md#SweepTypeDiag)
or [Segment Sweep](../../../S1_Settings/Sweep.md#segment) mode.  
---|---  
  
####  VB Syntax

|  mark.SetCenter  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
mark |  A [Marker](../Objects/Marker_Object.md) (object)  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  mark.SetCenter  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT SetCenter()  
  
#### Interface

|  IMarker

