##### Write/Read

|

##### [About Diff I/Q App](../../../Applications/Differential_IQ.md)  
  
---|---  
  
## PortAttenuator Property

* * *

#### Description

|  Sets and reads the amount of source attenuation. Sending this command will
set [AutoRangeState Property](AutoRangeState_Property.md) False. On the
[Source
Configuration](../../../Applications/Differential_IQ.htm#SourceConfigurationDiag)
dialog under Power, this is the Source Attenuation setting.  
---|---  
  
####  VB Syntax

|  DIQ.PortAttenuator (port) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
DIQ |  A [Differential I/Q](../Objects/DIQ_Object.md) (object)  
port |  (String) Source port name. Use [SourcePortNames](SourcePortNames_Property.md) to read a list of valid source ports.  
value |  (Double) Source Attenuation value. Choose from 0 to the maximum amount of source attenuation in the correct step size. Rounding will occur when the selected value can not be achieved. [See attenuators for all VNA models](../../../Support/Configurations.md).  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  oDIQ.PortAttenuator("port 2") = 0  
Value = oDIQ.PortAttenuator("port 2") 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PortAttenuator(BSTR port, double* PortAttenuator); HRESULT
put_PortAttenuator(BSTR port, double PortAttenuator);  
  
#### Interface

|  IDIQ  
  
* * *

