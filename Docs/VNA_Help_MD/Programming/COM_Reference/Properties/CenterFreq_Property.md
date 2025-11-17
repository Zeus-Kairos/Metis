##### Write/Read

|

##### [About Frequency](../../../S1_Settings/Frequency_Range.md)  
  
---|---  
  
## CenterFrequency Property

* * *

#### Description

|  Sets or returns the center frequency of the channel  
or  
Sets or returns the center frequency of the segment. See the [Measurement2
Interface](../Objects/Measurement_Object.htm#IMeasurement2Interface) to learn
how this method differs from [meas.Center](Center_Meas_Property.md).  
---|---  
  
#### VB Syntax

|  object.centerFrequency = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  A [Channel](../Objects/Channel_Object.md) (object) or A [Segment](../Objects/Segment_Object.md) (object)  
value |  (double) - Center frequency in Hertz. Choose any number between the minimum and maximum frequencies of the analyzer.  
  
#### Return Type

|  Double  
  
#### Default

|  Center of the frequency range  
  
#### Examples

|  chan.centerFrequency = 4.5e9 'sets the center frequency of a linear sweep
for the channel object -Write  
centfreq = chan.centerFrequency 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_CenterFrequency(double *pVal)  
HRESULT put_CenterFrequency(double newVal)  
  
#### Interface

|  IChannel ISegment

