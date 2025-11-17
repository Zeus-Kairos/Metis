##### Read/Write

|

##### [ ](../../../S3_Cals/ModifyCalKits.md)[About the Handler I/O
Connector](../../HandlerIO_Connector.htm)  
  
---|---  
  
## PortMode Property

* * *

#### Description

|  Sets and returns whether Port C or Port D is used for writing or reading
data on the Handler IO connector. The Handler IO Port C is connected
internally to the Port C of the Aux IO connector. Therefore, the Aux IO
connector will have the same input/output mode.  
---|---  
  
####  VB Syntax

|  handler.PortMode (port) = _value_  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
handler |  (object) - A Handler I/O object  
port |  (enum as NAMatHandlerPort) Port to be changed. Choose from: 2 -naPortC 3- naPortD  
value |  (enum as NaPortMode) \- Choose from: 0 - naInput \- set the port for reading 1 - naOutput \- set the port for writing  
  
#### Return Type

|  Long Integer  
  
#### Default

|  1 - naInput  
  
#### Examples

|  handler.PortMode(naPortC) = naInput 'Write value =
handler.PortMode(naPortD) 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_PortMode ( tagNAMatHandlerPort Port, tagNAPortMode Mode );
HRESULT get_PortMode ( tagNAMatHandlerPort Port, tagNAPortMode* Mode );  
  
#### Interface

|  IHWMaterialHandlerIO

