##### Read-Only

## PassFailStatus Property

* * *

#### Description

|  Returns the most recent pass/fail status value. Use this command as
follows:

  1. Set the VNA [trigger scope](Scope_Property.md) to GLOBAL
  2. Set the VNA [trigger source](Source_Property.md) to MANUAL or EXTERNAL.
  3. Configure and enable [Limit Testing](../Objects/LimitSegment_Object.md)
  4. Trigger the VNA.
  5. Use the [*OPC?](../../GP-IB_Command_Finder/Common_Commands.md#opc) (with [SCPIStringParser object](../Objects/SCPIStringParser_Object.md)) to determine when the sweep is complete.
  6. Use the PassFailStatus property to obtain the global pass/fail result.

[Learn more about Global
Pass/Fail.](../../../S4_Collect/Use_Limits_to_Test_Devices.htm#Limitdiag)  
---|---  
  
####  VB Syntax

|  var = object.PassFailStatus  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
var |  (enum as NAPassFailStatus) Variable to store returned status. One of the following will be returned: 0 - naStatusFail \- all measurements not in HOLD mode have been swept, and one or more limit tests failed according to the specified [Pass/Fail policy.](PassFailPolicy_Property.md) 1 - naStatusPass \- all measurements not in HOLD mode have been swept, and all associated limit tests have passed. 2 - naStatusNone \- status cannot be determined because measurements are in progress.  
object |  (object) \- An [Aux I/O](../Objects/HWauxIO_Object.md) or [Handler I/O](../Objects/HWMaterialHandlerIO_Object.md) object  
  
#### Return Type

|  Long Integer  
  
#### Default

|  Not Applicable  
  
#### Examples

|  status = aux.PassFailStatus 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_PassFailPolicy ( tagNAPassFailStatus* status);  
  
#### Interface

|  IHWAuxIO4 IHWMaterialHandlerIO2

