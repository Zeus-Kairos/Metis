##### Write/Read

|

##### [About Ext Pulse
Gens](../../../System/Configure_an_External_Pulse_Generator.htm)  
  
---|---  
  
## LowAmplitude Property

* * *

#### Description

|  Sets and returns the Low amplitude (voltage) of the pulse generator.  
---|---  
  
####  VB Syntax

|  extPulseGen.LowAmplitude = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
extPulseGen |  An [ExternalPulseGenerator](../Objects/ExternalPulseGenerator_Object.md) (object)  
value |  (Double) Pulse Generator low amplitude voltage.  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  extPulseGen.LowAmplitude = 4 'Write  
lo = extPulseGen.LowAmplitude 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_LowAmplitude (double *pValue) HRESULT put_LowAmplitude (double
newVal)  
  
#### Interface

|  IExternalPulseGenerator  
  
* * *

