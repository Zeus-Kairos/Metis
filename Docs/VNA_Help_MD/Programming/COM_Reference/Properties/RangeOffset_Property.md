##### Write/Read

|

##### [About Diff I/Q App](../../../Applications/Differential_IQ.md)  
  
---|---  
  
## RangeOffset Property

* * *

#### Description

|  Sets and reads the frequency range number to be used as an offset. The
frequencies of the range <n> will be offset from the 'coupled to' range by
this frequency range. The [RangeOffsetUp Property](RangeOffsetUp_Property.md)
command determines whether the offset is positive or negative. On the
[Frequency Range](../../../Applications/Differential_IQ.md#RangeDiag) dialog
under Coupling, this is the Offset setting.  
---|---  
  
####  VB Syntax

|  DIQ.RangeOffset (n) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
DIQ |  A [Differential I/Q](../Objects/DIQ_Object.md) (object)  
n |  (Long Integer) Frequency range number.  
value |  (Long Integer) Offset range number. The resulting range must be within the frequency range of the analyzer.  
  
#### Return Type

|  Long  
  
#### Default

|  1  
  
#### Examples

|  diq.RangeOffset 3 = 2 'Write, range 3 is offset from the 'coupled to' range
by the frequencies defined by range 2  
value = diq.RangeOffset 2 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_RangeOffset(long range, long* RangeOffset); HRESULT
put_RangeOffset(long range, long RangeOffset);  
  
#### Interface

|  IDIQ  
  
* * *

