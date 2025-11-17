##### Write/Read

|

##### About Fixturing  
  
---|---  
  
## Embed4PortNetworkFilename Property

* * *

#### Description

|  Specifies the 4-port touchstone file (*.s4p) in which the network to embed
or de-embed resides. If the specified file does not exist, an error occurs
when type command is sent. Following this command, send [Embed4PortNetworkMode
Property](Embed4PortNetworkMode_Property.htm). Note: This command affects ALL
measurements on the channel.  
---|---  
  
####  VB Syntax

|  fixture.Embed4PortNetworkFilename(netNum) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
netNum |  (Integer) Network position. Choose from 1 or 2. See [Embed4PortTopology Property](Embed4PortTopology_Property.md)  
value |  (String) Full path, file name, and extension (.s4P) of the circuit. Files are typically stored in "D:\".  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  fixture.Embed4PortNetworkFilename(2) = "D:\myFile.s4p" 'Write  
value = fixture.Embed4PortNetworkFilename(1) 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Embed4PortNetworkFilename( short networkNum, BSTR *filename);
HRESULT put_Embed4PortNetworkFilename( short networkNum, BSTR filename);  
  
#### Interface

|  IFixturing2

