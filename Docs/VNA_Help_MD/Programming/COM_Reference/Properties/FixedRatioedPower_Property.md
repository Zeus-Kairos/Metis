##### Write/Read

|

##### [About Phase Control](../../../S1_Settings/Phase_Control.md)  
  
---|---  
  
## FixedRatioedPower Property

* * *

#### Description

|  Write and read the fixed power ratioed value. Must NOT be in power sweep to
use this value during phase control.  
---|---  
  
####  VB Syntax

|  phase.FixedRatioedPower(srcPort) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
phase |  A [PhaseControl](../Objects/PhaseControl_Object.md) Object  
srcPort |  (Long Integer) Source port for which to make phase control settings. Note: If the source port is defined by a string name, such as an external source, a balanced port, or one of the Source 2 outputs on the 2-port 2-source PNA-X model, then use [chan.getPortNumber](../Methods/GetPortNumber_Method.md) to translate the string into a port number. To learn more see [Remotely Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.md)  
  
#### value

|  (Double) Fixed power ratio value in dBc within the allowable range of the
VNA.  
  
#### Return Type

|  Double  
  
#### Default

|  0 dBc  
  
#### Examples

|  phase.FixedRatioedPower 1 = -1 ' Write  
value = phase.FixedRatioedPower 2' Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_FixedRatioedPower(long port, double* pVal); HRESULT
put_FixedRatioedPower(long port, double newVal);  
  
#### Interface

|  IPhaseControl  
  
* * *

