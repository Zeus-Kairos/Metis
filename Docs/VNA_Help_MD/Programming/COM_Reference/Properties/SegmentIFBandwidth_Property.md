##### Write/Read

|

##### [About Mixer/Converter
Settings](../../../Applications/MixerConverter_Setup.htm)  
  
---|---  
  
# SegmentIFBandwidth Property

* * *

#### Description

|  Sets and returns the IF Bandwidth for the sweep segment. Send
[Apply](../Methods/Apply_Method.md) before sending a query (read). [Learn
more](../Objects/Converter_Object.htm#Scratch).  
---|---  
  
####  VB Syntax

|  conv.SegmentIFBandwidth(index, value)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
conv |  A [Converter Object](../Objects/Converter_Object.md)  
index |  (Long integer) Segment for which IF Bandwidth is to be set. Choose a segment between 1 and the current segment count. Use [SegmentCount Property](SegmentCount_Property.md) to read the current count in the [Applied Mixer](../Objects/Converter_Object.md#Scratch).  
value |  (Long integer) IF Bandwidth in Hz. The list of valid IF Bandwidths is different depending on the VNA model. [See the lists](../../../S2_Opt/Trce_Noise.md#IFDiag). If an invalid number is specified, the analyzer will round up to the closest valid number.  
  
#### Return Type

|  Long integer  
  
#### Default

|  100 kHz  
  
#### Examples

|  mxr.SegmentIFBandwidth(1,3)=10e3 'Sets IFBW to 10 kHz [See example
program](../../COM_Example_Programs/Create_a_Segmented_Sweep_for_Mixers.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SegmentIFBandwidth(long index, long * val); HRESULT
put_SegmentIFBandwidth(long index, long val);  
  
#### Interface

|  IConverter5  
  
* * *

