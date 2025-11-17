##### Write/Read

|

##### [About Diff I/Q App](../../../Applications/Differential_IQ.md)  
  
---|---  
  
## SourceStateProperty

* * *

#### Description

|  Sets and reads the ON / OFF state of the source specified by (port). At the
top of the [Source
Configuration](../../../Applications/Differential_IQ.htm#SourceConfigurationDiag)
dialog this is the Source State setting.  
---|---  
  
####  VB Syntax

|  DIQ.SourceState(port) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
DIQ |  A [Differential I/Q](../Objects/DIQ_Object.md) (object)  
port |  (String) Source port name. Use [SourcePortNames](SourcePortNames_Property.md) to read a list of valid source ports.  
value |  (Enum as NAPortState) Choose from: naPortAUTO (or 0) \- Source power is turned ON at the specified test port when required by the measurement. This is the most common (default) setting. Auto sources are turned OFF when other sources are performing Match Correction sweeps. naPortON (or 1) \- Source power is ALWAYS ON, regardless of measurements that are in process. Use this setting to supply source power to a DUT port that always requires power, such as an LO port. This could turn OFF power at another test port. [Learn about internal second source restrictions](../../../S0_Start/Internal_Second_Source.md). naPortOFF (or 2) \- Source power is never ON, regardless of the measurement requirements. Use this setting to prevent damage to a sensitive DUT test port.  
  
#### Return Type

|  Enum  
  
#### Default

|  naPortAUTO (or 0)  
  
#### Examples

|  diq.PortState("Port 2") = naPortAUTO 'Write  
Value = oDIQ.PortState("port 2") 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PortState(BSTR port, tagNASourceState* SourceState); HRESULT
put_PortState(BSTR port, tagNASourceState SourceState);  
  
#### Interface

|  IDIQ  
  
* * *

