##### Write/Read

|

##### [About Trigger](../../../S1_Settings/Trigger.md#scope)  
  
---|---  
  
## TriggerDelay Property

* * *

#### Description

|  Sets and reads the trigger delay for all measurements (GLOBAL). This delay
is only applied while in [app.Source =
naTriggerSourceExternal](Source_Property.htm) and [trigsetup.Scope =
naGlobalTrigger](Scope_Property.htm) . After an external trigger is applied,
the start of the sweep is delayed for the specified delay value plus any
inherent latency. To apply a trigger delay for a channel only, use
[ExternalTriggerDelay Property](ExternalTriggerDelay_Property.md).  
---|---  
  
####  VB Syntax

|  app.TriggerDelay = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
value |  Double\- Trigger delay value in seconds. Range is from 0 to 3.  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  app.TriggerDelay = .003 'Write  
delay = app.TriggerDelay 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_TriggerDelay(double *delay); HRESULT put_TriggerDelay(double
delay)  
  
#### Interface

|  IApplication

