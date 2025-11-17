##### Read-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## Get CalSetByGUID Method

* * *

#### Description

|  Requests a Cal Set by GUID. Returns an ICal Set interface.  
---|---  
  
####  VB Syntax

|  calMgr.GetCalSetByGUID (GUID)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calMgr |  (object) - A CalManager object  
GUID |  (string) \- GUID of the Cal Set being requested.  
  
#### Return Type

|  Interface object  
  
#### Default

|  Not Applicable  
  
#### Example

|  calMgr.GetCalSetByGUID (2B893E7A-971A-11d5-8D6C-00108334AE96)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT GetCalSetByGUID( BSTR* strGUID, ICal Set* pCalSet);  
  
#### Interface

|  ICalManager

