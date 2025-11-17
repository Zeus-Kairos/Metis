##### Write/Read

|

##### [About SA
Application](../../../Applications/Spectrum_Analyzer.htm#Force_ADC_Record_Size)  
  
---|---  
  
## EnableForceADCRecordSize Property

* * *

#### Description

|  Set and read enable force ADC record size mode.  
---|---  
  
#### VB Syntax

|  sa.EnableForceADCRecordSize = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (Boolean) Choose from: 0 - OFF \- ADC record size set automatically. 1 - ON \- Manually set ADC record to specified size using [ForceADCRecordSize](ForceADCRecordSize_Property.md). [Learn about these settings](../../../Applications/Spectrum_Analyzer.md#Force_ADC_Record_Enable).  
  
#### Return Type

|  Boolean  
  
#### Default

|  0  
  
#### Examples

|  sa.EnableForceADCRecordSize = AUTO  'Write  
value = sa.EnableForceADCRecordSize 'Read [See an example
program.](../../COM_Example_Programs/Spectrum_Analyzer.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_EnableForceADCRecordSize(VARIANT_BOOL bEnable); HRESULT
get_EnableForceADCRecordSize(VARIANT_BOOL* bEnable);  
  
#### Interface

|  ISpectrumAnalyzer  
  
* * *

