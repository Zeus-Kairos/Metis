##### Write/Read

|

##### [About Trigger](../../../S1_Settings/Trigger.md#scope)  
  
---|---  
  
## TriggerType Property - Superseded

* * *

#### Description

|  Note: This property has been replaced with [Scope](Scope_Property.md)
Property. Sets or returns the trigger type which determines the scope of a
trigger signal.  
---|---  
  
####  VB Syntax

|  app.TriggerType = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An Application (object)  
value |  (enum NATriggerType) \- Trigger type. Choose from:  
0 - naGlobalTrigger \- a trigger signal is applied to all triggerable channels
1 - naChannelTrigger - a trigger signal is applied to the current channel. The
next trigger signal will be applied to the next channel; not necessarily
channel 1-2-3-4.  
  
#### Return Type

|  Long Integer  
  
#### Default

|  naGlobalTrigger  
  
#### Examples

|  app.TriggerType = naGlobalTrigger 'Write  
trigtyp = app.TriggerType 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_TriggerType(tagNATriggerType *pTrigger)  
HRESULT put_TriggerType(tagNATriggerType trigger)  
  
#### Interface

|  IApplication

