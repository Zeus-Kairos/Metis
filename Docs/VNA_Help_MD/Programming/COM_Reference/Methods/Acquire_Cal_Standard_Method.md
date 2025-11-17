##### Write-only

|

##### [About Calibration Standards](../../../S3_Cals/ModifyCalKits.md)  
  
---|---  
  
## AcquireCalStandard Method - Superseded

* * *

#### Description

|  Note: This command has been replaced by [AcquireCalStandard2
Method](AcquireCalStandard2_Method.htm), which provides for acquisition of
sliding load standards. All other functionality is identical.  
---|---  
  
####  VB Syntax

|  cal.AcquireCalStandard std[,index]  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
cal |  A Calibrator (object)  
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
index |  (long integer) number of the standard. Optional argument - Used if there is more than one standard required to cover the necessary frequency range. If unspecified, value is set to 1. Note The behavior has changed with VNA revisions as follows:

  * Before 6.01: Accepted 0 and changed it to 1
  * 6.01 to 6.04: Did NOT accept 0
  * 6.04.11 and higher: Accepts 0 and changes it to 1

  
  
#### Return Type

|  None  
  
#### Default

|  Not Applicable  
  
* * *  
  
#### Examples

|  Cal.AcquireCalStandard naSOLT_Thru 'Write  
  
* * *  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT AcquireCalStandard(tagNACalClass enumClass, short standardNumber)  
  
#### Interface

|  ICalibrator  
  
* * *

