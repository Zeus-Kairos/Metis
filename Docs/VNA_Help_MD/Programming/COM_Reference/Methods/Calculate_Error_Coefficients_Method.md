##### Write-only

|

##### [About Performing a
Calibration](../../../S3_Cals/Measurement_Calibration.htm)  
  
---|---  
  
## CalculateErrorCoefficients Method

* * *

#### Description

|  This method is the final call in a calibration process. It calculates
error-correction terms, turns error-correction ON and saves the error-
correction terms to the channels Cal Register or a User Cal Set. Do NOT use
this command during an ECAL. Note: The destination (Cal Register or User Cal
Set) is determined by the setting of the
[RemoteCalStoragePreference](../Properties/RemoteCalStoragePreference_Property.md)
property.  
---|---  
  
####  VB Syntax

|  cal.CalculateErrorCoeffiecients  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
cal |  [Calibrator](../Objects/Calibrator_Object.md) (object)  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Cal.CalculateErrorCoeffiecients  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT CalculateErrorCoefficients()  
  
#### Interface

|  ICalibrator  
  
* * *

