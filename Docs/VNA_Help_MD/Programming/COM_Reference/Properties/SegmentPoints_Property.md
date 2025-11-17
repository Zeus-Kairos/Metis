##### Write/Read

|

##### [About Mixer/Converter
Settings](../../../Applications/MixerConverter_Setup.htm)  
  
---|---  
  
# SegmentPoints Property

* * *

#### Description

|  Sets and returns the number of data points to be measured in the sweep
segment. Send [Apply](../Methods/Apply_Method.md) before sending a query
(read). [Learn more](../Objects/Converter_Object.md#Scratch).  
---|---  
  
####  VB Syntax

|  conv.SegmentPoints(index) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
conv |  A [Converter Object](../Objects/Converter_Object.md)  
index |  (Long integer) Segment for which points is to be set. Choose a segment between 1 and the current segment count. Use [SegmentCount Property](SegmentCount_Property.md) to read the current count in the [Applied Mixer](../Objects/Converter_Object.md#Scratch).  
value |  (Long integer) - Choose a value between 1 and the [maximum number of data points allowed in the VNA](../../../S1_Settings/DPoints.md#PointsDiag). This is also the total number of points allowed for ALL segments.  
  
#### Return Type

|  Long integer  
  
#### Default

|  21  
  
#### Examples

|  mxr.SegmentPoints(1)=3 'Sets 3 points for segment 1. [See example
program](../../COM_Example_Programs/Create_a_Segmented_Sweep_for_Mixers.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SegmentPoints(long index, long * val); HRESULT
put_SegmentPoints(long index, long val);  
  
#### Interface

|  IConverter5  
  
* * *

