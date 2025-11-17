##### Read/Write

|

##### [ ](../../../S3_Cals/ModifyCalKits.md)[About the Handler I/O
Connector](../../HandlerIO_Connector.htm)  
  
---|---  
  
## ReadyForTriggerState Property

* * *

#### Description

|  Determines the control of Material Handler connector Pin 21.  
---|---  
  
####  VB Syntax

|  handler.ReadyForTriggerState = _value_  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
handler |  (object) - A [Handler I/O](../Objects/HWMaterialHandlerIO_Object.md) object  
value |  (boolean) False - Pin 21 is controlled by Output Port B7 True - Pin 21 is controlled by the Ready for Trigger signal  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  handler.ReadyForTriggerState = False 'Write bState =
handler.ReadyForTriggerState 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_ReadyForTriggerState (BOOL *pVal); HRESULT
get_ReadyForTriggerState (BOOL newVal);  
  
#### Interface

|  IHWMaterialHandlerIO2

