##### Read-Only

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
## VideoAveragingCount Property

* * *

#### Description

|  Reads the number of video bandwidth sweeps that are averaged together. This
readout is displayed on the [SA
setup](../../../Applications/Spectrum_Analyzer.htm#SetupTab) page.  
---|---  
  
#### VB Syntax

|  value = sa.VideoAveragingCount  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Long)  Variable to store the returned averaging count.  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
  
#### Return Type

|  Long  
  
#### Default

|  N/A  
  
#### Examples

|  value = sa.VideoAveragingCount 'Read [See an example
program.](../../COM_Example_Programs/Spectrum_Analyzer.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_VideoAveragingCount(long* count);  
  
#### Interface

|  ISpectrumAnalyzer  
  
* * *

