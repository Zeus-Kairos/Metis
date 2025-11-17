##### Read-only  
  
---  
  
## IDString Property

* * *

#### Description

|  Returns the ID of the analyzer, including the Model number, Serial Number,
and the Software revision number. Note: Beginning with Rev 6.01, this command
now returns the software revision with 6 digits instead of 4. For example,
A.06.01.02.  
---|---  
  
####  VB Syntax

|  value = app.IDString  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
value |  (string) - variable to contain the returned ID string  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  id = app.IDString  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT IDString(BSTR* IDString)  
  
#### Interface

|  IApplication

