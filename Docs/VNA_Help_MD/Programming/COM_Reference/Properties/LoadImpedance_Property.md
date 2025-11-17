##### Write/Read

|

##### [About Ext Pulse
Gens](../../../System/Configure_an_External_Pulse_Generator.htm)  
  
---|---  
  
## LoadImpedance Property

* * *

#### Description

|  Sets and returns the load impedance of the pulse generator.  
---|---  
  
####  VB Syntax

|  extPulseGen.LoadImpedance = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
extPulseGen |  An [ExternalPulseGenerator](../Objects/ExternalPulseGenerator_Object.md) (object)  
value |  (Double) Pulse generator load impedance.  
  
#### Return Type

|  Double  
  
#### Default

|  50  
  
#### Examples

|  extPulseGen.LoadImpedance = 50 'Write  
load = extPulseGen.LoadImpedance 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_LoadImpedance (double *pValue) HRESULT put_LoadImpedance
(double newVal)  
  
#### Interface

|  IExternalPulseGenerator  
  
* * *

