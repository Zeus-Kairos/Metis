##### Write-only

|

##### About Macros  
  
---|---  
  
## PutShortcut Method

* * *

#### Description

|  Defines a Macro (shortcut) file in the analyzer. This command links a file
name and path to the Macro file. The file must be put in the VNA at the
location indicated by this command.  
---|---  
  
####  VB Syntax

|  app.PutShortcut index,title,path, arguments  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
index |  (long) \- Number of the macro to be stored in the analyzer. Use a number between 1 and 25. If the index number already exists, the existing macro is replaced with the new macro.  
title |  (string) - The name to be assigned to the macro  
path |  (string) \- Full path, file name, and extension of the existing macro "executable" file.  
arguments |  (string) \- Arguments that may be required for the specified macro to run.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  app.PutShortcut 1,"Test","C:/Automation/MyTest.vbs",""  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT PutShortcut(long Number, BSTR title, BSTR pathname,BSTR arguments)  
  
#### Interface

|  IApplication  
  
* * *

