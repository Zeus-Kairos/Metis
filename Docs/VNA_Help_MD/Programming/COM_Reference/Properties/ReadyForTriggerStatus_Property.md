##### Read-only

|

##### [About External Trigger](../../../S1_Settings/External_Triggering.md)  
  
---|---  
  
# ReadyForTriggerStatus Property

* * *

#### Description

|  Checks if the PNA is ready for a hardware trigger. This command is not
intended to be used in a dynamic triggering situation where the ready status
is constantly changing. Instead, the expected use is a more static situation
where you are expecting the PNA to transition from not ready to ready, and
then wait for a trigger. The PNA is polled until it becomes ready and then an
operation that triggers the PNA is performed. Note: This command is only
supported on the PNA-L, PNA, and PNA-X with DSP5 installed. Any other model
will return an error.  
---|---  
  
####  VB Syntax

|  value = trigsetup.ReadyForTriggerStatus  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
trigsetup |  A [TriggerSetup](../Objects/TriggerSetup_Object.md) (object)  
value |  (Enum as NATriggerReadyStatusSource) 0 - naTriggerAny - Check if the PNA is ready for any of the following hardware triggers. 1 - naTriggerMeas - Check if the PNA is ready for an External trigger from the Meas Trig In BNC, Handler IO Pin 18, or Pulse 3 line. 2 - naTrigger Aux1 - Check if the PNA is ready for a trigger from the AUX TRIG 1 IN on the rear panel. 3 - naTriggerAux2 - Check if the PNA is ready for a trigger from the AUX TRIG 2 IN on the rear panel.  
  
#### Return Type

|  Boolean  
  
#### Default

|  Not applicable  
|  value = trigsetup.ReadyForTriggerStatus 0 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_ReadyForTriggerStatus(tagNATriggerReadyStatusSource
whichTrigger, VARIANT_BOOL* val);  
  
#### Interface

|  ITriggerSetup4  
  
* * *

