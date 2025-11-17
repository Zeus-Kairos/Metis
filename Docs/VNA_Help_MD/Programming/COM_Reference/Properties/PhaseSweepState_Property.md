##### Write/Read

|

##### [About Diff I/Q App](../../../Applications/Differential_IQ.md)  
  
---|---  
  
## PhaseSweepState Property

* * *

#### Description

|  Sets and reads the ON / OFF state of phase sweep. On the [Source
Configuration](../../../Applications/Differential_IQ.htm#SourceConfigurationDiag)
dialog under Phase, this is the Sweep Phase (On|Off) setting.  
---|---  
  
####  VB Syntax

|  DIQ.PhaseSweepState (port) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
DIQ |  A [Differential I/Q](../Objects/DIQ_Object.md) (object)  
port |  (String) Source port name. Use [SourcePortNames](SourcePortNames_Property.md) to read a list of valid source ports.  
value |  (Boolean) Choose from:

  * True - Sweep phase.
  * False - Do not sweep phase.

  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  oDIQ.PhaseSweepState("port 2") = True  
Value = oDIQ.PhaseSweepState("port 2") 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PhaseSweepState(BSTR port, BOOL* PhaseSweepState); HRESULT
put_PhaseSweepState(BSTR port, BOOL PhaseSweepState);  
  
#### Interface

|  IDIQ  
  
* * *

