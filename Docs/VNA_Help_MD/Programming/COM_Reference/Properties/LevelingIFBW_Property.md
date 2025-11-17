##### Write/Read

|

##### [About Receiver Leveling](../../../S1_Settings/Receiver_Leveling.md)  
  
---|---  
  
## LevelingIFBW Property

* * *

#### Description

|  Sets and returns the IFBW to be used for leveling sweeps. Enable separate
IFBW for leveling sweeps using [FastMode Property](FastMode_Property.md).  
---|---  
  
####  VB Syntax

|  RxLevel.LevelingIFBW(srcPort) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
RxLevel |  A [ReceiverLeveling](../Objects/RXLevelingConfiguration_Object.md) Object  
srcPort |  (Long Integer) Source port for which to set the LevelingIFBW for Receiver Leveling. Note: If the source port is defined by a string name, such as an external source, a balanced port, or one of the Source 2 outputs on the 2-port 2-source PNA-X model, then use [chan.getPortNumber](../Methods/GetPortNumber_Method.md) to translate the string into a port number. To learn more see [Remotely Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.md)  
  
#### value

|  (Double) IFBW for leveling sweeps in Hz. The list of valid IF Bandwidths is
different depending on the VNA model. [See
list.](../../../S2_Opt/Trce_Noise.htm#IFDiag) If an invalid number is
specified, the VNA will round up to the closest valid number.  
  
#### Return Type

|  (Double)  
  
#### Default

|  100 kHz  
  
#### Examples

|  rxLevel.LevelingIFBW (1) = 1e3 ' Write  
value = rxLevel.LevelingIFBW 2' Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_LevelingIFBW(long port, double* pVal); HRESULT
put_LevelingIFBW(long port, double newVal);  
  
#### Interface

|  IReceiverLevelingConfiguration  
  
* * *

