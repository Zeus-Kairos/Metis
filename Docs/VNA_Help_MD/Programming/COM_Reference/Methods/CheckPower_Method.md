##### Write-only

|

##### [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)  
  
---|---  
  
## CheckPower Method

* * *

#### Description

|  Measures power at a specified frequency. Use this method to test power
level before and/or after applying a source power calibration.  
---|---  
  
####  VB Syntax

|  pow = pwrCal.CheckPower (device, freq [,unit])  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pow |  (double) Variable to store power value returned by this method.  
pwrCal |  A [SourcePowerCalibrator](../Objects/SourcePowerCalibrator_Object.md) (object)  
device |  (enum NAPowerAcquisitionDevice) The specific sensor on the power meter to be used for the acquisition. Choose from: 0  naPowerSensor_A 1  naPowerSensor_B To use the sensor that currently corresponds to the frequency of interest, use the value from the [PowerAcquisitionDevice](../Properties/PowerAcquisitionDevice_Property.md) property.  
freq |  (double) Frequency (Hz) at which the sensor is to read the power.  
unit |  (enum NAPowerUnit) Optional argument. Choose from: naDBM  Returns the power in dBm.(default) naWATT  Returns the power in Watts.  
  
#### Return Type

|  Double  
  
#### Default

|  Not Applicable  
  
#### Examples

|  watt = powerCalibrator.CheckPower(naPowerSensor_A, 1E9, naWATT)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_CheckPower(tagNAPowerAcquisitionDevice enumAcqDevice, double
dFreq, tagNAPowerUnit enumPowerUnit, double *pdPower);  
  
#### Interface

|  ISourcePowerCalibrator2

