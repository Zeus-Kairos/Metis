##### Read-only

|

##### [About Source Ports](../../../S1_Settings/Power_Level.md#powerDiag)  
  
---|---  
  
## GetSupportedALCModes Method

* * *

#### Description

|  Returns the valid ALC Modes for the VNA. See
[ALCLevelingMode](../Properties/ALCLevelingMode_Property.md) for a list of
supported ALC Modes.  
---|---  
  
#### VB Syntax

|  value = chan.GetSupportedALCModes (sourcePort)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  Variant Array variable to store the returned valid ALC Modes.  
chan |  (object) - A [Channel](../Objects/Channel_Object.md) object  
sourcePort |  (long integer) \- Source port. Note: If the port is defined by a string name, such as an external source, a balanced port, or one of the Source 2 outputs on the 2-port 2-source VNA-x model, then you must use [chan.getPortNumber](GetPortNumber_Method.md) to translate the string into a port number. To learn more see [Remotely Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.md).  
  
#### Return Type

|  Variant array  
  
#### Default

|  Not Applicable  
  
#### Examples

|  modes = chan.GetSupportedALCModes(4) 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT GetSupportedALCModes(long port, VARIANT * ALCModes );  
  
#### Interface

|  IChannel9  
  
* * *

