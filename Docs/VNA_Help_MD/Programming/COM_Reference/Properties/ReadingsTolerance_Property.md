##### Write / Read

|

##### [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)

##### [About PMAR](../../../System/Configure_a_Power_Meter_As_Receiver.md)  
  
---|---  
  
## ReadingsTolerance Property

* * *

#### Description

|  This command, along with [ReadingsPerPoint
Property](ReadingsPerPoint_Property.htm) allows for settling of the power
sensor READINGS. Each power reading is averaged with the previous readings at
each stimulus point. When the average meets this tolerance value or the
maximum [ReadingsPerPoint](ReadingsPerPoint_Property.md) has been made, the
average is returned as the valid reading.  
---|---  
  
#### VB Syntax

|  pwrSens.ReadingsTolerance = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pwrCal |  A [SourcePowerCalibrator](../Objects/SourcePowerCalibrator_Object.md) (Object) or A [PowerSensorAsReceiver](../Objects/PowerSensorAsReceiver_Object.md) (Object)  
value |  (Double)  Power meter settling tolerance value in dB. Choose any number between 0 and 5.  
  
#### Return Type

|  Double  
  
#### Default

|  .05 dB  
  
#### Examples

|  pwrSens.ReadingsTolerance = .1 'Write  
ReadTol = pwrSensor.ReadingsTolerance 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_ReadingsTolerance( double *pVal); HRESULT
put_ReadingsTolerance( double newVal);  
  
#### Interface

|  ISourcePowerCalibrator3 IPowerSensorAsReceiver  
  
* * *

