##### Write-only

|

##### [About Auto Port
Extensions](../../../S3_Cals/Port_Extensions.htm#AutoPortExtensions)  
  
---|---  
  
## AutoPortExtReset Method

* * *

#### Description

|  Clears old port extension delay and loss data in preparation for acquiring
new data. Send this command prior to sending a new series of measurements
using [AutoPortExtMeasure Method](AutoPortExtMeasure_Method.md). If acquiring
both OPEN and SHORT standards, do not send this command between those
acquisitions.  
---|---  
  
####  VB Syntax

|  fixture.AutoPortExtReset  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  fixture.AutoPortExtReset  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT AutoPortExtReset();  
  
#### Interface

|  IFixturing2

