##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
## SpanResolutionBWRatio Property

* * *

#### Description

|  Set and read the Frequency Span / RBW ratio.  
---|---  
  
#### VB Syntax

|  sa.SpanResolutionBWRatio = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (Double) Frequency Span / RBW ratio. Choose a value between 1 and 200e9. [Learn about these settings](../../../Applications/Spectrum_Analyzer.md#Span_RBW).  
  
#### Return Type

|  Double  
  
#### Default

|  106  
  
#### Examples

|  sa.SpanResolutionBWRatio = 100  Write  
value = sa.SpanResolutionBWRatio 'Read [See an example
program.](../../COM_Example_Programs/Spectrum_Analyzer.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_SpanResolutionBWRatio(double ratio); HRESULT
get_SpanResolutionBWRatio(double* ratio);  
  
#### Interface

|  ISpectrumAnalyzer  
  
* * *

