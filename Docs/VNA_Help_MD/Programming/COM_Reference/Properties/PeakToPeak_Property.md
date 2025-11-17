##### Read-only

|

##### [About Trace
Statistics](../../../S4_Collect/Math_Operations.htm#statistics)  
  
---|---  
  
## PeakToPeak Property

* * *

#### Description

|  Returns the Peak to Peak value of the measurement.To retreive all 3
statistics value at the same time, use
[meas.GetTraceStatistics](../Methods/Get_Trace_Statistics_Method.md)  
---|---  
  
####  VB Syntax

|  pp = meas.PeakToPeak  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pp |  (single) \- Variable to store peak-to-peak value  
meas |  A Measurement (object)  
  
#### Return Type

|  Single  
  
#### Default

|  Not applicable  
  
#### Examples

|  pp = meas.PeakToPeak 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_PeakToPeak(float* pp)  
  
#### Interface

|  IMeasurement

