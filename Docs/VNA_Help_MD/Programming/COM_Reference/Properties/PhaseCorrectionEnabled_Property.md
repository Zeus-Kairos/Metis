##### Write/Read

|

##### [About Phase Control](../../../S1_Settings/Phase_Control.md)  
  
---|---  
  
## PhaseCorrectionEnabled Property

* * *

#### Description

|  Write and read whether to use the phase correction offset array. Use
[PhaseCorrectionData](PhaseCorrectionData_Property.md) to write or read the
offset data.  
---|---  
  
####  VB Syntax

|  phase.PhaseCorrectionEnabled(srcPort) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
phase |  A [PhaseControl](../Objects/PhaseControl_Object.md) Object  
srcPort |  (Long Integer) Source port for which to make phase control settings. Note: If the source port is defined by a string name, such as an external source, a balanced port, or one of the Source 2 outputs on the 2-port 2-source PNA-X model, then use [chan.getPortNumber](../Methods/GetPortNumber_Method.md) to translate the string into a port number. To learn more see [Remotely Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.md)  
  
#### value

|  (Boolean) Phase correction array state. True  Apply phase correction
offset array. False  Do NOT apply phase correction offset array.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  phase.PhaseCorrectionEnabled 1 = True ' Write  
value = phase.PhaseCorrectionEnabled 2' Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PhaseCorrectionEnabled(long port, VARIANT_BOOL* pVal); HRESULT
put_PhaseCorrectionEnabled(long port, VARIANT_BOOL newVal);  
  
#### Interface

|  IPhaseControl  
  
* * *

