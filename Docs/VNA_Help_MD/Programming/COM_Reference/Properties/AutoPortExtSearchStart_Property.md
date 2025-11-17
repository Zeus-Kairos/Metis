##### Write/Read

|

##### [About Auto Port
Extensions](../../../S3_Cals/Port_Extensions.htm#AutoPortExtensions)  
  
---|---  
  
## AutoPortExtSearchStart Property

* * *

#### Description

|  Set the start frequency for custom user span. Only applies when
[fixture.AutoPortExtConfig](AutoPortExtConfig_Property.md) = 0 naAPEC_CSPN.
[Learn more about User Span.](../../../S3_Cals/Port_Extensions.md#Search)  
---|---  
  
####  VB Syntax

|  fixture.AutoPortExtSearchStart = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
value |  (Double ) User span start value. Must be within the frequency range of the active channel and less than the value set by [AutoPortExtSearchStop Property](AutoPortExtSearchStop_Property.md)  
  
#### Return Type

|  Double  
  
#### Default

|  Start frequency of the current active channel.  
  
#### Examples

|  fixture.AutoPortExtSearchStart = 1E9  
value = fixture.AutoPortExtSearchStart 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_AutoPortExtSearchStart(double *pdVal ); HRESULT
put_AutoPortExtSearchStart(double dVal);  
  
#### Interface

|  IFixturing2

