##### Read-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## GetStandard Method Superseded

* * *

#### Description

|  This command has been replaced with [Get
StandardByString](Get_StandardByString_Method.htm) Returns standard
acquisition data from the Cal Set. The returned data is complex pairs. Learn
more about [Reading and Writing Cal
Data](../../Learning_about_COM/Read_and_Write_Calibration_Data_using_COM.htm)
See examples of
[Reading](../../COM_Example_Programs/COM_Reading_CalSet_Examples.md) and
[Writing](../../COM_Example_Programs/Writing_Cal_Set_Data_using_COM.md) Cal
Set Data  
---|---  
  
####  VB Syntax

|  data = CalSet.getStandard (standard, rcv, src)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
data |  (Variant) Two-dimensional safe array to store the returned data. Memory for the returned Variant is allocated by the VNA and must be released by client. Note: See also [getStandardComplex](Get_Standard_Complex_Method.md) on the ICalData2 interface to avoid using the variant data type.  
CalSet |  A Cal Set (object)  
standard |  (enum NACalClass) Standard data to be read. Choose from: |  1 - naClassA  
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
  
#### Return Type

|  (variant)  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim varStd As Variant Dim varStd2 As Variant Cal Set.OpenCalSet(
naCalType_TwoPortSOLT, 1, 2)  
varStd = CalSet.getStandard(naSOLT_Thru,2,1) varStd2 = Cal
Set.getStandard(naSOLT_Thru,1,2) Cal Set.CloseCalSet( )  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT getStandard(tagNACalClass stdclass, long ReceivePort, long
SourcePort, VARIANT* pData)  
  
#### Interface

|  ICalSet

