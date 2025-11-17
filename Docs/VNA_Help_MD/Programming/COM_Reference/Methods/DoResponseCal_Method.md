##### Write-only

|

##### [About Calibration](../../../S3_Cals/Select_Cal.md)  
  
---|---  
  
## DoResponseCal Method

* * *

#### Description

|  Performs and immediately applies a Response cal. Same as selecting
Normalize from the Unguided Cal - Measure Standards page. [Learn
more](../../../S3_Cals/Calibration_Wizard.htm#MechMeas).  
---|---  
  
#### VB Syntax

|  cal.DoResponseCal (measParam),(SourcePort)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
cal |  A [Calibrator](../Objects/Calibrator_Object.md) (object)  
measParam |  (String) Measurement parameter to correct. It is NOT necessary for this measurement to be present.  
SourcePort |  (long integer) Source port number to calibrate. Optional for S-parameter measurements. Choose from: 0 - N5264B Measurement Receiver (no source ports). 1 - Calibrate port 1 2 - Calibrate port 2 (default, if unspecified) 3 - Calibrate port 3 And so forth for all available VNA / test set ports.  
  
#### Return Type

|  None  
  
#### Default

|  Not Applicable  
  
#### Examples

|  cal.DoResponseCal "A/R",1  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT DoResponseCal(BSTR param, long SourcePort);  
  
#### Interface

|  ICalibrator9  
  
* * *

