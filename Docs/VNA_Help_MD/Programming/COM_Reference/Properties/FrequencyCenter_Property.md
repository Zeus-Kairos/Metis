##### Write/Read

|

##### [About Swept IMD](../../../Applications/Swept_IMD.md)  
  
---|---  
  
## FrequencyCenter Property

* * *

#### Description

|  Sets and returns the center frequency of the main tones. Use with IMD sweep
types:

  * naIMDToneCWSweep
  * naIMDTonePowerSweep
  * naIMDDeltaFrequencySweep

  
---|---  
  
####  VB Syntax

|  object.FrequencyCenter = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  A [SweptIMD](../Objects/SweptIMD_Object.md) or [IMSpectrum](../Objects/IMSpectrum_Object.md) Object  
value |  (Double) Tone center frequency in Hz. Both the F1 and F2 tones MUST be within the frequency range of the VNA.  
  
#### Return Type

|  Double  
  
#### Default

|  1.0 GHz  
  
#### Examples

|  imd.FrequencyCenter = 2e9 'Write  
value = imd.FrequencyCenter 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_FrequencyCenter(double *pVal)  
HRESULT put_FrequencyCenter(double *pVal)  
  
#### Interface

|  ISweptIMD IIMSpectrum  
  
* * *

