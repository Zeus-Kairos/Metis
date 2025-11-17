##### Write/Read

|

##### [About Receiver Leveling](../../../S1_Settings/Receiver_Leveling.md)  
  
---|---  
  
## IterationNumber Property

* * *

#### Description

|  Sets and returns the maximum leveling sweep iterations to be used in order
to achieve the tolerance setting.  
---|---  
  
####  VB Syntax

|  RxLevel.IterationNumber(srcPort) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
RxLevel |  A [ReceiverLeveling](../Objects/RXLevelingConfiguration_Object.md) Object  
srcPort |  (Long Integer) Source port for which to set the IterationNumber for Receiver Leveling. Note: If the source port is defined by a string name, such as an external source, a balanced port, or one of the Source 2 outputs on the 2-port 2-source PNA-X model, then use [chan.getPortNumber](../Methods/GetPortNumber_Method.md) to translate the string into a port number. To learn more see [Remotely Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.md)  
  
#### value

|  (Long Integer) Max iterations. Choose a value between 1 and 25.  
  
#### Return Type

|  (Long Integer)  
  
#### Default

|  5  
  
#### Examples

|  rxLevel.IterationNumber (1) = 10 ' Write  
value = rxLevel.IterationNumber 2' Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_IterationNumber(long port, long* pVal); HRESULT
put_IterationNumber(long port, long newVal);  
  
#### Interface

|  IReceiverLevelingConfiguration  
  
* * *

