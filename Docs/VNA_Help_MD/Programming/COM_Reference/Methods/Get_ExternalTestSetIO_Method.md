##### Read-only

|

##### [About the External TestSet connector](../../TestSetIO_Connector.md)  
  
---|---  
  
## Get ExternalTestSetIO Method

* * *

#### Description

|  This method returns the
[IExternalTestSetIO](../Objects/HWExternalTestSetIO_Object.md) interface.  
---|---  
  
####  VB Syntax

|  app.GetExternalTestSetIO  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
  
#### Return Type

|  IHWExternalTestSetIO  
  
#### Default

|  Not Applicable  
  
#### Example

|  Dim app As AgilentPNA835x.Application  
Dim ets As HWExternalTestSetIO  
Set ets = app.GetExternalTestSetIO  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT GetExternalTestSetIO (IHWExternalTestSetIO **ptestset);  
  
#### Interface

|  IApplication

