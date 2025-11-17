##### Read/Write

## PassFailPolicy Property

* * *

#### Description

|  Sets the policy used to determine how global pass/fail is computed. [Learn
more about Global
Pass/Fail.](../../../S4_Collect/Use_Limits_to_Test_Devices.htm#Limitdiag)  
---|---  
  
####  VB Syntax

|  object.PassFailPolicy = _value_  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  (object) \- An [Aux I/O](../Objects/HWauxIO_Object.md) or [Handler I/O](../Objects/HWMaterialHandlerIO_Object.md) object  
value |  (enum as NAPassFailPolicy) Choose from: 0 - naPolicyAllTests \- - Pass/Fail Status returns PASS if all tests on all measurements pass. 1 - naPolicyAllMeas \- Pass/Fail Status returns PASS if all measurements have associated tests, and all tests pass. FAIL is returned if even one measurement has no associated limit test. Only those measurements which are not in HOLD mode contribute to the pass/fail result.  
  
#### Return Type

|  Long Integer  
  
#### Default

|  naPolicyAllTests  
  
#### Examples

|  matHndler.PassFailPolicy = naPolicyAllTests 'Write policy =
aux.PassFailPolicy 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_PassFailPolicy ( tagNAPassFailPolicy Policy); HRESULT
get_PassFailPolicy ( tagNARearPanelIOLogic* Policy);  
  
#### Interface

|  IHWAuxIO4 IHWMaterialHandlerIO2

