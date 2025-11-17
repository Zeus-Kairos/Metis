##### Write/Read

|

##### [About Averaging](../../../S2_Opt/Trce_Noise.md#averaging)  
  
---|---  
  
## AverageMode Property

* * *

#### Description

|  Specifies the type of averaging to perform: Point or Sweep.  
---|---  
  
####  VB Syntax

|  chan.AverageMode = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan |  A [Channel](../Objects/Channel_Object.md) (object)  
value |  (Enum as naAverageMode) \- Average Type. Choose from: 0 - naPoint Averaging measurements are made on each data point before stepping to the next data point. 1 - naSweep Averaging measurements are made on subsequent sweeps until the required number of averaging sweeps are performed.  
  
#### Return Type

|  Enum  
  
#### Default

|  1-  naSweep  
  
#### Examples

|  chan.AverageMode = naSweep 'Write  
avgType = chan.AverageMode ' Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_AverageMode(NAAverageMode * mode); HRESULT
put_AverageMode(NAAverageMode mode);  
  
#### Interface

|  IChannel16  
  
* * *

