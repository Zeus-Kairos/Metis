##### Write/Read

|

##### About Fixturing  
  
---|---  
  
## Port2PdeembedCktModel Property

* * *

#### Description

|  Select whether or not to load a 2-port De-embedding circuit model for the
specified port number. Circuit model is applied when both "USER" is selected
and the filename is specified. To set the filename, use
[strPort2Pdeembed_S2PFile Property](strPort2Pdeembed_S2PFile_Property.md)
Note: This command affects ALL measurements on the channel.  
---|---  
  
####  VB Syntax

|  fixture.Port2PdeembedCktModel(port) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
port |  (Integer) Port number to receive circuit model.  
value |  (Enum as NAFixturing2PdeembedCkt) 0 naFix2PD_USER load a 2-port De-embedding circuit model 1 naFix2PD_NONE no model  
  
#### Return Type

|  Long Integer  
  
#### Default

|  naFix2PD_NONE  
  
#### Examples

|  fixture.Port2PdeembedCktModel(2) = naFix2PD_USER 'Write  
value = fixture.Port2PdeembedCktModel(1) 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Port2PdeembedCktModel(short port tagNAFixturing2PdeembedCkt
*pVal)  
HRESULT put_Port2PdeembedCktModel(short port tagNAFixturing2PdeembedCkt
newVal)  
  
#### Interface

|  IFixturing

