##### Write/Read

|

##### [About SA
Application](../../../Applications/Spectrum_Analyzer.htm#ADCFilterAuto)  
  
---|---  
  
# EnableADCFilterAuto Property

* * *

#### Description

|  Set and read how the ADC filter is set. When set to 1, ADC filter is set
based on the ADC sampling frequency.  
---|---  
  
#### VB Syntax

|  sa.EnableADCFilterAuto = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (Boolean) Choose from: 0 - OFF \- ADC filter is set manually using [ADCFilter](FFTWidthMode_Property.md). 1 - ON \- Automatically select ADC filter based on the ADC sampling frequency. [Learn about these settings](../../../Applications/Spectrum_Analyzer.md#ADCFilterAuto).  
  
#### Return Type

|  Boolean  
  
#### Default

|  1  
  
#### Examples

|  sa.EnableADCFilterAuto = 0  'Write  
value = sa.EnableADCFilterAuto 'Read [See an example
program.](../../COM_Example_Programs/Spectrum_Analyzer.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_EnableADCFilterAuto(VARIANT_BOOL bEnable); HRESULT
get_EnableADCFilterAuto(VARIANT_BOOL* bEnable);  
  
#### Interface

|  ISpectrumAnalyzer  
  
* * *

