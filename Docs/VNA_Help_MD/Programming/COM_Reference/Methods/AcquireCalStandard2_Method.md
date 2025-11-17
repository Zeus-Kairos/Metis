##### Write-only

|

##### [About Calibration Standards](../../../S3_Cals/ModifyCalKits.md)  
  
---|---  
  
## AcquireCalStandard2 Method

* * *

#### Description

|  Measures the specified standard from the selected calibration kit. The
calibration kit is selected using
[app.CalKitType](../Properties/CalKitType_Property.md). For 2-port
calibration, it is also necessary to specify direction with
[AcquisitionDirection](../Properties/AcquisitionDirection_Property.md). To
omit Isolation from a 2-port calibration, do not Acquire a cal standard for
naSOLT_Isolation. For using two sets of standards, see
[Simultaneous2PortAcquisition
Property](../Properties/Simultaneous2PortAcquisition_Property.htm). Note: This
command replaces [AcquireCalStandard](Acquire_Cal_Standard_Method.md). This
command provides for the acquisition of a sliding load cal. All other
functionality is identical.  
---|---  
  
####  VB Syntax

|  cal.AcquireCalStandard2 std[,index][,slide]  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
cal |  A [Calibrator](../Objects/Calibrator_Object.md) (object)  
std |  (enum NACalClass) Standard to be measured. Choose from: |  1 - naClassA  
---  
2 - naClassB  
3 - naClassC  
4 - naClassD  
5 - naClassE  
6 - naReferenceRatioLine  
7 - naReferenceRatioThru  
SOLT Standards  
1 - naSOLT_Open  
2 - naSOLT_Short  
3 - naSOLT_Load  
4 - naSOLT_Thru  
5 - naSOLT_Isolation  
TRL Standards  
1 - naTRL_Reflection  
2 - naTRL_Line_Reflection  
3 - naTRL_Line_Tracking  
4 - naTRL_Thru  
5 - naTRL_Isolation  
[index] |  (long integer) Number of the standard. Optional argument - Used if there is more than one standard required to cover the necessary frequency range. If unspecified, value is set to 1. Note The behavior has changed with VNA revisions as follows:

  * Before 6.01: Accepted 0 and changed it to 1
  * 6.01 to 6.04: Did NOT accept 0
  * 6.04.11 and higher: Accepts 0 and changes it to 1

  
[slide] |  (enum as NACalStandardSlidingState) Optional argument. State of the sliding load. The slide should be set a minimum of five times. Seven is the maximum that can be stored. Choose from: 0 - naNotSlidingStd \- not using a sliding load - Default if not specified. 1 - naSlideIsSet \- slide is set for acquisition 2 - naSlideIsDone \- this next acquisition will be the last. Calculations will then be performed.  
  
#### Return Type

|  None  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Cal.AcquireCalStandard2 naSOLT_Thru  
Cal.AcquireCalStandard2 naSOLT_Thru,2,naNotSlidingStd  
'measures the second standard listed in the class of naSOLT_Thru  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT AcquireCalStandard2(NACalClass enumClass, long standardPosition,
NACalStandardSlidingState slidingStandardState)  
  
#### Interface

|  ICalibrator  
  
* * *

