##### Write/Read

|

##### [About Limit
Test](../../../S4_Collect/Use_Limits_to_Test_Devices.htm#Limitdiag)  
  
---|---  
  
## LimitTestXPosition Property

* * *

#### Description

|  Sets and returns the X-axis position of the Limit Line Pass/Fail indicator
on the VNA screen. The lower-left corner of the Pass/Fail indicator is the
point of reference for positioning.  
---|---  
  
####  VB Syntax

|  win.LimitTestXPosition = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
win |  A [NAWindow](../Objects/NAWindow_Object.md) (object)  
value |  (Double) X-axis position. Choose a value between 0 (far left) and 10 (far right).  
  
#### Return Type

|  Double  
  
#### Default

|  7  
  
#### Examples

|  win.LimitTestXPosition = 3 'Write value =
app.ActiveNAWindow.LimitTestXPosition 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_LimitTestXPosition(double *pVal) HRESULT
put_LimitTestXPosition(double newVal)  
  
#### Interface

|  INAWindow4  
  
* * *

