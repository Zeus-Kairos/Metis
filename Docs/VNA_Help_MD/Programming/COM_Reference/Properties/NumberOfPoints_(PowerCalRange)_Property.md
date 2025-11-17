##### Write/Read

|

##### [About Independent Power
Calibration](../../../S3_Cals/Calibrate_All_Channels.htm#Setting_Up_an_Independent_Power_Calibration)  
  
---|---  
  
# NumberOfPoints (PowerCalRange) Property

* * *

#### Description

| Sets and gets the number of points for range <m> for source port<n>.  
---|---  
  
####  VB Syntax

| PwrrCalRange.NumberOfPoints = points  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
points | (Long) \- Variable to store the returned number of points.  
PwrrCalRange | A [PowerCalRange](../Objects/PowerCalRange_Object.md) (object)  
  
#### Return Type

| Long  
  
#### Default

| Not Applicable  
  
#### Example

|
CalibrateAllChannels.IndependentPowerCalibration(3).PowerCalRange(1).NumberOfPoints
= 7 'Write points =
CalibrateAllChannels.IndependentPowerCalibration(3).PowerCalRange(1).NumberOfPoints
'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_NumberOfPoints(long* points); HRESULT put_NumberOfPoints(long
points);  
  
#### Interface

| IPowerCalRange

