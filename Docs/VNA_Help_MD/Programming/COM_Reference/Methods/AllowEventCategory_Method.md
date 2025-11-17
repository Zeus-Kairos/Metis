##### Write/Read

|

##### [About Analyzer
Events](../../Learning_about_COM/Working_with_PNA_Events.htm)  
  
---|---  
  
## AllowEventCategory Method

* * *

#### Description

|  Sets event filtering to monitor a category of event.  
---|---  
  
####  VB Syntax

|  app.AllowEventCategory, category, state  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
category |  Category to monitor. Choose from list in [Working with the Analyzer's Events](../../Learning_about_COM/Working_with_PNA_Events.md)  
state |  (boolean)  
True \- monitor  
False \- do not monitor  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  app.AllowEventCategory  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT AllowEventCategory(tagNAEventCategory category, VARIANT_BOOL bAllow
)  
  
#### Interface

|  IApplication

