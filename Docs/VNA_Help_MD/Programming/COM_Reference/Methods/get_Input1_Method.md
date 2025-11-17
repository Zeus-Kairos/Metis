##### Read-only

|

##### [About the Handler IO Connector](../../HandlerIO_Connector.md)  
  
---|---  
  
## get_Input1 Method

* * *

#### Description

|  Reads a hardware latch that captures high to low transitions on Input1 of
the Material Handler IO. Reading the latch causes it to reset and is ready for
the next transition. The hardware latch is only capable of capturing one
transition per query. Additional transitions are ignored until after the next
query. Momentarily driving Input1 high, then low, causes a transition to be
detected and latched.  
---|---  
  
####  VB Syntax

|  inp1 = handlerIo.get_Input1  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
inp1 |  (variant) - A variable to store the return value  
handlerIo |  (object) \- A HandlerIO object  
  
#### Return Type

|  Variant - 0 - a high to low transition occurred at Input1 since the last
time it was queried. 1 \- no high to low transition occurred.  
  
#### Default

|  Not Applicable  
  
#### Examples

|  input1 = handlerIo.get_Input1 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Input1 (VARIANT* Data );  
  
#### Interface

|  IHWMaterialHandlerIO

