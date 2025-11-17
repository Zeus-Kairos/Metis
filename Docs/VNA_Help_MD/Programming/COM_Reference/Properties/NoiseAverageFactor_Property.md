##### Write/Read

|

##### [About Noise Figure](../../../Applications/Noise_Figure.md)  
  
---|---  
  
## NoiseAverageFactor Property

* * *

#### Description

|  Sets and reads the averaging of the noise receiver.  
---|---  
  
####  VB Syntax

|  noise.NoiseAverageFactor = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
noise |  A [NoiseFigure](../Objects/NoiseFigure_Object.md) (object)  
value |  (long integer) - Averaging value. Choose a number between 1 and 99.  
  
#### Return Type

|  Long Integer  
  
#### Default

|  1  
  
#### Examples

|  noise.NoiseAverageFactor = 10 'Write  
AvgNoise = noise.NoiseAverageFactor 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_NoiseAverageFactor(long* pVal) HRESULT
put_NoiseAverageFactor(long newVal)  
  
#### Interface

|  INoiseFigure  
  
* * *

