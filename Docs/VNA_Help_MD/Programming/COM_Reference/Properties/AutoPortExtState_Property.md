##### Write/Read

|

##### [About Auto Port
Extensions](../../../S3_Cals/Port_Extensions.htm#AutoPortExtensions)  
  
---|---  
  
## AutoPortExtState Property

* * *

#### Description

|  Enables and disables automatic port extensions on the specified port. All
enabled ports will have their reference plane automatically adjusted after
performing Automatic Port Extension.  
---|---  
  
####  VB Syntax

|  fixture.AutoPortExtState (port) = bool  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
port |  (Integer) Port number to enable or disable.  
bool |  (Boolean) True \- Enables Auto Port Extensions False \- Disables Auto Port Extensions  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  fixture.AutoPortExtState(1) = True  
value = fixture.AutoPortExtState(2) 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_AutoPortExtState(short port, VARIANT_BOOL *pState ); HRESULT
put_AutoPortExtState(short port, VARIANT_BOOL bVal);  
  
#### Interface

|  IFixturing2

