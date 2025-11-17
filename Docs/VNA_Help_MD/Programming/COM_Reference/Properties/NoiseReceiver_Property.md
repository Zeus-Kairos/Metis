##### Write/Read

|

##### [About Noise Figure](../../../Applications/Noise_Figure.md)  
  
---|---  
  
## NoiseReceiver Property

* * *

#### Description

|  Sets and returns the receiver to use for noise measurements.  
---|---  
  
####  VB Syntax

|  noise.NoiseReceiver = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
noise |  A [NoiseFigure](../Objects/NoiseFigure_Object.md) (object)  
value |  (Enum as NANoiseReceiverMode) Noise receiver. Choose from: 0 - naStandardReceiver The standard VNA receiver. (Opt 028 or 029) 1 - naNoiseReceiver The noise receiver. (Opt 029 ONLY)  
  
#### Return Type

|  Enum  
  
#### Default

|  1 - naNoiseReceiver  
  
#### Examples

|  noise.NoiseReceiver = naNoiseReceiver 'Write  
NoiseRec = noise.NoiseReceiver 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_NoiseReceiver(tagNoiseReceiverMode *pVal); HRESULT
put_NoiseReceiver(tagNoiseReceiverMode newVal);  
  
#### Interface

|  INoiseFigure5  
  
* * *

