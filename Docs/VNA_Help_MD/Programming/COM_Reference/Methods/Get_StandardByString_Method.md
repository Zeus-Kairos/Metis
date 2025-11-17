##### Read-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## GetStandardByString Method

* * *

#### Description

|  Returns standard acquisition data from the Cal Set. The returned data is
complex pairs. Learn more about [Reading and Writing Cal
Data](../../Learning_about_COM/Read_and_Write_Calibration_Data_using_COM.htm)
See examples of
[Reading](../../COM_Example_Programs/COM_Reading_CalSet_Examples.md) and
[Writing](../../COM_Example_Programs/Writing_Cal_Set_Data_using_COM.md) Cal
Set Data  
---|---  
  
####  VB Syntax

|  data = calSet.GetStandardByString(stdName)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
data |  (Variant) Two-dimensional safe array to store the returned data. Memory for the returned Variant is allocated by the VNA and must be released by client. Note: See also [Get StandardComplexByString](Get_StandardComplexByString_Method.md) on the ICalData2 interface to avoid using the variant data type.  
calSet |  A [CalSet](../Objects/CalSet_Object.md) (Object)  
stdName |  (String) The string used to identify a particular standard in the Cal Set. An example string requesting the data for the Load standard in a full 2 port cal might be "S11C(3,3)".  
  
#### Return Type

|  Variant  
  
#### Default

|  Not Applicable  
  
#### Examples

|  See an
[example](../../COM_Example_Programs/COM_Reading_CalSet_Examples.md)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT GetStandardByString( BSTR bufferName, VARIANT* pdata)  
  
#### Interface

|  ICalSet2

