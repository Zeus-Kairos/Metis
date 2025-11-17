##### Write/Read

|

##### [About Phase Control](../../../S1_Settings/Phase_Control.md)  
  
---|---  
  
## RatioedPowerCorrectionEnabled Property

* * *

#### Description

|  Write and read whether to use the ratioed power offset array. Use
[RatioedPowerCorrectionData Property](RatioedPowerCorrectionData_Property.md)
to write or read the offset data.  
---|---  
  
####  VB Syntax

|  phase.RatioedPowerCorrectionEnabled(srcPort) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
phase |  A [PhaseControl](../Objects/PhaseControl_Object.md) Object  
srcPort |  (Long Integer) Source port for which to make phase control settings. Note: If the source port is defined by a string name, such as an external source, a balanced port, or one of the Source 2 outputs on the 2-port 2-source PNA-X model, then use [chan.getPortNumber](../Methods/GetPortNumber_Method.md) to translate the string into a port number. To learn more see [Remotely Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.md)  
  
#### value

|  (Boolean) Ratioed power offset array state. True  Apply offset array.
False  Do NOT apply offset array.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  phase.RatioedPowerCorrectionEnabled 1 = True ' Write  
value = phase.RatioedPowerCorrectionEnabled 2' Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_RatioedPowerCorrectionEnabled(long port, VARIANT_BOOL* pVal);
HRESULT put_RatioedPowerCorrectionEnabled(long port, VARIANT_BOOL newVal);  
  
#### Interface

|  IPhaseControl  
  
* * *

