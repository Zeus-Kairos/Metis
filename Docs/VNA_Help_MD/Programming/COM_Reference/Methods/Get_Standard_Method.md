##### Read-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## GetStandard Method - Superseded

* * *

#### Description

|  This command has been replaced with [Get
StandardByString](Get_StandardByString_Method.htm) Retrieves data that was
acquired for a specific cal standard. This method returns the actual
measurement data - not the calculated error terms. This method returns a
variant which is less efficient than
[getStandardComplex](Get_Standard_Complex_Method.md) on the ICalData
interface. [Learn about reading and writing Calibration
data.](../../Learning_about_COM/Read_and_Write_Calibration_Data_using_COM.htm)  
---|---  
  
####  VB Syntax

|  data = cal.getStandardclass,rcv,src  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
data |  Variant array to store the data.  
cal |  A Calibrator (object)  
class |  (enum NACalClass) Standard to be measured. Choose from: |  1 - naClassA  
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
rcv |  (long integer) - Receiver Port  
src |  (long integer) - Source Port  
  
#### Return Type

|  (variant) \- two-dimensional array (0:1, 0:NumberOfPoints-1)  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim varStd As Variant  
varStd = cal.getStandard(naSOLT_Thru,2,1)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT raw_getStandard(tagNACalClass stdclass, long ReceivePort, long
SourcePort, VARIANT* pData)  
  
#### Interface

|  ICalibrator  
  
* * *

