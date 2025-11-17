##### Write/Read

|

##### [About Diff I/Q App](../../../Applications/Differential_IQ.md)  
  
---|---  
  
## PortPhaseStart Property

* * *

#### Description

|  Sets and reads the start value for a phase sweep. On the [Source
Configuration](../../../Applications/Differential_IQ.htm#SourceConfigurationDiag)
dialog under Phase, this is the Start Phase setting.  
---|---  
  
####  VB Syntax

|  DIQ.PortPhaseStart (port) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
DIQ |  A [Differential I/Q](../Objects/DIQ_Object.md) (object)  
port |  (String) Source port name. Use [SourcePortNames](SourcePortNames_Property.md) to read a list of valid source ports.  
value |  (Double) Start phase sweep value in degrees. Choose any positive or negative value.  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  oDIQ.PortPhaseStart("port 2") = -90  
Value = oDIQ.PortPhaseStart("port 2") 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PortPhaseStart(BSTR port, double* PortPhaseStart); HRESULT
put_PortPhaseStart(BSTR port, double PortPhaseStart);  
  
#### Interface

|  IDIQ  
  
* * *

