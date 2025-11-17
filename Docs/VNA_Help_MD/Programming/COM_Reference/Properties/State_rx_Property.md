##### Write/Read

|

##### [About Receiver Leveling](../../../S1_Settings/Receiver_Leveling.md)  
  
---|---  
  
## State (Rx Leveling) Property

* * *

#### Description

|  Sets and reads the state of Receiver Leveling for a specific source port.  
---|---  
  
####  VB Syntax

|  RxLevel.State(srcPort) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
RxLevel |  A [ReceiverLeveling](../Objects/RXLevelingConfiguration_Object.md) Object  
value |  (Boolean) Choose from: True \- Receiver leveling ON False \- Receiver leveling OFF  
  
#### srcPort

|  (Long Integer) Source port for which to set the state of Receiver Leveling.
Note: If the source port is defined by a string name, such as an external
source, a balanced port, or one of the Source 2 outputs on the 2-port 2-source
PNA-X model, then use
[chan.getPortNumber](../Methods/GetPortNumber_Method.md) to translate the
string into a port number. To learn more see [Remotely Specifying a Source
Port](../../Remotely_Specifying_a_Source_Port.htm)  
  
#### Return Type

|  Variant Boolean  
  
#### Default

|  False  
  
#### Examples

|  rxLevel.State (1) = True ' Write  
value = rxLevel.State 2' Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_State(long port, VARIANT_BOOL* pLevelingState); HRESULT
put_State(long port, VARIANT_BOOL LevelingState);  
  
#### Interface

|  IReceiverLevelingConfiguration  
  
* * *

