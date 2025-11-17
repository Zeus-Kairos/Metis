##### Write/Read

|

##### [About Dynamic Uncertainty](../../../S3_Cals/Dynamic_Uncertainty.md)  
  
---|---  
  
## CableRepeatabilityUncertainty Property

* * *

#### Description

|  Sets and returns whether the cable/connection repeatability contribution is
currently included in the uncertainty values for the measurement trace.  
---|---  
  
#### VB Syntax

|  uncert.CableRepeatabilityUncertainty = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
uncert |  An [Uncertainty](../Objects/Uncertainty_Object.md) (object)  
value |  (Boolean) Choose from: False \- Cable repeatability is NOT included. True \- Cable repeatability IS included.  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Examples

|  uncert.CableRepeatabilityUncertainty = True  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_CableRepeatabilityUncertainty(VARIANT_BOOL *pState); HRESULT
put_CableRepeatabilityUncertainty(VARIANT_BOOL state);  
  
#### Interface

|  IUncertainty  
  
* * *

