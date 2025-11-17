##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
## EnableDitherFFTGridOrigin Property

* * *

#### Description

|  Set and read the FFT grid dither state.  
---|---  
  
#### VB Syntax

|  sa.EnableDitherFFTGridOrigin = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (Boolean) Choose from: 0 - OFF \- FFT grid dithering is disabled. 1 - ON \- FFT grid dithering is enabled.  
  
#### Return Type

|  Boolean  
  
#### Default

|  0  
  
#### Examples

|  sa.EnableDitherFFTGridOrigin = 1 'Write  
value = sa.EnableDitherFFTGridOrigin 'Read [See an example
program.](../../COM_Example_Programs/Spectrum_Analyzer.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_EnableDitherFFTGridOrigin(VARIANT_BOOL bEnable); HRESULT
get_EnableDitherFFTGridOrigin(VARIANT_BOOL* bEnable);  
  
#### Interface

|  ISpectrumAnalyzer  
  
* * *

