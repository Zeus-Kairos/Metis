##### Read only

|

##### [About VNA Options](../../../Support/Configurations.md)  
  
---|---  
  
## GetPortNumber Method

* * *

#### Description

|  Returns the port number that is associated with the specified port name.
These numbers are used with several commands to specify a VNA port. To learn
more, see [Remotely Specifying a Source
Port](../../Remotely_Specifying_a_Source_Port.htm).  
---|---  
  
####  VB Syntax

|  value = object.GetPortNumber (portName)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Long) \- Variable to store the returned Port Number integer value.  
object |  A [Channel](../Objects/Channel_Object.md) (object) \- always more complete than capabilities object. A [Capabilities](../Objects/Capabilities_Object.md) (object) - use when a channel is not available  
portName |  (String) Name of the VNA port.

  * Use [SourcePortNames Property](../Properties/SourcePortNames_Property.md) to return a list of VNA port (string) names.
  * If an external source is selected, specify the external source name that is used in the [Select an External Source dialog](../../../System/Configure_an_External_Device.md#SelectExtSource).

  
  
#### Return Type

|  Long Integer  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = chan.GetPortNumber ("Src2 Out1") 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT GetPortNumber(BSTR name, long *number);  
  
#### Interface

|  IChannel13 ICapabilities4  
  
* * *

