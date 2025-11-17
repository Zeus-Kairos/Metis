##### Write / Read

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## Name Property

* * *

#### Description

|  Sets or returns the Name of the Cal Set.  
---|---  
  
#### VB Syntax

|  CalSet.Name = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
CalSet |  (object) - A [Cal Set](../Objects/CalSet_Object.md) object  
value |  (string) \- Name of the Cal Set.  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim pna  
set pna=CreateObject("AgilentPNA835x.Application")  
  
Dim calsets  
set calsets=pna.getcalmanager.calsets  
  
Dim c  
for each c in calsets  
wscript.echo c.name  
'Changes the name of CalSet_1  
if c.name="CalSet_1" then c.name="New"  
next  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Name(BSTR *name) HRESULT put_Name(BSTR name);  
  
#### Interface

|  ICalSet4

