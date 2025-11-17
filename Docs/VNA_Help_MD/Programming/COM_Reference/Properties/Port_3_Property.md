##### Write/Read

|

##### [About Port Extensions](../../../S3_Cals/Port_Extensions.md)  
  
---|---  
  
## Port3 Property Superseded

* * *

#### Description

|  This command is replaced by [PortDelay property.](PortDelay_Property.md)
Sets a Port Extension value for Port 3  
---|---  
  
####  VB Syntax

|  portExt.Port3 = value  
  
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

|  portExt.Port3 = 10e-6 'Write  
prt3 = portExt.Port3 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_Port3(double *pVal)  
HRESULT put_Port3(double newVal)  
  
#### Interface

|  IPortExtension

