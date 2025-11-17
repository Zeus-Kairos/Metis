##### Read / Write

|

##### [About CalPod as ECal](../../../S3_Cals/CalPod_as_ECal.md)  
  
---|---  
  
## InSituCharacterization Property

* * *

#### Description

|  Sets or returns whether the device (CalPod module) that was specified by
[ECalID](ECalID_Property.md) will be characterized as an in situ device.
[Learn more](../../../S3_Cals/CalPod_as_ECal.md#InSitu).  
---|---  
  
#### VB Syntax

|  ecalUser.InSituCharacterization = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
ecalUser |  An [ECalUserCharacterizer](../Objects/ECalUserCharacterizer_Object.md) (object)  
  
#### value

|  (Boolean) In situ state. Choose from: True \- Characterize the CalPod
module as an in situ device. False Do NOT characterize the CalPod module as an
in situ device.  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Examples

|  ecalUser.InSituCharacterization = False ' Write  
Value = ecalUser.InSituCharacterization  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_InSituCharacterization(VARIANT_BOOL *value); HRESULT
put_InSituCharacterization(VARIANT_BOOL value);  
  
#### Interface

|  IECalUserCharacterizer3  
  
* * *

