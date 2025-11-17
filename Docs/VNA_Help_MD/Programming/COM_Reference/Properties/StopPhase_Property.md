##### Write/Read

|

##### [About Phase Control](../../../S1_Settings/Phase_Control.md)  
  
---|---  
  
## StopPhase Property

* * *

#### Description

|  Write and read the stop value of phase sweep. Must also send [Sweep Type
Property](Sweep_Type_Property.htm) to put the analyzer into phase sweep mode.  
---|---  
  
####  VB Syntax

|  phase.StopPhase(srcPort) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
phase |  A [PhaseControl](../Objects/PhaseControl_Object.md) Object  
srcPort |  (Long Integer) Source port for which to make phase control settings. Note: If the source port is defined by a string name, such as an external source, a balanced port, or one of the Source 2 outputs on the 2-port 2-source PNA-X model, then use [chan.getPortNumber](../Methods/GetPortNumber_Method.md) to translate the string into a port number. To learn more see [Remotely Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.md)  
  
#### value

|  (Double) Stop phase value in degrees. Choose a value between -360 and 360.  
  
#### Return Type

|  Double  
  
#### Default

|  0 degrees  
  
#### Examples

|  phase.StopPhase 1 = 60 ' Write  
value = phase.StopPhase 2' Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_StopPhase(long port, double* pVal); HRESULT put_StopPhase(long
port, double newVal);  
  
#### Interface

|  IPhaseControl  
  
* * *

