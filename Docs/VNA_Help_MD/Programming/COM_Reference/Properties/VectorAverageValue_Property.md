##### Write/Read

|

##### [About Vector
Averaging](../../../Applications/Spectrum_Analyzer.htm#Vector_Averaging)  
  
---|---  
  
# VectorAverageValue Property

* * *

#### Description

|  Set and read the vector averaging value.  
---|---  
  
#### VB Syntax

|  sa.coherence.VectorAverageValue = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa.coherence |  A [SpectrumAnalyzerCoherence](../Objects/SpectrumAnalyzerCoherence.md) (object)  
value |  (Double) Choose a value between 0 and 65536. [Learn about these settings](../../../Applications/Spectrum_Analyzer.md#ADC_Stacking).  
  
#### Return Type

|  Double  
  
#### Default

|  1 (no averaging)  
  
#### Examples

|  sa.coherence.VectorAverageValue = 1  Write  
value = sa.coherence.VectorAverageValue 'Read [See an example
program.](../../COM_Example_Programs/Spectrum_Analyzer.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_VectorAverageValue(double val); HRESULT
get_VectorAverageValue(double* val);  
  
#### Interface

|  ICoherenceSA  
  
* * *

