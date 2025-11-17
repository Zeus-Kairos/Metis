##### Write / Read

|

##### [About Port Extensions](../../../S3_Cals/Port_Extensions.md)  
  
---|---  
  
## PortWGCutoffFreqProperty

* * *

#### Description

|  Sets and returns the cuttoff (minimum) frequency of the added waveguide
fixture or transmission line.  
---|---  
  
####  VB Syntax

|  fixture.PortWGCutoffFreq(port)= value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) Object  
port |  (Integer) Port Number for which media type is being set.  
value |  (Double) Cutoff frequency in Hz. This value is ignored when [PortMedium Property](PortMedium_Property.md) is set to COAX for the same port.  
  
#### Return Type

|  Double  
  
#### Default

|  System Media Cutoff Frequency  
  
#### Examples

|  fixture.PortWGCutoffFreq(2)= 1e9 'Write value = fixture.PortWGCutoffFreq(2)
'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_PortWGCutoffFreq(short portNum, double *pVal); HRESULT
put_PortWGCutoffFreq(short portNum, double newVal);  
  
#### Interface

|  IFixturing4  
  
* * *

