##### Write-only  
  
---  
  
## Quit Method

* * *

#### Description

|  Terminates the Network Analyzer application.  
---|---  
  
####  VB Syntax

|  app.Quit  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  app.Quit  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT Quit()  
  
#### Interface

|  IApplication  
  
#### Remarks

|  Under the rules of COM, the server should not exit until all references to
it have been released. This method is a brute force way of terminating the
application. Be sure to release all references (or terminate the client
program) before attempting to restart the Network Analyzer application. An
alternate approach to terminating the application is to make the application
invisible (app.[Visible](../Properties/Visible_Property.md) = False) and
release all references. The server will shutdown.

