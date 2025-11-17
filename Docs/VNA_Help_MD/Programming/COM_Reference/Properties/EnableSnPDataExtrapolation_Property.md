##### Write/Read

|

##### About Fixturing  
  
---|---  
  
## EnableSnPDataExtrapolation

* * *

#### Description

|  Turns ON and OFF SNP file extrapolation for both 2-port and 4-port
embedding/de-embedding.  
---|---  
  
####  VB Syntax

|  fixture.EnableSnPDataExtrapolation = bool  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
bool |  True \- Turns Extrapolation ON False \- Turns Extrapolation OFF  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  fixture.EnableSnPDataExtrapolation = True  
value = fixture.EnableSnPDataExtrapolation 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_EnableSnPDataExtrapolation(VARIANT_BOOL *pExtrap); HRESULT
put_EnableSnPDataExtrapolation(VARIANT_BOOL bExtrap);  
  
#### Interface

|  IFixturing6  
  
* * *

