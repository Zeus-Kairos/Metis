##### Write/Read

|

##### [About Limits](../../../S4_Collect/Use_Limits_to_Test_Devices.md)  
  
---|---  
  
## EndResponse Property

* * *

#### Description

|  When constructing a limit line, specifies the amplitude value at the end of
the limit segment.  
---|---  
  
####  VB Syntax

|  limtseg.EndResponse = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
limts |  A LimitSegment (object)  
value |  (double) - Y-axis value of the End Response limit. No units  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  Set limtseg = meas.LimitTest(1)  
limtseg.EndResponse = 10 'Write  
EndResp = limtseg.EndResponse 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_EndResponse(double *pVal)  
HRESULT put_EndResponse(double newVal)  
  
#### Interface

|  ILimitSegment

