##### Write-only

|

##### [About Macros](../../Using_Macros.md)  
  
---|---  
  
## ExecuteShortcut Method

* * *

#### Description

|  Executes a Macro (shortcut) stored in the analyzer. Use
[app.getShortcut](Get_Shortcut_Method.md) to list existing macros. Use
app.[putShortcut](Put_Shortcut_Method.md) to associate the macro number with
the file.  
---|---  
  
####  VB Syntax

|  app.ExecuteShortcut index  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
index |  (long integer) - Number of the macro stored in the analyzer.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  app.ExecuteShortcut 1  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT ExecuteShortcut(long index)  
  
#### Interface

|  IApplication

