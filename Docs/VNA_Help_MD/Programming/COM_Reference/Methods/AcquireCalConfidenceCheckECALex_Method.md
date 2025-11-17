##### Write-only

|

##### [About ECAL Confidence Check](../../../S3_Cals/Quest_Cal.md#AboutECal)  
  
---|---  
  
## AcquireCalConfidenceCheckECALEx Method

* * *

#### Description

|  This method replaces
[AcquireCalConfidenceCheckECAL](AcquireCalConfidenceCheckECAL.md) Transfers
confidence data from the specified ECal module into the measurement's memory
trace. The data is transferred to the specified S-parameter on the same
channel as this Calibrator object. The characterization within the ECal module
that the confidence data will be read from is specified by
[ECALCharacterizationEx](../Properties/ECALCharacterizationEx_Property.md).
The default value is 0. Note: A confidence check can NOT be performed remotely
from User Characterizations that are stored on the VNA disk.  
---|---  
  
####  VB Syntax

|  cal.AcquireCalConfidenceCheckECALEx Sparam [,ecalModule]  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
cal |  A Calibrator (object)  
Sparam |  (String) S-parameter to transfer confidence data to. This parameter must be present on the same channel as the calibrator object.  
ecalModule |  (Integer)  Optional argument. ECal module. Choose from modules 1 through 8 Use [IsECALModuleFoundEx](../Properties/IsECALModuleFoundEx_Property.md) to determine the number of modules connected to the VNA Use [GetECALModuleInfoEx](Get_ECALModuleInfoEx_Method.md) to return the model and serial number of each module.  
  
#### Return Type

|  None  
  
#### Default

|  Not applicable  
  
#### Examples

|  Cal.AcquireCalConfidenceCheckECALEx "S11", 2  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT AcquireCalConfidenceCheckECALEx(BSTR strParameter, long
moduleNumber = 1);  
  
#### Interface

|  ICalibrator4  
  
* * *

  

