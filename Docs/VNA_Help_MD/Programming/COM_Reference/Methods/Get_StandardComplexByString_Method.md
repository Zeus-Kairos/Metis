##### Read-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## GetStandardComplexByString Method

* * *

#### Description

|  Returns standard acquisition data from the Cal Set. Learn more about
[Reading and Writing Cal
Data](../../Learning_about_COM/Read_and_Write_Calibration_Data_using_COM.htm)
See examples of
[Reading](../../COM_Example_Programs/COM_Reading_CalSet_Examples.md) and
[Writing](../../COM_Example_Programs/Writing_Cal_Set_Data_using_COM.md) Cal
Set Data  
---|---  
  
####  VB Syntax

|  ICalData3.GetStandardComplexByString stdName, lnumPoints, real(0), imag(0)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
ICalData3 |  An [ICalData3](../Objects/CalSet_Object.md#ICalData3) pointer to a [CalSet](../Objects/CalSet_Object.md) (Object)  
stdName |  (String) The string used to identify a particular standard in the Cal Set. An example string requesting the data for the Load standard in a full 2 port cal might be "S11C(3,3)".  
lnumPoints |  (Long) An In/Out parameter. On the way in, you specify the max number of values being requested. On the way out, the VNA returns number of values actually returned.  
real |  (Single) The real component of the complex data.  
imag |  (Single) The imaginary component of the complex data.   
  
#### Return Value

|  Single  
  
#### Default

|  Not Applicable  
  
#### Examples

|  [See example](../../COM_Example_Programs/COM_Reading_CalSet_Examples.md)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT GetStandardComplexByString( BSTR bufferName, long* lnumPoints,
float* real, float* imag);  
  
#### Interface

|  ICalData3

