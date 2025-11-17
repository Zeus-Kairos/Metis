##### Write only

|

##### [About Power Calibration](../../../S3_Cals/PwrCalibration.md)  
  
---|---  
  
## SetPowerAcquisitionDevice Method

* * *

#### Description

|  Sets the power sensor channel (A or B) to be used. This performs the same
function as the Use this sensor only checkbox in the [Power Sensor
Settings](../../../S3_Cals/PwrCalibration.htm#SensorDiag) dialog. Note: This
method is only necessary when performing an SMC calibration.  
---|---  
  
####  VB Syntax

|  pwrCal.SetPowerAcquisitionDevice sensor  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pwrCal |  (Object) A [SourcePowerCalibrator](../Objects/SourcePowerCalibrator_Object.md) object  
sensor |  (enum NAPowerAcquisitionDevice) The power sensor channel. Choose from: 0  naPowerSensor_A 1  naPowerSensor_B  
  
#### Default

|  Not Applicable  
  
#### Examples

|  pwrCal.SetPowerAcquisitionDevice naPowerSensor_A  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT SetPowerAcquisitionDevice( tagNAPowerAcquisitionDevice
enumAcqDevice);  
  
#### Interface

|  ISourcePowerCalibrator3  
  
* * *

* * *

