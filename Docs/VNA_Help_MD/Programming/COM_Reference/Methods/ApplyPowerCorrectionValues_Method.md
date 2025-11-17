##### Write-only

|

##### [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)  
  
---|---  
  
## ApplyPowerCorrectionValues Method Superseded

* * *

#### Description

|  This command is replaced with [ApplyPowerCorrectionValuesEx
Method](ApplyPowerCorrectionValuesEx_Method.htm). Applies the array of power
correction values to the channel memory and turns correction ON. Perform after
completing a source power cal acquisition sweep. This command does NOT save
the correction values. To save correction values, save an [instrument /
calibration state (*.cst file)](../../../S5_Output/SaveRecall.htm#SaveAsDiag)
after performing a source power cal.  
---|---  
  
####  VB Syntax

|  powerCalibrator.ApplyPowerCorrectionValues  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
powerCalibrator |  (object) \- A [SourcePowerCalibrator](../Objects/SourcePowerCalibrator_Object.md) object  
  
#### Return Type

|  None  
  
#### Default

|  Not Applicable  
  
#### Examples

|  powerCalibrator.ApplyPowerCorrectionValues  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT ApplyPowerCorrectionValues();  
  
#### Interface

|  ISourcePowerCalibrator  
  
* * *

