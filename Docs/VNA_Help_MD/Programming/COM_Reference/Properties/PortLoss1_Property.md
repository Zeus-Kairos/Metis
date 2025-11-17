##### Write/Read

|

##### [About Port Extensions](../../../S3_Cals/Port_Extensions.md#PortDiag)  
  
---|---  
  
## PortLoss1 Property

* * *

#### Description

|  Sets and returns the Loss1 value for the specified port number. Note: This
command affects ALL measurements on the channel.  
---|---  
  
####  VB Syntax

|  fixture.PortLoss1(port) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
port |  (Integer) Port number to receive Loss value  
value |  (Double) Loss1 value in dB. Choose a value between -90 and 90.  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  fixture.PortLoss1(2) = .002 'Write  
value = fixture.PortLoss1(1) 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_PortLoss1(short port double *pVal)  
HRESULT put_PortLoss1(short port double newVal)  
  
#### Interface

|  IFixturing

