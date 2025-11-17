##### Write/Read

|

##### [About Trigger](../../../S1_Settings/Trigger.md#scope)  
  
---|---  
  
## AcceptTriggerBeforeArmed Property

* * *

#### Description

|  Determines what happens to an EDGE trigger signal if it occurs before the
VNA is ready to be triggered. (LEVEL trigger signals are always ignored.) For
more information, see [External
triggering](../../../S1_Settings/External_Triggering.htm#ExternalDiag).  
---|---  
  
####  VB Syntax

|  trigsetup.AcceptTriggerBeforeArmed = boolean  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
trigsetup |  A [TriggerSetup2](../Objects/TriggerSetup_Object.md) (object)  
boolean |  Choose from: False - A trigger signal is ignored if it occurs before the VNA is ready to be triggered. True - A trigger signal is remembered and then used when the VNA becomes armed (ready to be triggered). The VNA remembers only one trigger signal.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  trigsetup.AcceptTriggerBeforeArmed = True 'Write  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_AcceptTriggerBeforeArmed( BOOL *pVal); HRESULT
put_AcceptTriggerBeforeArmed( BOOL newVal);  
  
#### Interface

|  ITriggerSetup2

