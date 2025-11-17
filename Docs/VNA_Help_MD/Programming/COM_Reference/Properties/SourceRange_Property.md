##### Write/Read

|

##### [About Diff I/Q App](../../../Applications/Differential_IQ.md)  
  
---|---  
  
## SourceRange Property

* * *

#### Description

|  Sets and reads the frequency range number to which the specified source
port will be set. At the top of the [Source
Configuration](../../../Applications/Differential_IQ.htm#SourceConfigurationDiag)
dialog this is the Frequency Range setting.  
---|---  
  
####  VB Syntax

|  DIQ.SourceRange (port) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
DIQ |  A [Differential I/Q](../Objects/DIQ_Object.md) (object)  
port |  (String) Source port name. Use [SourcePortNames](SourcePortNames_Property.md) to read a list of valid source ports.  
value |  (Long) Frequency range number.  
  
#### Return Type

|  Long  
  
#### Default

|  1  
  
#### Examples

|  oDIQ.SourceRange("port 2") = 1  
Value = oDIQ.SourceRange("port 2") 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SourceRange(long range, long* SourceRange); HRESULT
put_SourceRange(long range, long SourceRange);  
  
#### Interface

|  IDIQ  
  
* * *

