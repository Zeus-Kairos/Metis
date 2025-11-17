##### Write / Read

|

##### [About Port Extensions](../../../S3_Cals/Port_Extensions.md)  
  
---|---  
  
## PortDistance Property

* * *

#### Description

|  Sets and returns the port extension delay in physical length (distance).  
---|---  
  
####  VB Syntax

|  fixture.PortDistance (port)= value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) Object  
port |  (Integer) Port Number that will receive the delay setting.  
value |  (Double) Physical length in distance. First specify units with [PortDistanceUnit](PortDistanceUnit_Property.md).  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  fixture.PortDistance(2)= .01 'Write value = fixture.PortDistance(2) 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_PortDistance(short portNum, double *pVal); HRESULT
put_PortDistance(short portNum, double newVal);  
  
#### Interface

|  IFixturing4  
  
* * *

