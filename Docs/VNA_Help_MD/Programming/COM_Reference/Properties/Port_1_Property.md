##### Write/Read

|

##### [About Port Extensions](../../../S3_Cals/Port_Extensions.md)  
  
---|---  
  
## Port1 Property Superseded

* * *

#### Description

|  This command is replaced by [PortDelay property.](PortDelay_Property.md)
Sets a Port Extension value for Port 1  
---|---  
  
####  VB Syntax

|  portExt.Port1 = value  
  
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

|  portExt.Port1 = 10e-6 'Write  
prt1 = portExt.Port1 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Port1(double *pVal)  
HRESULT put_Port1(double newVal)  
  
#### Interface

|  IPortExtension

