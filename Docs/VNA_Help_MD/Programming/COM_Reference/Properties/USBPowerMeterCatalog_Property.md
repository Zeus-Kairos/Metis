##### Read-only

|

##### [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)  
  
---|---  
  
## USBPowerMeterCatalog Property

* * *

#### Description

|  Returns the ID string of power meters / sensors that are connected to the
VNA USB. Use the list to select a power sensor for a source power cal.  
---|---  
  
#### VB Syntax

|  list = pwrCal.USBPowerMeterCatalog  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
list |  (String) Variable to store the returned list of USB power meters.  
pwrCal |  (object)  [A SourcePowerCalibrator](../Objects/SourcePowerCalibrator_Object.md) (object)  
  
#### Return Type

|  Comma-delimited strings. Two sensor strings are separated by a semicolon.  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Set pwrCal = pna.SourcePowerCalibrator  
list = pwrCal.USBPowerMeterCatalog'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_USBPowerMeterCatalog(BSTR *pUSBList);  
  
#### Interface

|  ISourcePowerCalibrator6  
  
* * *

