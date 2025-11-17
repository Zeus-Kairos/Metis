##### Write-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## DeleteCalSet Method

* * *

#### Description

|  Deletes a Cal Set from the set of available Cal Sets. This method
immediately updates the Cal Set file on the hard drive. If the Cal Set is
currently being used by a channel or does not exist, this request will be
denied and an error is returned. Using the [Cal Sets
collection](../Objects/CalSets_Collection.htm) is a convenient way to manage
Cal Sets.  
---|---  
  
####  VB Syntax

|  calMgr.DeleteCalSet (calset)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calMgr |  (object) - A [CalManager](../Objects/CalManager_Object.md) object  
calset |  (string) \- Cal Set to be deleted. Specify the Cal Set by GUID or Name. Use [EnumerateCalSets](EnumerateCalSets_Method.md) to list the available Cal Sets by name.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Example

|  Set pna=CreateObject("AgilentPNA835x.Application") Set cmgr =
pna.GetCalManager cmgr.DeleteCalSet ("MyCalSet")  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT DeleteCalSet( BSTR strCalset);  
  
#### Interface

|  ICalManager  
  
* * *

