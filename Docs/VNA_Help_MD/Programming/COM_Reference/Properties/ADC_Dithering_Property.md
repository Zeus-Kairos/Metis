##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
# EnableADCDither Property

* * *

#### Description

|  Set and read the ADC dither state.  
---|---  
  
#### VB Syntax

|  sa.EnableADCDither = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (Boolean) Choose from: 0 \- ADC dithering is disabled. 1 \- ADC dithering is enabled. [Learn about these settings](../../../Applications/Spectrum_Analyzer.md#ADC_Dither).  
  
#### Return Type

|  Boolean  
  
#### Default

|  0  
  
#### Examples

|  sa.EnableADCDither = 1 'Write  
value = sa.EnableADCDither 'Read [See an example
program.](../../COM_Example_Programs/Spectrum_Analyzer.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_EnableADCDither(VARIANT_BOOL bEnable); HRESULT
get_EnableADCDither(VARIANT_BOOL* bEnable);  
  
#### Interface

|  ISpectrumAnalyzer  
  
* * *

