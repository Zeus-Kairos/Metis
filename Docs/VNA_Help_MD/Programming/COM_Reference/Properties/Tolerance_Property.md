##### Write/Read

|

##### [About Receiver Leveling](../../../S1_Settings/Receiver_Leveling.md)  
  
---|---  
  
## Tolerance Property

* * *

#### Description

|  Sets and returns the tolerance value for leveling sweeps.  
---|---  
  
####  VB Syntax

|  RxLevel.Tolerance(srcPort) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
RxLevel |  A [ReceiverLeveling](../Objects/RXLevelingConfiguration_Object.md) Object  
srcPort |  (Long Integer) Source port for which to set the tolerance value for Receiver Leveling. Note: If the source port is defined by a string name, such as an external source, a balanced port, or one of the Source 2 outputs on the 2-port 2-source PNA-X model, then use [chan.getPortNumber](../Methods/GetPortNumber_Method.md) to translate the string into a port number. To learn more see [Remotely Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.md)  
  
#### value

|  (Double) Tolerance level in dB.  
  
#### Return Type

|  (Double)  
  
#### Default

|  .1 dB  
  
#### Examples

|  rxLevel.Tolerance (1) = .5 ' Write  
value = rxLevel.Tolerance 2' Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Tolerance(long port, double* pVal); HRESULT put_Tolerance(long
port, double newVal);  
  
#### Interface

|  IReceiverLevelingConfiguration  
  
* * *

