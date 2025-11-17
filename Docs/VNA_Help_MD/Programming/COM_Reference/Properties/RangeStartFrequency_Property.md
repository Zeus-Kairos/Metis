##### Write/Read

|

##### [About Diff I/Q App](../../../Applications/Differential_IQ.md)  
  
---|---  
  
## RangeStartFrequency Property

* * *

#### Description

|  Sets and reads the start value for the specified frequency range. On the
[Frequency Range](../../../Applications/Differential_IQ.md#RangeDiag) dialog
under Frequency, this is the Start setting.  
---|---  
  
####  VB Syntax

|  DIQ.RangeStartFrequency (n)= value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
DIQ |  A [Differential I/Q](../Objects/DIQ_Object.md) (object)  
n |  (Long) Frequency range number.  
value |  (Double)  Frequency range start value. Choose a value within the frequency range of the analyzer.  
  
#### Return Type

|  Double  
  
#### Default

|  Start frequency of the analyzer.  
  
#### Examples

|  diq.RangeStartFrequency(2) = 1e9 'Write  
value = diq.RangeStartFrequency(1) 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_RangeStartFrequency(long range, double* RangeStartFrequency);
HRESULT put_RangeStartFrequency(long range, double RangeStartFrequency);  
  
#### Interface

|  IDIQ  
  
* * *

