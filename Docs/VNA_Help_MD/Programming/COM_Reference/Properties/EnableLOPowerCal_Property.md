##### Write/Read  
  
---  
  
## EnableLOPowerCal Property

* * *

#### Description

|  Sets and returns whether or not the LO power cal step is included in the
cal steps when a Cal is performed. Set LO Power Level using  
---|---  
  
####  VB Syntax

|  obj.EnableLOPowerCal(n) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  A [SMCType](../Objects/SMC_Type_Object.md) (object) A [VMCType](../Objects/VMC_Type_Object.md) (object) A [SweptIMDCal](../Objects/SweptIMDCal_Object.md) (object) A [NoiseCal](../Objects/NoiseCal_Object.md) (object)  
n |  LO Stage. Choose 1. (Only single LO allowed)  
value |  (Boolean) Choose from: False - Skips over the LO Power Cal when calibrating. True - Includes a step for LO Power Cal when calibrating.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  imd.EnableLOPowerCal(1)= true 'Write  
loPwrCal = imd.EnableLOPowerCal(1) 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_EnableLOPowerCal (long stage, BOOL *enable) HRESULT
put_EnableLOPowerCal (long stage, BOOL enable)  
  
#### Interface

|  ISMCType IVMCType ISweptIMD2 INoiseCal2  
  
* * *

