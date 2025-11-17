##### Write/Read

|

##### [About IF BW](../../../S2_Opt/Trce_Noise.md#Variable_IF_Bandwidth)  
  
---|---  
  
## ReduceIFBandwidth Property

* * *

#### Description

|  Sets or returns the state of the [Reduced IF Bandwidth at Low
Frequencies](../../../S2_Opt/Trce_Noise.htm#IFDiag) setting.  
---|---  
  
####  VB Syntax

|  chan.ReduceIFBandwidth = state  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan |  A [Channel](../Objects/Channel_Object.md) (object)  
state |  (Enumas naStates) 0 - naOFF \- Turns Reduce IFBW OFF 1 - naON \- Turns Reduce IFBW ON  
  
#### Return Type

|  Enum as naStates  
  
#### Default

|  naON  
  
#### Examples

|  chan.ReduceIFBandwidth = naOFF'Write  
reduce = chan.ReduceIFBandwidth 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_ReduceIFBandwidth (tagNAStates *pState) HRESULT
put_ReduceIFBandwidth (tagNAStates newState)  
  
#### Interface

|  IChannel5  
  
* * *

