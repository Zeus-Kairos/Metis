##### Write/Read

|

##### [About Frequency Range](../../../S1_Settings/Frequency_Range.md)  
  
---|---  
  
## FrequencySpan Property

* * *

#### Description

|  Sets or returns the frequency span of the channel. Sets or returns the
frequency span of the segment.  
---|---  
  
####  VB Syntax

|  object.FrequencySpan = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  A Channel (object)  
or  
A Segment (object)  
value |  (double) - Frequency span in Hertz. Choose any number between 70 (minimum) and maximum frequency span of the analyzer.  
  
#### Return Type

|  Double  
  
#### Default

|  Full frequency span of the analyzer  
  
#### Examples

|  chan.FrequencySpan = 4.5e9 'sets the frequency span of a linear sweep for
the channel object -Write  
freqspan = chan.FrequencySpan 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_FrequencySpan(double *pVal)  
HRESULT put_FrequencySpan(double newVal)  
  
#### Interface

|  IChannel  
ISegment  
  
* * *

