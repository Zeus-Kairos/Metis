##### Write/Read

|

##### [About Auto Port
Extensions](../../../S3_Cals/Port_Extensions.htm#AutoPortExtensions)  
  
---|---  
  
## AutoPortExtDCOffset Property

* * *

#### Description

|  Specifies whether or not to include DC Offset as part of automatic port
extension. Learn more about [Automatic DC
Offset](../../../S3_Cals/Port_Extensions.htm#PlusDCOffset). Only allowed when
[AutoPortExtLoss Property](AutoPortExtLoss_Property.md) is set to ON.  
---|---  
  
####  VB Syntax

|  fixture.AutoPortExtDCOffset = bool  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
bool |  True \- Includes DC Offset correction. False \- Does NOT include DC Offset correction.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  fixture.AutoPortExtDCOffset = True  
value = fixture.AutoPortExtDCOffset 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_AutoPortExtDCOffset(VARIANT_BOOL *pState); HRESULT
put_AutoPortExtDCOffset(VARIANT_BOOL bState);  
  
#### Interface

|  IFixturing2

