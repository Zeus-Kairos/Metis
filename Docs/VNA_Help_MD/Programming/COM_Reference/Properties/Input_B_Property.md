##### Write/Read

|

##### [About Port Extensions](../../../S3_Cals/Port_Extensions.md)  
  
---|---  
  
## InputB Property - Obsolete

* * *

#### Description

|  This property has NO replacement and no longer works correctly. (Sept.
2004) Sets the Port Extension value for Receiver B  
---|---  
  
####  VB Syntax

|  portExt.InputB = value  
  
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

|  portExt.InputB = 10e-6 'Write  
inB = portExt.InputB 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_InputB(double *pVal)  
HRESULT put_InputB(double newVal)  
  
#### Interface

|  IPortExtension

