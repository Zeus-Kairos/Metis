##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
## SourceRepeatCount Property

* * *

#### Description

|  Set and read the number of SA (receiver) sweeps for each Source Step. This
setting is common to all sources.  
---|---  
  
#### VB Syntax

|  sa.SourceRepeatCount = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (Long)  Repeat count. Choose a value between 1 and 2e9.  
  
#### Return Type

|  Long  
  
#### Default

|  1  
  
#### Examples

|  sa.SourceRepeatCount = 10  'Write  
value = sa.SourceRepeatCount 'Read [See an example
program.](../../COM_Example_Programs/Spectrum_Analyzer.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_SourceRepeatCount(long count); HRESULT
get_SourceRepeatCount(long* count);  
  
#### Interface

|  ISpectrumAnalyzer  
  
* * *

