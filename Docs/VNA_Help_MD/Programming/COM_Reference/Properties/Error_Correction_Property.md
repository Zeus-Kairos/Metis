##### Write/Read

|

##### [About Error
Correction](../../../S3_Cals/Error_Correction_and_Interpolation.htm)  
  
---|---  
  
## ErrorCorrection Property

* * *

#### Description

|  Sets (or returns) error correction ON or OFF for the measurement.  
---|---  
  
####  VB Syntax

|  meas.ErrorCorrection = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas |  A Measurement (object)  
value |  (boolean) False \- Turns error correction OFF True \- Turns error correction ON  
  
#### Return Type

|  Boolean  
  
#### Default

|  See [Error
Correction](../../../S3_Cals/Error_Correction_and_Interpolation.htm)  
  
#### Examples

|  meas.ErrorCorrection = True 'Write  
errcorr = meas.ErrorCorrection 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_ErrorCorrection (VARIANT_BOOL bState)  
HRESULT get_ErrorCorrection (VARIANT_BOOL *bState)  
  
#### Interface

|  IMeasurement

