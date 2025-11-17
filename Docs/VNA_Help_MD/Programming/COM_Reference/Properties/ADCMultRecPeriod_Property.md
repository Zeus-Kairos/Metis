##### Write/Read

|

##### [About Multiple
Recordings](../../../Applications/Spectrum_Analyzer.htm#Multiple_Recordings)  
  
---|---  
  
# ADCMultRecPeriod Property

* * *

#### Description

|  Set and read the period to wait between ADC record chunks.  
---|---  
  
#### VB Syntax

|  sa.ADCMultRecPeriod = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (Long) Choose a value between 64 and 33554432. [Learn about these settings](../../../Applications/Spectrum_Analyzer.md#Multiple_Recordings).  
  
#### Return Type

|  Long  
  
#### Default

|  64  
  
#### Examples

|  sa.ADCMultRecPeriod = 256  'Write  
value = sa.ADCMultRecPeriod 'Read [See an example
program.](../../COM_Example_Programs/Spectrum_Analyzer.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_ADCMultRecPeriod(long val); HRESULT get_ADCMultRecPeriod(long*
val);  
  
#### Interface

|  ISpectrumAnalyzer  
  
* * *

