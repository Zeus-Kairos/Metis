##### Write/Read

|

##### [About Diff I/Q App](../../../Applications/Differential_IQ.md)  
  
---|---  
  
## RangeCoupleId Property

* * *

#### Description

|  Sets and reads the frequency range to couple settings to. On the [Frequency
Range](../../../Applications/Differential_IQ.htm#RangeDiag) dialog under
Coupling, this is the range to Couple To setting.  
---|---  
  
####  VB Syntax

|  DIQ.RangeCoupleId (n) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
DIQ |  A [Differential I/Q](../Objects/DIQ_Object.md) (object)  
n |  (Long Integer) Frequency range number.  
value |  (Long Integer) Frequency range number to couple to. This range should be already created using [AddRange Method](../Methods/AddRange_Method.md).  
  
#### Return Type

|  Long  
  
#### Default

|  1  
  
#### Examples

|  diq.RangeCoupleId 2 = 1 'Write, range 2 is coupled to range 1  
value = diq.RangeCoupleId 2 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_RangeCoupleId(long range, long* RangeCoupleId); HRESULT
put_RangeCoupleId(long range, long RangeCoupleId);  
  
#### Interface

|  IDIQ  
  
* * *

