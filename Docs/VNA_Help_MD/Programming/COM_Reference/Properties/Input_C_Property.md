##### Write/Read

|

##### [About Port Extensions](../../../S3_Cals/Port_Extensions.md)  
  
---|---  
  
## InputC Property Obsolete

* * *

#### Description

|  This property has NO replacement and no longer works correctly. (Sept.
2004) Sets the Port Extension value for Receiver C  
---|---  
  
####  VB Syntax

|  portExt.InputC = value  
  
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

|  portExt.InputC = 10e-6 'Write  
inC = portExt.InputC 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_InputC(double *pVal)  
HRESULT put_InputC(double newVal)  
  
#### Interface

|  IPortExtension

