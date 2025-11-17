##### Write/Read

|

##### [About Phase Control](../../../S1_Settings/Phase_Control.md)  
  
---|---  
  
## PhaseReferencePort Property

* * *

#### Description

|  Sets and returns the reference port for the Phase Control measurement.  
---|---  
  
####  VB Syntax

|  phase.PhaseReferencePort(srcPort) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
phase |  A [PhaseControl](../Objects/PhaseControl_Object.md) Object  
srcPort |  (Long Integer) Source port for which to make phase control settings. Note: If the source port is defined by a string name, such as an external source, a balanced port, or one of the Source 2 outputs on the 2-port 2-source PNA-X model, then use [chan.getPortNumber](../Methods/GetPortNumber_Method.md) to translate the string into a port number. To learn more see [Remotely Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.md)  
  
#### value

|  (Long Integer) Reference port number. ONLY specific ports are available to
be a reference for each source port. [Learn
more](../../../S1_Settings/Phase_Control.htm#PhaseSetupDiag).  
  
#### Return Type

|  Long Integer  
  
#### Default

|  Depends on the controlled port.  
  
#### Examples

|  phase.PhaseReferencePort 1 = 3 ' Write  
value = phase.PhaseReferencePort 2' Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PhaseReferencePort(long port, long* pVal); HRESULT
put_PhaseReferencePort(long port, long newVal);  
  
#### Interface

|  IPhaseControl  
  
* * *

