##### Read/Write

|

##### [About Embedded LO](../../../Applications/Embedded_LO.md)  
  
---|---  
  
## TuningMode Property

* * *

#### Description

|  Sets and returns the method used to determine the embedded LO Frequency.  
---|---  
  
####  VB Syntax

|  obj.TuningMode = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  An [EmbeddedLO](../Objects/EmbeddedLO_Object.md) (object) or A [ConverterEmbeddedLO](../Objects/ConverterEmbeddedLO_Object.md) (object)  
value |  (Enum as NAEmbeddedLOTuningMode) Tuning mode. Choose from: 0 - naEmbeddedLOTuningMode_Broadband_And_Precise 1 - naEmbeddedLOTuningMode_Precise_Only 2 - naEmbeddedLOTuningMode_None  
  
#### Return Type

|  (Enum)  
  
#### Default

|  0 - naEmbeddedLOTuningMode_Broadband_And_Precise  
  
#### Examples

|  embedLO.TuningMode = naEmbeddedLOTuningMode_None 'write  
value = embedLO.TuningMode 'read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_TuningMode(enum NAEmbeddedLOTuningMode* mode); HRESULT
put_TuningMode(enum NAEmbeddedLOTuningMode mode);  
  
#### Interface

|  IEmbededLO  
  
* * *

