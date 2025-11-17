##### Write/Read

|

##### [About Power Level](../../../S1_Settings/Power_Level.md)  
  
---|---  
  
## TestPortPower Property

* * *

#### Description

|  Sets or returns the RF power level for the channel  
or  
Sets or returns the RF power level of the segment.  
---|---  
  
####  VB Syntax

|  object.TestPortPower(srcPort) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  A [Channel](../Objects/Channel_Object.md) (object) - to set coupled power, use chan.[CouplePorts](Couple_Ports_Property.md). If CouplePorts = False, then each port power can be set independently. Otherwise, chanTestPortPower (1) = value sets power level at both ports.  
or  
A [CalSet](../Objects/CalSet_Object.md) (object) or A
[Segment](../Objects/Segment_Object.md) (object)  
srcPort |  (long integer) \- Source Port number. Note: If the port is defined by a string name, such as an external source, a balanced port, or one of the Source 2 outputs on the 2-port 2-source VNA-x model, then you must use [chan.getPortNumber](../Methods/GetPortNumber_Method.md) to translate the string into a port number. To learn more see [Remotely Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.md).  
value |  (double) \- RF Power in dBm. Note: The range of settable power values depends on the VNA model and if source attenuators are installed. To determine the range of values, use [cap.MaximumSourceALCPower](MaximumSourceALCPower_Property.md) and [cap.MinimumSourceALCPower](MinimumSourceALCPower_Property.md) Actual achievable leveled power depends on frequency.  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  chan.TestPortPower(1) = 5 'sets the port 1 RF power level for the channel
object -Write  
powerlev = Chan.TestPortPower(1) 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_TestPortPower(long port, double *pVal)  
HRESULT put_TestPortPower(long port, double newVal)  
  
#### Interface

|  IChannel  
ICalSet3  
ISegment  
  
* * *

