##### Write/Read

|

##### About Fixturing  
  
---|---  
  
## PortArbzState Property

* * *

#### Description

|  Turns Port Impedance ON or OFF for all ports on the channel.  
---|---  
  
####  VB Syntax

|  fixture.PortArbzState = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
value |  (Boolean) False \- Turns Port Impedance OFF True \- Turns Port Impedance ON  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  fixture.PortArbzState = False 'Write  
value = fixture.PortArbzState 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_PortArbzState(VARIANT_BOOL *pVal)  
HRESULT put_PortArbzState(VARIANT_BOOL newVal)  
  
#### Interface

|  IFixturing

