##### Write/Read

|

##### About Fixturing  
  
---|---  
  
## PortLossDC Property

* * *

#### Description

|  Sets and returns the Loss value at DC for the specified port number. [Learn
about Loss compensation
values.](../../../S3_Cals/Port_Extensions.htm#PortDiag) Note: This command
affects ALL measurements on the channel.  
---|---  
  
####  VB Syntax

|  fixture.PortLossDC(port) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
port |  (Integer) Port number to receive Loss value at DC.  
value |  (Double) Loss value in ohms. Choose a value between -90 and 90  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  fixture.PortLossDC(2) = .002 'Write  
value = fixture.PortLossDC(1) 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_PortLossDC(short port double *pVal)  
HRESULT put_PortLossDC(short port double newVal)  
  
#### Interface

|  IFixturing

