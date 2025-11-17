##### Write/Read

|

##### [About SMC Phase](../../../FreqOffset/SMC_plus_Phase.md)  
  
---|---  
  
## NormalizePoint Property

* * *

#### Description

|  Sets or returns the data point used for normalizing the phase measurement.  
---|---  
  
####  VB Syntax

|  obj.NormalizePoint = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  A [Mixer Interface](../Objects/IMixer_Interface.md) pointer to the [Measurement](../Objects/Measurement_Object.md) (object) A [Converter](../Objects/Converter_Object.md) (Object)  
value |  (Long) \- Normalization data point. Choose a data point number between 1 and the max number of data points in the sweep that has the least amount of expected noise.  
  
#### Return Type

|  Long Integer  
  
#### Default

|  Center point in the sweep  
  
#### Examples

|  mixer.NormalizePoint = 101  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_NormalizePoint(Long * val); HRESULT put_NormalizePoint(Long
val);  
  
#### Interface

|  IMixer13  
  
* * *

