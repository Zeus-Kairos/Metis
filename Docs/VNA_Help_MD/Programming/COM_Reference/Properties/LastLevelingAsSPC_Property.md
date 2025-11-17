##### Write/Read

|

##### [About Receiver Leveling](../../../S1_Settings/Receiver_Leveling.md)  
  
---|---  
  
## LastLevelingAsSPC Property

* * *

#### Description

|  Sets and returns the state of Use Last Result for Source Power Cal. When
Leveling Mode is switched back to Internal, this feature turns Source Power
Cal correction ON using the latest receiver leveling correction data.  
---|---  
  
####  VB Syntax

|  RxLevel.LastLevelingAsSPC(srcPort) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
RxLevel |  A [ReceiverLeveling](../Objects/RXLevelingConfiguration_Object.md) Object  
srcPort |  (Long Integer) Source port being used for Receiver Leveling. Note: If the source port is defined by a string name, such as an external source, a balanced port, or one of the Source 2 outputs on the 2-port 2-source PNA-X model, then use [chan.getPortNumber](../Methods/GetPortNumber_Method.md) to translate the string into a port number. To learn more see [Remotely Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.md)  
  
#### value

|  (Boolean) . Choose from: True \- When Leveling Mode is switched back to
Internal, Source Power Cal correction is turned ON using the latest receiver
leveling correction data. False \- When Leveling Mode is switched back to
Internal, Source Power Cal correction is NOT turned ON.  
  
#### Return Type

|  Variant Boolean  
  
#### Default

|  False  
  
#### Examples

|  rxLevel.LastLevelingAsSPC (1) = True ' Write  
value = rxLevel.LastLevelingAsSPC 2' Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_LastLevelingAsSPC(long port, VARIANT_BOOL* pVal); HRESULT
put_LastLevelingAsSPC(long port, VARIANT_BOOL newVal);  
  
#### Interface

|  IReceiverLevelingConfiguration2  
  
* * *

