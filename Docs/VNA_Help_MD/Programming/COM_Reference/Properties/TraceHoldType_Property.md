##### Write/Read

|

##### [About Trace
Hold](../../../S0_Start/Traces_Channels_and_Windows.htm#Trace_Hold)  
  
---|---  
  
## TraceHoldType Property

* * *

#### Description

|  Sets the type of trace hold operation to perform.  
---|---  
  
####  VB Syntax

|  meas.TraceHoldType = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas |  A [Measurement](../Objects/Measurement_Object.md) (object)  
value |  (Enum as NATraceHoldType) \- Choose from: naTraceHoldOff - Disables the Trace Hold feature. naTraceHoldMinimum - Sets Trace Hold to store the lowest measured data points. naTraceHoldMaximum - Sets Trace Hold to store the highest measured data points.  
  
#### Return Type

|  Enum  
  
#### Default

|  naTraceHoldOff  
  
#### VB Examples

|  meas.TraceHoldType = naTraceHoldOff 'Write  
hold = meas.TraceHoldType 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_TraceHoldType(tag NATraceHoldType *pVal) HRESULT
put_TraceHoldType(tag NATraceHoldType newVal)  
  
#### Interface

|  IMeasurement16  
  
* * *

