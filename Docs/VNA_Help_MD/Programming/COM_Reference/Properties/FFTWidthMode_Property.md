##### Write/Read

|

##### [About SA
Application](../../../Applications/Spectrum_Analyzer.htm#FFT_Width)  
  
---|---  
  
## ADCFilter Property

* * *

#### Description

|  Set and read the ADC filter width mode. The entered frequency value is
rounded to the closest value supported by the VNA (11 MHz or 38 MHz).  
---|---  
  
#### VB Syntax

|  sa.ADCFilter = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (Double) Choose a value within the range supported by the VNA. [Learn about these choices.](../../../Applications/Spectrum_Analyzer.md#FFT_Width)  
  
#### Return Type

|  Double  
  
#### Default

|  11 MHz  
  
#### Examples

|  sa.ADCFilter = 11MHz 'Write  
value = sa.ADCFilter 'Read [See an example
program.](../../COM_Example_Programs/Spectrum_Analyzer.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_ADCFilter(double cutfreq); HRESULT get_ADCFilter(double*
cutfreq);  
  
#### Interface

|  ISpectrumAnalyzer  
  
* * *

