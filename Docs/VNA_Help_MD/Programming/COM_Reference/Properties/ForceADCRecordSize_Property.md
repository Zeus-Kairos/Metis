##### Write/Read

|

##### [About SA
Application](../../../Applications/Spectrum_Analyzer.htm#Force_ADC_Record_Size)  
  
---|---  
  
## ForceADCRecordSize Property

* * *

#### Description

|  Set and read the ADC record size.  
---|---  
  
#### VB Syntax

|  sa.ForceADCRecordSize = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (Long) Choose a value between 64 and 33554432 [Learn about these settings](../../../Applications/Spectrum_Analyzer.md#Force_ADC_Record_Size).  
  
#### Return Type

|  Long  
  
#### Default

|  64  
  
#### Examples

|  sa.ForceADCRecordSize = 256  'Write  
value = sa.ForceADCRecordSize 'Read [See an example
program.](../../COM_Example_Programs/Spectrum_Analyzer.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_ForceADCRecordSize(long val); HRESULT
get_ForceADCRecordSize(long* val);  
  
#### Interface

|  ISpectrumAnalyzer  
  
* * *

