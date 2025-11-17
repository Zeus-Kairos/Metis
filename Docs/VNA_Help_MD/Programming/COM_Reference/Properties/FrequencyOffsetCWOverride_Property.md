##### Write/Read

|

##### [About Frequency Offset](../../../FreqOffset/Frequency_Offset_Mode.md)  
  
---|---  
  
## FrequencyOffsetCWOverride Property Superseded

* * *

#### Description

|  This method is replaced by properties on the [FOMRange
Object.](../Objects/FOMRange_Object.htm) Establishes a fixed (CW) stimulus
frequency while measuring the Response over a swept frequency range. For
example, a fixed-frequency VNA stimulus may be applied to the RF input of a
mixer whose local oscillator (LO) is being swept. Because the IF output of the
mixer will be swept, the VNA receivers must also be swept. See other
[Frequency Offset](../Objects/Channel_Object.md#FrequencyOffset) properties.  
---|---  
  
####  VB Syntax

|  object.FrequencyOffsetCWOverride = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  Channel (object) or CalSet (object) - Read-only property  
value |  (Enum as NaStates) \- Choose from: naOFF (0) - Turns CW override OFF naON (1) - Turns CW override ON  
  
#### Return Type

|  Enum  
  
#### Default

|  0 Hz  
  
#### Examples

|  chan.FrequencyOffsetCWOverride = 1 'Write  
fOffsetOV = chan.FrequencyOffsetCWOverride 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_FrequencyOffsetCWOverride (tagNAStates *pstate)  
HRESULT put_FrequencyOffsetCWOverride (tag NAStates newState)  
  
#### Interface

|  IChannel2 |CalSet3

