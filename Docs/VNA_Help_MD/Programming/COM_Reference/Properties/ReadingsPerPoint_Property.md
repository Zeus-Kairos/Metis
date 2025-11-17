##### Write / Read

|

##### [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)

##### [About PMAR](../../../System/Configure_a_Power_Meter_As_Receiver.md)  
  
---|---  
  
## ReadingsPerPoint Property

* * *

#### Description

|  This command, along with
[ReadingsTolerance](ReadingsTolerance_Property.md), allows for settling of
the power sensor READINGS. Specifies the maximum number of power readings that
are taken at each stimulus point to allow for power meter settling. Each
reading is averaged with the previous readings at that stimulus point. When
this average meets the [ReadingsTolerance](ReadingsTolerance_Property.md)
value or this number of readings has been made, the average is returned as the
valid reading.  
---|---  
  
#### VB Syntax

|  pwrSensor.ReadingsPerPoint = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pwrCal |  A [SourcePowerCalibrator](../Objects/SourcePowerCalibrator_Object.md) (Object) or A [PowerSensorAsReceiver](../Objects/PowerSensorAsReceiver_Object.md) (Object)  
value |  (long integer)  Number of power readings. Choose any number between 3 and 100.  
  
#### Return Type

|  Long Integer  
  
#### Default

|  3  
  
#### Examples

|  pwrSensor.ReadingsPerPoint = 3 'Write  
numReadings = pwrSensor.ReadingsPerPoint 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_ReadingsPerPoint(long newVal); HRESULT
get_ReadingsPerPoint(long *pVal);  
  
#### Interface

|  ISourcePowerCalibrator IPowerSensorAsReceiver  
  
* * *

