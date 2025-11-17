##### Read-only

|

##### [About Limit
Testing](../../../S4_Collect/Use_Limits_to_Test_Devices.htm)  
  
---|---  
  
## LimitTestFailed Property

* * *

#### Description

|  Returns the results of limit testing for the measurement.  
---|---  
  
####  VB Syntax

|  testFailed = meas.LimitTestFailed  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
testFailed |  (boolean) Variable to store the returned value False \- Limit Test Passed  
True \- Limit Test Failed  
meas |  A Measurement (object)  
  
#### Return Type

|  Boolean  
  
#### Default

|  False returned if there is no testing in progress.  
  
#### Examples

|  Dim testRes As Boolean  
testRes = meas.LimitTestFailed  
MsgBox (testRes)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_LimitTestFailed(VARIANT_BOOL* trueIfFailed)  
  
#### Interface

|  IMeasurement

