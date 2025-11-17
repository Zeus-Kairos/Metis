##### Write/Read

|

##### About Fixturing  
  
---|---  
  
## CmnModeZConvState Property

* * *

#### Description

|  Turns ON or OFF 4-port common port impedance conversion function. Must also
set the fixture simulator function to ON using [FixturingState
Property](FixturingState_Property.htm).  
---|---  
  
####  VB Syntax

|  fixture.CmnModeZConvState = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
value |  (Boolean) False \- Turns common port impedance conversion OFF True \- Turns common port impedance conversion ON  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  fixture.CmnModeZConvState = False 'Write  
value = fixture.CmnModeZConvState 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_CmnModeZConvState( VARIANT_BOOL *pVal) HRESULT
put_CmnModeZConvState( VARIANT_BOOL newVal)  
  
#### Interface

|  IFixturing2

