##### Read-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## ChannelClients Property

* * *

#### Description

|  Returns the numbers of the channels using the calset.  
---|---  
  
#### VB Syntax

|  value = calSet.ChannelClients  
  
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
app.GetCalManager.CalSets.Item(2) arry = CalSet.ChannelClients For i = 0 to
UBound(arry) Msgbox (arry(i)) Next  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_ChannelClients (VARIANT* vals)  
  
#### Interface

|  ICalSet8  
  
* * *

