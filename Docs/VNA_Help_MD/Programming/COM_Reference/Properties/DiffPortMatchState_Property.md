##### Write/Read

|

##### About Fixturing  
  
---|---  
  
## DiffPortMatchState Property

* * *

#### Description

|  Turns ON or OFF 4-port differential port matching function. Must also set
the fixture simulator function to ON using [FixturingState
Property](FixturingState_Property.htm).  
---|---  
  
####  VB Syntax

|  fixture.DiffPortMatchState = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
value |  (Boolean) False \- Turns differential port matching OFF True \- Turns differential port matching ON  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  fixture.DiffPortMatchState = False 'Write  
value = fixture.DiffPortMatchState 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_DiffPortMatchState( VARIANT_BOOL *pVal)  
HRESULT put_DiffPortMatchState( VARIANT_BOOL newVal)  
  
#### Interface

|  IFixturing2

