##### Write/Read

|

##### [About ECAL orientation](../../../S3_Cals/Using_ECal.md#Orient)  
  
---|---  
  
## AutoOrient Property

* * *

#### Description

|  Sets ECAL module automatic orientation ON or OFF.  
---|---  
  
####  VB Syntax

|  obj.AutoOrient = bool  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  [SMCType](../Objects/SMC_Type_Object.md) (object) or [VMCType](../Objects/VMC_Type_Object.md) (object)  
  
#### bool

|  (Boolean) True \- Set AutoOrientation ON False \- Set AutoOrientation OFF  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Examples

|  Smc.AutoOrient = True  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_AutoOrient(VARIANT_BOOL bAutoOrient); HRESULT
get_AutoOrient(VARIANT_BOOL *bAutoOrient);  
  
#### Interface

|  SMCType VMCType

