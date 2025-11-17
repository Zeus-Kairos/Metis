##### Write/Read

|

##### [About Averaging](../../../S2_Opt/Trce_Noise.md#averaging)  
  
---|---  
  
## AveragingFactor Property

* * *

#### Description

|  Specifies the number of measurements to combine for an average. Must also
turn averaging ON by setting chan.[Averaging](Averaging_Property.md) = 1.  
---|---  
  
####  VB Syntax

|  chan.AveragingFactor = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan |  A Channel (object)  
value |  (Long Integer) \- Number of measurement sweeps to average. Choose any number between 1 and 65536 (2^16).  
  
#### Return Type

|  Long Integer  
  
#### Default

|  1  
  
#### Examples

|  chan.AveragingFactor = 5 'Write  
avgfact = chan.AveragingFactor ' Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_AveragingFactor(long *pVal)  
HRESULT put_AveragingFactor(long newVal)  
  
#### Interface

|  IChannel  
  
* * *

