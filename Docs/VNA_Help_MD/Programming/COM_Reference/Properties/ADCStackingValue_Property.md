##### Write/Read

|

##### [About ADC
Stacking](../../../Applications/Spectrum_Analyzer.htm#ADC_Stacking)  
  
---|---  
  
# ADCStacking Property

* * *

#### Description

|  Set and read the ADC stacking value.  
---|---  
  
#### VB Syntax

|  sa.ADCStacking = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (Double) Choose a value between 0 and 65535. [Learn about these settings](../../../Applications/Spectrum_Analyzer.md#ADC_Stacking).  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  sa.ADCStacking = 1  Write  
value = sa.ADCStacking 'Read [See an example
program.](../../COM_Example_Programs/Spectrum_Analyzer.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_ADCStacking(double val); HRESULT get_ADCStacking(double* val);  
  
#### Interface

|  ISpectrumAnalyzer  
  
* * *

