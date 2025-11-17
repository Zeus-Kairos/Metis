##### Write/Read

|

##### About Fixturing  
  
---|---  
  
## Port2PdeembedState Property

* * *

#### Description

|  Turns de-embedding ON or OFF for all ports on the channel.  
---|---  
  
####  VB Syntax

|  fixture.Port2PdeembedState = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
value |  (Boolean) False \- Turns De-embedding OFF True \- Turns De-embedding ON  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  fixture.Port2PdeembedState = False 'Write  
value = fixture.Port2PdeembedState 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Port2PdeembedState(VARIANT_BOOL *pVal)  
HRESULT put_Port2PdeembedState(VARIANT_BOOL newVal)  
  
#### Interface

|  IFixturing

