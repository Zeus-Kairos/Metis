##### Write/Read

|

##### [About Diff I/Q App](../../../Applications/Differential_IQ.md)  
  
---|---  
  
## RangeOffsetUp Property

* * *

#### Description

|  Sets and reads the state of the Up / Down conversion setting. On the
[Frequency Range](../../../Applications/Differential_IQ.md#RangeDiag) dialog
under Coupling, this is the Up (On|Off) setting.  
---|---  
  
####  VB Syntax

|  DIQ.RangeOffsetUp (n) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
DIQ |  A [Differential I/Q](../Objects/DIQ_Object.md) (object)  
n |  (Long Integer) Frequency range number.  
value |  (Boolean) Choose from the following:

  * True -The offset range is ADDED to the 'coupled to' frequency range.
  * False - The offset range is SUBTRACTED from to the 'coupled to' frequency range.

  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  diq.RangeOffsetUp 2 = True 'Write  
value = diq.RangeOffsetUp 2 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_RangeOffsetUp(long range, VARIANT_BOOL* RangeOffsetUp); HRESULT
put_RangeOffsetUp(long range, VARIANT_BOOL RangeOffsetUp);  
  
#### Interface

|  IDIQ  
  
* * *

