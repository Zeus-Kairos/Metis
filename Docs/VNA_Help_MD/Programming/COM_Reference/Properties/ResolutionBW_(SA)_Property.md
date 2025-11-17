##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
## ResolutionBW Property

* * *

#### Description

|  Set and read the resolution bandwidth. Also set
[ResolutionBWMode](ResolutionBWMode_Property.md) to naManual.  
---|---  
  
#### VB Syntax

|  sa.ResolutionBW = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (Double) Choose a value between 6 Hz and 3 MHz. Attempting to set the bandwidth outside these bounds will force the bandwidth to the nearest bound. [Learn about these settings](../../../Applications/Spectrum_Analyzer.md#Resolution_Bandwidth).  
  
#### Return Type

|  Double  
  
#### Default

|  100 kHz  
  
#### Examples

|  sa.ResolutionBW = 1e6  'Write  
value = sa.ResolutionBW 'Read [See an example
program.](../../COM_Example_Programs/Spectrum_Analyzer.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_ResolutionBW(double freq); HRESULT get_ResolutionBW(double*
freq);  
  
#### Interface

|  ISpectrumAnalyzer  
  
* * *

