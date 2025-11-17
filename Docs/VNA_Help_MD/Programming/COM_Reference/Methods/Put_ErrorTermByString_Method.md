##### Write-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## PutErrorTermByString Method

* * *

#### Description

| Puts error term data into the Cal Set. If this command is being used to
modify a calset that is currently in use by the channel, you must send the
following commands to see the effects of the change: Calset::Save
Channel::ErrorCorrection = false Channel::ErrorCorrection = true Learn more
about [Reading and Writing Cal
Data](../../Learning_about_COM/Read_and_Write_Calibration_Data_using_COM.htm)
See examples of
[Reading](../../COM_Example_Programs/COM_Reading_CalSet_Examples.md) and
[Writing](../../COM_Example_Programs/Writing_Cal_Set_Data_using_COM.md) Cal
Set Data  
---|---  
  
####  VB Syntax

| calSet.PutErrorTermByString(errorName, vdata)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calSet | (Object) A [CalSet](../Objects/CalSet_Object.md) Object  
errorName | (String) The string name used to identify a particular error term in the Cal Set. An example string for port 3 directivity in a full 2 port cal might be "Directivity(3,3)". To determine the string names of error terms, see [GetErrorTermList2](Get_ErrorTermList2_Method.md).  
vdata | (Variant) This data array is usually two dimensional. Each element is a type single. The two elements represent the real and imaginary parts of a complex pair. Note: This structure is compatible with scripting clients who can only use variants. For alternative methods that use typed arrays, see [ICalData3](../Objects/Calibrator_Object.md#ICalData).  
  
#### Return Type

| Not Applicable  
  
#### Default

| Not Applicable  
  
#### Examples

| [See an
Example](../../COM_Example_Programs/Writing_Cal_Set_Data_using_COM.htm)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

| HRESULT PutErrorTermByString(BSTR errorName, VARIANT vdata)  
  
#### Interface

| ICalSet2

