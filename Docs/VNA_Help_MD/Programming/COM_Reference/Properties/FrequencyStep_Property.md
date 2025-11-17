##### Write/Read

|

##### [About Frequency
Range](../../../S1_Settings/Frequency_Range.htm#StartDiag)  
  
---|---  
  
## FrequencyStep Property

* * *

#### Description

|  Sets the frequency step size across the selected frequency range. This
effectively sets the number of data points. Available ONLY when
[SweepType](Sweep_Type_Property.md) = Linear.  
---|---  
  
####  VB Syntax

|  object.FrequencyStep = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  A Channel (object)  
value |  (double) - Frequency step size in Hertz. Select any value up to the frequency range of the analyzer.  
  
#### Return Type

|  Double  
  
#### Default

|  Not Applicable  
  
#### Examples

|  chan.FrequencyStep = 1e9 'sets the frequency step size of a linear sweep
for the channel object -Write  
freqstep = chan.FrequencyStep 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_FrequencyStep(double *pVal) HRESULT put_FrequencyStep(double
newVal)  
  
#### Interface

|  IChannel24  
  
* * *

