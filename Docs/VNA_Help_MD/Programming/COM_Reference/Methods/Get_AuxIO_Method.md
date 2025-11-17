##### Read-only

|  
---|---  
  
## GetAuxIO Method

* * *

#### Description

|  This method returns the [IAuxIO](../Objects/HWauxIO_Object.md) interface.  
---|---  
  
####  VB Syntax

|  app.GetAuxIO  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
  
#### Return Type

|  IHWAuxIO  
  
#### Default

|  Not Applicable  
  
#### Example

|  Dim app As AgilentPNA835x.Application  
Dim aux As HWAuxIO  
Set aux = app.GetAuxIO  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT GetAuxIO (IHWAuxIO **pAux);  
  
#### Interface

|  IApplication

