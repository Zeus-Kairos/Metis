##### Write/Read

|

##### [About Noise Figure](../../../Applications/Noise_Figure.md)  
  
---|---  
  
# NoiseGainCTCheck

* * *

#### Description

|  Turns noise threshold checking ON and OFF.  
---|---  
  
####  VB Syntax

|  noise.NoiseGainCTCheck = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
noise |  A [NoiseFigure2](../Objects/NoiseFigure_Object.md) (object)  
value |  (boolean) - Averaging state. 0- Turns noise threshold checking OFF 1- Turns noise threshold checking ON  
  
#### Return Type

|  Boolean  
  
#### Default

|  0 - OFF  
  
#### Examples

|  noise.NoiseGainCTCheck = OFF 'Write  
NoiseCT = noise.NoiseGainCTCheck 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_NoiseGainCTCheck(VARIANT_BOOL* on); HRESULT
put_NoiseGainCTCheck(VARIANT_BOOL on);  
  
#### Interface

|  INoiseFigure3

