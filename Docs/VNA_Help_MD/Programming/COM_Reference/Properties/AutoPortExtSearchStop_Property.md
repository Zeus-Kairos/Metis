##### Write/Read

|

##### [About Auto Port
Extensions](../../../S3_Cals/Port_Extensions.htm#AutoPortExtensions)  
  
---|---  
  
## AutoPortExtSearchStop Property

* * *

#### Description

|  Set the stop frequency for custom user span. Only applies when
[fixture.AutoPortExtConfig](AutoPortExtConfig_Property.md) = 0 naAPEC_CSPN.
[Learn more about User Span.](../../../S3_Cals/Port_Extensions.md#Search)
Only applies when [fixture.AutoPortExtConfig](AutoPortExtConfig_Property.md)
= 0 naAPEC_CSPN  
---|---  
  
####  VB Syntax

|  fixture.AutoPortExtSearchStop = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
value |  (Double ) User span stop value. Must be within the frequency range of the active channel and greater than the value set by [AutoPortExtSearchStart Property](AutoPortExtSearchStart_Property.md)  
  
#### Return Type

|  Double  
  
#### Default

|  Stop frequency of the current active channel.  
  
#### Examples

|  fixture.AutoPortExtSearchStop = 1E9  
value = fixture.AutoPortExtSearchStop 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_AutoPortExtSearchStop(double *pdVal ); HRESULT
put_AutoPortExtSearchStop(double dVal);  
  
#### Interface

|  IFixturing2

