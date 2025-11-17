##### Write/Read

|

##### [About Receiver Leveling](../../../S1_Settings/Receiver_Leveling.md)  
  
---|---  
  
## PowerStep Property

* * *

#### Description

|  Sets and returns the safe mode power step value.  
---|---  
  
####  VB Syntax

|  RxLevel.PowerStep(srcPort) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
RxLevel |  A [ReceiverLeveling](../Objects/RXLevelingConfiguration_Object.md) Object  
srcPort |  (Long Integer) Source port for which to set the power step for Receiver Leveling. Note: If the source port is defined by a string name, such as an external source, a balanced port, or one of the Source 2 outputs on the 2-port 2-source PNA-X model, then use [chan.getPortNumber](../Methods/GetPortNumber_Method.md) to translate the string into a port number. To learn more see [Remotely Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.md)  
  
#### value

|  (Double) Power step in dB.  
  
#### Return Type

|  (Double)  
  
#### Default

|  1 dB  
  
#### Examples

|  rxLevel.PowerStep (1) = 2 ' Write  
value = rxLevel.PowerStep 2' Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PowerStep(long port, double* pVal); HRESULT put_PowerStep(long
port, double newVal);  
  
#### Interface

|  IReceiverLevelingConfiguration  
  
* * *

