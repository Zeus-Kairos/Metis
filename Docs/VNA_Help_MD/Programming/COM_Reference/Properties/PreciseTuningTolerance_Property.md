##### Read/Write

|

##### [About Embedded LO](../../../Applications/Embedded_LO.md)  
  
---|---  
  
## PreciseTuningTolerance Property

* * *

#### Description

|  Sets and returns the tuning tolerance for precise tuning.  
---|---  
  
####  VB Syntax

|  obj.PreciseTuningTolerance = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  An [EmbeddedLO](../Objects/EmbeddedLO_Object.md) (object) or A [ConverterEmbeddedLO](../Objects/ConverterEmbeddedLO_Object.md) (object)  
value |  (Double) Tuning tolerance in Hz.  
  
#### Return Type

|  (Double)  
  
#### Default

|  1 Hz  
  
#### Examples

|  embedLO.PreciseTuningTolerance = .5 'write  
value = embedLO.PreciseTuningTolerance 'read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PreciseTuningTolerance(double* tolerance); HRESULT
put_PreciseTuningTolerance(double tolerance);  
  
#### Interface

|  IEmbededLO  
  
* * *

