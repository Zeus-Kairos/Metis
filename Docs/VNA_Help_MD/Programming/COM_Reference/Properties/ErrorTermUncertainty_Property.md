##### Write/Read

|

##### [About Dynamic Uncertainty](../../../S3_Cals/Dynamic_Uncertainty.md)  
  
---|---  
  
## ErrorTermUncertainty Property

* * *

#### Description

|  Sets and returns whether the uncertainties associated with the correction
error terms are being included in the uncertainty values for the measurement
trace.  
---|---  
  
#### VB Syntax

|  uncert.ErrorTermUncertainty = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
uncert |  An [Uncertainty](../Objects/Uncertainty_Object.md) (object)  
value |  (Boolean) Choose from: False \- Error Terms are NOT included. True \- Error Terms are included.  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Examples

|  uncert.ErrorTermUncertainty = True  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_ErrorTermUncertainty(VARIANT_BOOL *pState); HRESULT
put_ErrorTermUncertainty(VARIANT_BOOL state);  
  
#### Interface

|  IUncertainty  
  
* * *

