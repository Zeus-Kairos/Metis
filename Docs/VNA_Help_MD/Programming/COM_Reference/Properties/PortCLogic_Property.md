##### Read/Write

|  
---|---  
  
## PortCLogic Property

* * *

#### Description

|  Sets and reads the logic mode of Port C on the Handler IO connector.  
---|---  
  
####  VB Syntax

|  AuxIO.PortCLogic = _value_  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
AuxIO |  (object) - A Hardware Aux I/O object  
value |  (Enum as NaRearPanelIOLogic) - Choose from: 0 - naPositiveLogic \- The associated data line goes HIGH when writing a 1 to a PortC bit. 1 - naNegativeLogic \- The associated data line goes LOW when writing a 1 to a PortC bit. When Port C is in Output/Write mode, a change in logic causes the output lines to change state immediately. For example, Low levels change to High levels. When Port C is in Input/Read mode, a change in logic will not cause the lines to change, but data read from Port C will reflect the change in logic.  
  
#### Return Type

|  Enum  
  
#### Default

|  1 - naNegativeLogic  
  
#### Examples

|  auxIO.PortCLogic = value 'Write value = auxIo.PortCLogic 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_PortCLogic ( tagNARearPanelIOLogic Mode ); HRESULT
get_PortCLogic ( tagNARearPanelIOLogic* Mode );  
  
#### Interface

|  IHWAuxIO

