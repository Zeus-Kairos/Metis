##### Read/Write

|

##### [About the Handler I/O Connector](../../HandlerIO_Connector.md)  
  
---|---  
  
## IndexState Property

* * *

#### Description

|  Determines the control of Material Handler connector Pin 20.  
---|---  
  
####  VB Syntax

|  handler.IndexState = _value_  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
handler |  (object) - A [Handler I/O](../Objects/HWMaterialHandlerIO_Object.md) object  
value |  (boolean) False - Pin 20 is controlled by Output Port B6 True - Pin 20 is controlled by the Index signal  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  handler.IndexState = False 'Write bState = handler.IndexState 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_IndexState (BOOL *pVal); HRESULT get_IndexState (BOOL newVal);  
  
#### Interface

|  IHWMaterialHandlerIO2

