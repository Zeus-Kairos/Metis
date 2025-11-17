##### Write/Read

|

##### [About Phase Control](../../../S1_Settings/Phase_Control.md)  
  
---|---  
  
## CouplePhasePortSettings Property

* * *

#### Description

|  Sets and returns whether to couple phase control settings (IFBW, Tolerance,
Max Iterations).  
---|---  
  
####  VB Syntax

|  phase.CouplePhasePortSettings(srcPort) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
phase |  A [PhaseControl](../Objects/PhaseControl_Object.md) Object  
srcPort |  (Long Integer) Source port for which to make phase control settings. Note: If the source port is defined by a string name, such as an external source, a balanced port, or one of the Source 2 outputs on the 2-port 2-source PNA-X model, then use [chan.getPortNumber](../Methods/GetPortNumber_Method.md) to translate the string into a port number. To learn more see [Remotely Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.md)  
  
#### value

|  (Boolean) Coupling state. Choose from: True \- Couple phase control
settings. The phase control settings from <port> are copied to the other
phase-controlled ports. False \- Do NOT couple phase control settings. The
phase control settings for each phase-controlled port are made independently.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  phase.CouplePhasePortSettings 1 = True ' Write  
value = phase.CouplePhasePortSettings 2' Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_CouplePhasePortSettings(long port, VARIANT_BOOL* pVal); HRESULT
put_CouplePhasePortSettings(long port, VARIANT_BOOL newVal);  
  
#### Interface

|  IPhaseControl  
  
* * *

