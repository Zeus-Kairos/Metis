##### Write/Read

|

##### [About Mixer/Converter
Settings](../../../Applications/MixerConverter_Setup.htm)  
  
---|---  
  
# SegmentMixingMode Property

* * *

#### Description

|  Set and read whether the mixing mode (high side or low side) for the mixer
segment. Send [Apply](../Methods/Apply_Method.md) before sending a query
(read). [Learn more](../Objects/Converter_Object.md#Scratch).  
---|---  
  
####  VB Syntax

|  conv.SegmentMixingMode(index,range) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
conv |  A [Converter Object](../Objects/Converter_Object.md)  
index |  (Long integer) Segment for which mixing mode being set. Choose a segment between 1 and the current segment count. Use [SegmentCount Property](SegmentCount_Property.md) to read the current count in the [Applied Mixer](../Objects/Converter_Object.md#Scratch).  
range |  (Enum as ConverterFrequencyRange) Range for which mixing mode is being set. Choose from: 1 - naOutputFrequencies \- sets output frequencies for 1-stage or 2-stage mixers. 4 - naIFFrequencies \- sets IF frequencies for the first LO in 2-stage mixers.  
value |  (Enum as ConverterSideBand) Choose from: 0 - naLowSide Input minus LO 1 - naHighSide Input plus LO  
  
#### Return Type

|  Enum as ConverterSideBand  
  
#### Default

|  0 - naLowSide  
  
#### Examples

|  mxr.SegmentMixingMode(1,1)=1 'sets segment 1 output frequencies to Highside
mixing. [See example
program](../../COM_Example_Programs/Create_a_Segmented_Sweep_for_Mixers.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SegmentMixingMode(long index, tagConverterFrequencyRange range,
tagConverterSideBand *value); HRESULT put_SegmentMixingMode(long index,
tagConverterFrequencyRange value, tagConverterSideBand value);  
  
#### Interface

|  IConverter5  
  
* * *

