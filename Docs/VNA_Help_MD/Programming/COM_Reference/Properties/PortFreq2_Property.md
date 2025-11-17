##### Write/Read

|

##### [About Port Extensions](../../../S3_Cals/Port_Extensions.md#PortDiag)  
  
---|---  
  
## PortFreq2 Property

* * *

#### Description

|  Sets and returns Frequency2 value for the specified port number. Note: This
command affects ALL measurements on the channel.  
---|---  
  
####  VB Syntax

|  fixture.PortFreq2(port) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
port |  (Integer) Port number to receive extrapolated loss.  
value |  (Double) Frequency2 value. Choose a frequency within the frequency span of the PNA.  
  
#### Return Type

|  Double  
  
#### Default

|  1 GHz  
  
#### Examples

|  fixture.PortFreq2(2) = 10E9 'Write  
value = fixture.PortFreq2(1) 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PortFreq2(short port double *pVal)  
HRESULT put_PortFreq2(short port double newVal)  
  
#### Interface

|  IFixturing

