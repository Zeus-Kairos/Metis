##### Read-only  
  
---  
  
## WindowNumber Property

* * *

#### Description

|  Returns the window number. You might use this property to identify a
particular window so that you can create a new Measurement in that window.  
---|---  
  
####  VB Syntax

|  value = win.WindowNumber  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
win |  A NAWindow (object)  
value |  (long integer) - Variable to store the returned window number  
  
#### Return Type

|  Long Integer  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = app.ActiveNAWindow.WindowNumber  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT (long* windowNumber);  
  
#### Interface

|  INAWindow

