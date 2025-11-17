##### Write/Read

|

##### [About Port Extensions](../../../S3_Cals/Port_Extensions.md#PortDiag)  
  
---|---  
  
## PortLoss2 Property

* * *

#### Description

|  Sets and returns the Loss2 value for the specified port number. Note: This
command affects ALL measurements on the channel.  
---|---  
  
####  VB Syntax

|  fixture.PortLoss2(port) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
port |  (Integer) Port number to receive Loss value  
value |  (Double) Loss2 value in dB. Choose a value between -90 and 90.  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  fixture.PortLoss2(2) = .002 'Write  
value = fixture.PortLoss2(1) 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PortLoss2(short port double *pVal)  
HRESULT put_PortLoss2(short port double newVal)  
  
#### Interface

|  IFixturing

