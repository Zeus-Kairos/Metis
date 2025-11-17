##### Write/Read

|

##### [About Trigger](../../../S1_Settings/Trigger.md#scope)  
  
---|---  
  
## ExternalTriggerDelay Property

* * *

#### Description

|  Sets and reads the trigger delay for all measurements in the CHANNEL. This
delay is only applied while in [app.Source =
naTriggerSourceExternal](Source_Property.htm) and [trigsetup.Scope =
naChannelTrigger](Scope_Property.htm) . After an external trigger is applied,
the start of the sweep is delayed for the specified delay value plus any
inherent latency. To apply a trigger delay for all channels (Global), use
[TriggerDelay Property.](TriggerDelay_Property.md)  
---|---  
  
####  VB Syntax

|  chan.ExternalTriggerDelay = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan |  A [Channel](../Objects/Channel_Object.md) (object)  
value |  Double\- Trigger delay value in seconds. Range is from 0 to 3 seconds.  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  chan.ExternalTriggerDelay = .003 'Write  
delay = chan.ExternalTriggerDelay 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_ExternalTriggerDelay(double *delay); HRESULT
put_ExternalTriggerDelay(double delay)  
  
#### Interface

|  IChannel6

