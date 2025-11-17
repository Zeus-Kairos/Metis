##### Write/Read

|

##### [About Auto Port
Extensions](../../../S3_Cals/Port_Extensions.htm#AutoPortExtensions)  
  
---|---  
  
## AutoPortExtConfig Property

* * *

#### Description

|  Sets the frequency span that is used to calculate Automatic Port Extension.
[Learn more about calculating Automatic Port
Extension.](../../../S3_Cals/Port_Extensions.htm#Search)  
---|---  
  
####  VB Syntax

|  fixture.AutoPortExtConfig = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
value |  (ENUM as NAAutoPortExtConfig) 0 naAPEC_CSPN \- Use current span. 1 naAPEC_AMKR \- Use active marker frequency. 2 naAPEC_USPN \- Use custom user span. Use [AutoPortExtSearchStart Property](AutoPortExtSearchStart_Property.md) and [AutoPortExtSearchStop Property](AutoPortExtSearchStop_Property.md) to specify start and stop frequency.  
  
#### Return Type

|  ENUM  
  
#### Default

|  0 naAPEC_CSPN  
  
#### Examples

|  fixture.AutoPortExtConfig = naAPEC_AMKR  
value = fixture.AutoPortExtConfig 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_AutoPortExtConfig(tagNAAutoPortExtConfig *pVal ); HRESULT
put_AutoPortExtConfig(tagNAAutoPortExtConfig Val );  
  
#### Interface

|  IFixturing2

