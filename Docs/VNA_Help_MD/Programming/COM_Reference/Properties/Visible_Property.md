##### Write/Read  
  
---  
  
## Visible Property

* * *

#### Description

|  Makes the Network Analyzer application visible or not visible. In the Not
Visible state, the analyzer cycle time for making measurements can be
significantly faster because the display does not process data.  
---|---  
  
####  VB Syntax

|  app.Visible = state  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
state |  (boolean) False \- Network Analyzer application NOT visible True \- Network Analyzer application IS visible  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Examples

|  app.Visible = False 'Write  
vis = app.Visible 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Visible(VARIANT_BOOL * bVisible)  
HRESULT put_Visible(VARIANT_BOOL bVisible)  
  
#### Interface

|  IApplication

