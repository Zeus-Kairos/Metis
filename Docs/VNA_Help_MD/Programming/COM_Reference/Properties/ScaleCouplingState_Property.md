##### Write/Read

|

##### [About Scale Coupling](../../../S1_Settings/Scale.md#ScaleCoupling)  
  
---|---  
  
## ScaleCouplingState Property

* * *

#### Description

|  Enables and disables scale coupling for the window. Use
[ScaleCouplingMethod](ScaleCouplingMethod_Property.md) to select the coupling
method.  
---|---  
  
####  VB Syntax

|  win.ScaleCouplingState = bool  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
win |  An [NAWindow](../Objects/NAWindow_Object.md) (object) .  
bool |  (Boolean) False \- NO scale coupling for this window. True - Scale coupling enabled for this window.  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Examples

|  win.ScaleCouplingState = false 'Write coupled =
app.ActiveNAWindow.ScaleCouplingState 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_ScaleCouplingState(VARIANT_BOOL *pVal); HRESULT
put_ScaleCouplingState(VARIANT_BOOL newVal)  
  
#### Interface

|  INAWindow2  
  
* * *

