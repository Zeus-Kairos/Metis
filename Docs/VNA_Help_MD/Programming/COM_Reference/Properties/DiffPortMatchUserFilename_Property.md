##### Write/Read

|

##### About Fixturing  
  
---|---  
  
## DiffPortMatchUserFilename Property

* * *

#### Description

|  Specifies the 2-port touchstone file in which the information on the user-
defined differential matching circuit is saved. Following this command, send
[DiffPortMatchCircuit Property](DiffPortMatchMode_Property.md). If the
specified file does not exist, an error occurs when you set the type of
differential matching circuit to USER.  
---|---  
  
####  VB Syntax

|  fixture.DiffPortMatchUserFilename(pNum) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
pNum |  (Integer) Balanced (logical) port number. Choose from logical ports 1, 2  or 3. [Learn more about logical ports.](../../../S1_Settings/Balanced_Measurements.md#mapping)  
value |  (String) Full path, file name, and extension (.s2P) of the de-embedding circuit. Files are typically stored in "D:\".  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  fixture.DiffPortMatchUserFilename(2) = "D:\myFile.s4p" 'Write  
value = fixture.DiffPortMatchUserFilename(1) 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_DiffPortMatchUserFilename( short port, BSTR *bstrFile) HRESULT
put_DiffPortMatchUserFilename( short port, BSTR bstrFile)  
  
#### Interface

|  IFixturing2

