##### Read-only

|

##### [About Analyzer
Events](../../Learning_about_COM/Working_with_PNA_Events.htm)  
  
---|---  
  
## MessageText Property

* * *

#### Description

|  Returns text for the specified eventID  
---|---  
  
####  VB Syntax

|  app.MessageText,eventID,message  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
eventID |  (enum naEventID) Choose from the list in [Working with the Analyzer's Events](../../Learning_about_COM/Working_with_PNA_Events.md)  
message |  (string) - variable to store the returned message  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  RFNA.MessageText naEventID_ARRANGE_WINDOW_EXCEED_CAPACITY, message  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_MessageText( tagNAEventID msgID, BSTR* message)  
  
#### Interface

|  IApplication

