##### Write/Read

|

##### [About Averaging](../../../S2_Opt/Trce_Noise.md#averaging)  
  
---|---  
  
## Averaging Property

* * *

#### Description

|  Turns trace averaging ON or OFF for all measurements on the channel.
Averaging is only allowed on ratioed measurements; not on single input
measurements.  
---|---  
  
####  VB Syntax

|  chan.Averaging = state  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan |  A [Channel](../Objects/Channel_Object.md) (object)  
state |  (boolean)  
False \- Turns averaging OFF  
True \- Turns averaging ON  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  chan.Average = True 'Write  
averg = chan.Averaging 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Averaging(BOOL *pVal)  
HRESULT put_Averaging(BOOL newVal)  
  
#### Interface

|  IChannel

