##### Write/Read

|

##### [About Diff I/Q App](../../../Applications/Differential_IQ.md)  
  
---|---  
  
## MatchFrequencyRange Property

* * *

#### Description

|  Sets and reads the existing frequency ranges over which Match Correction is
to be performed. On the [Source
Configuration](../../../Applications/Differential_IQ.htm#SourceConfigurationDiag)
dialog under Match Correction, this is the Match Frequency Range setting.  
---|---  
  
####  VB Syntax

|  DIQ.MatchFrequencyRange (port) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
DIQ |  A [Differential I/Q](../Objects/DIQ_Object.md) (object)  
port |  (String) Source port name. Use [SourcePortNames](SourcePortNames_Property.md) to read a list of valid source ports.  
value |  (String) Frequency ranges, including the "F<n>", where <n> is the range number. Separate each range with a comma.  
  
#### Return Type

|  String  
  
#### Default

|  Depends on <port>  
  
#### Examples

|  oDIQ.MatchFrequencyRange("port 1") = "F1,F2,F3"  
Value = oDIQ.MatchFrequencyRange("port 2") 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_MatchFrequencyRange(BSTR port, BSTR* MatchFrequencyRange);
HRESULT put_MatchFrequencyRange(BSTR port, BSTR MatchFrequencyRange);  
  
#### Interface

|  IDIQ  
  
* * *

