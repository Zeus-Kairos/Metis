##### Write/Read

|

##### About Fixturing  
  
---|---  
  
## strPortMatch_S2PFile Property

* * *

#### Description

|  Sets and returns the Port Matching 'S2P' file name for the specified port
number. Model is applied when both the file name is specified and User is
specified using [PortMatchingCktModel
Property](PortMatchingCktModel_Property.htm). [Learn more about S2P
files.](../../../S5_Output/SaveRecall.htm#An *.s3p) Note: This command affects
ALL measurements on the channel.  
---|---  
  
####  VB Syntax

|  fixture.strPortMatch_S2PFile(port) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
port |  (Integer) Port number to receive circuit model.  
value |  (String) Full path, file name, and extension (.s2P) of the matching circuit. Files are typically stored in "D:\".  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  fixture.strPortMatch_S2PFile(2) = "D:\myFile.s2p" 'Write  
value = fixture.strPortMatch_S2PFile(1) 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_strPortMatch_S2PFile(short port BSTR *bstrFile) HRESULT
put_strPortMatch_S2PFile(short port BSTR bstrFile)  
  
#### Interface

|  IFixturing  
  
* * *

