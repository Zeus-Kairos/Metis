##### Read/Write

|

##### [About Embedded LO](../../../Applications/Embedded_LO.md)  
  
---|---  
  
## LOFrequencyDelta Property

* * *

#### Description

|  Sets and returns LO Frequency Delta. There is usually no need to set this
value. Read this value to determine the difference between the LO Frequency
that is stated in the Mixer dialog box and the last measured LO Frequency.  
---|---  
  
####  VB Syntax

|  obj.LOFrequencyDelta = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  An [EmbeddedLO](../Objects/EmbeddedLO_Object.md) (object) or A [ConverterEmbeddedLO](../Objects/ConverterEmbeddedLO_Object.md) (object)  
value |  (Double) LO Frequency delta in Hertz.  
  
#### Return Type

|  (Double)  
  
#### Default

|  Not Applicable  
  
#### Examples

|  embedLO.LOFrequencyDelta = 0 'write  
value = embedLO.LOFrequencyDelta 'read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_LOFrequencyDelta(double* val); HRESULT
put_LOFrequencyDelta(double val);  
  
#### Interface

|  IEmbededLO  
  
* * *

