##### Write/Read

|

##### [About Auto Port
Extensions](../../../S3_Cals/Port_Extensions.htm#AutoPortExtensions)  
  
---|---  
  
## AutoPortExtLoss Property

* * *

#### Description

|  Specifies whether or not to include loss correction as part of automatic
port extension. [Learn more about Loss Compensation in port
extension.](../../../S3_Cals/Port_Extensions.htm#LossCompensation)  
---|---  
  
####  VB Syntax

|  fixture.AutoPortExtLoss = bool  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
bool |  True \- Includes Loss correction. False \- Does NOT include Loss correction.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  fixture.AutoPortExtLoss = True  
value = fixture.AutoPortExtLoss 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_AutoPortExtLoss(VARIANT_BOOL *pState); HRESULT
put_AutoPortExtLoss(VARIANT_BOOL bState);  
  
#### Interface

|  IFixturing2

