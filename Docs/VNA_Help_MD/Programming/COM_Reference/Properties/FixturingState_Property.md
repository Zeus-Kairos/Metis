##### Write/Read

|

##### About Fixturing  
  
---|---  
  
## FixturingState Property

* * *

#### Description

|  Turns all three fixturing functions (de-embedding, port matching, impedance
conversion) ON or OFF for all ports on the specified channel. This does NOT
affect port extensions.  
---|---  
  
####  VB Syntax

|  fixture.FixturingState = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
value |  (boolean) True \- Turns Fixturing ON False - Turns Fixturing OFF  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  fixture.FixturingState = True 'Write  
value = fixture.FixturingState 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_FixturingState(VARIANT_BOOL *pVal) HRESULT
put_FixturingState(VARIANT_BOOL newVal)  
  
#### Interface

|  IFixturing

