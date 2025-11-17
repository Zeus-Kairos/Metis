##### Write-only

|

##### [About Marker Functions](../../../S4_Collect/Markers.md#functions)  
  
---|---  
  
## SetStart Method

* * *

#### Description

|  Changes the start stimulus to the stimulus value of the marker. The stop
stimulus stays the same and the span is adjusted. This command does not work
with channels that are in [CW](../../../S1_Settings/Sweep.md#SweepTypeDiag)
or [Segment Sweep](../../../S1_Settings/Sweep.md#segment) mode.  
---|---  
  
####  VB Syntax

|  mark.SetStart  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
mark |  A Marker (object)  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  mark.SetStart  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT SetStart()  
  
#### Interface

|  IMarker

