##### Read-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## GetCalManager Method

* * *

#### Description

|  This method returns the [ICalManager](../Objects/CalManager_Object.md)
interface.  
---|---  
  
####  VB Syntax

|  app.GetCalManager( )  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
  
#### Return Type

|  ICalManager*  
  
#### Default

|  Not Applicable  
  
#### Example

|  dim app as AgilentPNA835x.Application  
dim mgr as CalManager  
set mgr = app.GetCalManager()  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT GetCalManager( ICalManager **mgr);  
  
#### Interface

|  IApplication  
  
* * *

