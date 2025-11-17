##### Write/Read

|

##### [About Port Extensions](../../../S3_Cals/Port_Extensions.md#PortDiag)  
  
---|---  
  
## PortFreq1 Property

* * *

#### Description

|  Sets and returns Frequency1 value for the specified port number. Note: This
command affects ALL measurements on the channel.  
---|---  
  
####  VB Syntax

|  fixture.PortFreq1(port) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
port |  (Integer) Port number to receive extrapolated loss.  
value |  (Double) Frequency1 value. Choose a frequency within the frequency span of the VNA.  
  
#### Return Type

|  Double  
  
#### Default

|  1 GHz  
  
#### Examples

|  fixture.PortFreq1(2) = naFix2PD_USER 'Write  
value = fixture.PortFreq1(1) 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_PortFreq1(short port double *pVal)  
HRESULT put_PortFreq1(short port double newVal)  
  
#### Interface

|  IFixturing

