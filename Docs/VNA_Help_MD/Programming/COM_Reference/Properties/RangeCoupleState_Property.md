##### Write/Read

|

##### [About Diff I/Q App](../../../Applications/Differential_IQ.md)  
  
---|---  
  
## RangeCoupleState Property

* * *

#### Description

|  Sets and reads the ON / OFF state of frequency range coupling. On the
[Frequency Range](../../../Applications/Differential_IQ.md#RangeDiag) dialog
under Coupling, this is the Couple (On|Off) setting.  
---|---  
  
####  VB Syntax

|  DIQ.RangeCoupleState (n) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
DIQ |  A [Differential I/Q](../Objects/DIQ_Object.md) (object)  
n |  (Long) Frequency range number.  
value |  (Boolean) Choose from the following:

  * True - Range is coupled
  * False - Range is NOT coupled

  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  diq.RangeCoupleState 2 = True 'Write, range 2 is coupled to range 1  
value = diq.RangeCoupleState 2 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_RangeCoupleState(long range, VARIANT_BOOL* RangeCoupleState);
HRESULT put_RangeCoupleState(long range, VARIANT_BOOL RangeCoupleState);  
  
#### Interface

|  IDIQ  
  
* * *

