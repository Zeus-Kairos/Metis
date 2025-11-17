##### Write/Read

|

##### [About Mixer/Converter
Settings](../../../Applications/MixerConverter_Setup.htm)  
  
---|---  
  
# SegmentIsInputGreaterThanLO Property

* * *

#### Description

|  Set and read whether to use the Input frequency that is greater than the LO
or less than the LO. Send [Apply](../Methods/Apply_Method.md) before sending
a query (read). [Learn more](../Objects/Converter_Object.md#Scratch).  
---|---  
  
####  VB Syntax

|  conv.SegmentIsInputGreaterThanLO(index,range) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
conv |  A [Converter Object](../Objects/Converter_Object.md)  
index |  (Long integer) Segment which is being set. Choose a segment between 1 and the current segment count. Use [SegmentCount Property](SegmentCount_Property.md) to read the current count in the [Applied Mixer](../Objects/Converter_Object.md#Scratch).  
range |  (Enum as ConverterFrequencyRange) Range for which value is being set. Choose from: 0 - naInputFrequencies \- set input power 1 - naOutputFrequencies \- set output power 2 - naLO1Frequencies \- set LO1 power 3 - naLO2Frequencies \- set LO2 power 4 - naIFFrequencies \- set IF power  
value |  (Boolean) -Choose from the following: True \- Use the Input that is Greater than the specified LO. False \- Use the Input that is Less than the specified LO.  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Examples

|  mxr.SegmentIsInputGreaterThanLO(1,2=1'sets segment 1, LO1 to Input greater
[See example
program](../../COM_Example_Programs/Create_a_Segmented_Sweep_for_Mixers.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SegmentIsInputGreaterThanLO(long index,
tagConverterFrequencyRange range, VARIANT_BOOL *value); HRESULT
put_SegmentIsInputGreaterThanLO(long index, tagConverterFrequencyRange value,
VARIANT_BOOL value);  
  
#### Interface

|  IConverter5  
  
* * *

