##### Read-only

|

##### [About the Handler IO Connector](../../HandlerIO_Connector.md)  
  
---|---  
  
## get_Port Method

* * *

#### Description

|  Returns the value from the specified "readable" port.  
---|---  
  
####  VB Syntax

|  data = handlerIo.get_Port (port)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
data |  (variant) - A variable to store the return value. The following table shows what the returned data represents:  
  
|  Port |  MSB...........................................LSB  
8...................................................0  
---|---|---  
|  C |  C3...C0  
|  D |  D3...D0  
|  E |  D3...D0 + C3...C0  
  

handlerIo |  (object) \- A HandlerIO object  
---|---  
port |  (enum as NAMatHandlerPort) \- port to get data from. Choose from: naPortC - (2) naPortD - (3) naPortE - (4) Note: Reading data from the Write-only ports (A,B,F,G,H) will return an error.  
Ports C and D must be put in Read mode before reading from C, D, or E using
[PortMode Property](../Properties/PortMode_Property.md).  
  
#### Return Type

|  Variant  
  
#### Default

|  0  
  
#### Examples

|  data = handlerIo.get_Port(naPortC)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Port ( tagNAMatHandlerPort Port, VARIANT* Data );  
  
#### Interface

|  IHWMaterialHandlerIO

