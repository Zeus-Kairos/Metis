##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
## SourcePointCount Property

* * *

#### Description

|  Set and read the number of steps the source will make across the specified
source frequency range.  
---|---  
  
#### VB Syntax

|  sa.SourcePointCount = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (Long)  Point count. Choose a value between 1 and 2e9.  
  
#### Return Type

|  Long  
  
#### Default

|  1  
  
#### Examples

|  sa.SourcePointCount = 10  'Write  
value = sa.SourcePointCount 'Read [See an example
program.](../../COM_Example_Programs/Spectrum_Analyzer.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_SourcePointCount(long points); HRESULT
get_SourcePointCount(long* points);  
  
#### Interface

|  ISpectrumAnalyzer  
  
* * *

