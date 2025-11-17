##### Write/Read

|

##### [About Swept IMD](../../../Applications/Swept_IMD.md)  
  
---|---  
  
## DeltaFrequency Property

* * *

#### Description

|  Sets and returns the fixed tone spacing value. Use with IMD sweep types:

  * naIMDToneCWSweep
  * naIMDTonePowerSweep
  * naIMDToneCenterFreqSweep

  
---|---  
  
####  VB Syntax

|  object.DeltaFrequency = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  A [SweptIMD](../Objects/SweptIMD_Object.md) or [IMSpectrum](../Objects/IMSpectrum_Object.md) Object  
value |  (Double) - Tone spacing frequency in Hz. Both the F1 and F2 tones MUST be within the frequency range of the VNA.  
  
#### Return Type

|  Double  
  
#### Default

|  1 MHz  
  
#### Examples

|  imd.DeltaFrequency = 1e6 'Write  
value = imd.DeltaFrequency 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_DeltaFrequency(double *pVal)  
HRESULT put_DeltaFrequency(double newVal)  
  
#### Interface

|  ISweptIMD IIMSpectrum  
  
* * *

