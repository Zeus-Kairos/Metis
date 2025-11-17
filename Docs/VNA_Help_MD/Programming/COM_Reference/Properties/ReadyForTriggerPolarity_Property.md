##### Write/Read

|

##### [About External Trigger](../../../S1_Settings/External_Triggering.md)  
  
---|---  
  
## ReadyForTriggerPolarity Property

* * *

#### Description

|  Specifies the polarity of Ready for Trigger output. All existing Ready for
Trigger outputs for PNA-X and PNA-L models are configured simultaneously with
this command. [See Capabilities
Summary.](../../../S1_Settings/External_Triggering.htm#Capabilities) The Ready
for Trigger polarity can NOT be configured for E836x models.  
---|---  
  
####  VB Syntax

|  trigsetup.ReadyForTriggerPolarity = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
trigsetup |  A [TriggerSetup](../Objects/TriggerSetup_Object.md) (object)  
value |  (Enum as NALevel) Choose from: 0 - naLow - Outputs a TTL low when the VNA is ready for trigger. 1 - naHigh - Outputs a TTL high when the VNA is ready for trigger.  
  
#### Return Type

|  Enum  
  
#### Default

|  0 - naLow  
  
#### Examples

|  trigsetup.ReadyForTriggerPolarity = naLow 'Write  
pol = trigsetup.ReadyForTriggerPolarity 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_ReadyForTriggerPolarity(tagNALevel *pVal); HRESULT
put_ReadyForTriggerPolarity(tagNALevel newVal);  
  
#### Interface

|  ITriggerSetup3  
  
* * *

