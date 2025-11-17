##### Write/Read

|

##### [About Phase Control](../../../S1_Settings/Phase_Control.md)  
  
---|---  
  
## PhaseControlMode Property

* * *

#### Description

|  Write and read the Phase Control mode for the specified port.  
---|---  
  
####  VB Syntax

|  phase.PhaseControlMode(srcPort) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
phase |  A [PhaseControl](../Objects/PhaseControl_Object.md) Object  
srcPort |  (Long Integer) Source port for which to make phase control settings. Note: If the source port is defined by a string name, such as an external source, a balanced port, or one of the Source 2 outputs on the 2-port 2-source PNA-X model, then use [chan.getPortNumber](../Methods/GetPortNumber_Method.md) to translate the string into a port number. To learn more see [Remotely Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.md)  
  
#### value

|  (Enum as NAPhaseControlMode) Choose from: 0 - naPhaseControlOff Do NOT
control the phase of <port>. 1 - naPhaseControlParameter Control the phase of
<port>. 2 - naPhaseControlReference (READ-only) - reference port for a
'controlled' (parameter) Port. 3 - naPhaseControlOpenLoop Sets a raw phase
value for either swept phase or fixed phase, but no receivers are used to
control the phase.  
  
#### Return Type

|  Enum  
  
#### Default

|  0 - naPhaseControlOff  
  
#### Examples

|  phase.PhaseControlMode 1 = naPhaseControlParameter ' Write  
value = phase.PhaseControlMode 2' Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PhaseControlMode(long port, enum NAPhaseControlMode* pVal);
HRESULT put_PhaseControlMode(long port, enum NAPhaseControlMode newVal);  
  
#### Interface

|  IPhaseControl  
  
* * *

