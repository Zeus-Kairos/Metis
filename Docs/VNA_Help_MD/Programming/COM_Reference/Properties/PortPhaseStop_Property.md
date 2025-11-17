##### Write/Read

|

##### [About Diff I/Q App](../../../Applications/Differential_IQ.md)  
  
---|---  
  
## PortPhaseStop Property

* * *

#### Description

|  Sets and reads the Stop value for a phase sweep. On the [Source
Configuration](../../../Applications/Differential_IQ.htm#SourceConfigurationDiag)
dialog under Phase, this is the Stop Phase setting.  
---|---  
  
####  VB Syntax

|  DIQ.PortPhaseStop (port) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
DIQ |  A [Differential I/Q](../Objects/DIQ_Object.md) (object)  
port |  (String) Source port name. Use [SourcePortNames](SourcePortNames_Property.md) to read a list of valid source ports.  
value |  (Double) Stop phase sweep value in degrees. Choose any positive or negative value.  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  oDIQ.PortPhaseStop("port 2") = -90  
Value = oDIQ.PortPhaseStop("port 2") 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PortPhaseStop(BSTR port, double* PortPhaseStop); HRESULT
put_PortPhaseStop(BSTR port, double PortPhaseStop);  
  
#### Interface

|  IDIQ  
  
* * *

