##### Write / Read

|

##### [About Source Ports](../../../S1_Settings/Power_Level.md#powerDiag)  
  
---|---  
  
## ALCLevelingMode Property

* * *

#### Description

|  Sets and returns the ALC mode for the specified channel and port. Use
[GetSupportedALCModes](../Methods/GetSupportedALCModes_Method.md) to return a
list of valid ALC modes for the VNA. [Learn more about ALC
mode.](../../../S1_Settings/Power_Level.htm#Advanced)  
---|---  
  
#### VB Syntax

|  chan.ALCLevelingMode (sourcePort) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan |  (object) - A [Channel](../Objects/Channel_Object.md) object  
sourcePort |  (long integer) \- The source port for which to make this setting. If ports are [remapped](../../../System/External_Testset_Control.md#Balanced), specify the logical port number. Note: If the port is defined by a string name, such as an external source, a balanced port, or one of the Source 2 outputs on the 2-port 2-source VNA-x model, then you must use [chan.getPortNumber](../Methods/GetPortNumber_Method.md) to translate the string into a port number. To learn more see [Remotely Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.md).  
value |  (enum as naALCLevelingMode) \- Choose from:

  * 0 naALCInternal
  * 2 naALCOpenLoop (PNA-X only)

  
  
#### Return Type

|  Enum  
  
#### Default

|  naALCInternal  
  
#### Examples

|  chan.ALCLevelingMode(1) = 2 'Write  
state = chan.ALCLevelingMode(4) 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_ALCLevelingMode(long port, tagNAALCLevelingMode* pVal); HRESULT
put_ALCLevelingMode(long port,tagNAALCLevelingMode newVal);  
  
#### Interface

|  IChannel9  
  
* * *

