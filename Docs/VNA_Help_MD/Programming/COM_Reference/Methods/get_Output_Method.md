##### Read-only

|

##### [About the Handler IO Connector](../../HandlerIO_Connector.md)  
  
---|---  
  
## get_Output Method

* * *

#### Description

|  [Type 1 and Type2
configurations:](../../HandlerIO_Connector.htm#PinAssignments) Returns the
last value written to the selected output pin. [Type3
configuration](../../HandlerIO_Connector.htm#PinAssignments): Returns the
current state of the selected output pin. If an Input1 trigger occurs, the
state may not be the same value as was written. All configurations: Data is
written using [put_Output](put_Output_Method.md) Method.  
---|---  
  
####  VB Syntax

|  data = handlerIo.get_Output (pin)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
data |  (variant) - A variable to store the return value. The returned value will be one of the following: 0 \- TTL Low 1 \- TTL High  
handlerIo |  (object) \- A HandlerIO object  
pin |  (enum as NAMatHandlerOutput) \- output to read. Choose from: naOutput1 (0)  
naOutput1User (1)  
naOutput2 (2)  
naOutput2User (3) [Learn about User
Output](../../HandlerIO_Connector.htm#OUTPUT1)  
  
#### Return Type

|  Variant  
  
#### Default

|  Not Applicable  
  
#### Examples

|  data = handlerIo.get_Output(naOutput1)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Output ( tagNAMatHandlerOutput Output, VARIANT* Data );  
  
#### Interface

|  IHWMaterialHandlerIO

