##### Write/Read

|

##### [About Frequency Offset](../../../FreqOffset/Frequency_Offset_Mode.md)  
  
---|---  
  
## FrequencyOffsetState Property Superseded

* * *

#### Description

|  This method is replaced by properties on the [FOMRange
Object.](../Objects/FOMRange_Object.htm) Enables Frequency Offset on ALL
measurements that are present on the active channel. This immediately causes
the source and receiver to tune to separate frequencies. The receiver
frequencies are specified with other channel and offset settings. To make the
stimulus settings, use Channel Start, Stop Frequency properties. See other
[Frequency Offset](../Objects/Channel_Object.md#FrequencyOffset) properties.
Tip: To avoid unnecessary errors, first make other frequency offset settings.
Then turn Frequency Offset ON.  
---|---  
  
####  VB Syntax

|  object.FrequencyOffsetState = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  Channel (object) or CalSet (object) - Read-only property  
value |  (Enum as NaStates) \- Choose from: naOFF (0) - Turns Frequency Offset OFF naON (1) - Turns Frequency Offset ON  
  
#### Return Type

|  Enum  
  
#### Default

|  naOFF (0)  
  
#### Examples

|  chan.FrequencyOffsetState = naON 'Write  
Foffset = chan.FrequencyOffsetState 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT FrequencyOffsetState (tag NAStates *pState);  
HRESULT FrequencyOffsetState (tag NAStates newState)  
  
#### Interface

|  IChannel2 |CalSet3

