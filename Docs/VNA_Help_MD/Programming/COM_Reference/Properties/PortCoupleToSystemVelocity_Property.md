##### Write / Read

|

##### [About Port Extensions](../../../S3_Cals/Port_Extensions.md)  
  
---|---  
  
## PortCoupleToSystemVelocity Property

* * *

#### Description

|  Sets and returns the state of coupling with the system Velocity Factor.  
---|---  
  
####  VB Syntax

|  fixture.PortCoupleToSystemVelocity (port)= value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) Object  
port |  (Integer) Port Number that will receive the coupling change.  
value |  (Boolean) Coupling state. Choose from:

  * True \- Velocity Factor is coupled with the system setting.
  * False \- Velocity Factor is NOT coupled with the system setting.

  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Examples

|  fixture.PortCoupleToSystemVelocity(2)= True  
bool = fixture.PortCoupleToSystemVelocity(1)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_PortCoupleToSystemVelocity(short portNum, VARIANT_BOOL *pVal);
HRESULT put_PortCoupleToSystemVelocity(short portNum, VARIANT_BOOL newVal);  
  
#### Interface

|  IFixturing4  
  
* * *

