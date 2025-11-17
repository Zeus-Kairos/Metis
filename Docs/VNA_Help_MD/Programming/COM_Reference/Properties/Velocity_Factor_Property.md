##### Write/Read

|

##### [About Port Extensions](../../../S3_Cals/Port_Extensions.md)  
  
---|---  
  
## VelocityFactor Property

* * *

#### Description

|  Sets the velocity factor to be used with Electrical Delay, Port Extensions,
and Time Domain marker distance calculations.  
---|---  
  
####  VB Syntax

|  app.VelocityFactor = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
value |  (double) - Velocity factor. Choose a number between: 0 and 10  
(.66 polyethylene dielectric; .7 PTFE dielectric)  
  
#### Return Type

|  Double  
  
#### Default

|  1  
  
#### Examples

|  app.VelocityFactor = .66 'Write  
RelVel = app.VelocityFactor 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_VelocityFactor(double *pVal)  
HRESULT put_VelocityFactor(double newVal)  
  
#### Interface

|  IApplication

