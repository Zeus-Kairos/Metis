##### Write-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## PutStandardComplexByString

* * *

#### Description

|  Puts standard acquisition data into the Cal Set. Learn more about [Reading
and Writing Cal
Data](../../Learning_about_COM/Read_and_Write_Calibration_Data_using_COM.htm)
See examples of
[Reading](../../COM_Example_Programs/COM_Reading_CalSet_Examples.md) and
[Writing](../../COM_Example_Programs/Writing_Cal_Set_Data_using_COM.md) Cal
Set Data.  
---|---  
  
####  VB Syntax

|  ICalData3.PutStandardComplexByString(stdName, lnumPoints , real(o) ,
imag(0))  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
ICalData3 |  An [ICalData3](../Objects/CalSet_Object.md#ICalData3) pointer to a Cal Set object.  
stdName |  (String) The string used to identify a particular standard in the Cal Set. An example string requesting the data for the Load standard in a full 2 port cal might be "S11C(3,3)".  
lnumpoints |  (long) - The number of data points in the real and imaginary arrays.  
real |  (Single) The real component of the complex data.  
imag |  (Single) The imaginary component of the complex data.  
  
#### Return Value

|  Single  
  
#### Default

|  Not Applicable  
  
#### Examples

|  [See an
Example](../../COM_Example_Programs/Writing_Cal_Set_Data_using_COM.htm)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT PutStandardComplexByString( BSTR bufferName, long lnumPoints,
float* real, float* imag);  
  
#### Interface

|  ICalData3

