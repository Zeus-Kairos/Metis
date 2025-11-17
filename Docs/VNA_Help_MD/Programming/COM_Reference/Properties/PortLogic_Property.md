##### Read/Write

|

##### [About the Handler I/O Connector](../../HandlerIO_Connector.md)  
  
---|---  
  
## PortLogic Property

* * *

#### Description

|  Sets and returns the logic mode of data ports A-H on the HandlerIO
connector. Port C of the Handler IO is connected internally to the Port C of
the Aux IO connector. Therefore, it will have the same logic mode.  
---|---  
  
####  VB Syntax

|  handler.PortLogic = _value_  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
handler |  (object) - A HandlerI/O object  
value |  (enum as NaRearPanelIOLogic) - Choose from: 0 - naPositiveLogic \- When a value of one is written, the associated line goes High 1 - naNegativeLogic \- When a value of one is written, the associated line goes Low For ports that are in output (write) mode, a change in logic causes the output lines to change state immediately. For example, Low levels change immediately to High levels. For ports that are in input (read) mode (C,D,E only), a change in logic will be reflected when data is read from that port. For example, if a line read 0, the next read after a logic change will read 1.  
  
#### Return Type

|  Long Integer  
  
#### Default

|  1 - naNegativeLogic  
  
#### Examples

|  handler.PortLogic = value 'Write value = handler.PortLogic 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_PortLogic( tagNARearPanelIOLogic Mode ); HRESULT get_PortLogic(
tagNARearPanelIOLogic* Mode );  
  
#### Interface

|  IHWMaterialHandlerIO

