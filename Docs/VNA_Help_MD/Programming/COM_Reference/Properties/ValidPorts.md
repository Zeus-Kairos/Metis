##### Read-only

|

##### [About Independent Power
Calibration](../../../S3_Cals/Calibrate_All_Channels.htm#Setting_Up_an_Independent_Power_Calibration)  
  
---|---  
  
# ValidPorts Property

* * *

#### Description

| Queries available ports for independent power calibration.  
---|---  
  
####  VB Syntax

| value = IndependentPwrrCal.ValidPorts  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value | (Variant) \- Variable to store the returned ports.  
IndependentPwrrCal | A [IndependentPowerCalibration](../Objects/IndependentPowerCalibration_Object.md) (object)  
  
#### Return Type

| Variant  
  
#### Default

| Not Applicable  
  
#### Example

| value = CalibrateAllChannels.IndependentPowerCalibration.ValidPorts 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT ValidPorts(VARIANT* ports);  
  
#### Interface

| IIndependentPowerCalibration

