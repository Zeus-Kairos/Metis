##### Write/Read

|

##### [About Swept IMD](../../../Applications/Swept_IMD.md)  
  
---|---  
  
## F1Frequency Property

* * *

#### Description

|  Sets and returns the frequency of the F1 tone. Use with IMD sweep types:

  * naIMDToneCWSweep
  * naIMDTonePowerSweep

  
---|---  
  
####  VB Syntax

|  object.F1Frequency = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  A [SweptIMD](../Objects/SweptIMD_Object.md) or [IMSpectrum](../Objects/IMSpectrum_Object.md) Object  
value |  (Double) F1 tone frequency in Hz. The F1 and F2 tones MUST be within the frequency range of the VNA.  
  
#### Return Type

|  Double  
  
#### Default

|  .9995 GHz  
  
#### Examples

|  imd.F1Frequency = 100e6 'Write  
value = imd.F1Frequency 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_F1Frequency(double *pVal)  
HRESULT put_F1Frequency(double newVal)  
  
#### Interface

|  ISweptIMD IIMSpectrum  
  
* * *

