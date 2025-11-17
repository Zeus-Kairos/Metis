##### Write/Read

|

##### [About Receiver Leveling](../../../S1_Settings/Receiver_Leveling.md)  
  
---|---  
  
## SafeMode Property

* * *

#### Description

|  Sets and returns the state of Safe Mode.  
---|---  
  
####  VB Syntax

|  RxLevel.SafeMode(srcPort) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
RxLevel |  A [ReceiverLeveling](../Objects/RXLevelingConfiguration_Object.md) Object  
value |  (Boolean) Choose from: True \- Safe mode ON False \- Safe mode OFF  
  
#### srcPort

|  (Long Integer) Source port for which to set the Safe Mode state for
Receiver Leveling. Note: If the source port is defined by a string name, such
as an external source, a balanced port, or one of the Source 2 outputs on the
2-port 2-source PNA-X model, then use
[chan.getPortNumber](../Methods/GetPortNumber_Method.md) to translate the
string into a port number. To learn more see [Remotely Specifying a Source
Port](../../Remotely_Specifying_a_Source_Port.htm)  
  
#### Return Type

|  Variant Boolean  
  
#### Default

|  False  
  
#### Examples

|  rxLevel.SafeMode (1) = True ' Write  
value = rxLevel.SafeMode 2' Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_SafeMode(long port, VARIANT_BOOL* pLevelingSafeMode); HRESULT
put_SafeMode(long port, VARIANT_BOOL LevelingSafeMode);  
  
#### Interface

|  IReceiverLevelingConfiguration  
  
* * *

