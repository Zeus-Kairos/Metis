##### Read only

|

##### [About VNA Options](../../../Support/Configurations.md)  
  
---|---  
  
## SourcePortCount Property

* * *

#### Description

|  Returns the number of ports that can output a signal. To learn more, see
[Remotely Specifying a Source
Port](../../Remotely_Specifying_a_Source_Port.htm).  
---|---  
  
####  VB Syntax

|  value = object.SourcePortCount  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Long) - Variable to store the returned integer value of the number of source ports.  
object |  A [Channel](../Objects/Channel_Object.md) (object)\- always more complete than capabilities object. A [Capabilities](../Objects/Capabilities_Object.md) (object) - use when a channel is not available, or to find the common ports across all channels.  
  
#### Return Type

|  Long  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = chan.SourcePortCount 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_SourcePortCount(long * count );  
  
#### Interface

|  IChannel13 ICapabilities4  
  
* * *

