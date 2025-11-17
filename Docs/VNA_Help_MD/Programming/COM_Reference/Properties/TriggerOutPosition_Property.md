##### Write/Read

|

##### [About Auxiliary
Triggering](../../../S1_Settings/External_Triggering.htm#AuxTrigDiag)  
  
---|---  
  
## TriggerOutPosition Property

* * *

#### Description

|  Specifies whether the Aux trigger out signal is sent Before or After the
acquisition.  
---|---  
  
####  VB Syntax

|  auxTrig.TriggerOutPosition = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
auxTrig |  An [AuxTrigger](../Objects/AuxTrigger_Object.md) (object)  
value |  (enum NATriggerPosition) Choose from: naTriggerOutBeforeAcquire Use if the external device needs to be triggered before the data is acquired, such as a power meter. naTriggerOutAfterAcquire Use if the external device needs to be triggered just after data has been acquired, such as an external source. This could be more efficient since it allows the external device to get ready for the next acquisition at the same time as the VNA.  
  
#### Return Type

|  Enum  
  
#### Default

|  naTriggerOutAfterAcquire  
  
#### Exaamples

|  auxTrig.TriggerOutPosition = naTriggerOutAfterAcquire 'Write  
value = auxTrig.TriggerOutPosition 'Read the value  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_TriggerOutPosition(enum NATriggerPosition *val);  
HRESULT put_TriggerOutPosition(NATriggerPosition val);  
  
#### Interface

|  IAuxTrigger  
  
* * *

