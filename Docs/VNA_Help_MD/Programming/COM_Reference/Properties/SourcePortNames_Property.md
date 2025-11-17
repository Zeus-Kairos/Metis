##### Read only

|

##### [About VNA Options](../../../Support/Configurations.md)  
  
---|---  
  
## SourcePortNames Property

* * *

#### Description

| Returns the string names of ports that can output a signal. The following is
a list of string names for the PNA-X. Your VNA will NOT have all of these
ports. Use [GetPortNumber Method](../Methods/GetPortNumber_Method.md) to
return the correct port number for the specified port name.

  * Port 1
  * Port 2
  * Port 3
  * Port 4
  * Src2 Out1
  * Src2 Out2
  * Port 1 Src2

For [iTMSA (Opt S93460A/B)](../../../Applications/iTMSA.md)

  * "Bal Port 1"
  * "Bal Port 2"
  * "SE Port1"
  * "SE Port 2"

This command also lists the [External
Sources](../../../System/Configure_an_External_Device.htm) that are currently
configured and selected. To learn more, see [Remotely Specifying a Source
Port](../../Remotely_Specifying_a_Source_Port.htm).  
---|---  
  
####  VB Syntax

| value = object.SourcePortNames  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value | (Variant array) - Variable to store the returned list of source port names.  
object | A [Channel](../Objects/Channel_Object.md) (object) \- always more complete than capabilities object. A [Capabilities](../Objects/Capabilities_Object.md) (object) - use when a channel is not available, or to find the common ports across all channels.  
  
#### Return Type

| Variant array of string names.  
  
#### Default

| Not Applicable  
  
#### Examples

| value = chan.SourcePortNames 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

| HRESULT get_SourcePortNames(VARIANT *names);  
  
#### Interface

| IChannel13 ICapabilities4  
  
* * *

* * *

