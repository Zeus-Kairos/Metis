##### Read-only

|

##### [About Trace
Statistics](../../../S4_Collect/Math_Operations.htm#statistics)  
  
---|---  
  
## Mean Property

* * *

#### Description

|  Returns the mean value of the measurement . To retrieve all 3 statistics
value at the same time, use
[meas.GetTraceStatistics](../Methods/Get_Trace_Statistics_Method.md)  
---|---  
  
####  VB Syntax

|  average = meas.Mean  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
average |  (single) - Variable to store mean value  
meas |  A Measurement (object)  
  
#### Return Type

|  Single  
  
#### Default

|  Not applicable  
  
#### Examples

|  Dim average as Single  
average = meas.Mean 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Mean(float* mean)  
  
#### Interface

|  IMeasurement

