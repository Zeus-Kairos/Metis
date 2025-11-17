##### Write-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## PutStandardByString

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

|  PutStandardByString(stdName, vdata)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
stdName |  (String) The string used to identify a particular standard in the Cal Set. An example string requesting the data for the Load standard in a full 2 port cal might be "S11C(3,3)".  
vdata |  (Variant) The variant containing a safearray of variants. This data is usually two dimensional. Note: The vardata array is a safearray of variants wrapped in a variant. This structure is compatible with scripting clients who can only use variants. For alternative methods that used typed arrays, see ICalData3.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  [See an
Example](../../COM_Example_Programs/Writing_Cal_Set_Data_using_COM.htm)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT PutStandardByString( BSTR bufferName, VARIANT vardata);  
  
#### Interface

|  ICalSet2

