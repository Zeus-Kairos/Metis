##### Write/Read

|

##### [About Triggering
ADC](../../../Applications/Spectrum_Analyzer.htm#Advanced_Trigger_Modes)  
  
---|---  
  
# TriggerADCLevelValue Property

* * *

#### Description

|  Set and read the ADC trigger level.  
---|---  
  
#### VB Syntax

|  sa.TriggerADCLevelValue = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (Long) Choose a value between 0 and 16383. [Learn about these settings](../../../Applications/Spectrum_Analyzer.md#Advanced_Trigger_Modes).  
  
#### Return Type

|  Long  
  
#### Default

|  100  
  
#### Examples

|  sa.TriggerADCLevelValue = 256  'Write  
value = sa.TriggerADCLevelValue 'Read [See an example
program.](../../COM_Example_Programs/Spectrum_Analyzer.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_TriggerADCLevelValue(long val); HRESULT
get_TriggerADCLevelValue(long* val);  
  
#### Interface

|  ISpectrumAnalyzer  
  
* * *

