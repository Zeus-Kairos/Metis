##### Read/Write

## PassFailLogic Property

* * *

#### Description

|  Sets and reads the logic of the PassFail line on the [HANDLER IO
connector](../../HandlerIO_Connector.htm) (pin 33). [Learn more about Global
Pass/Fail.](../../../S4_Collect/Use_Limits_to_Test_Devices.htm#Limitdiag)
Note: This line is connected to both the Handler IO and Aux IO in the VNA.
Therefore, this command will affect both of these connectors in the same way.  
---|---  
  
####  VB Syntax

|  object.PassFailLogic = _value_  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  (object) \- An Aux I/O or Handler I/O object  
value |  (enum as NARearPanelIOLogic) Choose from: 0 - naPositiveLogic - Causes the PassFail line to have positive logic (high = pass, low = fail). 1 - naNegativeLogic \- Causes the PassFail line to have negative logic (high = fail, low = pass).  
  
#### Return Type

|  Long Integer  
  
#### Default

|  naPositiveLogic  
  
#### Examples

|  aux.PassFailLogic = naNegativeLogic 'Write Text1.Text = aux.PassFailLogic
'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_PassFailLogic ( tagNARearPanelIOLogic Mode ); HRESULT
get_PassFailLogic ( tagNARearPanelIOLogic* Mode );  
  
#### Interface

|  IHWAuxIO IHWMaterialHandlerIO

