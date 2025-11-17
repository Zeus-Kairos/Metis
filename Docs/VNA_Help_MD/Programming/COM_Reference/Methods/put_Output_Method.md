##### Write-only

|

##### [About the Handler IO Connector](../../HandlerIO_Connector.md)  
  
---|---  
  
## put_Output Method

* * *

#### Description

|  Writes a TTL HI or TTL Low to output pins 3 or 4 of the Material Handler IO
connector. Each pin also has a latched output which is written to with USER.
With the latched (USER) outputs, the value is not applied to the associated
pin until a positive edge is detected at INPUT1 (pin 2).  
---|---  
  
####  VB Syntax

|  handlerIo.put_Output (pin) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
handlerIo |  (object) \- A HandlerIO object  
pin |  (enum as NAMatHandlerOutput) \- pin to write data to. Choose from: naOutput1 - (0) - pin3  
naOutput1User (1) - pin3 latched (applied to pin 3 on positive edge of
Input1-pin2)  
naOutput2 (2) - pin4  
naOutput2User (3) - pin4 latched (applied to pin 4 on positive edge of
Input1-pin2)  
value |  (Variant) Value to write to the selected pin. Choose from 0 \- TTL LOW 1 \- TTL HIGH  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  0  
  
#### Examples

|  handlerIo.put Output(naOutput1)= 1  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_Output ( tagNAMatHandlerOutput Output, VARIANT Data );  
  
#### Interface

|  IHWMaterialHandlerIO

