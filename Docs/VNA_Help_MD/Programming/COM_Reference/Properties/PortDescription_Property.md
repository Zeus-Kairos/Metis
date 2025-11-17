##### Write / Read

|

##### [About ECal User
Characterization](../../../S3_Cals/ECal_User_Characterization.htm)  
  
---|---  
  
## PortDescription Property

* * *

#### Description

|  For each port of the ECal module that is going to be characterized, sets
and reads the description of the adapters, cable, or fixture to be included in
the user characterization. This description is stored with the
characterization in the ECal module. Set this description before sending
[Initialize](../Methods/Initialize_ECal.md) or the default (empty string)
will be used.  
---|---  
  
####  VB Syntax

|  userChar.PortDescription (port)= value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
userChar |  An [ECalUserCharacterizer](../Objects/ECalUserCharacterizer_Object.md) Object  
port |  (Enum) ECal port for which description is to be set. Choose from: 1 or naECalPort_A 2 or naECalPort_B 3 or naECalPort_C 4 or naECalPort_D  
value |  (String) Descriptive text, limited to 24 characters maximum.  
  
#### Return Type

|  String  
  
#### Default

|  "" (Empty String)  
  
#### Examples

|  userChar.PortDescription (naECalPort_C)= "3.5 mm adapter, SN 00001"  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PortDescription(NAECalPort port, *BSTR description); HRESULT
put_PortDescription(NAECalPort port, BSTR description);  
  
#### Interface

|  IECalUserCharacterizer  
  
* * *

