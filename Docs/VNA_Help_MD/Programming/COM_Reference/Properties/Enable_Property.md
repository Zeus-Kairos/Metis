##### Write/Read

|

##### [About Auxiliary
Triggering](../../../S1_Settings/External_Triggering.htm#AuxTrigDiag)  
  
---|---  
  
## Enable Property

* * *

#### Description

|  Turns ON / OFF the trigger output.  
---|---  
  
####  VB Syntax

|  auxTrig.Enable = state  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
auxTrig |  An [AuxTrigger](../Objects/AuxTrigger_Object.md) (object)  
state |  (boolean) True \- Trigger Output ON False \- Trigger Output OFF  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Exaamples

|  auxTrig.Enable = True 'Write  
value = auxTrig.Enable 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Enable(VARIANT_BOOL * enable); HRESULT put_Enable(VARIANT_BOOL
enable);  
  
#### Interface

|  IAuxTrigger  
  
* * *

