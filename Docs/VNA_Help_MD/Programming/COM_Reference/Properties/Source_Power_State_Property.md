##### Write/Read

|

##### [About Source Power](../../../S1_Settings/Power_Level.md)  
  
---|---  
  
## SourcePowerState Property

* * *

#### Description

|  Turns Source Power ON and OFF. [See note about source power state with
instrument state save and
recall](../../../S1_Settings/Power_Level.htm#powerDiag).  
---|---  
  
####  VB Syntax

|  app.SourcePowerState = state  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
state |  (boolean) False \- Turns Source Power OFF True - Turns Source Power ON  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Examples

|  app.SourcePowerState = True 'Write  
pwr = app.SourcePowerState 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_SourcePowerState(VARIANT_BOOL *pVal)  
HRESULT put_SourcePowerState(VARIANT_BOOL newVal)  
  
#### Interface

|  IApplication

