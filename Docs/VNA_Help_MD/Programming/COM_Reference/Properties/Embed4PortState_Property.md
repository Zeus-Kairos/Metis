##### Write/Read

|

##### About Fixturing  
  
---|---  
  
## Embed4PortState Property

* * *

#### Description

|  Turns ON or OFF 4-port Network embedding for all ports on the channel.  
---|---  
  
####  VB Syntax

|  fixture.Embed4PortState = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
value |  (Boolean) False \- Turns Embedding OFF True \- Turns Embedding ON  
  
#### Return Type

|  Boolean  
  
#### Default

|  False (OFF)  
  
#### Examples

|  fixture.Embed4PortState = False 'Write  
value = fixture.Embed4PortState 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Embed4PortState(VARIANT_BOOL *pVal)  
HRESULT put_Embed4PortState(VARIANT_BOOL newVal)  
  
#### Interface

|  IFixturing2

