##### Write only

|

##### [About ECal User
Characterization](../../../S3_Cals/ECal_User_Characterization.htm)  
  
---|---  
  
## InitializeEx Method

* * *

#### Description

|  Note: This property replaces [Initialize (ECal)
Method](Initialize_ECal.htm). Initiates a User Characterization of an ECal
module. The specified channel number must be an S-parameter measurement
channel. The channel must already be calibrated using the same, or greater
number of VNA ports as the ECal module. Also, the calibrated VNA ports must
begin with Port 1 and use sequential port numbers. For characterizations that
are to be saved to the ECal module, the User Characterization number must
already be set before issuing this command using [CharacterizationNumber
Property](../Properties/CharacterizationNumber_Property.htm). For
characterizations that are to be saved to the VNA disk memory, setting the
User Characterization number is not necessary. After this command is executed,
subsequent commands can be used to query the number of measurement steps,
issue the acquisition commands, query the connection description strings, and
subsequently complete an Ecal User characterization.  
---|---  
  
####  VB Syntax

|  userChar.InitializeEx (chan,bool)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
userChar |  [ECalUserCharacterizer](../Objects/ECalUserCharacterizer_Object.md) (object)  
  
#### chan

|  (Long) Channel number of a calibrated S-parameter channel.  
  
#### bool

|  (Boolean) Choose from: True Check ECal memory to ensure that a new
characterization with the channels current number of points will fit in the
module memory. Select for User Characterizations to be stored in internal ECal
memory. False Skip the check. Select for User Characterizations is to be
stored to VNA disk memory.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  userchar.InitializeEx(2,True)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_InitializeEx(long chanNum,VARIANT_BOOL bCheck);  
  
#### Interface

|  IECalUserCharacterizer2  
  
* * *

