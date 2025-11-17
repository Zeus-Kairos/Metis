##### Write/Read

|

##### [About SA
Application](../../../Applications/Spectrum_Analyzer.htm#Force_FFT_to_Frequency)  
  
---|---  
  
## EnableForceLOToFrequency Property

* * *

#### Description

|  Set and read enable force LO to frequency mode.  
---|---  
  
#### VB Syntax

|  sa.EnableForceLOToFrequency = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (Boolean) Choose from: 0 - OFF \- Force LO to frequency is disabled. 1 - ON \- Force LO to frequency is set manually using [ForceLOToFrequency](ForceFFTToFrequency_Property.md). [Learn about these settings](../../../Applications/Spectrum_Analyzer.md#Force_LO_Enable).  
  
#### Return Type

|  Boolean  
  
#### Default

|  0  
  
#### Examples

|  sa.EnableForceLOToFrequency = AUTO  'Write  
value = sa.EnableForceLOToFrequency 'Read [See an example
program.](../../COM_Example_Programs/Spectrum_Analyzer.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_EnableForceLOToFrequency(VARIANT_BOOL bEnable); HRESULT
get_EnableForceLOToFrequency(VARIANT_BOOL* bEnable);  
  
#### Interface

|  ISpectrumAnalyzer  
  
* * *

