##### Write/Read

|

##### [About Diff I/Q App](../../../Applications/Differential_IQ.md)  
  
---|---  
  
## RangeStopFrequency Property

* * *

#### Description

|  Sets and reads the Stop value for the specified frequency range. On the
[Frequency Range](../../../Applications/Differential_IQ.md#RangeDiag) dialog
under Frequency, this is the Stop setting.  
---|---  
  
####  VB Syntax

|  DIQ.RangeStopFrequency (n)= value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
DIQ |  A [Differential I/Q](../Objects/DIQ_Object.md) (object)  
n |  (Long) Frequency range number.  
value |  (Double)  Frequency range stop value. Choose a value within the frequency range of the analyzer.  
  
#### Return Type

|  Double  
  
#### Default

|  Maximum frequency of the analyzer.  
  
#### Examples

|  diq.RangeStopFrequency(2) = 1e9 'Write  
value = diq.RangeStopFrequency(1) 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_RangeStopFrequency(long range, double* RangeStopFrequency);
HRESULT put_RangeStopFrequency(long range, double RangeStopFrequency);  
  
#### Interface

|  IDIQ  
  
* * *

