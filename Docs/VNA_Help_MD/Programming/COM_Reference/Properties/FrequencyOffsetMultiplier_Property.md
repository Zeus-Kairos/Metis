##### Write/Read

|

##### [About Frequency Offset](../../../FreqOffset/Frequency_Offset_Mode.md)  
  
---|---  
  
## FrequencyOffsetMultiplier Property Superseded

* * *

#### Description

|  This method is replaced by properties on the [FOMRange
Object.](../Objects/FOMRange_Object.htm) Specifies (along with
[FrequencyOffsetDivisor](FrequencyOffsetDivisor_Property.md)) the value to
multiply by the stimulus. See other [Frequency
Offset](../Objects/Channel_Object.htm#FrequencyOffset) properties.  
---|---  
  
####  VB Syntax

|  object.FrequencyOffsetMultiplier = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  Channel (object) or CalSet (object) - Read-only property  
value |  (Double) \- Multiplier value. Range is 1 to 1000  
  
#### Return Type

|  Double  
  
#### Default

|  1  
  
#### Examples

|  chan.FrequencyOffsetMultiplier = 2 'Write  
fOffsetMult = chan.FrequencyOffsetMultiplier 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_FrequencyOffsetMultiplier (double*pval);  
HRESULT put_FrequencyOffsetMultiplier (double newVal);  
  
#### Interface

|  IChannel2 |CalSet3

