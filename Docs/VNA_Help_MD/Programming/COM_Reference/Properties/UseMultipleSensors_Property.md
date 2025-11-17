##### Read/Write

|

#####  
  
---|---  
  
## UseMultipleSensors Property

* * *

#### Description

|  Enable and disable the use of multiple power sensors during a guided
calibration.  
---|---  
  
#### VB Syntax

|  guidPwrSensors.UseMultipleSensors = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
guidPwrSensors |  [GuidedCalibrationPowerSensors Collection](../Objects/GuidedCalibrationPowerSensors_Collection.md)  
value |  (Boolean) True Use multiple power sensors False Do NOT use multiple power sensors  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  guidedPwrSensors.UseMultipleSensors = True value =
guidedPwrSensors.UseMultipleSensors  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_UseMultipleSensors(VARIANT_BOOL* val); HRESULT
put_UseMultipleSensors(VARIANT_BOOL newVal);  
  
#### Interface

|  IGuidedCalibrationPowerSensors  
  
* * *

