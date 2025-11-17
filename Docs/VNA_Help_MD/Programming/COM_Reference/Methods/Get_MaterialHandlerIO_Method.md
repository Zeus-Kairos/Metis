##### Read-only

|

##### [About the MaterialHandler connector](../../HandlerIO_Connector.md)  
  
---|---  
  
## Get MaterialHandlerIO Method

* * *

#### Description

|  This method returns the
[MaterialHandlerIO](../Objects/HWMaterialHandlerIO_Object.md) interface.  
---|---  
  
####  VB Syntax

|  app.GetMaterialHandlerIO  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
  
#### Return Type

|  IHWMaterialHandlerIO  
  
#### Default

|  Not Applicable  
  
#### Example

|  Dim app As AgilentPNA835x.Application  
Dim hand As HWMaterialHandlerIO  
Set hand = app.GetMaterialHandlerIO  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT GetMaterialHandlerIO (IHWMaterialHandlerIO **phand);  
  
#### Interface

|  IApplication

