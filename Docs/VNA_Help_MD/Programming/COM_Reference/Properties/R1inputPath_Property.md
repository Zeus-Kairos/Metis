##### Write/Read

|

##### [About Frequency Offset](../../../FreqOffset/Frequency_Offset_Mode.md)  
  
---|---  
  
## R1inputPath Property

* * *

#### Description

|  All VNA models (except the N523xA models) have a switch in the test set
that allows access to the port 1 reference receiver through the front panel
Reference 1 connectors. This command throws that switch between the internal
path to the receiver, or through the external connectors. See other [Frequency
Offset](../Objects/Channel_Object.htm#FrequencyOffset) properties.  
---|---  
  
####  VB Syntax

|  chan.R1InputPath = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan |  A [Channel](../Objects/Channel_Object.md) (object)  
value |  (Enum as naInputPath) \- Choose from:naPathInternal - (0) \- internal path to the reference receiver naPathExternal (1) \- path through external connectors  
  
#### Return Type

|  Enum  
  
#### Default

|  naPathInternal - (0)  
  
#### Examples

|  chan.R1InputPath = naPathInternal 'Write  
Inpath = chan.R1InputPath 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_R1InputPath (tag NAInputPath *pPath); HRESULT put_R1InputPath
(tag NAInputPath newPath);  
  
#### Interface

|  IChannel2  
  
* * *

