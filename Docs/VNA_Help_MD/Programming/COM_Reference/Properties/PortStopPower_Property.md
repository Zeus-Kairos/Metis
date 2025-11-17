##### Write/Read

|

##### [About Diff I/Q App](../../../Applications/Differential_IQ.md)  
  
---|---  
  
## PortStopPower Property

* * *

#### Description

|  Sets and reads the stop value of a power sweep. On the [Source
Configuration](../../../Applications/Differential_IQ.htm#SourceConfigurationDiag)
dialog under Power, this is the Stop Power setting.  
---|---  
  
####  VB Syntax

|  DIQ.PortStopPower (port) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
DIQ |  A [Differential I/Q](../Objects/DIQ_Object.md) (object)  
port |  (String) Source port name. Use [SourcePortNames](SourcePortNames_Property.md) to read a list of valid source ports.  
value |  (Double) Power sweep stop value in dBm. Choose start and stop value within a single attenuator range of the analyzer (generally about 30 dB).  
  
#### Return Type

|  Double  
  
#### Default

|  -5 dBm  
  
#### Examples

|  oDIQ.PortStopPower("port 2") = 0  
Value = oDIQ.PortStopPower("port 2") 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PortStopPower(BSTR port, double* PortStopPower); HRESULT
put_PortStopPower(BSTR port, double PortStopPower);  
  
#### Interface

|  IDIQ  
  
* * *

