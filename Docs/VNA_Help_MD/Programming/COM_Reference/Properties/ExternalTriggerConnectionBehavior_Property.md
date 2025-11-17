##### Write/Read

|

##### [About Trigger](../../../S1_Settings/Trigger.md#scope)  
  
---|---  
  
## ExternalTriggerConnectionBehavior Property

* * *

#### Description

|  Configures the external triggering signal for the VNA and PNA-X.

  * [TriggerSouce Property](Source_Property.md) is automatically set to External when ExternalTriggerConnectionBehavior is sent.
  * Edge triggering is only available on some VNA models.
  * For more information, see [External Triggering](../../../S1_Settings/External_Triggering.md#Edge).

  
---|---  
  
####  VB Syntax

|  trigsetup.ExternalTriggerConnectionBehavior (conn) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
trigsetup |  A [TriggerSetup](../Objects/TriggerSetup_Object.md) (object)  
conn |  (enum NATriggerConnection) Rear Panel connector to send or receive trigger signals. Choose from: Only one of the input connectors is active at a time. When a command is sent to one, the VNA automatically makes the other INACTIVE. 0 - naTriggerConnectionAUXT Trigger IN from rear-panel AUX IO connector Pin 19 (No longer supported. 1 - naTriggerConnectionBNC1 Trigger IN

  * [MEAS TRIG IN](../../../Rear_Panel/XRtour.md#ExternalTrig) on models

2 - naTriggerConnectionBNC2 Trigger OUT. Only useful in point sweep mode.

  * [AUX TRIG 1 OUT](../../../Rear_Panel/XRtour.md#ExternalTrig) on models

3 - naTriggerConnectionMATH Trigger IN from rear-panel [Material Handler
connector Pin 18](../../HandlerIO_Connector.htm) 4 -
naTriggerConnectionBypassPulse3 \- Internal routing of pulse 3 output to the
MEAS TRIG IN on the rear panel.  
value |  (enum NAExternalTriggerBehavior) - 0 - naTriggerInactive \- Disables the specified connector. Choose from 1 through 4 when <conn> is set to naTriggerConnectionBNC1 1 - naTriggerInEdgeNegative \- Triggers the VNA when receiving a negative going signal 2 - naTriggerInEdgePositive \- Triggers the VNA when receiving a positive going signal 3 - naTriggerInLevelLow \- Triggers the VNA when receiving a low level signal 4 - naTriggerInLevelHigh \- Triggers the VNA when receiving a High-level signal Choose from 5 through 8 when <conn> is set to naTriggerConnectionBNC2. In addition to sending this command, you must also use [TriggerOutputEnabled Property](TriggerOutputEnabled_Property.md) to enable the BNC2 output. 5 - naTriggerOutPulsePositiveAfter \- Sends a POSITIVE going TTL pulse at the END of each point during the sweep. 6 - naTriggerOutPulsePositiveBefore \- Sends a POSITIVE going TTL pulse at the START of each point during the sweep. 7 - naTriggerOutPulseNegativeAfter \- Sends a NEGATIVE going TTL pulse at the END of each point during the sweep. 8 - naTriggerOutPulseNegativeBefore \- Sends a NEGATIVE going TTL pulse at the START of each point during the sweep.  
  
#### Return Type

|  Enum as NAExternalTriggerBehavior  
  
#### Default

|  BNC1 = naTriggerInactive BNC2 = naTriggerInactive When [Output is
enabled](TriggerOutputEnabled_Property.htm) BNC1 = naTriggerInactive BNC2 =
naTriggerOutPulsePositiveAfter  
  
#### Examples

|  trigsetup.ExternalTriggerConnectionBehavior (naTriggerConnectionBNC1) =
naTriggerInLevelLow 'Write  
trigBehav = trigsetup.ExternalTriggerConnectionBehavior
(naTriggerConnectionAUXT) 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_ExternalTriggerConnectionBehavior(tagNATriggerConnection
connection,tagNAExternalTriggerBehavior *trigger); HRESULT
put_ExternalTriggerConnectionBehavior(tagNATriggerConnection
connection,tagNAExternalTriggerBehavior trigger);  
  
#### Interface

|  ITriggerSetup  
  
* * *

  

