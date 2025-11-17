##### Write/Read

|

##### [About Swept IMD](../../../Applications/Swept_IMD.md)  
  
---|---  
  
## TonePower Property

* * *

#### Description

|  Sets and returns the power level of the Main Tones. Use with IMD sweep
types:

  * naIMDToneCWSweep,
  * naIMDToneCenterFreqSweep
  * naIMDDeltaFrequencySweep. 

When tone power is coupled, setting either F1 or F2 power sets both.  
---|---  
  
####  VB Syntax

|  object.TonePower (tone) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  A [SweptIMD](../Objects/SweptIMD_Object.md) or [IMSpectrum](../Objects/IMSpectrum_Object.md) Object  
tone |  (Enum as NAIMDTonePowerID) Choose from: 0 - naIMDF1Power \- F1 tone 1 - naIMDF2Power \- F2 tone  
value |  (Double) Tone power level in dBm. Choose a value between +30 dBm and -30 dBm.  
  
#### Return Type

|  Double  
  
#### Default

|  -20 dBm  
  
#### Examples

|  imd.TonePower(naIMDF1Power) = 0 'Write  
value = imd.TonePower(naIMDF2Power) 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_TonePower(tagNAIMDTonePowerID naIMDF1, double * pVal); HRESULT
put_TonePower(tagNAIMDTonePowerID naIMDF1, double newVal);  
  
#### Interface

|  ISweptIMD IIMSpectrum  
  
* * *

