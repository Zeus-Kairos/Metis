##### Read-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## ContentDescriptor Property

* * *

#### Description

|  Returns the Cal Types from the calset. [Learn more about Cal
Type](../../../S3_Cals/Cal_Sets.htm#context).  
---|---  
  
#### VB Syntax

|  value = calSet.ContentDescriptor  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calSet |  A [CalSet](../Objects/CalSet_Object.md) (object)  
  
#### Return Type

|  1-dimensional variant array  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Set app = CreateObject("AgilentPNA835x.Application") Set calset =
app.GetCalManager.CalSets.Item(2) desc = CalSet.ContentDescriptor For i = 0 to
UBound(desc) MsgBox (desc(i)) Next  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_ContentDescriptor (VARIANT* vals)  
  
#### Interface

|  ICalSet8  
  
* * *

