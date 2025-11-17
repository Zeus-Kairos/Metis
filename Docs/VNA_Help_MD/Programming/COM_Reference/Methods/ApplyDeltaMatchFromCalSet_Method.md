##### Write-only

|

#####  
  
---|---  
  
## ApplyDeltaMatchFromCalSet Method

* * *

#### Description

|  Specifies a Cal Set as a source of delta match correction. If GUID is not
supplied then the Global Delta Match Cal Set is assumed. An error is returned
if the specified Cal Set does not meet the following Delta Match criteria. The
Global Delta Match Cal can ALWAYS be applied.

  * Must have been performed using ECal or as a guided mechanical cal (not Unguided).
  * Must have the same start freq, stop freq, and number of points as the channel being calibrated.
  * Must calibrate the ports that are required by the TRL or Unknown Thru Cal as indicated by [PortsNeedingDeltaMatch Property](../Properties/PortsNeedingDeltaMatch_Property.md).

[Learn more about Delta Match
calibration.](../../../S3_Cals/TRL_Calibration.htm#4Port)  
---|---  
  
####  VB Syntax

|  guided.ApplyDeltaMatchFromCalSet [GUID]  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
guided |  [GuidedCalibration](../Objects/GuidedCalibration_Object.md) (object)  
GUID |  Optional Argument. GUID of the Cal Set to use. If unspecified, the Global Delta Match Cal Set is used.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  guided.ApplyDeltaMatchFromCalSet "{2B893E7A-971A-11d5-8D6C-00108334AE96}"  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT ApplyDeltaMatchFromCalSet(BSTR calsetGUID);  
  
#### Interface

|  IGuidedCalibration2

