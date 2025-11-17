##### Write/Read

|

##### [About Phase Control](../../../S1_Settings/Phase_Control.md)  
  
---|---  
  
## PhaseParameter Property

* * *

#### Description

|  Write and read the ratioed receivers (parameter) and paired port to use for
phase control.  
---|---  
  
####  VB Syntax

|  phase.PhaseParameter(srcPort) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
phase |  A [PhaseControl](../Objects/PhaseControl_Object.md) Object  
srcPort |  (Long Integer) Source port for which to make phase control settings. Note: If the source port is defined by a string name, such as an external source, a balanced port, or one of the Source 2 outputs on the 2-port 2-source PNA-X model, then use [chan.getPortNumber](../Methods/GetPortNumber_Method.md) to translate the string into a port number. To learn more see [Remotely Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.md)  
  
#### value

|  (String) Ratioed parameter. Choose any two VNA physical receivers. Use
either standard receiver notation ("R/R3") or [logical receiver
notation](../../../S1_Settings/Measurement_Parameters.htm#RecNotation)
("a1/a3"). Separate the two receiver names by a forward slash '/'. For
example: "a1/a3".  
  
#### Return Type

|  String  
  
#### Default

|  "a1/b1"  
  
#### Examples

|  phase.PhaseParameter 1 = "a1/a3" ' Write  
value = phase.PhaseParameter 2' Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PhaseParameter(long port, BSTR* pVal); HRESULT
put_PhaseParameter(long port, BSTR newVal);  
  
#### Interface

|  IPhaseControl  
  
* * *

