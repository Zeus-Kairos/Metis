##### Write/Read

|

##### [About Noise Figure](../../../Applications/Noise_Figure.md)  
  
---|---  
  
## NoiseBandwidth Property

* * *

#### Description

|  Set the bandwidth of the noise receiver.  
---|---  
  
####  VB Syntax

|  noise.NoiseBandwidth = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
noise |  A [NoiseFigure](../Objects/NoiseFigure_Object.md) (object)  
value |  (double) Bandwidth value. For [NoiseReceiver](NoiseReceiver_Property.md) = naNoiseReceiver (Opt 029) choose from: 800 KHz, 2 MHz, 4 MHz, 8 MHz, or 24 MHz or the numerical equivalent, such as 8e6 and so forth. NOTE: The [Receiver Characterization Method](RcvCharMethod_Property.md) = "Power Meter" is NOT allowed when the Noise Bandwidth is 8 MHz or 24 MHz. For NoiseReceiver = naStandardReceiver (Opt 028) choose from: 720 kHz or 1.2 MHz If the value does not match one of these, it is rounded up to the next valid bandwidth value.  
  
#### Return Type

|  Double  
  
#### Default

|  4 MHz for naNoiseReceiver 1.2 MHz for naStandardReceiver  
  
#### Examples

|  noise.NoiseBandwidth = 2E6 'Write  
NoiseBW = noise.NoiseBandwidth 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_NoiseBandwidth(double *pVal); HRESULT put_NoiseBandwidth(double
newVal);  
  
#### Interface

|  INoiseFigure  
  
* * *

