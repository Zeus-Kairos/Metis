##### Write/Read

|

##### [About Mixer/Converter
Settings](../../../Applications/MixerConverter_Setup.htm)  
  
---|---  
  
# SegmentFixedPower Property

* * *

#### Description

|  Set and read the fixed power level for the mixer segment.  
---|---  
  
####  VB Syntax

|  conv.SegmentFixedPower(index,range) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
conv |  A [Converter Object](../Objects/Converter_Object.md)  
index |  (Long integer) Segment for which power is being set. Choose a segment between 1 and the current segment count. Use [SegmentCount Property](SegmentCount_Property.md) to read the current count in the [Applied Mixer](../Objects/Converter_Object.md#Scratch).  
range |  (Enum as ConverterFrequencyRange) Range for which power is being set. Choose from: 0 - naInputFrequencies \- set input power 1 - naOutputFrequencies \- set output power 2 - naLO1Frequencies \- set LO1 power 3 - naLO2Frequencies \- set LO2 power 4 - naIFFrequencies \- set IF power  
value |  (Double) Power level in dBm. Choose a value within the power/attenuation range of the VNA.  
  
#### Return Type

|  Double  
  
#### Default

|  
  
#### Examples

|  mxr.SegmentFixedPower(1,0)=0 'sets the input power level to 0 dBm [See
example
program](../../COM_Example_Programs/Create_a_Segmented_Sweep_for_Mixers.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SegmentFixedPower(long index, tagConverterFrequencyRange range,
double *value); HRESULT put_SegmentFixedPower(long index,
tagConverterFrequencyRange value, double value);  
  
#### Interface

|  IConverter5  
  
* * *

