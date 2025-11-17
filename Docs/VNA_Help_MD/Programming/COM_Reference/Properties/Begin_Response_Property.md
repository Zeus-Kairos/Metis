##### Write/Read

|

##### [About Limits](../../../S4_Collect/Use_Limits_to_Test_Devices.md)  
  
---|---  
  
## BeginResponse Property

* * *

#### Description

|  When constructing a limit line, specifies the amplitude value of the start
of a limit segment.  
---|---  
  
####  VB Syntax

|  limtseg.BeginResponse = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
limtseg |  A LimitSegment (object)  
value |  (double) \- Amplitude value. No units  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  Set limtseg = meas.LimitTest(1)  
limtseg.BeginResponse = 10 'Write  
BegResp = limtseg.BeginResponse 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_BeginResponse(double *pVal)  
HRESULT put_BeginResponse(double newVal)  
  
#### Interface

|  ILimitSegment

