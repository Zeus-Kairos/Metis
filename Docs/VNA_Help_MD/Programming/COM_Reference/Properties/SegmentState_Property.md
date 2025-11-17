##### Write/Read

|

##### [About Mixer/Converter
Settings](../../../Applications/MixerConverter_Setup.htm)  
  
---|---  
  
# SegmentState Property

* * *

#### Description

|  Sets and returns the ON|OFF state of a sweep segment. Off segments are not
included is a segment sweep. Send [Apply](../Methods/Apply_Method.md) before
sending a query (read). [Learn more](../Objects/Converter_Object.md#Scratch).  
---|---  
  
####  VB Syntax

|  conv.SegmentState(index) =state  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
conv |  A [Converter Object](../Objects/Converter_Object.md)  
index |  (Long integer) Segment to set ON or OFF. Choose a segment between 1 and the current segment count. Use [SegmentCount Property](SegmentCount_Property.md) to read the current count in the [Applied Mixer](../Objects/Converter_Object.md#Scratch).  
state |  (Boolean) \- Choose from: True \- Segment ON False \- Segment OFF  
  
#### Return Type

|  Boolean  
  
#### Default

|  ON when added.  
  
#### Examples

|  mxr.SegmentState(1)=False 'Turns segment 1 OFF. [See example
program](../../COM_Example_Programs/Create_a_Segmented_Sweep_for_Mixers.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SegmentState(long index, VARIANT_BOOL * val); HRESULT
put_SegmentState(long index, VARIANT_BOOL val);  
  
#### Interface

|  IConverter5  
  
* * *

