##### Write/Read

|

##### About Fixturing  
  
---|---  
  
## DiffZConvState Property

* * *

#### Description

|  Turns ON or OFF 4-port differential impedance conversion function. Must
also set the fixture simulator function to ON using [FixturingState
Property](FixturingState_Property.htm).  
---|---  
  
####  VB Syntax

|  fixture.DiffZConvState = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
value |  (Boolean) False \- Turns differential impedance conversion OFF. True \- Turns differential impedance conversion ON.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  fixture.DiffZConvState = False 'Write  
value = fixture.DiffZConvState 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_DiffZConvState( VARIANT_BOOL *pVal)  
HRESULT put_DiffZConvState( VARIANT_BOOL newVal)  
  
#### Interface

|  IFixturing2

