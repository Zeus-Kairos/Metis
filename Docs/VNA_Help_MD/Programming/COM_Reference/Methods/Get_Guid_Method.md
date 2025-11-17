####  Read-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## GetGuid Method

* * *

#### Description

|  Returns a string containing the GUID identifying this Cal Set. Each Cal Set
is assigned a GUID (global unique ID). GUIDs are used to retrieve and select
Cal Sets on the VNA. Learn more about [reading and writing Cal Data using
COM.](../../Learning_about_COM/Read_and_Write_Calibration_Data_using_COM.htm)  
---|---  
  
#### VB Syntax

|  value = CalSet.GetGuid  
---|---  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (string) \- Variable to store the returned GUID  
CalSet |  (object) - A Cal Set object  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  guid = CalSet.GetGuid 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT GetGUID( BSTR* pGUIDString);  
  
#### Interface

|  ICalSet

