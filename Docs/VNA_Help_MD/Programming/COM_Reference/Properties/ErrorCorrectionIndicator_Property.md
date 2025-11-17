##### Read-only

|

##### [About Error
Correction](../../../S3_Cals/Error_Correction_and_Interpolation.htm)  
  
---|---  
  
## ErrorCorrectionIndicator Property

* * *

#### Description

|  Returns the error correction state for the measurement.  
---|---  
  
####  VB Syntax

|  value = meas.ErrorCorrectionIndicator  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Enum) Error correction state.

  * 0 - naErrorCorrectionIndicator_None \- No error correction
  * 1 - naErrorCorrectionIndicator_Master \- Original error correction terms applied.
  * 2 - naErrorCorrectionIndicator_Interpolated \- Error terms are interpolated. [Learn more](../../../S3_Cals/Error_Correction_and_Interpolation.md)
  * 3 - naErrorCorrectionIndicator_Delta \- Delta Match calibration terms. [Learn more](../../../S3_Cals/Delta_Match_Calibration.md)
  * 4 - naErrorCorrectionIndicator_Invalid  Error terms are not valid.

  
meas |  A Measurement (object)  
  
#### Return Type

|  Enum as NAErrorCorrectionIndicator  
  
#### Default

|  See [Error
Correction](../../../S3_Cals/Error_Correction_and_Interpolation.htm)  
  
#### Examples

|  errcorr = meas.ErrorCorrectionIndicator 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_ErrorCorrectionIndicator (enum NAErrorCorrectionIndicator
*pIndicator);  
  
#### Interface

|  IMeasurement14  
  
* * *

