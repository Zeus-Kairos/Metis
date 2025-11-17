##### Read-only

|

##### [About Traces](../../../S0_Start/Traces_Channels_and_Windows.md#trace)  
  
---|---  
  
## Measurement Property

* * *

#### Description

|  Returns the measurement handle of the trace object. Learn the difference
between a [Trace and a Measurement](../Objects/Measurement_Object.md).  
---|---  
  
####  VB Syntax

|  myMeas = trace.Measurement  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
myMeas |  (Object) Variable to store the returned [Measurement](../Objects/Measurement_Object.md) object.  
trace |  A [Trace](../Objects/Trace_Object.md) (object)  
  
#### Return Type

|  Object  
  
#### Default

|  Not Applicable  
  
#### Examples

|  myMeas = myTrace.Measurement  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_Measurement(IMeasurement** ppMeas);  
  
#### Interface

|  ITrace2  
  
* * *

* * *

