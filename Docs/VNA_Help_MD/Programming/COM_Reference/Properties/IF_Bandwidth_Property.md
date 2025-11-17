##### Write/Read

|

##### [About IF Bandwidth](../../../S2_Opt/Trce_Noise.md)  
  
---|---  
  
## IFBandwidth Property

* * *

#### Description

|  Sets or returns the IF Bandwidth of the channel. Sets or returns the IF
Bandwidth of the segment. Returns the IF Bandwidth used in the Cal Set  
---|---  
  
####  VB Syntax

|  object.IFBandwidth = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  Channel (object) or Segment (object) or CalSet (object) - Read-only property  
value |  (double) \- IF Bandwidth in Hz. The list of valid IF Bandwidths is different depending on the VNA model. [(Click to see the lists.)](../../../S2_Opt/Trce_Noise.md#IFDiag) If an invalid number is specified, the analyzer will round up to the closest valid number.  
  
#### Return Type

|  Double  
  
#### Default

|  Varies with VNA model.  
  
#### Examples

|  chan.IFBandwidth = 3e3 'sets the IF Bandwidth of for the channel object to
3 kHz. -Write  
seg.IFBandwidth = 5 'sets the IF Bandwidth of the segment to 5 Hz. -Write  
ifbw = chan.IFBandwidth -Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_IFBandwidth(double *pVal); HRESULT put_IFBandwidth(double
newVal);  
  
#### Interface

|  IChannel  
ISegment |CalSet3

