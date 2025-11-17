##### Read-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## GetStandardComplex Method Superseded

* * *

#### Description

|  This command is [replaced](../../Replacement_Commands.md) with [Get
StandardComplexByString](Get_StandardComplexByString_Method.htm) Returns
standard acquisition data from the Cal Set. The returned data is complex
pairs. Learn more about [Reading and Writing Cal
Data](../../Learning_about_COM/Read_and_Write_Calibration_Data_using_COM.htm)
See examples of
[Reading](../../COM_Example_Programs/COM_Reading_CalSet_Examples.md) and
[Writing](../../COM_Example_Programs/Writing_Cal_Set_Data_using_COM.md) Cal
Set Data  Note: This method exists on a non-default interface. If you cannot
access this method, use the [GetStandard](Get_Standard2_Method.md) Method on
ICal Set  
---|---  
  
####  VB Syntax

|  ICalData2.getStandardComplex class, rcv, src, numPts, real(), imag()  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
ICalData2 |  An [ICalData2](../Objects/CalSet_Object.md#ICalData2) pointer to the Cal Set object  
class |  (enum NACalClass) Standard data to be read. Choose from: |  1 - naClassA  
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
src |  (long) \- Source Port  
numPts |  (Long) An In/Out parameter. On the way in, you specify the max number of values being requested. On the way out, the VNA returns number of values actually returned.  
real() |  (single) \- array to accept the real part of the calibration data. One-dimensional for the number of data points.  
imag() |  (single) \- array to accept the imaginary part of the calibration data. One-dimensional for the number of data points.  
  
#### Return Type

|  (single)  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim numpts as long  
numpts = ActiveChannel.NumberOfPoints  
ReDim r(numpts) ' real part  
ReDim i(numpts) ' imaginary part  
Dim Cal Set as Cal Set  
set Cal Set = pna.GetCalManager.GetCal SetByGUID( txtGUID )  
Dim sData As ICalData2  
Set sData = Cal Set  
sdata.getStandardComplex naSOLT_Open, 1, 1, numpts, r(0), i(0)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT getStandardComplex(tagNACalClass stdclass, long ReceivePort, long
SourcePort, long* pNumValues, float* pReal, float* pImag)  
  
#### Interface

|  ICalData2

