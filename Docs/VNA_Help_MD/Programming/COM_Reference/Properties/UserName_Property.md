##### Read-only

|

##### [About ECal User
Characterization](../../../S3_Cals/ECal_User_Characterization.htm)  
  
---|---  
  
## UserName Property

* * *

#### Description

|  Sets and reads the description of the person and/or company who is
producing the ECal user characterization. This description is stored with the
characterization in the ECal module. Set this description before sending
[Initialize](../Methods/Initialize_ECal.md) or the default (empty string)
will be used.  
---|---  
  
####  VB Syntax

|  userChar.UserName = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
userChar |  An [ECalUserCharacterizer](../Objects/ECalUserCharacterizer_Object.md) Object  
value |  (String) Descriptive text, limited to 19 characters maximum.  
  
#### Return Type

|  String  
  
#### Default

|  "" (Empty String)  
  
#### Examples

|  userChar.UserName = "John Doe, Acme Inc."  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_UserName(BSTR *name); HRESULT put_UserName(BSTR name);  
  
#### Interface

|  IECalUserCharacterizer  
  
* * *

