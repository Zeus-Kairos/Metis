##### Write/Read

|

##### [About Trigger Source](../../../S1_Settings/Trigger.md#Source)  
  
---|---  
  
## TriggerSignal Property - Superseded

* * *

#### Description

|  Note: This command has been replaced by [Source](Source_Property.md)
Property Sets or returns the trigger source.  
---|---  
  
####  VB Syntax

|  app.TriggerSignal = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An Application (object)  
value |  (enum NATriggerSignal) - Choose from: 0 - naTriggerInternal \- free run 1 - naTriggerExternalPositive \- a trigger signal is generated when a TTL high is sensed on the external trigger pin of the Aux IO connector 2 - naTriggerExternalNegative \- a trigger signal is generated when a TTL low is sensed on the external trigger pin of the Aux IO connector. 3 - naTriggerManual \- manual trigger source; use app.[ManualTrigger](../Methods/Manual_Trigger_Method.md) to send a trigger signal. 4 \- naTriggerExternalHigh - a trigger signal is generated when a TTL high is sensed on the external trigger pin of the Aux IO connector 5 \- naTriggerExternalLow - a trigger signal is generated when a TTL low is sensed on the external trigger pin of the Aux IO connector  
  
#### Return Type

|  Long Integer  
  
#### Default

|  naTriggerInternal  
  
#### Examples

|  app.TriggerSignal = naTriggerExternalPositive 'Write  
trigsign = app.TriggerSignal 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_TriggerSignal(tagNATriggerSignal *pSignal)  
HRESULT put_TriggerSignal(tagNATriggerSignal signal)  
  
#### Interface

|  IApplication

