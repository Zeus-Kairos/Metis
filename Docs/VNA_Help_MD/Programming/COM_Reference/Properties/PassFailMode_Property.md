##### Read/Write

## PassFailMode Property

* * *

#### Description

|  Sets and reads the mode of the PassFail line on the [HANDLER IO
connector](../../HandlerIO_Connector.htm) (pin 33). [Learn more about Global
Pass/Fail.](../../../S4_Collect/Use_Limits_to_Test_Devices.htm#Limitdiag)  
---|---  
  
####  VB Syntax

|  object.PassFailMode = _value_  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  (object) \- An Aux I/O or Handler I/O object  
value |  (enum as NAPassFailMode).Choose from:  
0 - naDefaultPassNoWaitMode\- the line stays in PASS state. When a device
fails, then the line goes to fail IMMEDIATELY. 1 - naDefaultPassWaitMode \-
the line stays in PASS state. When a device fails, then the line goes to fail
after the Sweep End line is asserted. 2 - naDefaultFailWaitMode\- the line
stays in FAIL state. When a device passes, then the line goes to PASS state
after the Sweep End line is asserted.  
  
#### Return Type

|  Long Integer  
  
#### Default

|  0 - naDefaultPassNoWaitMode  
  
#### Examples

|  HWAuxIO.PassFailMode = naDefaultPassNoWaitMode 'Write mode =
HWAuxIO.PassFailMode 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_PassFailMode ( tagNAPassFailMode Mode ); HRESULT
get_PassFailMode ( tagNAPassFailMode* Mode );  
  
#### Interface

|  IHWAuxIO IHWMaterialHandlerIO

