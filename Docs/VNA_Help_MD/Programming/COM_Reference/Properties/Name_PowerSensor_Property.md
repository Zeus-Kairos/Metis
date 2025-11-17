##### Read-Write

|

##### [About Multiple Power
Sensors](../../../FreqOffset/Frequency_Offset_Mode.htm)  
  
---|---  
  
## Name Property

* * *

#### Description

|  Sets and returns the name of the Power Sensor (object) to be used as part
of a Guided Power Calibration.  
---|---  
  
####  VB Syntax

|  pSensor.Name = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pSensor |  A [GuidedCalibrationPowerSensor](../Objects/GuidedCalibrationPowerSensor_Object.md) (object)  
value |  (string) \- Name of the power sensor. The power sensor must be already configured as a PMAR device using this name. [Learn how to remotely configure a PMAR device.](../Objects/ExternalDevice_Object.md)  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Sensor.Name = "26GHzSesnsor" 'write value = pSensor.Name 'Read [See example
program](../../COM_Example_Programs/Perform_a_Guided_Power_Cal_using_Multiple_Power_Sensors.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_Name(BSTR *pPsensorName) HRESULT put_Name(BSTR pPsensorName)  
  
#### Interface

|  IGuidedCalibrationPowerSensor  
  
* * *

