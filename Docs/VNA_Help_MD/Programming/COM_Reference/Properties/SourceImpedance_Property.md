##### Write/Read

|

##### [About Ext Pulse
Gens](../../../System/Configure_an_External_Pulse_Generator.htm)  
  
---|---  
  
## SourceImpedance Property

* * *

#### Description

|  Sets and returns the source impedance of the pulse generator.  
---|---  
  
####  VB Syntax

|  extPulseGen.SourceImpedance = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
extPulseGen |  An [ExternalPulseGenerator](../Objects/ExternalPulseGenerator_Object.md) (object)  
value |  (Double) Pulse generator source impedance.  
  
#### Return Type

|  Double  
  
#### Default

|  50  
  
#### Examples

|  extPulseGen.SourceImpedance = 50 'Write  
srcImp = extPulseGen.SourceImpedance 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SourceImpedance (double *pValue) HRESULT put_SourceImpedance
(double newVal)  
  
#### Interface

|  IExternalPulseGenerator  
  
* * *

