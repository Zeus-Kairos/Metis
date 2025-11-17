##### Write/Read

|

##### [About Auxiliary
Triggering](../../../S1_Settings/External_Triggering.htm#AuxTrigDiag)  
  
---|---  
  
## TriggerOutInterval Property

* * *

#### Description

|  Specifies how often a trigger output signal is sent.  
---|---  
  
####  VB Syntax

|  auxTrig.TriggerOutInterval = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
auxTrig |  An [AuxTrigger](../Objects/AuxTrigger_Object.md) (object)  
value |  (single) \- Choose from: 0 - naTriggerModePoint \- a single data point is measured with each trigger signal the channel receives. Subsequent trigger signals continue to go to the channel in Point mode until the channel measurements are complete. This is effectively the same as [trigger point mode](../../../S1_Settings/Trigger.md#state_point). 1 - naTriggerModeMeasurement - entire traces are swept with a trigger signal. which and how many traces depends on the Scope setting.  
  
#### Return Type

|  Enum  
  
#### Default

|  1 - naTriggerModeMeasurement  
  
#### Exaamples

|  auxTrig.TriggerOutInterval = naTriggerModeMeasurement 'Write  
value = auxTrig.TriggerOutInterval 'Read the value  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_TriggerOutInterval(enum NATriggerMode *val);  
HRESULT put_TriggerOutInterval(enum NATriggerMode val);  
  
#### Interface

|  IAuxTrigger  
  
* * *

