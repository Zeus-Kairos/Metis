##### Write/Read

|

##### [About Auxiliary
Triggering](../../../S1_Settings/External_Triggering.htm#AuxTrigDiag)

##### [About
PulseGenerators](../../../IFAccess/IF_Path_Configuration.htm#PulseGens)  
  
---|---  
  
## TriggerInType Property

* * *

#### Description

|  Specifies the type of trigger input being supplied to the VNA.

  * AuxTrigger Object \- Sets the type to which the rear-panel AuxTrig IN responds.
  * PulseGenerator Object \- Sets the type of trigger to which the internal pulse generators will respond when being externally triggered. Note: This feature requires DSP version: 4.0 FPGA:34 or higher. [Learn more](../../../S0_Start/HelpAbout.md).

Note: Use on PNA-X ONLY.  
---|---  
  
####  VB Syntax

|  obj.TriggerInType = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  An [AuxTrigger](../Objects/AuxTrigger_Object.md) (object) or A [PulseGenerator](../Objects/PulseGenerator_Object.md) (object  
value |  (enum NATriggerSignalType) Choose from: naTriggerEdge VNA responds to the edge (rising or falling) of a signal naTriggerLevel VNA responds to the level (HIGH or LOW) of a signal Use [TriggerInPolarity](TriggerInPolarity_Property.md) to set Positive or Negative polarity.  
  
#### Return Type

|  Enum  
  
#### Default

|  naTriggerLevel - Also the type used for the PulseGenerator Object when the
PNA-X does not have the required DSP hardware  
  
#### Exaamples

|  obj.TriggerInType = naTriggerEdge 'Write  
value = obj.TriggerInType 'Read the value  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_TriggerInType(enum NATriggerSignalType *val);  
HRESULT put_TriggerInType(enum NATriggerSignalType val);  
  
#### Interface

|  IAuxTrigger IPulseGenerator3  
  
* * *

