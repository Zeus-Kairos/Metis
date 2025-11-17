##### Write/Read

|

##### [About Noise Figure](../../../Applications/Noise_Figure.md)  
  
---|---  
  
## NoiseGain Property

* * *

#### Description

|  Sets and reads the gain state of the noise receiver. This setting is NOT
used when [NoiseReceiver](NoiseReceiver_Property.md) = naStandardReceiver
(Opt 028)  
---|---  
  
####  VB Syntax

|  noise.NoiseGain = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
noise |  A [NoiseFigure](../Objects/NoiseFigure_Object.md) (object)  
value |  (long integer) - Gain value. Choose from: 0 Low Gain select if the gain of your DUT is relatively high (>35 dB). 15 Medium Gain select if the gain of your DUT is about average (20 dB to 45 dB). 30 High Gain ..select if the gain of your DUT is relatively low (<30 dB). If the value does not match one of these, it is rounded up to the next legal value. [Learn more about Noise Receiver Gain setting.](../../../Applications/Noise_Figure.md#NoiseSettingDiag)  
  
#### Return Type

|  Long Integer  
  
#### Default

|  30  
  
#### Examples

|  noise.NoiseGain = 30 'Write  
GainNoise = noise.NoiseGain 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_NoiseGain(long* pVal) HRESULT put_NoiseGain(long newVal)  
  
#### Interface

|  INoiseFigure  
  
* * *

