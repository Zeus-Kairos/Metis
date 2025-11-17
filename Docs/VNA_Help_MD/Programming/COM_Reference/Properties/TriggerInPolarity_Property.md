##### Write/Read

|

##### [About Auxiliary
Triggering](../../../S1_Settings/External_Triggering.htm#AuxTrigDiag)

##### [About Pulse
Generators](../../../IFAccess/IF_Path_Configuration.htm#PulseGens)  
  
---|---  
  
## TriggerInPolarity Property

* * *

#### Description

|  Specifies the polarity of the trigger IN signal.

  * AuxTrigger Object \- Sets the polarity to which the rear-panel AuxTrig IN responds.
  * PulseGenerator Object \- Sets the polarity of trigger to which the internal pulse generators will respond when being externally triggered. Note: This feature requires DSP version: 4.0 FPGA:34 or higher. [Learn more](../../../S0_Start/HelpAbout.md).

Note: Used on PNA-X ONLY.  
---|---  
  
####  VB Syntax

|  object.TriggerInPolarity = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  An [AuxTrigger](../Objects/AuxTrigger_Object.md) (object) or A [PulseGenerator](../Objects/PulseGenerator_Object.md) (object)  
value |  (enum NATriggerPolarity) \- Choose from: naTriggerPositive VNA responds to rising edge or HIGH level naTriggerNegative VNA responds to falling edge or LOW level. Set Edge or Level triggering using [TriggerInType Property](TriggerInType_Property.md)  
  
#### Return Type

|  Enum  
  
#### Default

|  AuxTriggerIn Object - naTriggerNegative PulseGenerator Object -
naTriggerPositive. Also the polarity used when the PNA-X does not have the
required DSP hardware  
  
#### Exaamples

|  obj.TriggerInPolarity = naTriggerPositive 'Write  
value = obj.TriggerInPolarity 'Read the value  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_TriggerInPolarity(enum NATriggerPolarity *val);  
HRESULT put_TriggerInPolarity(enum NATriggerPolarity val);  
  
#### Interface

|  IAuxTrigger IPulseGenerator3  
  
* * *

