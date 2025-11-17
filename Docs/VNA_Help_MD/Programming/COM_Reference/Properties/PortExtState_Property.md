##### Write/Read

|

##### About Fixturing  
  
---|---  
  
## PortExtState Property

* * *

#### Description

|  Turns Port Extension ON or OFF for all ports on the channel.  
---|---  
  
####  VB Syntax

|  fixture.PortExtState = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
value |  (Boolean) False \- Turns Port Extensions OFF True \- Turns Port Extensions ON  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  fixture.PortExtState = 0 'Write  
value = fixture.PortExtState 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PortExtState(VARIANT_BOOL *pVal)  
HRESULT put_PortExtState(VARIANT_BOOL newVal)  
  
#### Interface

|  IFixturing

