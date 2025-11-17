##### Write / Read

|

##### [About ECal User
Characterization](../../../S3_Cals/ECal_User_Characterization.htm)  
  
---|---  
  
## CharacterizationNumber Property

* * *

#### Description

|  Sets and reads the number to which the user characterization will be stored
in the ECal module. The number must be set before sending
[Initialize](../Methods/Initialize_ECal.md) or the default value (1) will be
used.  
---|---  
  
####  VB Syntax

|  userChar.CharacterizationNumber = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
userChar |  An [ECalUserCharacterizer](../Objects/ECalUserCharacterizer_Object.md) Object  
value |  (Long) User Characterization number. Choose a value between 1 and 12.  
  
#### Return Type

|  Long Integer  
  
#### Default

|  Not Applicable  
  
#### Examples

|  userChar.CharacterizationNumber = 5  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_CharacterizationNumber(long *Number);  
  
#### Interface

|  IECalUserCharacterizer  
  
* * *

