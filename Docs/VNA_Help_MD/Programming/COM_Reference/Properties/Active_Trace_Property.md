##### Read-only

|

##### [About Traces](../../../S0_Start/Traces_Channels_and_Windows.md#Trace)  
  
---|---  
  
## ActiveTrace Property

* * *

#### Description

|  Returns a handle to the Active Trace object. You can either (1) use the
handle directly to access trace properties and methods, or (2) set a variable
to the trace object. The variable retains a handle to the original trace if
another trace becomes active.  
---|---  
  
#### VB Syntax

|  1) win.ActiveTrace.<setting>  
or  
2) Set trce = win.ActiveTrace  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
trce |  A Trace (object)  
win |  An NAWindow (object)  
<setting> |  A trace property (or method) and arguments  
  
#### Return Type

|  An NAWindow object  
  
#### Default

|  None  
  
#### Examples

|  1) win.ActiveTrace.Autoscale  
2) Public trce as Trace  
Set trce = Application.ActiveNAWindow.ActiveTrace  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_ActiveTrace(ITrace* *pVal)  
  
#### Interface

|  INAWindow

