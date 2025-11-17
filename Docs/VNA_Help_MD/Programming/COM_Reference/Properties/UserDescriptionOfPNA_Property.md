##### Write/Read

|

##### [About ECal User
Characterization](../../../S3_Cals/ECal_User_Characterization.htm)  
  
---|---  
  
## UserDescriptionOfPNA Property

* * *

#### Description

|  Sets and reads a description of the VNA used to perform the User
Characterization. This description is stored with the characterization in the
ECal module. Set this description before sending
[Initialize](../Methods/Initialize_ECal.md) or the default (empty string)
will be used.  
---|---  
  
####  VB Syntax

|  userChar.UserDescriptionOfPNA = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
userChar |  An [ECalUserCharacterizer](../Objects/ECalUserCharacterizer_Object.md) Object  
value |  (String) Descriptive text, limited to 14 characters maximum.  
  
#### Return Type

|  String  
  
#### Default

|  ""(Empty String)  
  
#### Examples

|  userChar.UserDescriptionOfPNA = "My PNA"  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_UserDescriptionOfPNA(BSTR *info); HRESULT
put_UserDescriptionOfPNA(BSTR info);  
  
#### Interface

|  IECalUserCharacterizer  
  
* * *

