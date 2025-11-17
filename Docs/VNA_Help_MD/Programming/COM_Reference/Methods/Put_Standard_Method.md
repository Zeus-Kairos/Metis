##### Write-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## PutStandard Method - Superseded

* * *

#### Description

|  Note: This command is replaced by
[PutStandardByString](Put_StandardByString_Method.md) Writes variant data to
the error correction buffer holding measurement data acquired for a specific
standard. [Learn about reading and writing Calibration
data.](../../Learning_about_COM/Read_and_Write_Calibration_Data_using_COM.htm)  
---|---  
  
####  VB Syntax

|  cal.putStandard class,rcv,src,data  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
cal |  A Calibrator (object)  
class |  (enum NACalClass) Standard. Choose from: |  1 - naClassA  
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
rcv |  (long) - Receiver Port  
src |  (long) - Source Port  
data |  (variant) Two dimensional array (0:1, 0:points-1)  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim varStd (1,200) As Variant  
cal.putStandard naSOLT_Thru, 2, 1, varStd  
  
#### [C++](../../learning_about_com/c++_and_the_com_interface.md) Syntax

|  HRESULT raw_putStandard(tagNACalClass stdclass, long ReceivePort, long
SourcePort, VARIANT varData)  
  
#### Interface

|  ICalibrator

