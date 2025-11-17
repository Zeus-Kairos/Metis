##### Write/Read

|

##### [About Diff I/Q App](../../../Applications/Differential_IQ.md)  
  
---|---  
  
## MatchState Property

* * *

#### Description

|  Sets and reads the Match Correction ON/OFF state. On the [Source
Configuration](../../../Applications/Differential_IQ.htm#SourceConfigurationDiag)
dialog under Match Correction, this is the Match Correction ON setting.  
---|---  
  
####  VB Syntax

|  DIQ.MatchState (port) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
DIQ |  A [Differential I/Q](../Objects/DIQ_Object.md) (object)  
port |  (String) Source port name. Use [SourcePortNames](SourcePortNames_Property.md) to read a list of valid source ports.  
value |  (Boolean) Choose from:

  * True - Perform Match Correction
  * False - Do not perform Match Correction.

  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  oDIQ.MatchState("port 2") = True  
Value = oDIQ.MatchState("port 2") 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_MatchState(BSTR port, BOOL* MatchState); HRESULT
put_MatchState(BSTR port, BOOL MatchState);  
  
#### Interface

|  IDIQ  
  
* * *

