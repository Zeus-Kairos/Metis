##### Write/Read

|

##### About Fixturing  
  
---|---  
  
## PortMatchingState Property

* * *

#### Description

|  Sets and returns the Port Matching State on the channel.  
---|---  
  
####  VB Syntax

|  fixture.PortMatchingState = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
value |  (boolean)  
True \- Turns Port Matching ON False \- Turns Port Matching OFF  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  fixture.PortMatchingState = True 'Write  
value = fixture.PortMatchingState 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_PortMatchingState(VARIANT_BOOL *pVal)  
HRESULT put_PortMatchingState(VARIANT_BOOL newVal)  
  
#### Interface

|  IFixturing

