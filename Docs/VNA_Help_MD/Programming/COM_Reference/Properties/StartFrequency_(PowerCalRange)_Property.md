##### Write/Read

|

##### [About Independent Power
Calibration](../../../S3_Cals/Calibrate_All_Channels.htm#Setting_Up_an_Independent_Power_Calibration)  
  
---|---  
  
# StartFrequency (PowerCalRange) Property

* * *

#### Description

| Sets and gets the start frequency for range <m> for source port<n>.  
---|---  
  
####  VB Syntax

| PwrrCalRange.StartFrequency = freq  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
freq | (Long) \- Variable to store the returned start frequency.  
PwrrCalRange | A [PowerCalRange](../Objects/PowerCalRange_Object.md) (object)  
  
#### Return Type

| Double  
  
#### Default

| Not Applicable  
  
#### Example

|
CalibrateAllChannels.IndependentPowerCalibration(3).PowerCalRange(1).StartFrequency
= 20e9 'Write freq =
CalibrateAllChannels.IndependentPowerCalibration(3).PowerCalRange(1).StartFrequency
'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_StartFrequency(double* freq); HRESULT put_StartFrequency(double
freq);  
  
#### Interface

| IPowerCalRange

