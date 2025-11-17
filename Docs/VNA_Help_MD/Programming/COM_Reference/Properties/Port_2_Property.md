##### Write/Read

|

##### [About Port Extensions](../../../S3_Cals/Port_Extensions.md)  
  
---|---  
  
## Port2 Property Superseded

* * *

#### Description

|  This command is replaced by [PortDelay property.](PortDelay_Property.md)
Sets a Port Extension value for Port 2  
---|---  
  
####  VB Syntax

|  portExt.Port2 = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
portExt |  A Port Extension (object)  
value |  (double) - Port Extension value in seconds. Choose any number between -10 and 10  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  portExt.Port2 = 10e-6 'Write  
prt2 = portExt.Port2 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Port2(double *pVal)  
HRESULT put_Port2(double newVal)  
  
#### Interface

|  IPortExtension

