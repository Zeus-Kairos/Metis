##### Write-only

|

##### [About Marker Functions](../../../S4_Collect/Markers.md#functions)  
  
---|---  
  
## SetCWFreq Method

* * *

#### Description

|  Sets the CW frequency to the frequency of the active marker. Does NOT
change sweep type. Use ONLY when the current sweep type is sweeping frequency
- NOT available in CW or Power Sweep. Use this command to first set the CW
Frequency to a value that is known to be within the current calibrated range,
THEN set [Sweep Type](../Properties/Sweep_Type_Property.md) to naPowerSweep
or naCWTimeSweep.  
---|---  
  
####  VB Syntax

|  mark.SetCWFreq  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
mark |  A Marker (object)  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  mark.SetCWFreq  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT SetCWFreq()  
  
#### Interface

|  IMarker3  
  
* * *

