##### Write only

|

##### [About ECal User
Characterization](../../../S3_Cals/ECal_User_Characterization.htm)  
  
---|---  
  
## SaveToDiskMemory Method

* * *

#### Description

|  Saves the User Characterization to VNA disk memory. To save to ECal
internal memory, use [SaveToECal Method](SaveToECal_Method.md). User
Characterization can be saved to both VNA disk memory and ECal module memory.
Note: An ECal confidence check can NOT be performed remotely from User
Characterizations that are stored on the VNA disk.  
---|---  
  
####  VB Syntax

|  userChar.SaveToDiskMemory (name)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
userChar |  An [ECalUserCharacterizer](../Objects/ECalUserCharacterizer_Object.md) (object)  
name |  (String) User characterization name. Although there is no limit to the number of characters, only about 10 characters appear in the Cal Wizard dialog when selecting a user characterization for use.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  userChar.SaveToDiskMemory "DUT1"  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT SaveToDiskMemory(BSTR name);  
  
#### Interface

|  IECalUserCharacterizer2  
  
* * *

  

