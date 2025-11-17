##### Write/Read

|

##### [About Ext Pulse
Gens](../../../System/Configure_an_External_Pulse_Generator.htm)  
  
---|---  
  
## HighAmplitude Property

* * *

#### Description

|  Sets and returns the High amplitude (voltage) of the pulse generator.  
---|---  
  
####  VB Syntax

|  extPulseGen.HighAmplitude = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
extPulseGen |  An [ExternalPulseGenerator](../Objects/ExternalPulseGenerator_Object.md) (object)  
value |  (Double) Pulse Generator high amplitude voltage.  
  
#### Return Type

|  Double  
  
#### Default

|  5  
  
#### Examples

|  extPulseGen.HighAmplitude = 4 'Write  
hi = extPulseGen.HighAmplitude 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_HighAmplitude (double *pValue) HRESULT put_HighAmplitude
(double newVal)  
  
#### Interface

|  IExternalPulseGenerator  
  
* * *

* * *

