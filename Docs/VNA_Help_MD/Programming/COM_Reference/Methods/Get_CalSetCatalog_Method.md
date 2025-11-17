##### Read-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## GetCalSetCatalog Method - Superseded

* * *

#### Description

|  This method is replaced with
[EnumerateCalSets](EnumerateCalSets_Method.md) Returns a string containing a
list of comma-separated GUIDs in the following format:
{FD6F863E-9719-11d5-8D6C-00108334AE96},
{1B03B2CE-971A-11d5-8D6C-00108334AE96}, {2B893E7A-971A-11d5-8D6C-00108334AE96}  
---|---  
  
####  VB Syntax

|  value = calMgr.GetCalSetCatalog  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (string) \- Variable to store the returned GUID list  
calMgr |  (object) - A CalManager object  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Example

|  value = calMgr.GetCalSetCatalog  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT GetCalSetCatalog( BSTR);  
  
#### Interface

|  ICalManager  
  
* * *

