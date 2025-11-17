##### Write-only  
  
---  
  
## GenerateSteps Method

* * *

#### Description

|  Returns the number of steps required to complete the calibration. For an
ECal User Characterization this generate steps for the ECal User
Characterization process. The channel must already be calibrated using the
same, or greater number of VNA ports as the ECal module. Also, the VNA ports
must begin with Port 1 and use sequential port numbers. After this command is
executed, subsequent commands can be used to query the number of measurement
steps, issue the acquisition commands, query the connection description
strings, and subsequently complete a User Characterization calibration.  
---|---  
  
####  VB Syntax

|  value = obj.GenerateSteps  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (long) - Variable to store the returned number of steps  
obj |  Any of the following: [GuidedCalibration](../Objects/GuidedCalibration_Object.md) (object) [SMCType](../Objects/SMC_Type_Object.md) (object) [VMCType](../Objects/VMC_Type_Object.md) (object) [ECalUserCharacterizer](../Objects/ECalUserCharacterizer_Object.md) (object)  
  
#### Return Type

|  Long  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = SMC.GenerateSteps  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_GenerateSteps(long* steps);  
  
#### Interface

|  IGuidedCalibration SMCType VMCType IECalUserCharacterizer  
  
* * *

