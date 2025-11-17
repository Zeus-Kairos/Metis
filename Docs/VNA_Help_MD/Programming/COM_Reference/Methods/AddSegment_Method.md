##### Write-only

|

##### [About Mixer/Converter
Settings](../../../Applications/MixerConverter_Setup.htm)  
  
---|---  
  
# AddSegment Method

* * *

#### Description

|  Adds the specified number of segments to the [scratch
mixer](../Objects/Converter_Object.htm#Scratch) at the index position. All
segments are added with default settings.  
---|---  
  
####  VB Syntax

|  conv.AddSegment index,count  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
conv |  A [Converter Object](../Objects/Converter_Object.md)  
index |  (Long integer) Position at which to add segments. Valid index range is between 1 and the current segment count +1. Using count +1 adds segments to the end of the segment table. Use [SegmentCount Property](../Properties/SegmentCount_Property.md) to read the current count in the [Applied Mixer](../Objects/Converter_Object.md#Scratch).  
count |  (Long integer) Optional argument. Number of segments to add. If unspecified, 1 segment is added.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  mxr.AddSegment 1,5 'Adds 5 segments beginning at the first position. [See
example
program](../../COM_Example_Programs/Create_a_Segmented_Sweep_for_Mixers.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT AddSegment(long index, long count);  
  
#### Interface

|  IConverter5  
  
* * *

