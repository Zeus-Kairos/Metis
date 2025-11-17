##### Read/Write

|

##### [About Embedded LO](../../../Applications/Embedded_LO.md)  
  
---|---  
  
## TuningIFBW Property

* * *

#### Description

|  Set the IF Bandwidth for Broadband and Precise tuning sweeps.  
---|---  
  
####  VB Syntax

|  obj.TuningIFBW = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  An [EmbeddedLO](../Objects/EmbeddedLO_Object.md) (object) or A [ConverterEmbeddedLO](../Objects/ConverterEmbeddedLO_Object.md) (object)  
value |  (Double) IF Bandwidth  
  
#### Return Type

|  (Double)  
  
#### Default

|  30 kHz  
  
#### Examples

|  embedLO.TuningIFBW = 10e3 'write  
value = embedLO.TuningIFBW 'read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_TuningIFBW(double* ifbw); HRESULT put_TuningIFBW(double ifbw);  
  
#### Interface

|  IEmbededLO  
  
* * *

