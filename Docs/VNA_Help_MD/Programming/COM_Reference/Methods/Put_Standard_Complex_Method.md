##### Write-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## PutStandardComplex Method Superseded

* * *

#### Description

|  This command is replaced with
[PutStandardComplexByString](Put_StandardComplexByString_Method.md) Puts
standards acquisition data into the Cal Set. Learn more about [Reading and
Writing Cal
Data](../../Learning_about_COM/Read_and_Write_Calibration_Data_using_COM.htm)
See examples of
[Reading](../../COM_Example_Programs/COM_Reading_CalSet_Examples.md) and
[Writing](../../COM_Example_Programs/Writing_Cal_Set_Data_using_COM.md) Cal
Set Data  
---|---  
  
####  VB Syntax

|  ICalData2.putStandardComplex class, rcv, src, numPts,real(),imag()  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
ICalData2 |  An [ICalData2](../Objects/CalSet_Object.md#ICalData2) pointer to the Cal Set object  
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
src |  (long) \- Source Port  
numPts |  (long) - The number of data points in the real and imaginary arrays.  
real() |  (single) \- one-dimensional array containing the real part of the acquisition data. (0:points-1)  
imag() |  (single) \- one-dimensional array containing the imaginary part of the acquisition data. (0:points-1)  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim sdata As ICalData2  
Set sdata = calmanager.CreateCal Set( 1 )  
sdata.putStandardComplex naSOLT_Open, 1, 1, numpts, rel(0), img(0)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT putStandardComplex(tagNACalClass stdclass, long ReceivePort, long
SourcePort, long lNumValues, float* pReal, float* pImag)  
  
#### Interface

|  ICalData2

