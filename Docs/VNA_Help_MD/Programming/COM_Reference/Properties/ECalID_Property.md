##### Write / Read

|

##### [About ECal User
Characterization](../../../S3_Cals/ECal_User_Characterization.htm)  
  
---|---  
  
## ECalID Property

* * *

#### Description

|  Selects the model and serial number of the ECal module to be characterized.
This command does NOT set the model and serial number of the ECal module.  
---|---  
  
####  VB Syntax

|  userChar.ECalID = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
userChar |  An [ECalUserCharacterizer](../Objects/ECalUserCharacterizer_Object.md) Object  
value |  (String) Model and serial number of the ECal module to be characterized.  
  
#### Return Type

|  String  
  
#### Default

|  "" (Empty String)  
  
#### Examples

|  userChar.ECalID ="N4433A,00001"  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_ECalID(BSTR id);  
  
#### Interface

|  IECalUserCharacterizer  
  
* * *

