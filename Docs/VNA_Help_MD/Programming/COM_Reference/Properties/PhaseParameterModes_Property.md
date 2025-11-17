##### Read-only

|

##### [About Phase Control](../../../S1_Settings/Phase_Control.md)  
  
---|---  
  
## PhaseParameterModes Property

* * *

#### Description

|  Returns the available phase control modes for the specified port. Use
[PhaseControlMode](PhaseControlMode_Property.md) to set the Phase Control
mode.  
---|---  
  
####  VB Syntax

|  phase.PhaseParameterModes(srcPort) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
phase |  A [PhaseControl](../Objects/PhaseControl_Object.md) Object  
srcPort |  (Long Integer) Source port for which to make phase control settings. Note: If the source port is defined by a string name, such as an external source, a balanced port, or one of the Source 2 outputs on the 2-port 2-source PNA-X model, then use [chan.getPortNumber](../Methods/GetPortNumber_Method.md) to translate the string into a port number. To learn more see [Remotely Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.md)  
  
#### value

|  (String) Choose from: "Off" \- Turn phase control OFF "Openloop" \- Sets a
raw phase value for either swept phase or fixed phase, but no receivers are
used to control the phase. "Parameter" \- Sets and controls the phase of the
signal at <port>. "Reference" \- Reference port for a controlled (parameter)
port. Use [PhaseReferencePort](PhaseReferencePort_Property.md) to set the
reference port.  
  
#### Return Type

|  String  
  
#### Default

|  "Off"  
Example |  value = phase.PhaseParameterModes 2' Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PhaseParameterModes(long port, BSTR* pVal);  
  
#### Interface

|  IPhaseControl  
  
* * *

