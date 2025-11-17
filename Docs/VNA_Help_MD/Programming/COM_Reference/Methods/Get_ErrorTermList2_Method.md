##### Read-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## GetErrorTermList2 Method

* * *

#### Description

|  Returns a list of error terms found in the Cal Set containing the specified
text filter. Learn more about [Reading and Writing Cal
Data](../../Learning_about_COM/Read_and_Write_Calibration_Data_using_COM.htm)
See examples of
[Reading](../../COM_Example_Programs/COM_Reading_CalSet_Examples.md) and
[Writing](../../COM_Example_Programs/Writing_Cal_Set_Data_using_COM.md) Cal
Set Data  
---|---  
  
####  VB Syntax

|  list = CalSet.GetErrorTermList2(setNumber, filter)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
list |  (Variant) Variant containing a string array of error term names.  
CalSet |  (object) - A [CalSet](../Objects/CalSet_Object.md) object  
setNumber |  (Long) There can be more than one set of error terms in a Cal Set.

  * setNumber 0 contains the original set of error terms for a Cal Set.
  * setNumbers > 0 contain Interpolated error terms. Interpolated error terms are generated when interpolation is required and destroyed when no longer used. [Learn about Interpolation](../../../S3_Cals/Quest_Cal.md).
  * To determine the setNumber in use by a channel, see [GetCalSetUsageInfo](Get_CalSetUsageInfo_Method.md)

  
filter |  (String) This string is used as a filter so that only the error term names of interest are returned. If the filter is empty, all terms are returned. The string is case-insensitive. Here are some examples:

  *  (empty string)- returns all error term names for the identified Cal Set and setNumber
  * TRACKING - returns all error term names that include the substring tracking, such as ResponseTracking(S21) and TransmissionTracking(S21)
  * (s21) - returns all error term names that end with (S21)

  
  
#### Return Type

|  Variant  
  
#### Default

|  Not Applicable  
  
#### Examples

|  [See an
Example](../../COM_Example_Programs/COM_Reading_CalSet_Examples.htm)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT GetErrorTermList2 (long SetNumber, BSTR filter, VARIANT* list)  
  
#### Interface

|  ICalSet2

