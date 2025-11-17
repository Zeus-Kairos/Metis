##### Write-only

|

##### [About the Handler IO Connector](../../HandlerIO_Connector.md)  
  
---|---  
  
## put_Port Method

* * *

#### Description

|  Writes a value to the specified port. Use the
[get_Port](get_Port_Method.md) Method to read the settings from the
"readable" ports (C, D, E).  
---|---  
  
####  VB Syntax

|  handlerIo.put_Port (port, value)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
handlerIo |  (object) \- A HandlerIO object  
port |  (enum as NAMatHandlerPort) \- port to put data into. Choose from: naPortA - (0) naPortB - (1) naPortC - (2) naPortD - (3) naPortE - (4) naPortF - (5) naPortG - (6) naPortH - (7)  
value |  The number of the data bits to set. The following table shows what the value represents: Note: When writing to port G, port C must be set to output mode  
When writing to port H, both port C and port D must be set to output mode. Use
Port Mode Property  
  
|  Port |  Max allowable <num> |  MSB...........................................LSB  
23...................................................0 |   
---|---|---|---|---  
|  A |  255 |  A7...A0 |  Write-only  
|  B |  255 |  B7...B0 |  Write-only  
|  C |  15 |  C3...C0 |  Read-Write  
|  D |  15 |  D3...D0 |  Read-Write  
|  E |  255 |  D3...D0 + C3...C0 |  Read-Write  
|  F |  65535 |  B7...B0 + A7...A0 |  Write-only  
|  G |  1048575 |  C3...C0 + B7...B0 + A7...A0 |  Write-only  
|  H |  16777215 |  D3...D0 + C3...C0 + B7...B0 + A7...A0 |  Write-only  
  
  
#### Return Type

|  Not Applicable  
---|---  
  
#### Default

|  Not Applicable  
  
#### Examples

|  handlerIo.put_Port(naPortB, 1)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_Port ( tagNAMatHandlerPort Port, VARIANT Data );  
  
#### Interface

|  IHWMaterialHandlerIO  
  
* * *

