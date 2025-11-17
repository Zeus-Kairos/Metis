##### Read/Write

## PassFailScope Property

* * *

#### Description

|  Sets and reads the Scope of the PassFail line on the [HANDLER IO
connector](../../HandlerIO_Connector.htm) (pin 33). [Learn more about Global
Pass/Fail.](../../../S4_Collect/Use_Limits_to_Test_Devices.htm#Limitdiag)  
---|---  
  
####  VB Syntax

|  object.PassFailScope = _value_  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  (object) \- An Aux I/O or Handler IO object  
value |  (enum NAPassFailScope ) Choose from: 0 - naChannelScope \- The PassFail line returns to its default state before sweeps on the next channel start. (A channel measurement may require several sweeps.) 1 - naGlobalScope \- The PassFail line returns to its default state before the sweeps for the next [triggerable](JavaScript:hhctrl.TextPopup\('a channel that is not in Hold','Arial,8',10,10,00000000,0xc0ffff\)) channel start. The default state of the PassFail line before a measurement occurs and after a failure occurs is set by the [PassFailMode](PassFailMode_Property.md) property.  
  
#### Return Type

|  enum NAPassFailScope  
  
#### Default

|  1 - naGlobalScope  
  
#### Examples

|  HWAuxIO.PassFailScope = naGlobalScope 'Write scope = HWAuxIO.PassFailScope
'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_PassFailScope ( tagNAPassFailScope Scope ); HRESULT
get_PassFailScope ( tagNAPassFailScope* Scope );  
  
#### Interface

|  IHWAuxIO IHWMaterialHandlerIO

