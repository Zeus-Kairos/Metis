##### Read/Write

|

##### [About Embedded LO](../../../Applications/Embedded_LO.md)  
  
---|---  
  
## NormalizePoint Property

* * *

#### Description

|  Sets and returns the sweep data point around which to perform broadband and
precise tuning.  
---|---  
  
####  VB Syntax

|  obj.NormalizePoint = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  An [EmbeddedLO](../Objects/EmbeddedLO_Object.md) (object) or A [ConverterEmbeddedLO](../Objects/ConverterEmbeddedLO_Object.md) (object)  
value |  (Long) Mixer Sweep data point. Choose a data point number between 1 and the max number of data points in the sweep that has the least amount of expected noise.  
  
#### Return Type

|  (Long)  
  
#### Default

|  Center point in the sweep span  
  
#### Examples

|  embedLO.NormalizePoint = 101 'write  
value = embedLO.NormalizePoint 'read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_NormalizePoint(long *point); HRESULT put_NormalizePoint(long
point);  
  
#### Interface

|  IEmbededLO  
  
* * *

