##### Write/Read

|

##### [About Diff I/Q App](../../../Applications/Differential_IQ.md)  
  
---|---  
  
## PowerSweepState Property

* * *

#### Description

|  Sets and reads the state of sweeping power. On the [Source
Configuration](../../../Applications/Differential_IQ.htm#SourceConfigurationDiag)
dialog under Power, this is the Sweep Power (On|Off) setting.  
---|---  
  
####  VB Syntax

|  DIQ.PowerSweepState (port) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
DIQ |  A [Differential I/Q](../Objects/DIQ_Object.md) (object)  
port |  (String) Source port name. Use [SourcePortNames](SourcePortNames_Property.md) to read a list of valid source ports.  
value |  (Boolean) Sweep Power state. Choose from:

  * True - Perform power sweep.
  * False - Do not perform power sweep.

  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  oDIQ.PowerSweepState("port 2") = True  
Value = oDIQ.PowerSweepState("port 2") 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PowerSweepState(BSTR port, BOOL* PowerSweepState); HRESULT
put_PowerSweepState(BSTR port, BOOL PowerSweepState);  
  
#### Interface

|  IDIQ  
  
* * *

