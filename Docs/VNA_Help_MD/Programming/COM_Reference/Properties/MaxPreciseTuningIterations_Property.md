##### Read/Write

|

##### [About Embedded LO](../../../Applications/Embedded_LO.md)  
  
---|---  
  
## MaxPreciseTuningIterations Property

* * *

#### Description

|  Sets and returns the maximum number of tuning iterations to achieve the
precise tolerance.  
---|---  
  
####  VB Syntax

|  obj.MaxPreciseTuningIterations = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  An [EmbeddedLO](../Objects/EmbeddedLO_Object.md) (object) or A [ConverterEmbeddedLO](../Objects/ConverterEmbeddedLO_Object.md) (object)  
value |  (Long) Maximum number of tuning iterations.  
  
#### Return Type

|  (Long)  
  
#### Default

|  5  
  
#### Examples

|  embedLO.MaxPreciseTuningIterations = 3 'write  
value = embedLO.MaxPreciseTuningIterations 'read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_MaxPreciseTuningIterations long* iter); HRESULT
put_MaxPreciseTuningIterations long iter);  
  
#### Interface

|  IEmbededLO  
  
* * *

