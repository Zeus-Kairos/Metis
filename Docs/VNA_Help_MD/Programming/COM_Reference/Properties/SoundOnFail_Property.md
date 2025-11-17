##### Write/Read

|

##### [About Limits](../../../S4_Collect/Use_Limits_to_Test_Devices.md)  
  
---|---  
  
## SoundOnFail Property

* * *

#### Description

|  Turns ON or OFF the audio indicator for limit failures.  
---|---  
  
####  VB Syntax

|  limitst.SoundOnFail = state  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
limitst |  A LimitTest (object)  
state |  (boolean) False \- Turns the sound OFF  
True \- Turns the sound ON  
  
#### Return Type

|  Long Integer  
  
#### Default

|  True  
  
#### Examples

|  Limttest.SoundOnFail = False 'Write  
sound = Limttest.SoundOnFail 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_SoundOnFail(VARIANT_BOOL *pVal)  
HRESULT put_SoundOnFail(VARIANT_BOOL newVal)  
  
#### Interface

|  ILimitTest

