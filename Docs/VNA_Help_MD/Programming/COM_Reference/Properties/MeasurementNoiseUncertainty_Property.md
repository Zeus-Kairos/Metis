##### Write/Read

|

##### [About Dynamic Uncertainty](../../../S3_Cals/Dynamic_Uncertainty.md)  
  
---|---  
  
## MeasurementNoiseUncertainty Property

* * *

#### Description

|  Sets and returns whether the noise contribution is currently included in
the uncertainty values for the measurement trace.  
---|---  
  
#### VB Syntax

|  uncert.MeasurementNoiseUncertainty = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
uncert |  An [Uncertainty](../Objects/Uncertainty_Object.md) (object)  
value |  (Boolean) Choose from: False \- Noise contribution is NOT included. True \- Noise contribution is included.  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Examples

|  uncert.MeasurementNoiseUncertainty = True  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_MeasurementNoiseUncertainty(VARIANT_BOOL *pState); HRESULT
put_MeasurementNoiseUncertainty(VARIANT_BOOL state);  
  
#### Interface

|  IUncertainty  
  
* * *

