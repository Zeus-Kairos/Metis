##### Write/Read

|

##### [About Independent Power
Calibration](../../../S3_Cals/Calibrate_All_Channels.htm#Setting_Up_an_Independent_Power_Calibration)  
  
---|---  
  
# StopFrequency (PowerCalRange) Property

* * *

#### Description

| Sets and gets the stop frequency for range <m> for source port<n>.  
---|---  
  
####  VB Syntax

| PwrrCalRange.StopFrequency = freq  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
freq | (Long) \- Variable to store the returned stop frequency.  
PwrrCalRange | A [PowerCalRange](../Objects/PowerCalRange_Object.md) (object)  
  
#### Return Type

| Double  
  
#### Default

| Not Applicable  
  
#### Example

|
CalibrateAllChannels.IndependentPowerCalibration(3).PowerCalRange(1).StopFrequency
= 21e9 'Write freq =
CalibrateAllChannels.IndependentPowerCalibration(3).PowerCalRange(1).StopFrequency
'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_StopFrequency(double* freq); HRESULT put_StopFrequency(double
freq);  
  
#### Interface

| IPowerCalRange

