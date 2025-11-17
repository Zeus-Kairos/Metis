##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
## ResolutionBWVideoBWRatio Property

* * *

#### Description

|  Set and read the RBW / VBW ratio.  
---|---  
  
#### VB Syntax

|  sa.ResolutionBWVideoBWRatio = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (Double) RBW / VBW ratio. [Learn about these settings](../../../Applications/Spectrum_Analyzer.md#RBW_VBW).  
  
#### Return Type

|  Double  
  
#### Default

|  1.0  
  
#### Examples

|  sa.ResolutionBWVideoBWRatio = 1  'Write  
value = sa.ResolutionBWVideoBWRatio 'Read [See an example
program.](../../COM_Example_Programs/Spectrum_Analyzer.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_ResolutionBWVideoBWRatio(double ratio); HRESULT
get_ResolutionBWVideoBWRatio(double* ratio);  
  
#### Interface

|  ISpectrumAnalyzer  
  
* * *

