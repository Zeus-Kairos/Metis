##### Write/Read

|

##### [About Frequency Offset](../../../FreqOffset/Frequency_Offset_Mode.md)  
  
---|---  
  
## FrequencyOffsetFrequency Property Superseded

* * *

#### Description

|  This method is replaced by properties on the [FOMRange
Object.](../Objects/FOMRange_Object.htm) Specifies an absolute offset
frequency in Hz. For mixer measurements, this would be the LO frequency. See
other [Frequency Offset](../Objects/Channel_Object.md#FrequencyOffset)
properties.  
---|---  
  
####  VB Syntax

|  object.FrequencyOffsetFrequency = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  Channel (object) or CalSet (object) - Read-only property  
value |  (Double) \- Offset value. Range is +/- 1000 GHz. (Offsets can be positive or negative.)  
  
#### Return Type

|  Double  
  
#### Default

|  0 Hz  
  
#### Examples

|  chan.FrequencyOffsetFrequency = 2 'Write  
fOffsetFreq = chan.FrequencyOffsetFrequency 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_FrequencyOffsetFrequency(double*pval)  
HRESULT put_FrequencyOffsetFrequency(double newVal)  
  
#### Interface

|  IChannel2 |CalSet3

