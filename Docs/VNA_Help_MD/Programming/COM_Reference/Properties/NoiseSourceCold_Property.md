##### Write/Read

|

##### [About Noise Figure](../../../Applications/Noise_Figure.md)  
  
---|---  
  
## NoiseSourceCold Property

* * *

#### Description

|  Sets and returns the temperature of the noise source connector.  
---|---  
  
####  VB Syntax

|  noise.NoiseSourceCold = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
noise |  A [NoiseCal](../Objects/NoiseCal_Object.md) (object)  
value |  (double) Noise source temperature in Kelvin.  
  
#### Return Type

|  Double  
  
#### Default

|  Not Applicable  
  
#### Examples

|  noise.NoiseSourceCold = 295 'Write  
temp = noise.NoiseSourceCold 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_NoiseSourceCold(double* pTemp) HRESULT
put_NoiseSourceCold(double pNewTemp)  
  
#### Interface

|  INoiseCal  
  
* * *

