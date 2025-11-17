##### Write/Read

|

##### [About Scale Coupling](../../../S1_Settings/Scale.md#ScaleCoupling)  
  
---|---  
  
## ScaleCouplingMethod Property

* * *

#### Description

|  Sets and returns the method of scale coupling.  
---|---  
  
####  VB Syntax

|  win.ScaleCouplingMethod = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
win |  An [NAWindow](../Objects/NAWindow_Object.md) (object) Any window object can be used to set this global property.  
value |  (enum NAScaleCouplingMethod) 0  naScaleCouplingOff \- Scale Coupling is Off 1  naScaleCouplingWindow \- Traces within selected windows share scaling 2  naScaleCouplingAll - Scaling is shared among traces in all selected windows Select windows using [ScaleCouplingState Property](ScaleCouplingState_Property.md)  
  
#### Return Type

|  Enum  
  
#### Default

|  0  naScaleCouplingOff  
  
#### Examples

|  win.ScaleCouplingMethod = naScaleCouplingWindow 'Write method =
app.ActiveNAWindow.ScaleCouplingMethod 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_ScaleCouplingMethod(tagNAScaleCouplingMethod* couplingMethod);
HRESULT put_ScaleCouplingMethod(tagNAScaleCouplingMethod couplingMethod);  
  
#### Interface

|  INAWindow2  
  
* * *

