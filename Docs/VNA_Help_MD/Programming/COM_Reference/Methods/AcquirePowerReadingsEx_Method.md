##### Write-only

|

##### [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)  
  
---|---  
  
## AcquirePowerReadingsEx Method

* * *

#### Description

|  This command replaces [AcquirePowerReadings
Method](AcquirePowerReadings_Method.htm) Initiates a source power cal
acquisition.  
---|---  
  
####  VB Syntax

|  powerCalibrator.AcquirePowerReadingsEx calMethod, acqdevice [,sync]  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
powerCalibrator |  (object) \- A [SourcePowerCalibrator](../Objects/SourcePowerCalibrator_Object.md) object  
calMethod |  (enum NASourcePowerCalMethod) Selects the calibration method to be used for the source power cal acquisition. 0  naPowerMeter Use power meter for all readings. 1 - naPowerMeterAndReceiver Power meter for the first iteration; then use the reference receiver for remaining readings if necessary. 2 - naReceiver Use VNA measurement receiver for all readings.  
acqdevice |  (String) The specific acquisition device to be used. NOT case sensitive. Choose from: If calMethod = naPowerMeter or naPowerMeterAndReceiver, choose from:

  * ASEN -- Sensor on power meter channel A.
  * BSEN -- Sensor on power meter channel B.
  * To use the sensor that currently corresponds to the frequency of interest, use the value from the [PowerAcquisitionDevice](../Properties/PowerAcquisitionDevice_Property.md) property.

If calMethod = naReceiver, choose from:

  * The receiver names for your specific VNA using either physical receiver notation or [logical receiver notation](../../../S1_Settings/Measurement_Parameters.md#RecNotation). For example, a1 or "A".
  * Any configured PMAR device name. [Learn more about PMAR Devices](../../../System/Configure_an_External_Device.md). [See PMAR commands](../Objects/ExternalDevices_Collection.md)

  
[sync] |  (boolean) Optional argument. If not specified, value is set to False. Choose from: True (1)  The method does not return until this acquisition has completed (the program calling this method is halted while waiting for the method to return). False (0)  The method initiates an acquisition then returns immediately (while the acquisition still proceeds). The program calling this method can then perform other operations during the acquisition.  
  
#### Return Type

|  None  
  
#### Default

|  Not Applicable  
  
#### Examples

|  powerCalibrator.AcquirePowerReadingsEx naPowerMeter, "asen", True
powerCalibrator.AcquirePowerReadingsEx naReceiver, "b2"
powerCalibrator.AcquirePowerReadingsEx naReceiver, "MyPMAR"  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT AcquirePowerReadingsEx (tagNASourcePowerCalMethod enumCalMethod,
BSTR bstrAcqDevice, VARIANT_BOOL bSync);  
  
#### Interface

|  ISourcePowerCalibrator4  
  
* * *

