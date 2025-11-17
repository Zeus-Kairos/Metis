##### Write/Read

|

##### [About E5091 Testset Control](../../../System/E5091_TestSet_Control.md)

##### [About External Testset
Control](../../../System/External_Testset_Control.htm)  
  
---|---  
  
## Enabled Property

* * *

#### Description

|  Enables and disables (ON/OFF) the port mapping and control line output of
the specified test set. If the specified test set is not connected or not ON,
then setting Enabled = True will report an error. All other properties can be
set when the test set is not connected. When this command is set to ON or OFF,
then the display of the test set status bar ([ShowProperties
Property](ShowProperties_Property.htm)) is also set to ON or OFF.  
---|---  
  
####  VB Syntax

|  tset.Enabled = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
tset |  A [TestsetControl](../Objects/TestsetControl_Object.md) object OR An [E5091Testset](../Objects/E5091Testset_Object.md) object  
value |  (Boolean) True Enables test set control. False Disables test set control.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  [See E5091A Example
Program](../../COM_Example_Programs/E5091Testset_Control.htm) [See External
Testset Program](../../COM_Example_Programs/External_Testset_Control.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_Enabled(VARIANT_BOOL *state);  
HRESULT put_Enabled(VARIANT_BOOL state);  
  
#### Interface

|  ITestsetControl IE5091Testsets

