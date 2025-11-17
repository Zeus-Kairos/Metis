##### Write/Read

|

##### [About PointAveraging](../../../S2_Opt/Trce_Noise.md#averaging)  
  
---|---  
  
## PointAveragingState Property

* * *

#### Description

|  Turns point averaging ON or OFF for all measurements on the channel.  
---|---  
  
####  VB Syntax

|  chan.PointAveragingState = state  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan |  A [Channel](../Objects/Channel_Object.md) (object)  
state |  (Enun) False \- Turns point averaging OFF True \- Turns point averaging ON  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  chan.PointAveragingState = True 'Write  
averg = chan.PointAveragingState 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PointAveragingState(BOOL *pVal)  
HRESULT put_PointAveragingState(BOOL newVal)  
  
#### Interface

|  IChannel16  
  
* * *

