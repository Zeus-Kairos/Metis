##### Write / Read

|

##### [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)  
  
---|---  
  
## UsePowerSensorFrequencyLimits Property

* * *

#### Description

|  Specifies if subsequent calls to the
[AcquirePowerReadings](../Methods/AcquirePowerReadings_Method.md) method will
observe frequency values of the
[MinimumFrequency](MinimumFrequency_sourceCal_Property.md) and
[MaximumFrequency](MaximiumFrequency_sourceCal_Property.md) properties.  
---|---  
  
####  VB Syntax

|  pwrCal.UsePowerSensorFrequencyLimits = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pwrCal |  (object)  A SourcePowerCalibrator (object)  
value |  (boolean) -  False  Do not use power sensor frequency limits. An acquisition will use just one power sensor for the entire sweep, regardless of frequency. True  Use power sensor frequency limits. A requested acquisition will only succeed for those frequency points which fall between the MinimumFrequency and MaximumFrequency values of that PowerSensor. An acquisition will pause in mid-sweep if the frequency is about to exceed the MaximumFrequency value. When the sweep is paused in this manner, a sensor connected to the other channel input of the power meter can be connected to the measurement port in place of the previous sensor, and then the sweep completed by another call to AcquirePowerReadings. However, the MaximumFrequency specified for the second sensor would need to be sufficient for the sweep to complete.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  Set powerCalibrator = pna.SourcePowerCalibrator  
powerCalibrator.UsePowerSensorFrequencyLimits = True'Write  
FreqCheck = powerCalibrator.UsePowerSensorFrequencyLimits 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_UsePowerSensorFrequencyLimits(VARIANT_BOOL bState); HRESULT
get_UsePowerSensorFrequencyLimits(VARIANT_BOOL *bState);  
  
#### Interface

|  ISourcePowerCalibrator

