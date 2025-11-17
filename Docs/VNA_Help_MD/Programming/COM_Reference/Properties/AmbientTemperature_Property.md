##### Write/Read

|

##### [About Noise Figure](../../../Applications/Noise_Figure.md)  
  
---|---  
  
## AmbientTemperature Property

* * *

#### Description

|  Sets and returns the temperature at which the current noise measurement is
occurring. [Learn
more.](../../../Applications/Noise_Figure.htm#NoiseSettingDiag)  
---|---  
  
####  VB Syntax

|  noiseCal.AmbientTemperature = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
noiseCal |  A [NoiseCal](../Objects/NoiseCal_Object.md) (object)  
value |  (double) Ambient temperature in Kelvin.  
  
#### Return Type

|  Double  
  
#### Default

|  295  
  
#### Examples

|  noise.AmbientTemperature = 289'Write  
temp = noise.AmbientTemperature 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_AmbientTemperature(Double* pValue) HRESULT
put_AmbientTemperature(Double pNewValue)  
  
#### Interface

|  INoiseCal  
  
* * *

