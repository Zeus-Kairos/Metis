##### Write/Read

|

##### [About Diff I/Q App](../../../Applications/Differential_IQ.md)  
  
---|---  
  
## RangeDivisor Property

* * *

#### Description

|  Sets and reads the value by which the coupled range will be divided to
achieve the frequency range specified by <rNum>. On the [Frequency
Range](../../../Applications/Differential_IQ.htm#RangeDiag) dialog under
Coupling, this is the Divisor setting.  
---|---  
  
####  VB Syntax

|  DIQ.RangeDivisor (n) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
DIQ |  A [Differential I/Q](../Objects/DIQ_Object.md) (object)  
n |  (Long Integer) Frequency range number.  
value |  (Long Integer) Divisor value. Choose a positive or negative integer.  
  
#### Return Type

|  Long  
  
#### Default

|  1  
  
#### Examples

|  diq.RangeDivisor 2 = 2 'Write  
value = diq.RangeDivisor 2 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_RangeDivisor(long range, long* RangeDivisor); HRESULT
put_RangeDivisor(long range, long RangeDivisor);  
  
#### Interface

|  IDIQ  
  
* * *

