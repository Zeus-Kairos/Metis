##### Write-only

|

##### [About Independent Power
Calibration](../../../S3_Cals/Calibrate_All_Channels.htm#Setting_Up_an_Independent_Power_Calibration)  
  
---|---  
  
# AddPowerCalRange Method

* * *

#### Description

| This command adds a power cal range for a specific port <n>. Note that
external sources are valid and specifying a source port is the same as other
remote commands. By default this will create a range with the preset
start/stop frequency and 201 points. The maximum number of ranges that can be
added is 100 (same as the maximum number of segments).  
---|---  
  
####  VB Syntax

| IndependentPwrrCalPort.AddPowerCalRange  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
IndependentPwrrCalPort | A [IndependentPowerCalibrationPort](../Objects/IndependentPowerCalibrationPort_Object.md) (object)  
  
#### Return Type

| Not Applicable  
  
#### Default

| Not Applicable  
  
#### Example

| CalibrateAllChannels.IndependentPowerCalibrationPort(3).AddPowerCalRange  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

| HRESULT AddPowerCalRange  
  
#### Interface

| IIndependentPowerCalibrationPort

