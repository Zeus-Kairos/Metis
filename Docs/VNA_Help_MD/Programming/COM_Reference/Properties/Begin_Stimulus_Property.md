##### Write/Read

|

##### [About Limits](../../../S4_Collect/Use_Limits_to_Test_Devices.md)  
  
---|---  
  
## BeginStimulus Property

* * *

#### Description

|  When constructing a limit line, specifies the beginning X-axis value.  
---|---  
  
####  VB Syntax

|  limtseg.BeginStimulus = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
limtseg |  A LimitSegment (object)  
value |  (double) - Stimulus value. No units  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  Set limtseg = meas.LimitTest(1)  
limtseg.Type = naLimitSegmentType_Maximum  
limtseg.BeginStimulus = 3e9  
limtseg.EndStimulus = 4e9  
limtseg.BeginResponse = 10  
limtseg.EndResponse = 10  
BegStim = limtseg.BeginStimulus 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_BeginStimulus(double *pVal)  
HRESULT put_BeginStimulus(double newVal)  
  
#### Interface

|  ILimitSegment

