##### Write/Read

|

##### [About Noise Figure Cal](../../../Applications/Noise_Cal.md#Overview)  
  
---|---  
  
## RcvCharMethod Property

* * *

#### Description

|  Set and read the method used to characterize the noise receivers.  
---|---  
  
####  VB Syntax

|  noise.RcvCharMethod = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
noise |  A [NoiseCal](../Objects/NoiseCal_Object.md) (object)  
value |  (string) Receiver characterization method. NOT case-sensitive. Choose from:

  * "NoiseSource \- Use a noise source. This selection is NOT allowed when a standard VNA receiver is used as the noise receiver. ([noise.NoiseReceiver](NoiseReceiver_Property.md) = naStandardReceiver).
  * PowerMeter \- Use a power meter.

NOTE: The Power Meter selection is NOT allowed when the Noise Bandwidth is 8
MHz or 24 MHz.  
  
#### Return Type

|  String  
  
#### Default

|  "NoiseSource  
  
#### Examples

|  noise.RcvCharMethod = "PowerMeter"'Write  
receiverMethod = noise.RcvCharMethod 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_RcvCharMethod(BSTR* pValue) HRESULT put_RcvCharMethod(BSTR
pNewValue)  
  
#### Interface

|  INoiseCal3  
  
* * *

