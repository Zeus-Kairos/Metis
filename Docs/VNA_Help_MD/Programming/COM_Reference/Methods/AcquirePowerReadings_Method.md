##### Write-only

|

##### [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)  
  
---|---  
  
## AcquirePowerReadings Method - Superseded

* * *

#### Description

|  This command is replaced with [AcquirePowerReadingsEx
Method](AcquirePowerReadingsEx_Method.htm) Initiates a source power cal
acquisition.  
---|---  
  
####  VB Syntax

|  powerCalibrator.AcquirePowerReadings device [,sync]  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
powerCalibrator |  (object) \- A [SourcePowerCalibrator](../Objects/SourcePowerCalibrator_Object.md) object  
device |  (enum NAPowerAcquisitionDevice) The specific device (sensor on the power meter) to be used for the acquisition. Choose from: 0  naPowerSensor_A 1  naPowerSensor_B To use the sensor that currently corresponds to the frequency of interest, use the value from the [PowerAcquisitionDevice](../Properties/PowerAcquisitionDevice_Property.md) property.  
sync |  (boolean) Optional argument. If not specified, value is set to False. Choose from: True (1)  The method does not return until this acquisition has completed (the program calling this method is halted while waiting for the method to return). False (0)  The method initiates an acquisition then returns immediately (while the acquisition still proceeds). The program calling this method can then perform other operations during the acquisition.  
  
#### Return Type

|  None  
  
#### Default

|  Not Applicable  
  
#### Examples

|  powerCalibrator.AcquirePowerReadings naPowerSensor_A, True  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT AcquirePowerReadings(tagNAPowerAcquisitionDevice enumAcqDevice,
VARIANT_BOOL bSync);  
  
#### Interface

|  ISourcePowerCalibrator  
  
* * *

