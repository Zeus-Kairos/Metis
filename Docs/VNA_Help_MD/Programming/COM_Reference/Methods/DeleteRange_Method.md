##### Write-only

|

##### [About Differential IQ](../../../Applications/Differential_IQ.md)  
  
---|---  
  
# DeleteRange Method

* * *

#### Description

|  Deletes the specified frequency range. On the [Measurement Setup
dialog](../../../Applications/Differential_IQ.htm#SetupDiag) this is the
Remove setting.  
---|---  
  
####  VB Syntax

|  DIQ.DeleteRange (n)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
DIQ |  A [DIQ Object](../Objects/DIQ_Object.md)  
n |  (Long) Frequency range number to delete.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  diq.DeleteRange 2 'removes frequency range 2 [See example
program](../../COM_Example_Programs/Create_and_Cal_a_Diff_IQ_Measurement.htm.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT DeleteRange(long range);  
  
#### Interface

|  IDIQ  
  
* * *

