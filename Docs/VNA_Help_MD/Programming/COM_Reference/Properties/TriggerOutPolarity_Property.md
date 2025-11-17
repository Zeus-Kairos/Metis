##### Write/Read

|

##### [About Auxiliary
Triggering](../../../S1_Settings/External_Triggering.htm#AuxTrigDiag)  
  
---|---  
  
## TriggerOutPolarity Property

* * *

#### Description

|  Specifies the polarity of the trigger output signal being supplied by the
VNA.  
---|---  
  
####  VB Syntax

|  auxTrig.TriggerOutPolarity = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
auxTrig |  An [AuxTrigger](../Objects/AuxTrigger_Object.md) (object)  
value |  (enum NATriggerPolarity) \- Choose from: naTriggerPositive VNA sends positive going (active HIGH) pulse. naTriggerNegative VNA sends negative going (active LOW) pulse.  
  
#### Return Type

|  Enum  
  
#### Default

|  
  
#### Exaamples

|  auxTrig.TriggerOutPolarity = naTriggerPositive 'Write  
value = auxTrig.TriggerOutPolarity 'Read the value  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_TriggerOutPolarity(enum NATriggerPolarity *val);  
HRESULT put_TriggerOutPolarity(enum NATriggerPolarity val);  
  
#### Interface

|  IAuxTrigger  
  
* * *

