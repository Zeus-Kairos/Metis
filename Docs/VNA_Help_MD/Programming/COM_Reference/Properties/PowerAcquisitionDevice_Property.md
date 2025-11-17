##### Read only

|

##### [About Power Calibration](../../../S3_Cals/PwrCalibration.md)  
  
---|---  
  
## PowerAcquisitionDevice Property

* * *

#### Description

|  Returns the power sensor channel (A or B) that is currently selected for
use at a specific frequency.  If
[UsePowerSensorFrequencyLimits](UsePowerSensorFrequencyLimits_Property.md) is
set to False, this property will return the sensor channel last used for a
source power calibration. This setting corresponds to the Use this sensor only
checkbox in the [Power Sensor
Settings](../../../S3_Cals/PwrCalibration.htm#SensorDiag) dialog. When
performing an SMC calibration, use [SetPowerAcquisitionDevice
Method](../Methods/SetPowerAcquisitionDevice_Method.htm) to set the power
sensor channel.  
---|---  
  
####  VB Syntax

|  sensor = pwrCal.PowerAcquisitionDevice(dFreq)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sensor |  (enum NAPowerAcquisitionDevice) The currently selected sensor channel for the specified frequency. Choose from: 0  naPowerSensor_A 1  naPowerSensor_B  
pwrCal |  A SourcePowerCalibrator (object)  
dFreq |  (double) Frequency (Hz) for the power reading of interest.  
  
#### Return Type

|  enum NAPowerAcquisitionDevice  
  
#### Default

|  Not Applicable  
  
#### Examples

|  selectedSensor = pwrCal.PowerAcquisitionDevice(1.E9) 'Write  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_PowerAcquisitionDevice(double dFreq,
tagNAPowerAcquisitionDevice* enumAcqDevice);  
  
#### Interface

|  ISourcePowerCalibrator2

