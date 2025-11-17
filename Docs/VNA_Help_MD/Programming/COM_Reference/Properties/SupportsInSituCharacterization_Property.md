##### Read-only

|

##### [About CalPod as ECal](../../../S3_Cals/CalPod_as_ECal.md)  
  
---|---  
  
## SupportsInSituCharacterization Property

* * *

#### Description

|  Returns whether the device that was specified by
[ECalID](ECalID_Property.md) is a CalPod module, which is capable of being
characterized as an in situ device.  
---|---  
  
#### VB Syntax

|  value = ecalUser.SupportsInSituCharacterization  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Boolean) True \- Device is a CalPod module False Device is NOT a CalPod module  
ecalUser |  An [ECalUserCharacterizer](../Objects/ECalUserCharacterizer_Object.md) (object)  
  
#### Return Type

|  Boolean  
Examples |  Value = ecalUser.SupportsInSituCharacterization  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SupportsInSituCharacterization(VARIANT_BOOL *value);  
  
#### Interface

|  IECalUserCharacterizer3  
  
* * *

