##### Read/Write

|

##### [About Embedded LO](../../../Applications/Embedded_LO.md)  
  
---|---  
  
## BroadbandTuningSpan Property

* * *

#### Description

|  Sets and returns the frequency span for the broadband tuning sweep.  
---|---  
  
####  VB Syntax

|  obj.BroadbandTuningSpan = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  An [EmbeddedLO](../Objects/EmbeddedLO_Object.md) (object) or A [ConverterEmbeddedLO](../Objects/ConverterEmbeddedLO_Object.md) (object)  
value |  (Double) Broadband frequency span in Hz.  
  
#### Return Type

|  (Double)  
  
#### Default

|  3 MHz  
  
#### Examples

|  embedLO.BroadbandTuningSpan = 1E6 'write  
value = embedLO.BroadbandTuningSpan 'read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_BroadbandTuningSpan(double* span); HRESULT
put_BroadbandTuningSpan(double span);  
  
#### Interface

|  IEmbededLO  
  
* * *

  

