##### Write/Read

|

##### [About Receiver Leveling](../../../S1_Settings/Receiver_Leveling.md)  
  
---|---  
  
## ReceiverRatio Property

* * *

#### Description

|  Sets and returns the receiver ratio pair to be used with Receiver Leveling.
To perform receiver leveling with a ratioed receiver, use [ReceiverRatio
Property](ReceiverRatio_Property.htm).  
---|---  
  
####  VB Syntax

|  RxLevel.ReceiverRatio(srcPort) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
RxLevel |  A [ReceiverLeveling](../Objects/RXLevelingConfiguration_Object.md) Object  
srcPort |  (Long Integer) Source port for which to set the receiver for Receiver Leveling. Note: If the source port is defined by a string name, such as an external source, a balanced port, or one of the Source 2 outputs on the 2-port 2-source PNA-X model, then use [chan.getPortNumber](../Methods/GetPortNumber_Method.md) to translate the string into a port number. To learn more see [Remotely Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.md)  
  
#### value

|  (String) Receiver to use for the leveling sweeps. (Not case sensitive).
Choose any receiver in your VNA. see the block diagram of your VNA, located at
the bottom of all [Specs documents.](../../../Specs/ManualChoice.md)
Receivers can also be referred to using logical receiver notation. This
notation makes it easy to refer to receivers with an [external test
set](../../../System/External_Testset_Control.htm) connected to the VNA. You
do not need to know which physical receiver is used for each test port. [Learn
more](../../../S1_Settings/Measurement_Parameters.htm#RecNotation).  
  
#### Return Type

|  String  
  
#### Default

|  Not applicable  
  
#### Examples

|  rxLevel.ReceiverRatio (1) = "R1" ' Write rxLevel.ReceiverRatio (1) = "b2" '
Write  
value = rxLevel.ReceiverRatio 2' Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_ReceiverRatio( long port, BSTR* pVal); HRESULT
put_ReceiverRatio( long port, BSTR newVal);  
  
#### Interface

|  IReceiverLevelingConfiguration  
  
* * *

