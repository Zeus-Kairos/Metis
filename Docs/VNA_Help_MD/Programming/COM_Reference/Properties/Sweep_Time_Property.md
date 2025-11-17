##### Write/Read

|

##### [About Sweep Time](../../../S2_Opt/Long_Devices.md#slow)  
  
---|---  
  
## SweepTime Property

* * *

#### Description

|  Sets the Sweep time of the analyzer. If sweep time accuracy is critical,
use ONLY the values that are attained using the up and down arrows next to the
sweep time entry box. [See Sweep
Time.](../../../S1_Settings/Sweep.htm#sweepTimeDiag)  
---|---  
  
####  VB Syntax

|  object.SweepTime = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  [Channel](../Objects/Channel_Object.md) (object) or [Segment](../Objects/Segment_Object.md) (object) first set [SweepTimeOption](SweepTimeOption_Property.md) to true. or [CalSet](../Objects/CalSet_Object.md) (object) - Read-only property  
value |  (double) \- Sweep time in seconds. The maximum sweep time of the VNA is 86400 seconds (1 day). To set the fastest sweep speed possible, set this value to 0.  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  chan.SweepTime = 3e-3 'Write  
swptme = chan.SweepTime 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_SweepTime(double *pVal)  
HRESULT put_SweepTime(double newVal)  
  
#### Interface

|  IChannel CalSet3 ISegment2

