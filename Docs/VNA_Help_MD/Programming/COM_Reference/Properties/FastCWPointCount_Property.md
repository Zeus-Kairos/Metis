##### Write-Read

|

##### [About FastCW](../../../IFAccess/FIFO_and_other_Antenna_Features.md)  
  
---|---  
  
## FastCWPointCount Property

* * *

#### Description

|  Enables Fast CW sweep and sets the number of data points for the channel.
[Sweep Type](Sweep_Type_Property.md) must already be set to CWTime and FIFO
must already be enabled.

### See Also

[FIFO and other Antenna
Features](../../../IFAccess/FIFO_and_other_Antenna_Features.htm) [FIFO
Object](../Objects/FIFO_Object.htm) [Example
program](../../COM_Example_Programs/Setup_FastCW_and_FIFO.htm) [N5264B
Measurement Receiver](../../../IFAccess/N5264A.htm)  
---|---  
  
####  VB Syntax

|  chan.FastCWPointCount = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan |  A [Channel](../Objects/Channel_Object.md) Object  
value |  (Long Integer) Number of data points to measure in Fast CW mode. This setting overwrites the standard number of points setting for the channel. This setting overwrites the standard number of points setting for the channel. The minimum value is 1. The maximum value is 232 \- 1 = 2,147,483,647. The "-1" indicates infinite point count (i.e., go forever). Any other value will produce invalid results. If the data acquisition rate exceeds 400,000 points per second, the upper limit on the number of points is 11e6. The following are conditions that can cause the higher data rate:

  * IFBW's >= 1 MHz and internally triggered.
  * fastCW sweeps that are externally triggered at a rate faster than 400,000 points per second.

Set to 0 to disable Fast CW.  
  
#### Return Type

|  Long Integer  
  
#### Default

|  0  
  
#### Examples

|  chan.FastCWPointCount = 1e3 'Write  
value = chan.FastCWPointCount 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_FastCWPointCount(long *value) HRESULT put_FastCWPointCount(long
value)  
  
#### Interface

|  IChannel16  
  
* * *

  

