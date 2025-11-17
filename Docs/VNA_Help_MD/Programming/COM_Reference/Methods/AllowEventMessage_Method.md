##### Write/Read

|

##### [About Analyzer
Events](../../Learning_about_COM/Working_with_PNA_Events.htm)  
  
---|---  
  
## AllowEventMessage Method

* * *

#### Description

|  Sets event filtering to monitor specific events.  
---|---  
  
####  VB Syntax

|  app.AllowEventMessage event  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
event |  Event to monitor. Refer to list in [Working with the Analyzer's Events](../../Learning_about_COM/Working_with_PNA_Events.md)  
state |  (boolean)  
True \- monitor  
False \- do not monitor  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  app.AllowEventMessage  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT AllowEventMessage( tagNAEventID eventID, VARIANT_BOOL bAllow)  
  
#### Interface

|  IApplication

