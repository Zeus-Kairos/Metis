##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
## ForceLOToFrequency Property

* * *

#### Description

|  Set and read the LO frequency.  
---|---  
  
#### VB Syntax

|  sa.ForceLOToFrequency= value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (Double) Choose a value within the LO frequency range. [Learn about these settings](../../../Applications/Spectrum_Analyzer.md#Force_FFT_to_Frequency).  
  
#### Return Type

|  Double  
  
#### Default

|  1 GHz  
  
#### Examples

|  sa.ForceLOToFrequency= 1e9  Write  
value = sa.ForceLOToFrequency 'Read [See an example
program.](../../COM_Example_Programs/Spectrum_Analyzer.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_ForceLOToFrequency(double val); HRESULT
get_ForceLOToFrequency(double* val);  
  
#### Interface

|  ISpectrumAnalyzer  
  
* * *

