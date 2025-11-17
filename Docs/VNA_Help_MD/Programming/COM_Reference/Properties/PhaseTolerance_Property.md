##### Write/Read

|

##### [About Phase Control](../../../S1_Settings/Phase_Control.md)  
  
---|---  
  
## PhaseTolerance Property

* * *

#### Description

|  Write and read the tolerance value to be used for background phase sweeps.  
---|---  
  
####  VB Syntax

|  phase.PhaseTolerance(srcPort) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
phase |  A [PhaseControl](../Objects/PhaseControl_Object.md) Object  
srcPort |  (Long Integer) Source port for which to make phase control settings. Note: If the source port is defined by a string name, such as an external source, a balanced port, or one of the Source 2 outputs on the 2-port 2-source PNA-X model, then use [chan.getPortNumber](../Methods/GetPortNumber_Method.md) to translate the string into a port number. To learn more see [Remotely Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.md)  
  
#### value

|  (Double) Tolerance for background sweeps in degrees. Choose a value between
1 and 5.  
  
#### Return Type

|  Double  
  
#### Default

|  5 degrees  
  
#### Examples

|  phase.PhaseTolerance 1 = 3 ' Write  
value = phase.PhaseTolerance 2' Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PhaseTolerance(long port, double* pVal); HRESULT
put_PhaseTolerance(long port, double newVal);  
  
#### Interface

|  IPhaseControl  
  
* * *

