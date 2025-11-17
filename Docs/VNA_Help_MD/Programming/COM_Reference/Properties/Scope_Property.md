##### Write/Read

|

##### [About Trigger](../../../S1_Settings/Trigger.md#scope)  
  
---|---  
  
## Scope Property

* * *

#### Description

|  Sets or returns the scope of a trigger signal. This determines whether a
trigger signal affects a single channel or all channels in the VNA. Note:
[Trigger Modes](Trigger_Mode_Property.md) Point and EverySweep require that
Trigger.Scope be set to naChannelTrigger.  
---|---  
  
####  VB Syntax

|  trigsetup.Scope = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
trigsetup |  A [TriggerSetup](../Objects/TriggerSetup_Object.md) (object)  
value |  (enum NATriggerType) \- Trigger type. Choose from: 0 - naGlobalTrigger \- a trigger signal is applied to all triggerable channels 1 - naChannelTrigger - a trigger signal is applied to the current channel. The next trigger signal will be applied to the next channel;not necessarily the next channel in numeric sequence (1-2-3-4 and so forth). 2 - naActiveChannelTrigger \- a trigger signal is sent only to the active channel.  
  
#### Return Type

|  Long Integer  
  
#### Default

|  naGlobalTrigger  
  
#### Examples

|  trigsetup.Scope = naGlobalTrigger 'Write  
trigtyp = trigsetup.Scope 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Scope(tagNATriggerType *pTrigger)  
HRESULT put_Scope(tagNATriggerType trigger)  
  
#### Interface

|  ITriggerSetup  
  
* * *

