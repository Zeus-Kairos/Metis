##### Write/Read

|

##### [About Diff I/Q App](../../../Applications/Differential_IQ.md)  
  
---|---  
  
## MatchTestReceiver Property

* * *

#### Description

|  Sets and reads the test port receiver to be used to perform Match
Correction. On the [Source
Configuration](../../../Applications/Differential_IQ.htm#SourceConfigurationDiag)
dialog under Match Correction, this is the Test Receiver setting.  
---|---  
  
####  VB Syntax

|  DIQ.MatchTestReceiver (port) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
DIQ |  A [Differential I/Q](../Objects/DIQ_Object.md) (object)  
port |  (String) Source port name. Use [SourcePortNames](SourcePortNames_Property.md) to read a list of valid source ports.  
value |  (String) Choose any of the test port receivers in the analyzer using logical receiver notation. [Learn more](../../../S1_Settings/Measurement_Parameters.md#RecNotation). These would be "b_" where _ is the test port number.  
  
#### Return Type

|  String  
  
#### Default

|  Depends on <port>  
  
#### Examples

|  oDIQ.MatchTestReceiver("port 1") = "b1"  
Value = oDIQ.MatchTestReceiver("port 2") 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_MatchTestReceiver(BSTR port, BSTR* MatchTestReceiver); HRESULT
put_MatchTestReceiver(BSTR port, BSTR MatchTestReceiver);  
  
#### Interface

|  IDIQ  
  
* * *

