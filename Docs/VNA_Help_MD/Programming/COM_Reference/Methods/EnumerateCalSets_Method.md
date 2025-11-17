##### Read-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## EnumerateCalSets Method

* * *

#### Description

|  Returns an array of Cal Set names being stored on the PNA.  
---|---  
  
####  VB Syntax

|  value = calMgr.EnumerateCalSets  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (variant) \- Variable to store the returned Cal Set names  
calMgr |  (object) - A [CalManager](../Objects/CalManager_Object.md) object  
  
#### Return Type

|  VARIANT array  
  
#### Default

|  Not Applicable  
  
#### Example

|  Dim pna  
set pna=CreateObject("AgilentPNA835x.Application")  
  
Dim catalog  
catalog=pna.getcalmanager.EnumerateCalSets  
for i=lbound(catalog) to Ubound(catalog)  
wscript.echo catalog(i)  
next  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT EnumerateCalSets(VARIANT* names);  
  
#### Interface

|  ICalManager4

