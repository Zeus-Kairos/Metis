##### Write-only

|

##### [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)  
  
---|---  
  
## ApplyPowerCorrectionValuesEx Method

* * *

#### Description

|  This command replaces [ApplyPowerCorrectionValues
Method](ApplyPowerCorrectionValues_Method.htm). Applies the array of power
correction values to the channel memory and turns correction ON. Perform after
completing a source power cal acquisition sweep. This command does NOT save
the correction values. To save correction values, save an [instrument /
calibration state (*.cst file)](../../../S5_Output/SaveRecall.htm#SaveAsDiag)
after performing a source power cal. Optionally, as part of the source power
calibration, perform calibration of the reference receiver used in the power
calibration. [Learn more.](../../../S3_Cals/PwrCalibration.md#Options)  
---|---  
  
####  VB Syntax

|  powerCalibrator.ApplyPowerCorrectionValuesEX [rRec]  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
powerCalibrator |  (object) \- A [SourcePowerCalibrator](../Objects/SourcePowerCalibrator_Object.md) object  
rRec |  (Enum as NASourcePowerApplyCorrectionOption) Optional argument. Choose from: 0 - naSourcePowerApplyCorrectionDefault Do NOT perform and save a calibration of the reference receiver. (Default if not specified). 1 - naIncludeReferenceReceiverPowerCal Perform and save a calibration of the reference receiver. The Cal Set, which includes only the reference receiver cal, is saved to the destination specified by [RemoteCalStoragePreference](../Properties/RemoteCalStoragePreference_Property.md).  
  
#### Return Type

|  None  
  
#### Default

|  Not Applicable  
  
#### Examples

|  powerCalibrator.ApplyPowerCorrectionValuesEX
powerCalibrator.ApplyPowerCorrectionValuesEX
(naIncludeReferenceReceiverPowerCal)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT ApplyPowerCorrectionValuesEx(enum
NASourcePowerApplyCorrectionOption option);  
  
#### Interface

|  ISourcePowerCalibrator5  
  
* * *

