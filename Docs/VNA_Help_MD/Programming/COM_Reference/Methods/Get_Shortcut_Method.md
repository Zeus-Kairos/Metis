##### Read-only

|

#####  
  
---|---  
  
## GetShortcut Method

* * *

#### Description

|  From the index (line number in the user interface) returns the Title, Path,
and optional argument strings, of the specified Macro (shortcut). Use this
method to list the titles and paths of macros in the analyzer.  
---|---  
  
####  VB Syntax

|  app.GetShortcut index, title, path, arguments  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
index |  (long) - Number of the macro. Use a number between 1 and 25.  
title |  (string) \- Title of the specified macro. (Appears in the softkey label)  
path |  (string) \- Pathname of the specified macro.  
arguments |  (string) \- Arguments for the specified macro  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Example

|  Dim t As String  
Dim p As String  
Dim arg As String  
Dim i As Integer  
For i = 1 to 25  
app.GetShortcut i,t,p,arg  
Print t,p  
Next  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT GetShortcut(long Number, BSTR* title, BSTR* pathname, BSTR*
arguments)  
  
#### Interface

|  IApplication  
  
#### Remarks

|  Shortcuts can also be defined and accessed using the macro key on the front
panel. However, the benefit of this feature is primarily for the interactive
user  
  
* * *

