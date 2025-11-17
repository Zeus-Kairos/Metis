##### Read-only

|

##### About Windows  
  
---|---  
  
## ActiveNAWindow Property

* * *

#### Description

|  Returns a handle to the Active Window object. You can either (1) use the
handle directly to access window properties and methods, or (2) set a variable
to the window object. The variable retains a handle to the original window if
another window becomes active.  
---|---  
  
####  VB Syntax

|  1) app.ActiveNAWindow.<setting>  
or  
2) Set win = app.ActiveNAWindow  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
win |  A NAWindow (object)  
app |  An [Application](../Objects/Application_Object.md) (object)  
<setting> |  A NAWindow property (or method) and arguments  
  
#### Return Type

|  A NAWindow object  
  
#### Default

|  Not applicable  
  
#### Examples

|  Public win as NAWindow  
Set win = app.ActiveWindow  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_ActiveNAWindow(INAWindow **ppWindow)  
  
#### Interface

|  IApplication

