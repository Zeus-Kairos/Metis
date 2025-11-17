##### Read-only

|

##### [About
Channels](../../../S0_Start/Traces_Channels_and_Windows.htm#channel)  
  
---|---  
  
## ActiveChannel Property

* * *

#### Description

|  Returns a handle to the Active Channel object. You can either (1) use the
handle directly to access channel properties and methods, or (2) set a
variable to the channel object. The variable retains a handle to the original
channel if another channel becomes active.  
---|---  
  
####  VB Syntax

|  (1) app.ActiveChannel.<setting>  
or  
(2) Set chan = app.ActiveChannel  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan |  A Channel (object)  
app |  An [Application](../Objects/Application_Object.md) (object)  
<setting> |  A channel property (or method) and arguments  
  
#### Return Type

|  Channel object  
  
#### Default

|  Not applicable  
  
#### Examples

|  1) app.ActiveChannel.Averaging = 1  
2) Public chan as Channel  
Set chan = app.ActiveChannel  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_ActiveChannel( IChannel* *pVal)  
  
#### Interface

|  IApplication

