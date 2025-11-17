##### Write-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## PutErrorTermComplexByString Method

* * *

#### Description

|  Puts error term data into the Cal Set. Learn more about [Reading and
Writing Cal
Data](../../Learning_about_COM/Read_and_Write_Calibration_Data_using_COM.htm)
See examples of
[Reading](../../COM_Example_Programs/COM_Reading_CalSet_Examples.md) and
[Writing](../../COM_Example_Programs/Writing_Cal_Set_Data_using_COM.md) Cal
Set Data  
---|---  
  
####  VB Syntax

|  ICalData3.PutErrorTermComplexByString errorName, lnumPoints, real(0),
imag(0)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
ICalData3 |  An [ICalData3](../Objects/CalSet_Object.md#ICalData3) pointer to a Cal Set object.  
errorName |  (String) The string name used to identify a particular error term in the Cal Set. An example string for port 3 directivity in a full 2 port cal might be "Directivity(3,3)". To determine the string names of error terms, see [GetErrorTermList2](Get_ErrorTermList2_Method.md).  
lnumPoints |  (Long) The number of data points in the real and imaginary arrays.  
real |  (Single) The real component of the complex data.  
imag |  (Single) The imaginary component of the complex data. Note: The size of the real and imaginary arrays should be the same.  
  
#### Return Value

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  [See
example](../../COM_Example_Programs/Writing_Cal_Set_Data_using_COM.htm)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT PutErrorTermComplexByString( BSTR bufferName, long lnumPoints,
float* real, float* imag);  
  
#### Interface

|  ICalData3

