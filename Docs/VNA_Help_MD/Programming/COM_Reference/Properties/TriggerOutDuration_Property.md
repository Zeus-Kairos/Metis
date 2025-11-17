##### Write/Read

|

##### [About Auxiliary
Triggering](../../../S1_Settings/External_Triggering.htm#AuxTrigDiag)  
  
---|---  
  
## TriggerOutDuration Property

* * *

#### Description

|  Specifies the width of the output pulse, which is the time that the Aux
trigger output will be asserted.  
---|---  
  
####  VB Syntax

|  auxTrig.TriggerOutDuration = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
auxTrig |  An [AuxTrigger](../Objects/AuxTrigger_Object.md) (object)  
value |  (single) \- Duration value in seconds. Choose a value between 1E-6 and 1.  
  
#### Return Type

|  Double  
  
#### Default

|  1E-6 sec  
  
#### Exaamples

|  auxTrig.TriggerOutDuration = 1e-3 'Write  
value = auxTrig.TriggerOutDuration 'Read the value  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_TriggerOutDuration(double *val);  
HRESULT put_TriggerOutDuration(double val);  
  
#### Interface

|  IAuxTrigger  
  
* * *

