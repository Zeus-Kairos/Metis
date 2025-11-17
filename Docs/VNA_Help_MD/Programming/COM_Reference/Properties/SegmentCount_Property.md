##### Read-only

|

##### [About Mixer/Converter
Settings](../../../Applications/MixerConverter_Setup.htm)  
  
---|---  
  
# SegmentCount Property

* * *

#### Description

|  Returns the number of segments on the [Applied
mixer](../Objects/Converter_Object.htm#Scratch).  
---|---  
  
####  VB Syntax

|  value = conv.SegmentCount  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Long integer) Variable in which to store the returned segment count.  
conv |  A [Converter Object](../Objects/Converter_Object.md)  
  
#### Return Type

|  Long integer  
  
#### Default

|  1 Segment is created on new converter objects.  
  
#### Examples

|  count=mxr.SegmentCount [See example
program](../../COM_Example_Programs/Create_a_Segmented_Sweep_for_Mixers.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SegmentCount(long *value);  
  
#### Interface

|  IConverter5  
  
* * *

