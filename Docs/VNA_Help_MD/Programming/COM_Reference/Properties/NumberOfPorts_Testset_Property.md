##### Read-only

|

##### [About E5091 Testset Control](../../../System/E5091_TestSet_Control.md)

##### [About External Testset
Control](../../../System/External_Testset_Control.htm)  
  
---|---  
  
## NumberOfPorts Property

* * *

#### Description

|  Returns the number of ports on the specified testset. Returns 0 if no test
set is connected.  
---|---  
  
####  VB Syntax

|  value = tset.NumberOfPorts  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Long) variable to store the returned information.  
tset |  A [TestsetControl](../Objects/TestsetControl_Object.md) object. OR An [E5091Testset](../Objects/E5091Testset_Object.md) object.  
  
#### Return Type

|  Long Integer  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = testset1.NumberOfPorts [See E5091A Example
Program](../../COM_Example_Programs/E5091Testset_Control.htm) [See External
Testset Program](../../COM_Example_Programs/External_Testset_Control.htm)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_NumberOfPorts(long *numberOfPorts);  
  
#### Interface

|  ITestsetControl IE5091Testset

