##### Read-only

|

##### [About Trace
Statistics](../../../S4_Collect/Math_Operations.htm#statistics)  
  
---|---  
  
## StandardDeviation Property

* * *

#### Description

|  Returns the standard deviation of the measurement.  
To retreive all 3 statistics value at the same time, use
[meas.GetTraceStatistics](../Methods/Get_Trace_Statistics_Method.md)  
---|---  
  
####  VB Syntax

|  stdev = meas.StandardDeviation  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
stdev |  (single) - Variable to store standard deviation value  
meas |  A Measurement (object)  
  
#### Return Type

|  Single  
  
#### Default

|  Not applicable  
  
#### Examples

|  stdev = meas.StandardDeviation 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_StandardDeviation(float* stdDeviation)  
  
#### Interface

|  IMeasurement

