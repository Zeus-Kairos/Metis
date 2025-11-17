##### Write-only

|

##### [About Multiple Power
Sensors](../../../S3_Cals/Guided_Power_Calibration.htm#MultipleSensors)  
  
---|---  
  
## Add (GuidedPowerSensors) Method

* * *

#### Description

|  Adds a power sensor name and item number to be used during a source power
calibration. Use when multiple power sensors are to be used to calibrate the
entire frequency span. The Name is used to recognize the sensor in the User
Interface. Item numbers in the
[GuidedCalibrationPowerSensors](../Objects/GuidedCalibrationPowerSensors_Collection.md)
collection are used to refer to the power sensor remotely. Use the [Count
Property](../Properties/Count_Property.htm) to return the number of power
sensor items that are configured for use on the channel. The port number to be
calibrated is set using the [PerformPowerCalibration
Property](../Properties/PerformPowerCalibration_Property.htm). [Learn about
using multiple power
sensors](../../../S3_Cals/Guided_Power_Calibration.htm#MultipleSensors)  
---|---  
  
#### VB Syntax

|  sensors.Add (name)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sensors |  A [GuidedCalibrationPowerSensors](../Objects/GuidedCalibrationPowerSensors_Collection.md) (collection)  
name |  (String) \- Name of the power sensor to add. The power sensor must be already configured as a PMAR device using this name. [Learn how to remotely configure a PMAR device.](../Objects/ExternalDevice_Object.md)  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  sensors.Add "pmar2" [See Example
program](../../COM_Example_Programs/Perform_a_Guided_Power_Cal_using_Multiple_Power_Sensors.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT Add(BSTR name);  
  
#### Interface

|  IGuidedCalibrationPowerSensors  
  
* * *

