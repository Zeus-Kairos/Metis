##### Write/Read

|

##### [About Power Sweep](../../../S1_Settings/Sweep.md#power)  
  
---|---  
  
## StopPowerEx Property

* * *

#### Description

|  Sets and reads the power sweep start power value for a specific port. This
allows uncoupled forward and reverse power sweep ranges. Must also set
[SweepType](Sweep_Type_Property.md) = naPowerSweep,
[Coupled](Coupled_Property.md) = False (Off), and
[StartPowerEx.](StartPowerEx_Property.md)  
---|---  
  
####  VB Syntax

|  chan.StopPowerEx (srcPort) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan |  A [Channel](../Objects/Channel_Object.md) (object)  
srcPort |  (long integer)  Source port for which to set the Stop power value. Note: If the port is defined by a string name, such as an external source, a balanced port, or one of the Source 2 outputs on the 2-port 2-source VNA-x model, then you must use [chan.getPortNumber](../Methods/GetPortNumber_Method.md) to translate the string into a port number. To learn more see [Remotely Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.md).  
value |  (double) \- Stop Power in dBm. Note: The range of settable power values depends on the VNA model and if source attenuators are installed. To determine the range of values, use [cap.MaximumSourceALCPower](MaximumSourceALCPower_Property.md) and [cap.MinimumSourceALCPower](MinimumSourceALCPower_Property.md) Auto attenuation is not allowed in Power Sweep.  
  
#### Return Type

|  Double  
  
#### Default

|  0 dBm  
  
#### Examples

|  Chan.StopPowerEx 1 = -10 'Write  
stopPwr = Chan.StopPowerEx 2 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_StopPowerEx(long port, double *pVal)  
HRESULT put_StopPowerEx(long port, double newVal)  
  
#### Interface

|  IChannel13  
  
* * *

