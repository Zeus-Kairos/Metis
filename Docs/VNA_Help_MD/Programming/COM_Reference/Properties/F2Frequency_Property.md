##### Write/Read

|

##### [About Swept IMD](../../../Applications/Swept_IMD.md)  
  
---|---  
  
## F2Frequency Property

* * *

#### Description

|  Sets and returns the frequency of the F2 tone. Use with IMD sweep types:

  * naIMDToneCWSweep
  * naIMDTonePowerSweep

  
---|---  
  
####  VB Syntax

|  object.F2Frequency = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  A [SweptIMD](../Objects/SweptIMD_Object.md) or [IMSpectrum](../Objects/IMSpectrum_Object.md) Object  
value |  (Double) F2 tone frequency in Hz. The F1 and F2 tones MUST be within the frequency range of the VNA.  
  
#### Return Type

|  Double  
  
#### Default

|  1.0005 GHz  
  
#### Examples

|  imd.F2Frequency = 200e9 'Write  
value = imd.F2Frequency 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_F2Frequency(double *pVal)  
HRESULT put_F2Frequency(double newVal)  
  
#### Interface

|  ISweptIMD IIMSpectrum  
  
* * *

