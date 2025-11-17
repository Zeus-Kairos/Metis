##### Read-only

|

##### [About Auxiliary
Triggering](../../../S1_Settings/External_Triggering.htm#AuxTrigDiag)  
  
---|---  
  
## Number Property

* * *

#### Description

|  Returns the number of the Auxiliary Trigger connector pair currently being
used with the instance of the [AuxTrigger](../Objects/AuxTrigger_Object.md)
object. Set the trigger pair with the AuxTrig object.  
---|---  
  
####  VB Syntax

|  value = auxTrig.Number  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
auxTrig |  An [AuxTrigger](../Objects/AuxTrigger_Object.md) (object)  
value |  (Long Integer) \- Connector pair. PNA-X returns 1 or 2. All other models that do not have the Aux trigger connector returns 1.  
  
#### Return Type

|  Single  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = auxTrig.Number 'Read the value  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Number(long *auxID);  
  
#### Interface

|  IAuxTrigger  
  
* * *

