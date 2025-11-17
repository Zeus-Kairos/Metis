##### Read-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## Properties Property

* * *

#### Description

|  Returns the properties of the calset. [See the Calset Properties
page.](../../../S3_Cals/Cal_Sets.htm#CalSetProps)  
---|---  
  
#### VB Syntax

|  value = calSet.Properties  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calSet |  A [CalSet](../Objects/CalSet_Object.md) (object)  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Set app = CreateObject("AgilentPNA835x.Application") Set calset =
app.GetCalManager.CalSets.Item(2) props = CalSet.Properties Msgbox (props)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_Properties (BSTR* vals);  
  
#### Interface

|  ICalSet8  
  
* * *

