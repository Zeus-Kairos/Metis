##### Write/Read

|

##### [About Receiver Leveling](../../../S1_Settings/Receiver_Leveling.md)  
  
---|---  
  
## FrequencyType Property

* * *

#### Description

|  Sets and returns the frequency range to use for receiver leveling. On the
user interface, this is the "Receiver frequency is determined by:" setting.  
---|---  
  
####  VB Syntax

|  RxLevel.FrequencyType(srcPort) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
RxLevel |  A [ReceiverLeveling](../Objects/RXLevelingConfiguration_Object.md) Object  
srcPort |  (Long Integer) Source port for Receiver Leveling. Note: If the source port is defined by a string name, such as an external source, a balanced port, or one of the Source 2 outputs on the 2-port 2-source PNA-X model, then use [chan.getPortNumber](../Methods/GetPortNumber_Method.md) to translate the string into a port number. To learn more see [Remotely Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.md)  
  
#### value

|  (Enum) Frequency range. Choose from: naAutoFrequency (0) \- always uses the
frequency range that is assigned to the measurement receiver. naInputFrequency
(3) \- Mixer/Converter input frequency range. naOutputFrequency (4) \-
Mixer/Converter input frequency range. naReceiverFrequency (1) \- FOM Receiver
frequency range. naSourceFrequency (2) \- FOM Source frequency range  
  
#### Return Type

|  Enum  
  
#### Default

|  naAutoFrequency (0)  
  
#### Examples

|  rxLevel.FrequencyType (1) = naAutoFrequency ' Write  
value = rxLevel.FrequencyType 2' Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_FrequencyType(long port, tagNAFrequencyType* pVal); HRESULT
put_FrequencyType(long port, tagNAFrequencyType newVal);  
  
#### Interface

|  IRxLevelingConfiguration3  
  
* * *

