##### Write/Read

|

##### [About Noise Figure](../../../Applications/Noise_Figure.md)  
  
---|---  
  
## NoiseAverageState Property

* * *

#### Description

|  Turns Noise Averaging ON and OFF.  
---|---  
  
####  VB Syntax

|  noise.NoiseAverageState = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
noise |  A [NoiseFigure](../Objects/NoiseFigure_Object.md) (object)  
value |  (boolean) - Averaging state. False - Turns Noise Averaging OFF True - Turns Noise Averaging ON  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  noise.NoiseAverageState = OFF 'Write  
NoiseAvgState = noise.NoiseAverageState 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_NoiseAverageState(VARIANT_BOOL* on); HRESULT
put_NoiseAverageState(VARIANT_BOOL on);  
  
#### Interface

|  INoiseFigure  
  
* * *

