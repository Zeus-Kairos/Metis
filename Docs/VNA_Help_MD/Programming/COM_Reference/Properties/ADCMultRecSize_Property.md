##### Write/Read

|

##### [About Multiple
Recordings](../../../Applications/Spectrum_Analyzer.htm#Multiple_Recordings)  
  
---|---  
  
# ADCMultRecSize Property

* * *

#### Description

|  Set and read the size of the ADC record chunks.  
---|---  
  
#### VB Syntax

|  sa.ADCMultRecSize = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (Long) Choose a value between 1 and (ADC record size / 2). [Learn about these settings](../../../Applications/Spectrum_Analyzer.md#Multiple_Recordings).  
  
#### Return Type

|  Long  
  
#### Default

|  32  
  
#### Examples

|  sa.ADCMultRecSize = 256  'Write  
value = sa.ADCMultRecSize 'Read [See an example
program.](../../COM_Example_Programs/Spectrum_Analyzer.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_ADCMultRecSize(long val); HRESULT get_ADCMultRecSize(long*
val);  
  
#### Interface

|  ISpectrumAnalyzer  
  
* * *

