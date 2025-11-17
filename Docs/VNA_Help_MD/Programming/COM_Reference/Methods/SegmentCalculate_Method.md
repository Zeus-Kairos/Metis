##### Write-only

|

##### [About Mixer/Converter
Settings](../../../Applications/MixerConverter_Setup.htm)  
  
---|---  
  
# SegmentCalculate Method

* * *

#### Description

|  Calculates the specified parameter for the segment.  
---|---  
  
####  VB Syntax

|  conv.SegmentCalculate index,param  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
conv |  A [Converter Object](../Objects/Converter_Object.md)  
index |  (Long integer) Segment for which calculation is performed. Choose a segment between 1 and the current segment count. Use [SegmentCount Property](../Properties/SegmentCount_Property.md) to read the current count in the [Applied Mixer](../Objects/Converter_Object.md#Scratch).  
param |  (Enum as ConverterCalculation) Mixer port for which to calculate start and stop frequencies. Choose from: |  |  enum |  1st or only stage requires: |  In addition, 2nd stage requires:  
---|---|---|---  
0 |  naCalculateINPUT | 

  * Output Start and Stop frequencies
  * LO frequency
  * Output sideband (High or Low)

|

  * IF Start and Stop frequencies
  * 2nd LO frequency
  * IF sideband (High or Low)

  
1 |  naCalculateINPUT AndOUTPUT (2 stage mixers ONLY) |  NA | 

  * IF Start and Stop frequencies
  * Both LO frequencies

  
2 |  naCalculateOUTPUT | 

  * Input Start and Stop frequencies
  * LO frequency
  * Output sideband (High or Low)

|

  * IF Start and Stop frequencies
  * 2nd LO frequency
  * IF sideband (High or Low)

  
3 |  naCalculateLO1 | 

  * Input Start and Stop frequencies
  * Output frequency
  * Output sideband (High or Low)

|

  * IF Start and Stop frequencies
  * 2nd LO frequency
  * IF sideband (High or Low)

  
4 |  naCalculateLO2 |  NA | 

  * Input Start and stop frequencies
  * 1st LO start and stop frequencies
  * Output frequency
  * IF sideband(High or Low
  * Output sideband(High or Low)

  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  mxr.SegmentCalculate 1,2 'Calculates the output frequencies for segment 1.
[See example
program](../../COM_Example_Programs/Create_a_Segmented_Sweep_for_Mixers.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT SegmentCalculate(long index, ConverterCalculation param);  
  
#### Interface

|  IConverter5  
  
* * *

