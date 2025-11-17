##### Read/Write

|

#####  
  
---|---  
  
## OmitIsolation Property - Superseded

* * *

#### Description

|  This command is replaced with
[SetIsolationPaths](../Methods/SetIsolationPaths_Method.md) and
[GetIsolationPaths](../Methods/GetIsolationPaths_Method.md). Sets and returns
whether Isolation portion of the calibration will be performed or not.  
---|---  
  
#### VB Syntax

|  obj.OmitIsolation = bool  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  [SMCType](../Objects/SMC_Type_Object.md) (object) or [VMCType](../Objects/VMC_Type_Object.md) (object)  
bool |  (Boolean) True \- Isolation is NOT performed False \- Isolation is performed  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Examples

|  value = SMC.OmitIsolation  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_OmitIsolation (VARIANT_BOOL bState)  
HRESULT get_OmitIsolation (VARIANT_BOOL *bState)  
  
#### Interface

|  SMCType VMCType  
  
* * *

