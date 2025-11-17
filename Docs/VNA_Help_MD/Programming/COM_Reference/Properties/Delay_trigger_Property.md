##### Write/Read

|

##### [About Auxiliary
Triggering](../../../S1_Settings/External_Triggering.htm#AuxTrigDiag)  
  
---|---  
  
## Delay Property

* * *

#### Description

|  Specifies the delay that should be applied by the VNA after the aux trigger
input is received and before the acquisition is made. Note: Use on PNA-X ONLY.
Other models do NOT have an Aux Input.  
---|---  
  
####  VB Syntax

|  auxTrig.Delay = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
auxTrig |  An [AuxTrigger](../Objects/AuxTrigger_Object.md) (object)  
value |  (double) \- Delay value in seconds. Choose a value between 0 and 3.0 seconds.  
  
#### Return Type

|  Double  
  
#### Default

|  Not Applicable  
  
#### Exaamples

|  auxTrig.Delay = 1.2 'Write 1.2s Delay  
value = auxTrig.Delay 'Read the value  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_Delay(double *val); HRESULT put_Delay(double val);  
  
#### Interface

|  IAuxTrigger  
  
* * *

