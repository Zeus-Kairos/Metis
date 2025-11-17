##### Write only

|

##### [About ECal User
Characterization](../../../S3_Cals/ECal_User_Characterization.htm)  
  
---|---  
  
## Initialize Method Superseded

* * *

#### Description

|  Note: This command is replaced with [InitializeEx
Method](InitializeEx_Method.htm) Initiates a User Characterization of an ECal
module. The specified channel number must be an S-parameter measurement
channel. The User characterization number must already be set before issuing
this command using [CharacterizationNumber
Property](../Properties/CharacterizationNumber_Property.htm).  
---|---  
  
####  VB Syntax

|  userChar.Initialize (chan)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
userChar |  [ECalUserCharacterizer](../Objects/ECalUserCharacterizer_Object.md) (object)  
  
#### chan

|  (Long) Channel number of a calibrated S-parameter channel.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  userchar.Initialize(2)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_Initialize(long chanNum);  
  
#### Interface

|  IECalUserCharacterizer  
  
* * *

