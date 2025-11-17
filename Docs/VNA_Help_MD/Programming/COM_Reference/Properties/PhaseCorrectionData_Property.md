##### Write/Read

|

##### [About Phase Control](../../../S1_Settings/Phase_Control.md)  
  
---|---  
  
## PhaseCorrectionData Property

* * *

#### Description

|  Write and read an array of phase offsets. Each phase offset is summed with
each phase point to get new target value. The VNA attempts to set phase for
each target value. The number of phase offset values must be the same as the
number of data points.  
---|---  
  
####  VB Syntax

|  phase.PhaseCorrectionData(srcPort) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
phase |  A [PhaseControl](../Objects/PhaseControl_Object.md) Object  
srcPort |  (Long Integer) Source port for which to make phase control settings. Note: If the source port is defined by a string name, such as an external source, a balanced port, or one of the Source 2 outputs on the 2-port 2-source PNA-X model, then use [chan.getPortNumber](../Methods/GetPortNumber_Method.md) to translate the string into a port number. To learn more see [Remotely Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.md)  
  
#### value

|  (Long values) Phase offset data array.  
  
#### Return Type

|  Long data array  
  
#### Default

|  Not Applicable  
  
#### Examples

|  phase.PhaseCorrectionData 1 = 10,11,12 ' Write 3 phase offset values  
value = phase.PhaseCorrectionData 2' Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PhaseCorrectionData(long port, long* pVals); HRESULT
put_PhaseCorrectionData(long port, long newVals);  
  
#### Interface

|  IPhaseControl  
  
* * *

