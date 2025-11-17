##### Write-only

|

##### [About Mixer/Converter
Settings](../../../Applications/MixerConverter_Setup.htm)  
  
---|---  
  
# DeleteSegment Method

* * *

#### Description

|  Removes the specified number of segments from the [scratch
mixer](../Objects/Converter_Object.htm#Scratch) starting at the index
position.  
---|---  
  
####  VB Syntax

|  conv.DeleteSegment index,count  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
conv |  A [Converter Object](../Objects/Converter_Object.md)  
index |  (Long integer) Position at which to start removing segments. Valid index range is between 1 and the current segment count. Use [SegmentCount Property](../Properties/SegmentCount_Property.md) to read the current count in the [Applied Mixer](../Objects/Converter_Object.md#Scratch).  
count |  (Long integer) Optional argument. Number of segments to remove. If unspecified, 1 segment is removed.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  mxr.DeleteSegment 1,5 'Removes 5 segments beginning at the first position.
[See example
program](../../COM_Example_Programs/Create_a_Segmented_Sweep_for_Mixers.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT DeleteSegment(long index, long count);  
  
#### Interface

|  IConverter5  
  
* * *

