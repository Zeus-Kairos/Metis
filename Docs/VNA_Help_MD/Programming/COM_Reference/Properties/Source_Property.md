##### Write/Read

|

##### [About Trigger Source](../../../S1_Settings/Trigger.md#Source)  
  
---|---  
  
## Source Property

* * *

#### Description

|  Sets or returns the source of triggering on the VNA and PNA-X.  
---|---  
  
####  VB Syntax

|  trigSetup.Source = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
trigSetup |  A [TriggerSetup](../Objects/TriggerSetup_Object.md) (object)  
value |  (enum NATriggerSource) \- Choose from: 0 - naTriggerSourceInternal \- free run 1 - naTriggerSourceManual \- manual trigger source; use app.[ManualTrigger](../Methods/Manual_Trigger_Method.md) to send a trigger signal. 2 \- naTriggerSouceExternal - a trigger signal is generated when a signal is sensed on the appropriate external trigger input connector. Use [ExternalTriggerConnectionBehavior](ExternalTriggerConnectionBehavior_Property.md) to configure the characteristics of the external trigger signal. This setting has implications on Calibration. [Learn more.](PreferInternalTriggerOnChannelSingle_Property.md)  
  
#### Return Type

|  Long Integer  
  
#### Default

|  naTriggerSourceInternal  
  
#### Examples

|  trigSetup.Source = naTriggerSourceInternal 'Write  
trigsource = trigSetup.Source 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Source(tagNATriggerSource *pTrigger); HRESULT
put_Source(tagNATriggerSource trigger);  
  
#### Interface

|  ITriggerSetup  
  
* * *

* * *

