##### Write-only

|

##### [About Macros](../../Using_Macros.md)  
  
---|---  
  
## DeleteShortCut Method

* * *

#### Description

|  Removes a macro from the list of macros in the analyzer. Does not remove
the file. Note: There are always 25 macro positions. They do not have to be
sequential. For example, you can have number 7 but not numbers 1 to 6.  
---|---  
  
####  VB Syntax

|  app.DeleteShortCut item  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
item |  (long integer) number of the macro to be deleted.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  app.DeleteShortCut 2  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT DeleteShortcut(long Number )  
  
#### Interface

|  IApplication  
  
* * *

