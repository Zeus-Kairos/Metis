##### Write/Read

|

##### [About Limits](../../../S4_Collect/Use_Limits_to_Test_Devices.md)  
  
---|---  
  
## EndStimulus Property

* * *

#### Description

|  When constructing a limit line, specifies the stimulus value for the end of
the segment.  
---|---  
  
####  VB Syntax

|  limtseg.EndStimulus = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
limtseg |  A LimitSegment (object)  
value |  (double) - End Stimulus X-axis value. No units  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  Set limtseg = meas.LimitTest(1)  
limtseg.EndStimulus = 8e9 'Write  
EndStim = limtseg.EndStimulus 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_EndStimulus(double *pVal)  
HRESULT put_EndStimulus(double newVal)  
  
#### Interface

|  ILimitSegment

