##### Write/Read

|

##### About Fixturing  
  
---|---  
  
## Embed4PortNetworkMode Property

* * *

#### Description

|  Specify the type of processing to take place on the specified 4-port
network. First specify the network filename with
[FSim.Embed4PortNetworkFilename
Property](Embed4PortNetworkFilename_Property.htm).  
---|---  
  
####  VB Syntax

|  fixture.Embed4PortNetworkMode(netNum) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
netNum |  (Integer) Network position. Choose from 1 or 2. See [Embed4PortTopology Property](Embed4PortTopology_Property.md)  
value |  (Enum as NA4PortEmbedNetworkMode) Processing mode. Choose from:

  * 0 or naNO_NETWORK \- The same as disabling.
  * 1 or naEMBED_NETWORK \- Add Network circuit.
  * 2 or naDEEMBED_NETWORK \- Remove Network circuit

  
  
#### Return Type

|  Enum  
  
#### Default

|  naNO_NETWORK  
  
#### Examples

|  fixture.Embed4PortNetworkMode(1) = naNO_NETWORK 'Write  
value = fixture.Embed4PortNetworkMode(2) 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Embed4PortNetworkMode( short networkNum,
tagNA4PortEmbedNetworkMode *eVal );  
HRESULT put_Embed4PortNetworkMode( short networkNum,
tagNA4PortEmbedNetworkMode eVal );  
  
#### Interface

|  IFixturing2

