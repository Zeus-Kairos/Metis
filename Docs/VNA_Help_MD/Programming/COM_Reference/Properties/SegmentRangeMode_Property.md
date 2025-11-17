##### Write/Read

|

##### [About Mixer/Converter
Settings](../../../Applications/MixerConverter_Setup.htm)  
  
---|---  
  
# SegmentRangeMode Property

* * *

#### Description

|  Sets or returns the segment sweep mode (Swept or Fixed) for the specified
range (Input/LO/Output). Send [Apply](../Methods/Apply_Method.md) before
sending a query (read). [Learn more](../Objects/Converter_Object.md#Scratch).  
---|---  
  
####  VB Syntax

|  conv.SegmentRangeMode(index,range) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
conv |  A [Converter Object](../Objects/Converter_Object.md)  
index |  (Long integer) Segment for which mixing mode being set. Choose a segment between 1 and the current segment count. Use [SegmentCount Property](SegmentCount_Property.md) to read the current count in the [Applied Mixer](../Objects/Converter_Object.md#Scratch).  
range |  (Enum as ConverterFrequencyRange) Range for which sweep mode is being set. Choose from: 0 - naInputFrequencies \- set input sweep mode. 1 - naOutputFrequencies \- set output sweep mode. 2 - naLO1Frequencies \- set LO1 sweep mode. 3 - naLO2Frequencies \- set LO2 sweep mode. 4 - naIFFrequencies \- set IF sweep mode.  
value |  (Enum as NARangeMode) Choose from: 0 - naSwept Range is swept 1 - naFixed Range is fixed.  
  
#### Return Type

|  Enum as NARangeMode  
  
#### Default

|  Input and Output - naSwept LO (1 and 2) - naFixed  
  
#### Examples

|  mxr.SegmentRangeMode(1,1)=0 'sets segment 1 output range to swept. [See
example
program](../../COM_Example_Programs/Create_a_Segmented_Sweep_for_Mixers.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SegmentRangeMode(long index, tagConverterFrequencyRange range,
tagNARangeMode *value); HRESULT put_SegmentRangeMode(long index,
tagConverterFrequencyRange value, tagNARangeMode value);  
  
#### Interface

|  IConverter5  
  
* * *

