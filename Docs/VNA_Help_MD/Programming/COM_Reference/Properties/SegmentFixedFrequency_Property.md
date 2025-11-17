##### Write/Read

|

##### [About Mixer/Converter
Settings](../../../Applications/MixerConverter_Setup.htm)  
  
---|---  
  
# SegmentFixedFrequency Property

* * *

#### Description

|  Set and read the CW Frequency for mixer segments. The specified
[SegmentRangeMode](SegmentRangeMode_Property.md) must be set to Fixed. Send
[Apply](../Methods/Apply_Method.md) before sending a query (read). [Learn
more](../Objects/Converter_Object.htm#Scratch).  
---|---  
  
####  VB Syntax

|  conv.SegmentFixedFrequency(index,range) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
conv |  A [Converter Object](../Objects/Converter_Object.md)  
index |  (Long integer) Segment for which fixed frequency is being set. Choose a segment between 1 and the current segment count. Use [SegmentCount Property](SegmentCount_Property.md) to read the current count in the [Applied Mixer](../Objects/Converter_Object.md#Scratch).  
range |  (Enum as ConverterFrequencyRange) Range for which fixed frequency is being set. Choose from: 0 - naInputFrequencies \- set input frequency 1 - naOutputFrequencies \- set output frequency 2 - naLO1Frequencies \- set LO1 frequency 3 - naLO2Frequencies \- set LO2 frequency 4 - naIFFrequencies \- set IF frequency  
value |  (Double) CW Frequency. Choose a value within the frequency range of the VNA.  
  
#### Return Type

|  Double  
  
#### Default

|  Center frequency of the VNA  
  
#### Examples

|  mxr.SegmentFixedFrequency(1,0)=1e9 'sets the input frequency to 1 GHz [See
example
program](../../COM_Example_Programs/Create_a_Segmented_Sweep_for_Mixers.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SegmentFixedFrequency(long index, tagConverterFrequencyRange
range, double *value); HRESULT put_SegmentFixedFrequency(long index,
tagConverterFrequencyRange value, double value);  
  
#### Interface

|  IConverter5  
  
* * *

