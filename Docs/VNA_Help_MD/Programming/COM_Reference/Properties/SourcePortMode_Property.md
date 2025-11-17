##### Write / Read

|

##### [About VNA Second Source](../../../S0_Start/Internal_Second_Source.md)  
  
---|---  
  
## SourcePortMode Property

* * *

#### Description

|  Sets the state of the VNA source for the specified port.  
---|---  
  
#### VB Syntax

|  chan.SourcePortMode (sourcePort) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan |  (object) - A [Channel](../Objects/Channel_Object.md) object  
sourcePort |  (long integer) \- The source port for which to make this setting. Note: If the port is defined by a string name, such as an external source, a balanced port, or one of the Source 2 outputs on the 2-port 2-source VNA-x model, then you must use [chan.getPortNumber](../Methods/GetPortNumber_Method.md) to translate the string into a port number. To learn more see [Remotely Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.md).  
value |  (enum) \- State of the source. Choose from: 0 - naSourcePortAuto Port power is turned on when required for a measurement. 1 - naSourcePortOn Port power is always ON, regardless of the measurement. 2 - naSourcePortOff Port power is always OFF, regardless of the measurement. 3 - naSourcePortNOTUSE Do not send OFF commands to the external sources. If an external source is in the OFF state, this option is used to stop sending OFF commands to the external source to increase sweep speed.  
  
#### Return Type

|  Enum  
  
#### Default

|  0 - naSourcePortAuto  
  
#### Examples

|  chan.SourcePortMode(1) = naSourcePortOn 'Write  
state = chan.SourcePortMode(4) 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_SourcePortMode(long sourcePort, enum NASourcePortMode*);
HRESULT put_SourcePortMode(long sourcePort, enum NASourcePortMode);  
  
#### Interface

|  IChannel9  
  
* * *

