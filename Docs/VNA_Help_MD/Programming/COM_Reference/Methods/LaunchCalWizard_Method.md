##### Read-Write

|

##### [About the Cal Wizard](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## LaunchCalWizard Method

* * *

#### Description

|  Launches the S-parameter Cal Wizard on the VNA and does not return until
the Cal Wizard is dismissed. To launch the Cal Wizard for a VNA Application,
use the [LaunchDialog Method](LaunchDialog_Method.md). Note: The Cal Wizard
operates on the active measurement. Therefore, activate the measurement to be
calibrated before launching the Cal Wizard.  
---|---  
  
####  VB Syntax

|  success = app.LaunchCalWizard (newCS)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
success |  (boolean) - variable to store the returned value True - The Cal was completed False \- The Cal was canceled without completing the calibration.  
app |  An [Application](../Objects/Application_Object.md) (object)  
newCS |  (boolean) True \- Cal will be performed on a new Cal Set. False \- Cal will be performed using the existing Cal Set assigned to the channel. If no Cal Set is found, a new Cal Set will be created.  
  
#### Return Type

|  Boolean  
  
#### Default

|  Not Applicable  
  
#### Example

|  dim bSuccess as boolean  
dim bNewCalset as boolean  
bNewCalSet = false  
bSuccess = app.LaunchCalWizard( bNewCalSet)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT LaunchCalWizard(VARIANT_BOOL bCalsuccess)  
  
#### Interface

|  IApplication  
  
* * *

