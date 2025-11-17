##### Write/Read

|

##### [About Phase Control](../../../S1_Settings/Phase_Control.md)  
  
---|---  
  
## StartRatioedPower Property

* * *

#### Description

|  Write and read the start power ratioed value. Must also set
[SweepType](Sweep_Type_Property.md) to Power.  
---|---  
  
####  VB Syntax

|  phase.StartRatioedPower(srcPort) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
phase |  A [PhaseControl](../Objects/PhaseControl_Object.md) Object  
srcPort |  (Long Integer) Source port for which to make phase control settings. Note: If the source port is defined by a string name, such as an external source, a balanced port, or one of the Source 2 outputs on the 2-port 2-source PNA-X model, then use [chan.getPortNumber](../Methods/GetPortNumber_Method.md) to translate the string into a port number. To learn more see [Remotely Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.md)  
  
#### value

|  (Double) Start power ratio value in dBc. Must be within the allowable range
of the VNA.  
  
#### Return Type

|  Double  
  
#### Default

|  0 dBc  
  
#### Examples

|  phase.StartRatioedPower 1 = -1 ' Write  
value = phase.StartRatioedPower 2' Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_StartRatioedPower(long port, double* pVal); HRESULT
put_StartRatioedPower(long port, double newVal);  
  
#### Interface

|  IPhaseControl  
  
* * *

