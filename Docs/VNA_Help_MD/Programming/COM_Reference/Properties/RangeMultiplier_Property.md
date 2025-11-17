##### Write/Read

|

##### [About Diff I/Q App](../../../Applications/Differential_IQ.md)  
  
---|---  
  
## RangeMultiplier Property

* * *

#### Description

|  Sets and reads the value by which the coupled range will be multiplied to
achieve the frequency range specified by <n>. On the [Frequency
Range](../../../Applications/Differential_IQ.htm#RangeDiag) dialog under
Coupling, this is the Multiplier setting.  
---|---  
  
####  VB Syntax

|  DIQ.RangeMultiplier (n) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
DIQ |  A [Differential I/Q](../Objects/DIQ_Object.md) (object)  
n |  (Long Integer) Frequency range number.  
value |  (Long Integer) Multiplier value. Choose a positive or negative integer.  
  
#### Return Type

|  Long  
  
#### Default

|  1  
  
#### Examples

|  diq.RangeMultiplier 2 = 1 'Write  
value = diq.RangeMultiplier 2 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_RangeMultiplier(long range, long* RangeMultiplier); HRESULT
put_RangeMultiplier(long range, long RangeMultiplier);  
  
#### Interface

|  IDIQ  
  
* * *

