##### Write-only

|

##### [About Auto Port
Extensions](../../../S3_Cals/Port_Extensions.htm#AutoPortExtensions)  
  
---|---  
  
## AutoPortExtMeasure Method

* * *

#### Description

|  Measures either an OPEN or SHORT standard. When this command is sent, the
VNA acquires the measurement with which to set automatic port extensions.
[Learn more about choosing which standard to
measure.](../../../S3_Cals/Port_Extensions.htm#MeasStandard)  
---|---  
  
####  VB Syntax

|  fixture.AutoPortExtMeasure value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
value |  (Enum as NAAutoPortExtMeasure) 0 - naAPEM_OPEN - Measure OPEN 1 - naAPEM_SHORT - Measure SHORT  
  
#### Return Type

|  ENUM  
  
#### Default

|  Not Applicable  
  
#### Examples

|  fixture.AutoPortExtMeasure naAPEM_OPEN  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_AutoPortExtMeasure(tagNAAutoPortExtMeasure *pVal );  
  
#### Interface

|  IFixturing2

