##### Read-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## GetStandardList2 Method

* * *

#### Description

|  Returns a list of standards names found in the Cal Set object for the
specified text filter. Note: The Standards data container in the calset is
intended for internal use only. External access is provided for use in
diagnosing calibration problems. Users should not form any expectations as to
the presence of the data or the naming conventions used.  
---|---  
  
####  VB Syntax

|  list = calset.GetStandardList2(standard filter)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calset |  (object) - A [CalSet](../Objects/CalSet_Object.md) object  
list |  (Variant) Variant containing a string array of standards for the specified filter.  
standard filter |  (String) This string is used as a filter so that only the standards of interest are returned. If the filter is empty, all standards are returned. The string is case-insensitive. Here are some examples:

  *  (empty string) - returns all standard names for the identified Cal Set
  * THR - returns all standard names that include the substring thr, such as Thru(1,1) and Thru(1,2), etc.
  * (1,2) - returns all standards that contain (1,2), such as Isolation(1,2) and Thru(1,2).

  
  
#### Return Type

|  Variant  
  
#### Default

|  Not Applicable  
  
#### Examples

|  [See an
example](../../COM_Example_Programs/COM_Reading_CalSet_Examples.htm)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT GetStandardList2 (BSTR filter, VARIANT* list)  
  
#### Interface

|  ICalSet2

