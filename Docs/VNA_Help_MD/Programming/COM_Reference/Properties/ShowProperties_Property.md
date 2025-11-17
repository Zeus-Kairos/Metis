##### Write/Read

|

##### [About E5091 Testset Control](../../../System/E5091_TestSet_Control.md)

##### [About External Testset
Control](../../../System/External_Testset_Control.htm)  
  
---|---  
  
## ShowProperties Property

* * *

#### Description

|  Turns ON and OFF the display of the test set control status bar. This
status bar indicates the test set that is being controlled and the current
port mappings. This setting is turned ON and OFF automatically when the test
set is enabled or disabled.  
---|---  
  
####  VB Syntax

|  tset.ShowProperties = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
tset |  A [TestsetControl](../Objects/TestsetControl_Object.md) object. OR An [E5091Testset](../Objects/E5091Testset_Object.md) object.  
value |  (Boolean) True - Turns display of testset properties ON. False - Turns display of testset properties OFF.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False (True when test set control is enabled.)  
  
#### Examples

|  [See E5091A Example
Program](../../COM_Example_Programs/E5091Testset_Control.htm) [See External
Testset Program](../../COM_Example_Programs/External_Testset_Control.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_ShowProperties(VARIANT_BOOL *state);  
HRESULT put_ShowProperties(VARIANT_BOOL state);  
  
#### Interface

|  IE5091Testsets ITestsetControl

