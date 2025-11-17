##### Write/Read

|

##### [About SA
Application](../../../Applications/Spectrum_Analyzer.htm#ADC_Sample_Rate)  
  
---|---  
  
## ADCSampleRate Property

* * *

#### Description

|  Set and read the ADC sample frequency setting. The entered frequency is
rounded to the closest value supported by the VNA (25 MHz or 100 MHz).  
---|---  
  
#### VB Syntax

|  sa.ADCSampleRate = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (Double) Choose from 100 MHz or 25 MHz. [Learn about these settings](../../../Applications/Spectrum_Analyzer.md#ADC_Sample_Rate).  
  
#### Return Type

|  Double  
  
#### Default

|  100 MHz  
  
#### Examples

|  sa.ADCSampleRate = 100MHz  'Write  
value = sa.ADCSampleRate 'Read [See an example
program.](../../COM_Example_Programs/Spectrum_Analyzer.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_ADCSampleRate(double rate); HRESULT get_ADCSampleRate(double*
rate);  
  
#### Interface

|  ISpectrumAnalyzer  
  
* * *

