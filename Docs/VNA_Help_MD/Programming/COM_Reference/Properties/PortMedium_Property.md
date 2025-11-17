##### Write / Read

|

##### [About Port Extensions](../../../S3_Cals/Port_Extensions.md)  
  
---|---  
  
## PortMedium Property

* * *

#### Description

|  Sets and returns the media type of the added fixture or transmission line.  
---|---  
  
####  VB Syntax

|  fixture.PortMedium (port)= value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) Object  
port |  (Integer) Port Number for which media type is being set.  
value |  (enum NACalStandardMedium) - Medium of the transmission line of the standard. Choose from: 0 - naCoax \- Coaxial Cable 1 - naWaveGuide - Waveguide  
  
#### Return Type

|  Enum  
  
#### Default

|  0 - naCoax  
  
#### Examples

|  fixture.PortMedium(2)= naCoax 'Write value = fixture.PortMedium(2) 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_PortMedium(short portNum, tagNACalStandardMedium* pVal);
HRESULT put_PortMedium(short portNum, tagNACalStandardMedium newVal);  
  
#### Interface

|  IFixturing4  
  
* * *

