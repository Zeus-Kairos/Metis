##### Write-only

|

##### [About
Windows](../../../S0_Start/Traces_Channels_and_Windows.htm#Window_Layout)  
  
---|---  
  
## ActivateWindow Method

* * *

#### Description

|  Makes a window object the Active Window. In order to change properties on
any of the active objects, you must first have a "handle" to the active object
using the Set command. For more information, See [Programming the Analyzer
Object Model](../../Learning_about_COM/Getting_a_Handle_to_an_Object.htm). You
do not have to make an object "Active" to set or read its properties remotely.
But an object must be "Active" to change its values from the front panel.  
---|---  
  
####  VB Syntax

|  app.ActivateWindow n  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
n |  (long) Number of the window to make active  
  
#### Return Type

|  Window Object  
  
#### Default

|  Not Applicable  
  
#### Examples

|  app.ActivateWindow 4  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT ActivateWindow(long WindowNumber)  
  
#### Interface

|  IApplication  
  
[See the VNA Object Model](../Objects/The_Analyzer_Object_Model.md)

