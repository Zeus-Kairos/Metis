##### Write/Read

|

##### [About Port Extensions](../../../S3_Cals/Port_Extensions.md)  
  
---|---  
  
## PortVelocityFactor Property

* * *

#### Description

|  Sets and returns the Port Extensions Velocity Factor value for the
specified port number. Note: This command affects ALL measurements on the
channel.  
---|---  
  
####  VB Syntax

|  fixture.PortVelocityFactor(port) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
port |  (Integer) Port number to receive velocity factor value.  
value |  (Double) Velocity Factor value. Choose a number between: 0 and 10 (.66 polyethylene dielectric; .7 PTFE dielectric)  
  
#### Return Type

|  Double  
  
#### Default

|  1  
  
#### Examples

|  fixture.PortVelocityFactor(2) = .6 'Write  
value = fixture.PortVelocityFactor(1) 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_PortVelocityFactor(short port double *pVal)  
HRESULT put_PortVelocityFactor(short port double newVal)  
  
#### Interface

|  IFixturing4  
  
* * *

