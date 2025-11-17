##### Read-only

|

##### [About E5091 Testset Control](../../../System/E5091_TestSet_Control.md)

##### [About External Testset
Control](../../../System/External_Testset_Control.htm)  
  
---|---  
  
## ID Property

* * *

#### Description

|  Returns the test set ID number. For GPIB testsets, the ID is equivalent to
the GPIB address. For testset I/O testsets, the ID is the base address of the
testset (0 for the first testset, 1 for the second, and so on).  
---|---  
  
####  VB Syntax

|  value = tset.ID  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Long) variable to store the returned information.  
testsets(1) |  A [TestsetControl](../Objects/TestsetControl_Object.md) object. OR An [E5091Testset](../Objects/E5091Testset_Object.md) object.  
  
#### Return Type

|  Long Integer  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = testset1.ID [See E5091A Example
Program](../../COM_Example_Programs/E5091Testset_Control.htm) [See External
Testset Program](../../COM_Example_Programs/External_Testset_Control.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_ID(long *idNumber);  
  
#### Interface

|  ITestsetControl IE5091Testset

