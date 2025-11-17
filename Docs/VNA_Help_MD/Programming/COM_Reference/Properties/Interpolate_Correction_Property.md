##### Write/Read

|

##### [About
Interpolation](../../../S3_Cals/Error_Correction_and_Interpolation.htm)  
  
---|---  
  
## Interpolate Correction Property

* * *

#### Description

|  Turns ON and OFF correction interpolation which calculates new error terms
when stimulus values change after calibration. When this property is ON and
error correction is being applied, the calibration subsystem attempts to
interpolate the error terms whenever the stimulus parameters are changed. When
this property is OFF under the same circumstances, error correction is turned
OFF.  
---|---  
  
####  VB Syntax

|  meas.InterpolateCorrection = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas |  A [Measurement](../Objects/Measurement_Object.md) (object)  
value |  (boolean) - Choose from: True \- Turns correction interpolation ON False \- Turns correction interpolation OFF  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Examples

|  meas.InterpolateCorrection = False  
calInterpolate = InterpolateCorrection 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_InterpolateCorrection(boolean *pVal)  
HRESULT put_InterpolateCorrection(boolean newVal)  
  
#### Interface

|  IMeasurement

