##### Write-Read

## DisplayAutomationErrors Property

* * *

#### Description

|  Enables or disables automation error messages from being displayed on the
screen.  
---|---  
  
####  VB Syntax

|  app.DisplayAutomationErrors = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
value |  (Boolean) True allows error to show on display, False turns error off from display.  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Examples

|  Dim app As Application Set app = New Application
app.DisplayAutomationErrors = False 'Turns off display print
app.DisplayAutomationErrors 'prints False  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_DisplayAutomationErrors(VARIANT_BOOL * Val); HRESULT
put_DisplayAutomationErrors(VARIANT_BOOL Val);  
  
#### Interface

|  IApplication2

