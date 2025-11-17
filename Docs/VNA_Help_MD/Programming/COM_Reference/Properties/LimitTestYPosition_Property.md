##### Write/Read

|

##### [About Limit
Test](../../../S4_Collect/Use_Limits_to_Test_Devices.htm#Limitdiag)  
  
---|---  
  
## LimitTestYPosition Property

* * *

#### Description

|  Sets and returns the Y-axis position of the Limit Line Pass/Fail indicator
on the VNA screen. The lower-left corner of the Pass/Fail indicator is the
point of reference for positioning.  
---|---  
  
####  VB Syntax

|  win.LimitTestYPosition = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
win |  A [NAWindow](../Objects/NAWindow_Object.md) (object)  
value |  (Double) Y-axis position. Choose a value between 0 (bottom) and 10 (top).  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  win.LimitTestYPosition = 3 'Write value =
app.ActiveNAWindow.LimitTestYPosition 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_LimitTestYPosition(double *pVal) HRESULT
put_LimitTestYPosition(double newVal)  
  
#### Interface

|  INAWindow4  
  
* * *

