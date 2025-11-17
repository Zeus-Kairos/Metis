##### Write/Read

|

##### [About Receiver Leveling](../../../S1_Settings/Receiver_Leveling.md)  
  
---|---  
  
## FastMode Property

* * *

#### Description

|  Sets and returns the state of a separate IFBW setting for leveling sweeps.
ON allows a higher (faster) IFBW than the measurement sweep. It also causes
leveling sweeps to be noisier.  
---|---  
  
####  VB Syntax

|  RxLevel.FastMode(srcPort) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
RxLevel |  A [ReceiverLeveling](../Objects/RXLevelingConfiguration_Object.md) Object  
srcPort |  (Long Integer) Source port for which to set Fast Mode for Receiver Leveling. Note: If the source port is defined by a string name, such as an external source, a balanced port, or one of the Source 2 outputs on the 2-port 2-source PNA-X model, then use [chan.getPortNumber](../Methods/GetPortNumber_Method.md) to translate the string into a port number. To learn more see [Remotely Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.md)  
  
#### value

|  (Boolean) Separate IFBW setting state. Choose from: True \- Use separate
IFBW setting. Specify IFBW using [LevelingIFBW](LevelingIFBW_Property.md).
False \- Use same IFBW as the measurement sweep. Specify IFBW using [IF
Bandwidth](IF_Bandwidth_Property.htm).  
  
#### Return Type

|  Variant Boolean  
  
#### Default

|  True  
  
#### Examples

|  rxLevel.FastMode (1) = True ' Write  
value = rxLevel.FastMode 2' Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_FastMode(long port, VARIANT_BOOL* pVal); HRESULT
put_FastMode(long port, VARIANT_BOOL newVal);  
  
#### Interface

|  IReceiverLevelingConfiguration  
  
* * *

