##### Read-only

|

##### [About Auxiliary
Triggering](../../../S1_Settings/External_Triggering.htm#AuxTrigDiag)  
  
---|---  
  
# AuxiliaryTriggerCount Property

* * *

#### Description

|  Returns the number of aux trigger input / output connector pairs in the VNA  
---|---  
  
####  VB Syntax

|  value = app.AuxiliaryTriggerCount  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Long Integer) Variable to store the returned value. 2 = PNA-X models 1 = All other VNA models  
app |  An [Application](../Objects/Application_Object.md) (object)  
  
#### Return Type

|  Long Integer  
  
#### Default

|  Not Applicable  
  
#### Examples

|  ioConns = app.AuxiliaryTriggerCount  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT AuxiliaryTriggerCount(long *count);  
  
#### Interface

|  IApplication11  
  
* * *

